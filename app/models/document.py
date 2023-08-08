from sqlalchemy import Column, Integer, String
from app.models.base_model import DBBaseModel

class Document(DBBaseModel):
    """
    Model representing a resource.

    Attributes:
        id (String): The primary key of the resource.
        name (String): The name of the resource.
        size (Integer): The size of the resource.
        type (String): The type of the resource (e.g., application/pdf).
        agent_id (String): The ID of the agent associated with the resource.
    """

    __tablename__ = 'documents'

    id = Column(String, primary_key=True)
    name = Column(String)
    size = Column(Integer)
    type = Column(String)
    agent_id = Column(String)

    def __repr__(self):
        """
        Returns a string representation of the Resource object.

        Returns:
            str: String representation of the Resource object.
        """

        return f"Resource(id={self.id}, name='{self.name}', size='{self.size}', type='{self.type}', agent_id={self.agent_id}"
