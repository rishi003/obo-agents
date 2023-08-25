import uuid
from typing import List

from fastapi import APIRouter
from fastapi import HTTPException, status
from fastapi_sqlalchemy import db
from pydantic import BaseModel

from sqlalchemy import and_
from app.models.user import User
from app.models.chat import Chat
from app.models.participant import Participant
from app.models.message import Message
from app.models.document import Document
from app.agent.agent_docquery import run_query

router = APIRouter(tags=["Chats"])

class ChatIn(BaseModel):
    user_id: str

class ChatOut(BaseModel):
    id: str
    name: str
    class Config:
        orm_mode = True

class ParticipantOut(BaseModel):
    id: str
    userId: str
    chatId: str
    class Config:
        orm_mode = True

class MessageIn(BaseModel):
    user_id: str
    chat_id: str
    content: str

class MessageOut(BaseModel):
    id: str
    userId: str
    chatId: str
    content: str
    byAgent: bool
    class Config:
        orm_mode = True


@router.post("/add", response_model=ChatOut, status_code=status.HTTP_201_CREATED, responses={400: {"detail": "User not found"}})
def create_chat(chat: ChatIn):
    """
        Creates a new Chat
        
        Args:
            chat (ChatIn): An object representing the Chat to be created.
                Contains the following attributes:
                - user_id (str): Identifier of the associated user
        
        Returns:
            Chat: An object of Chat representing the created Chat.
        
        Raises:
            HTTPException (Status Code=400): If user not found
    """
    user = db.session.query(User).filter(User.id == chat.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")
    chat_name = "OBO Chat"
    db_chat = Chat(id=str(uuid.uuid4()), name=chat_name)
    db.session.add(db_chat)
    db.session.commit()
    return db_chat

@router.get("/get", response_model=ParticipantOut, responses={404: {"detail": "No chats found"}})
def get_chat(user_id: str):
    """
        Get all chats for an user
        
        Args:
            user_id (str): ID of the user
        
        Returns:
            List[Chat]: List of chats belonging to the user
        
        Raises:
            HTTPException (Status Code=404): If no chats found
    """
    chats = db.session.query(Participant).filter(Participant.userId == user_id).all()
    if not chats:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No chats found")
    return chats

@router.get("/get/{chat_id}/messages", response_model=List[MessageOut], responses={404: {"detail": "Chat not found"}})
def get_messages(chat_id: str):
    """
        Get all messages for a chat
        
        Args:
            chat_id (str): ID of the chat
        
        Returns:
            List[Message]: List of messages belonging to the chat
        
        Raises:
            HTTPException (Status Code=404): If no messages found
    """
    messages = db.session.query(Message).filter(Message.chatId == chat_id).all()
    if not messages:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found")
    return messages

@router.post("/add/{chat_id}/message", response_model=MessageOut, status_code=status.HTTP_201_CREATED, responses={404: {"detail": "Chat not found"}})
def create_message(message: MessageIn):
    """
        Creates a new message
        
        Args:
            message (MessageIn): An object representing the message to be created.
                Contains the following attributes:
                - user_id (str): Identifier of the associated user
                - chat_id (str): Identifier of the associated chat
                - content (str): Content of the message
        
        Returns:
            Message: An object of Message representing the created message.
        
        Raises:
            HTTPException (Status Code=404): If chat not found
            HTTPException (Status Code=404): If no documents found
    """
    chat = db.session.query(Chat).filter(Chat.id == message.chat_id).first()
    if not chat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found")

    docs = db.session.query(Document).filter(Document.userId == message.user_id).all()
    if not docs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No documents found for user")

    participant = db.session.query(Participant).filter(Participant.chatId == message.chat_id, and_(Participant.userId == message.user_id)).first()
    if not participant:
        db_participant = Participant(id=str(uuid.uuid4()), userId=message.user_id, chatId=message.chat_id)
        db.session.add(db_participant)
        db.session.commit()
    db_message = Message(id=str(uuid.uuid4()), userId=message.user_id, chatId=message.chat_id, content=message.content)
    db.session.add(db_message)
    db.session.commit()
    response = run_query(message.user_id, message.chat_id, message.content, db)
    return response
