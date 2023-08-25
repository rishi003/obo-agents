from sqlalchemy import Column, String, Boolean

from app.models.base_model import DBBaseModel

class Agent(DBBaseModel):
    """
    Represents an agent entity.

    Attributes:
        id (String): The unique identifier.
        userId (String): The identifier of the associated user.
        name (String): The name of the agent.
        isDeleted (Boolean): The flag associated for agent deletion
    """

    __tablename__ = 'agents'

    id = Column(String, primary_key=True)
    userId = Column(String)
    name = Column(String)
    isDeleted = Column(Boolean, default = False)

    def __repr__(self):
        """
        Returns a string representation of the Agent object.

        Returns:
            str: String representation of the Agent.

        """
        return f"Agent(id={self.id}, userId={self.userId}, name='{self.name}', " \
               f"is_deleted='{self.isDeleted}')"

    @classmethod
    def get_agent_from_id(cls, session, id):
        """
            Get Agent from id

            Args:
                session: The database session.
                id(str) : Unique identifier of an Agent.

            Returns:
                Agent: Agent object is returned.
        """
        return session.query(Agent).filter(Agent.id == id).first()
