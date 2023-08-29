from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey

from app.models.base_model import DBBaseModel

class Message(DBBaseModel):
    """
    Represents a message entity.

    Attributes:
        id (String): The unique identifier.
        userId (String): The identifier of the associated user.
        chatId (String): The identifier of the associated chat.
        content (String): The content of the message.
        byAgent (Boolean): The flag associated for message by agent
        inputTokens (Integer): The number of tokens in the input.
        outputTokens (Integer): The number of tokens in the output.
        totalCost (Float): The total cost of the message
    """

    __tablename__ = 'Message'

    id = Column(String, primary_key=True)
    userId = Column(String, ForeignKey('User.id'))
    chatId = Column(String, ForeignKey('Chat.id'))
    content = Column(String)
    byAgent = Column(Boolean, default=False)
    inputTokens = Column(Integer, default=0)
    outputTokens = Column(Integer, default=0)
    totalCost = Column(Float, default=0.0)

    def __repr__(self):
        """
        Returns a string representation of the Message object.

        Returns:
            str: String representation of the Message.
        """
        return f"Message(id={self.id}, userId={self.userId}, chatId={self.chatId}, " \
               f"content='{self.content}', by_agent='{self.byAgent}'), inputTokens={self.inputTokens}, " \
               f"outputTokens={self.outputTokens}, totalCost={self.totalCost})"
