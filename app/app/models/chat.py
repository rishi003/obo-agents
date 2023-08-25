from sqlalchemy import Column, String

from app.models.base_model import DBBaseModel

class Chat(DBBaseModel):
    """
    Represents a chat entity.

    Attributes:
        id (String): The unique identifier.
        name (String): The name of the chat.
    """

    __tablename__ = 'chats'

    id = Column(String, primary_key=True)
    name = Column(String)

    def __repr__(self):
        """
        Returns a string representation of the Chat object.

        Returns:
            str: String representation of the Chat.
        """
        return f"Chat(id={self.id}, name='{self.name}')"
