from sqlalchemy import Column, Integer, String, Boolean

from app.models.base_model import DBBaseModel

class User(DBBaseModel):
    """
    Represents an user entity.
    
    Attributes:
        id (String): The unique identifier.
        name (String): The name of the user.
        email (String): The email of the user.
        emailVerified (Boolean): The flag associated for email verification
        image (String): The image of the user
    """

    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)
    emailVerified = Column(Boolean, default = False)
    image = Column(String, default="")

    def __repr__(self):
        """
        Returns a string representation of the User object.
        
        Returns:
            str: String representation of the User.
        """
        return f"User(id={self.id}, name='{self.name}', email={self.email}, " \
               f"email_verified='{self.emailVerified}', image='{self.image}')"

    @classmethod
    def get_user_from_id(cls, session, id):
        """
            Get User from id

            Args:
                session: The database session.
                id(str) : Unique identifier of an User.

            Returns:
                User: User object is returned.
        """
        return session.query(User).filter(User.id == id).first()
