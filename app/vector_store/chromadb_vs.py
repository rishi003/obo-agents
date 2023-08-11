import uuid
from typing import Any, Dict, Optional, Iterable, List

import chromadb

from app.vector_store.base import VectorStore
from app.vector_store.document import Document
from app.vector_store.embedding.base import BaseEmbedding

def _build_chroma_client():
    return chromadb.PersistentClient()


class ChromaDB(VectorStore):
    def __init__(
            self,
            collection_name: str,
            embedding_model: BaseEmbedding,
            text_field: str,
            namespace: Optional[str] = "default",
    ):
        self.client = _build_chroma_client()
        self.collection_name = collection_name
        self.embedding_model = embedding_model
        self.text_field = text_field
        self.namespace = namespace
        self.collection = self.create_collection(self.collection_name)

    def create_collection(self, collection_name):
        """Create a Chroma Collection.
        Args:
        collection_name: The name of the collection to create.
        """
        return self.client.get_or_create_collection(name=collection_name)

    def add_texts(
            self,
            texts: Iterable[str],
            metadatas: Optional[List[dict]] = None,
            ids: Optional[List[str]] = None,
            namespace: Optional[str] = None,
            batch_size: int = 32,
            **kwargs: Any,
    ) -> List[str]:
        """Add texts to the vector store."""
        if namespace is None:
            namespace = self.namespace

        metadatas = []
        ids = ids or [str(uuid.uuid4()) for _ in texts]
        if len(ids) < len(texts):
            raise ValueError("Number of ids must match number of texts.")

        if not metadatas:
            for text, _ in zip(texts, ids):
                metadata = {}
                metadata[self.text_field] = text
                metadatas.append(metadata)
        embeddings = self.embedding_model.get_embedding_docs(texts)
        self.collection.add(
            documents=texts,
            metadatas=metadatas,
            ids=ids,
            embeddings=embeddings
        )
        return ids

    def get_matching_text(self, query: str, top_k: int = 5,
                          metadata: Optional[dict] = None, **kwargs: Any) -> List[Document]:
        """Return docs most similar to query using specified search type."""
        if metadata is None:
            metadata = {}
        embedding_vector = self.embedding_model.get_embedding_query(query)
        filters = {}
        for key in metadata.keys():
            filters[key] = metadata[key]
        results = self.collection.query(
            query_embeddings=embedding_vector,
            include=["metadatas", "documents", "distances"],
            n_results=top_k,
            where=filters
        )
        print(results)
        documents = []

        for node_id, text, metadata in zip(
                results["ids"][0],
                results["documents"][0],
                results["metadatas"][0]):
            documents.append(
                Document(
                    text_content=text,
                    metadata=metadata
                )
            )

        return documents

    def get_index_stats(self) -> dict:
        """Returns stats or information of an index"""
        emb_count = self.collection.count()
        return {"embeddings_count": emb_count}

    def add_embeddings_to_vector_db(self, embeddings: dict) -> None:
        pass

    def delete_embeddings_from_vector_db(self, ids: List[str], where: Dict | None = None) -> None:
        """Delete embeddings from the vector store."""
        self.collection.delete(ids=ids, where=where)
