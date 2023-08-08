from datetime import datetime
import uuid

from fastapi import APIRouter
from fastapi import HTTPException, status
from fastapi_sqlalchemy import db
from pydantic import BaseModel

from sqlalchemy import or_
from app.models.agent import Agent

router = APIRouter(tags=["Agents"])

class AgentOut(BaseModel):
    name: str
    user_id: str
    agent_id: str
    class Config:
        orm_mode = True


class AgentIn(BaseModel):
    name: str
    user_id: str
    class Config:
        orm_mode = True

class AgentDelete(BaseModel):
    success: bool

@router.post("/add", response_model=AgentOut, status_code=status.HTTP_201_CREATED, responses={409: {"detail": "Agent for the user already exists"}})
def create_agent(agent: AgentIn):
    """
        Creates a new Agent

        Args:
            agent (Agent): An object representing the Agent to be created.
                Contains the following attributes:
                - name (str): Name of the Agent
                - user_id (str): Identifier of the associated user

        Returns:
            Agent: An object of Agent representing the created Agent.
            
        Raises:
            HTTPException (Status Code=409): If an Agent for user already exists
    """
    user = db.session.query(Agent).filter(Agent.user_id == agent.user_id).first()

    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Agent for the user already exists")

    db_agent = Agent(name=agent.name, user_id=agent.user_id, agent_id=str(uuid.uuid4()))
    db.session.add(db_agent)
    db.session.commit()
    return db_agent


@router.get("/get/{agent_id}", response_model=AgentOut, responses={404: {"detail": "agent not found"}})
def get_agent(agent_id: str):
    """
        Get an Agent by ID

        Args:
            agent_id (str): Identifier of the Agent to retrieve

        Returns:
            Agent: An object of Agent representing the retrieved Agent.

        Raises:
            HTTPException (Status Code=404): If the Agent is not found or deleted.
    """

    if (db_agent := db.session.query(Agent)
            .filter(Agent.agent_id == agent_id, or_(Agent.is_deleted == False, Agent.is_deleted is None))
            .first()):
        return db_agent
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="agent not found")


@router.put("/delete/{agent_id}", status_code=200, response_model=AgentDelete, responses={404: {"detail": "Agent not found or already deleted"}})
def delete_agent(agent_id: str):
    """
        Delete an existing Agent
            - Updates the is_deleted flag: Executes a soft delete

        Args:
            agent_id (str): Identifier of the Agent to delete

        Returns:
            A dictionary containing a "success" key with the value True to indicate a successful delete.

        Raises:
            HTTPException (Status Code=404): If the Agent is not found or deleted already.
    """

    db_agent = db.session.query(Agent).filter(Agent.agent_id == agent_id).first()

    if not db_agent or db_agent.is_deleted:
        raise HTTPException(status_code=404, detail="Agent not found or already deleted")

    # Deletion Procedure
    db_agent.is_deleted = True
    db.session.commit()
    return {"success": True}
