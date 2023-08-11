from typing import List
from langchain.embeddings import HuggingFaceEmbeddings
import torch

from app.config import Config

class HuggingfaceEmbedding:
    """HuggingfaceEmbeddings class."""
    def __init__(self):
        model_name = Config.EMBEDDING_MODEL
        model_kwargs = {'device': 'cuda' if torch.cuda.is_available() else 'cpu'}
        encode_kwargs = {'normalize_embeddings': True}
        self.model = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )

    def get_embedding_query(self, text: str):
        """Get embeddings for a query."""
        embeddings = self.model.embed_query(text)
        return embeddings

    def get_embedding_docs(self, text: List[str]):
        """Get embeddings for a list of documents."""
        embeddings = self.model.embed_documents(text)
        return embeddings
