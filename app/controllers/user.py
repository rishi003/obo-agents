import uuid

from fastapi import APIRouter
from fastapi import HTTPException, status
from fastapi_sqlalchemy import db
from pydantic import BaseModel

from app.models.user import User

router = APIRouter(tags=["User"])

class UserIn(BaseModel):
    name: str
    email: str

class UserOut(BaseModel):
    id: str
    name: str
    email: str
    class Config:
        orm_mode = True

@router.post("/add", response_model=UserOut, status_code=status.HTTP_201_CREATED, responses={409: {"detail": "User already exists"}})
def create_user(user: UserIn):
    """
        Creates a new User

        Args:
            user (UserIn): An object representing the User to be created.
                Contains the following attributes:
                - name (str): Name of the User
                - email (str): Email of the User
        
        Returns:
            User: An object of User representing the created User.
        
        Raises:
            HTTPException (Status Code=409): If an User already exists
    """
    existing_user = db.session.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")

    db_user = User(id=str(uuid.uuid4()), name=user.name, email=user.email)
    db.session.add(db_user)
    db.session.commit()
    return db_user
