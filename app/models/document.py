from sqlalchemy import Column, Integer, String
from app.models.base_model import DBBaseModel

class Document(DBBaseModel):
    """
    Model representing a document.

    Attributes:
        id (String): The identifier of the document.
        userId (String): The identifier of the associated user.
        name (String): The name of the document.
        location (String): The location of the document.
        type (String): The type of the document (e.g., pdf, txt, docx).
    """

    __tablename__ = 'documents'

    id = Column(String, primary_key=True)
    userId = Column(String)
    name = Column(String)
    location = Column(String)
    type = Column(String)

    def __repr__(self):
        """
        Returns a string representation of the document object.

        Returns:
            str: String representation of the document object.
        """
        return f"Document(id={self.id}, userId={self.userId}, name='{self.name}', location='{self.location}', type='{self.type}'"
