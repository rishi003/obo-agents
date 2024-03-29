import os
from pathlib import Path
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from fastapi_sqlalchemy import db

from app.models.document import Document
from app.utils.utils import get_root_input_dir
from app.config import Config

class DocLoader:
    """A class for loading documents."""
    def __init__(self, db_session, document_id):
        self.document_id = document_id
        document = db_session.query(Document).filter(Document.id == document_id).first()
        self.path = str(document.location)
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=Config.SPLIT_CHUNK_SIZE,
                                                       chunk_overlap=Config.SPLIT_CHUNK_OVERLAP)

    def load_document(self) -> list:
        """Load a document."""
        if self.path.endswith(".pdf"):
            return self._load_pdf()
        if self.path.endswith(".txt"):
            return self._load_txt()
        if self.path.endswith(".docx"):
            return self._load_docx()

    def _load_pdf(self) -> list:
        """Load a PDF document."""
        loader = PyPDFLoader(self.path)
        docs = loader.load_and_split(self.splitter)
        # Add document_id as metadata to all docs
        for doc in docs:
            doc.metadata["document_id"] = self.document_id
        return docs

    def _load_txt(self) -> list:
        """Load a text document."""
        with open(self.path, "r", encoding="utf-8") as f:
            text = f.read()
        docs = self.splitter.create_documents([text])
        for doc in docs:
            doc.metadata["document_id"] = self.document_id
        return docs

    def _load_docx(self) -> list:
        """Load a docx document."""
        loader = Docx2txtLoader(self.path)
        docs = loader.load()
        docs = self.splitter.transform_documents(docs)
        for doc in docs:
            doc.metadata["document_id"] = self.document_id
        return docs
