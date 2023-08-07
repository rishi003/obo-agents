from sqlalchemy import Column, Integer, String, Boolean

from app.models.base_model import DBBaseModel

class Agent(DBBaseModel):
    """
    Represents an agent entity.

    Attributes:
        id (int): The unique identifier.
        name (str): The name of the agent.
        user_id (str): The identifier of the associated user.
        agent_id (str): The identifier of the agent.
        is_deleted (bool): The flag associated for agent deletion
    """

    __tablename__ = 'agents'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    user_id = Column(String)
    agent_id = Column(String)
    is_deleted = Column(Boolean, default = False)

    def __repr__(self):
        """
        Returns a string representation of the Agent object.

        Returns:
            str: String representation of the Agent.

        """
        return f"Agent(id={self.id}, name='{self.name}', user_id={self.user_id}, " \
               f"agent_id={self.agent_id}, is_deleted='{self.is_deleted}')"

    @classmethod
    def get_agent_from_id(cls, session, agent_id):
        """
            Get Agent from agent_id

            Args:
                session: The database session.
                agent_id(int) : Unique identifier of an Agent.

            Returns:
                Agent: Agent object is returned.
        """
        return session.query(Agent).filter(Agent.agent_id == agent_id).first()
