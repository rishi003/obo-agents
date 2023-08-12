import os
from pathlib import Path
from typing import List
import uuid

from fastapi import APIRouter
from fastapi import File, Form, UploadFile
from fastapi import HTTPException, status
from fastapi.responses import StreamingResponse
from fastapi_sqlalchemy import db
from pydantic import BaseModel

from app.logger import logger
from app.models.agent import Agent
from app.models.document import Document
from app.utils.utils import get_root_input_dir
from app.worker import add_document, patch_document, remove_document

router = APIRouter(tags=["Documents"])

class DocumentOut(BaseModel):
    id: str
    name: str
    size: int
    type: str
    agent_id: str
    class Config:
        orm_mode = True

@router.post("/upload/{agent_id}", status_code=status.HTTP_201_CREATED, responses={400: {"detail": "File type not supported! / Agent does not exists"}}, response_model=DocumentOut)
async def upload(agent_id: str, file: UploadFile = File(...),
                 name=Form(...), size=Form(...), type=Form(...)):
    """
    Upload a file as a document for an agent.

    Args:
        agent_id (str): ID of the agent.
        file (UploadFile): Uploaded file.
        name (str): Name of the document.
        size (str): Size of the document.
        type (str): Type of the document.

    Returns:
        Document: Uploaded document.

    Raises:
        HTTPException (status_code=400): If the agent with the specified ID does not exist.
        HTTPException (status_code=400): If the file type is not supported.

    """

    agent = db.session.query(Agent).filter(Agent.agent_id == agent_id).first()
    if agent is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Agent does not exists")

    # accepted_file_types is a tuple because endswith() expects a tuple
    accepted_file_types = (".pdf", ".docx", ".txt")
    if not name.endswith(accepted_file_types):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="File type not supported!")

    id = str(uuid.uuid4())
    save_directory = get_root_input_dir(agent_id)
    file_path = os.path.join(save_directory, f"{id}.{type}")
    os.makedirs(save_directory, exist_ok=True)
    with open(file_path, "wb") as f:
        contents = await file.read()
        f.write(contents)
        file.file.close()

    document = Document(id=id, name=name, size=size, type=type, agent_id=agent_id)

    db.session.add(document)
    db.session.commit()
    db.session.flush()

    add_document.delay(agent_id, document.id)
    logger.info(document)

    return document

@router.get("/get/all/{agent_id}", status_code=status.HTTP_200_OK, response_model=List[DocumentOut])
def get_all_documents(agent_id: str):
    """
    Get all documents for an agent.

    Args:
        agent_id (str): ID of the agent.

    Returns:
        List[Document]: List of documents belonging to the agent.

    """

    documents = db.session.query(Document).filter(Document.agent_id == agent_id).all()
    return documents

@router.get("/get/{document_id}", status_code=status.HTTP_200_OK, responses={404: {"detail": "Document not found / File not found"}})
def download_file_by_id(document_id: str):
    """
    Download a particular document by document_id.

    Args:
        document_id (str): ID of the document.

    Returns:
        StreamingResponse: Streaming response for downloading the document.

    Raises:
        HTTPException (status_code=400): If the document with the specified ID is not found.
        HTTPException (status_code=404): If the file is not found.

    """

    document = db.session.query(Document).filter(Document.id == document_id).first()

    if not document:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Document Not found!")

    save_directory = get_root_input_dir(document.agent_id)
    file_name = f"{document.id}.{document.type}"
    abs_file_path = Path(os.path.join(save_directory, file_name)).resolve()
    if not abs_file_path.is_file():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")
    content = open(str(abs_file_path), "rb")

    return StreamingResponse(
        content,
        media_type="application/octet-stream",
        headers={
            "Content-Disposition": f"attachment; filename={file_name}"
        }
    )

@router.patch("/update/{document_id}", status_code=status.HTTP_200_OK, responses={400: {"detail": "File type not supported! / Document not found"}}, response_model=DocumentOut)
async def update_document(document_id: str, agent_id: str, file: UploadFile = File(...),
                    name=Form(...), size=Form(...), type=Form(...)):
    """
    Patch a particular document by document_id.
    
    Args:
        document_id (str): ID of the document.
        agent_id (str): ID of the agent.
        file (UploadFile): Uploaded file.
        name (str): Name of the document.
        size (str): Size of the document.
        type (str): Type of the document.
    
    Returns:
        Document: Uploaded document.
    
    Raises:
        HTTPException (status_code=400): If the document with the specified ID is not found.
        HTTPException (status_code=400): If the file type is not supported.
    
    """
    document = db.session.query(Document).filter(Document.id == document_id).first()

    if not document:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Document Not found!")

    # accepted_file_types is a tuple because endswith() expects a tuple
    accepted_file_types = (".pdf", ".docx", ".txt")
    if not name.endswith(accepted_file_types):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="File type not supported!")

    save_directory = get_root_input_dir(document.agent_id)
    file_name = f"{document.id}.{document.type}"
    file_path = os.path.join(save_directory, file_name)
    with open(file_path, "wb") as f:
        contents = await file.read()
        f.write(contents)
        file.file.close()

    # Update document in database
    db.session.query(Document).filter(Document.id == document_id).update({
        "name": name,
        "size": size,
        "type": type
    })
    db.session.commit()
    db.session.flush()
    document = db.session.query(Document).filter(Document.id == document_id).first()

    patch_document.delay(agent_id, document.id)
    logger.info(document)

    return document

@router.delete("/delete/{document_id}", status_code=status.HTTP_200_OK, responses={404: {"detail": "Document not found / File not found"}})
def delete_document(document_id: str, agent_id: str):
    """
    Delete a particular document by document_id.
    
    Args:
        document_id (str): ID of the document.
        agent_id (str): ID of the agent.
    
    Returns:
        A dictionary containing a "success" key with the value True to indicate a successful delete.
    
    Raises:
        HTTPException (status_code=404): If the document with the specified ID is not found.
        HTTPException (status_code=404): If the file is not found.
    
    """
    document = db.session.query(Document).filter(Document.id == document_id).first()
    if not document:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Document Not found!")

    save_directory = get_root_input_dir(document.agent_id)
    file_name = f"{document.id}.{document.type}"
    abs_file_path = Path(os.path.join(save_directory, file_name)).resolve()
    if not abs_file_path.is_file():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")
    os.remove(abs_file_path)

    # Delete document from database
    db.session.query(Document).filter(Document.id == document_id).delete()
    db.session.commit()
    db.session.flush()

    remove_document.delay(agent_id, document.id)

    return {"success": True}
