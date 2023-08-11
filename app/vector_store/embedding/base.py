from abc import ABC, abstractmethod
from typing import List


class BaseEmbedding(ABC):

    @abstractmethod
    def get_embedding_query(self, text: str):
        pass
    
    @abstractmethod
    def get_embedding_docs(self, text: List[str]):
        pass