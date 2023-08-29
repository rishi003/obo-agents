from sqlalchemy import Column, String, ForeignKey

from app.models.base_model import DBBaseModel

class Participant(DBBaseModel):
    """
    Represents a participant entity.

    Attributes:
        id (String): The unique identifier.
        userId (String): The identifier of the associated user.
        chatId (String): The identifier of the associated chat.
    """

    __tablename__ = 'Participant'
    id = Column(String, primary_key=True)
    userId = Column(String, ForeignKey('User.id'))
    chatId = Column(String, ForeignKey('Chat.id'))

    def __repr__(self):
        """
        Returns a string representation of the Participant object.

        Returns:
            str: String representation of the Participant.
        """
        return f"Participant(id={self.id}, userId={self.userId}, chatId={self.chatId})"
