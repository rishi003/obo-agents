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
from app.models.user import User
from app.models.document import Document
from app.utils.utils import get_root_input_dir
from app.worker import add_document, patch_document, remove_document

router = APIRouter(tags=["Documents"])

class DocumentOut(BaseModel):
    id: str
    userId: str
    name: str
    location: str
    type: str
    class Config:
        orm_mode = True

@router.post("/upload/{user_id}", status_code=status.HTTP_201_CREATED, responses={400: {"detail": "File type not supported! / User does not exists"}}, response_model=DocumentOut)
async def upload(user_id: str, file: UploadFile = File(...),
                 name=Form(...), type=Form(...)):
    """
    Upload a file as a document for an user.

    Args:
        user_id (str): ID of the user.
        file (UploadFile): Uploaded file.
        name (str): Name of the document.
        type (str): Type of the document.

    Returns:
        Document: Uploaded document.

    Raises:
        HTTPException (status_code=400): If the user with the specified ID does not exist.
        HTTPException (status_code=400): If the file type is not supported.

    """

    user = db.session.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User does not exists")

    accepted_file_types = ["pdf", "docx", "txt"]
    if not type in accepted_file_types:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="File type not supported!")

    id = str(uuid.uuid4())
    save_directory = get_root_input_dir(user_id)
    file_name = f"{id}.{type}"
    file_path = os.path.join(save_directory, file_name)
    os.makedirs(save_directory, exist_ok=True)
    with open(file_path, "wb") as f:
        contents = await file.read()
        f.write(contents)
        file.file.close()

    document = Document(id=id, userId=user_id, name=name, location=file_path, type=type)

    db.session.add(document)
    db.session.commit()
    db.session.flush()

    add_document.delay(user_id, document.id)
    logger.info(document)

    return document

@router.get("/get/all/{user_id}", status_code=status.HTTP_200_OK, response_model=List[DocumentOut])
def get_all_documents(user_id: str):
    """
    Get all documents for an user.

    Args:
        user_id (str): ID of the user.

    Returns:
        List[Document]: List of documents belonging to the user.

    """

    documents = db.session.query(Document).filter(Document.userId == user_id).all()
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

    save_directory = get_root_input_dir(document.userId)
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
async def update_document(document_id: str, user_id: str, file: UploadFile = File(...),
                    name=Form(...), type=Form(...)):
    """
    Patch a particular document by document_id.
    
    Args:
        document_id (str): ID of the document.
        user_id (str): ID of the user.
        file (UploadFile): Uploaded file.
        name (str): Name of the document.
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

    accepted_file_types = ["pdf", "docx", "txt"]
    if not type in accepted_file_types:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="File type not supported!")

    os.remove(document.location)
    save_directory = get_root_input_dir(document.userId)
    file_name = f"{document.id}.{type}"
    file_path = os.path.join(save_directory, file_name)
    with open(file_path, "wb") as f:
        contents = await file.read()
        f.write(contents)
        file.file.close()

    # Update document in database
    db.session.query(Document).filter(Document.id == document_id).update({
        "name": name,
        "location": file_path,
        "type": type
    })
    db.session.commit()
    db.session.flush()
    document = db.session.query(Document).filter(Document.id == document_id).first()

    patch_document.delay(user_id, document.id)
    logger.info(document)

    return document

@router.delete("/delete/{document_id}", status_code=status.HTTP_200_OK, responses={404: {"detail": "Document not found / File not found"}})
def delete_document(document_id: str, user_id: str):
    """
    Delete a particular document by document_id.
    
    Args:
        document_id (str): ID of the document.
        user_id (str): ID of the user.
    
    Returns:
        A dictionary containing a "success" key with the value True to indicate a successful delete.
    
    Raises:
        HTTPException (status_code=404): If the document with the specified ID is not found.
        HTTPException (status_code=404): If the file is not found.
    
    """
    document = db.session.query(Document).filter(Document.id == document_id).first()
    if not document:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Document Not found!")

    save_directory = get_root_input_dir(document.userId)
    file_name = f"{document.id}.{document.type}"
    abs_file_path = Path(os.path.join(save_directory, file_name)).resolve()
    if not abs_file_path.is_file():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")
    os.remove(abs_file_path)

    # Delete document from database
    db.session.query(Document).filter(Document.id == document_id).delete()
    db.session.commit()
    db.session.flush()

    remove_document.delay(user_id, document.id)

    return {"success": True}
