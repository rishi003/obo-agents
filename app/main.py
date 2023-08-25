from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.controllers.user import router as user_router
from app.controllers.agent import router as agent_router
from app.controllers.document import router as document_router
from app.controllers.chat import router as chat_router
from app.logger import logger
from app.models.base_model import DBBaseModel
from app.config import Config

app = FastAPI()

database_url = Config.DATABASE_URL

engine = create_engine(database_url)

app.add_middleware(DBSessionMiddleware, db_url=database_url)

# Configure CORS middleware
origins = [
    # Add more origins if needed
    "*",  # Allow all origins
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DBBaseModel.metadata.create_all(bind=engine, checkfirst=True)

app.include_router(user_router, prefix="/users")
app.include_router(agent_router, prefix="/agents")
app.include_router(document_router, prefix="/documents")
app.include_router(chat_router, prefix="/chats")

@app.on_event("startup")
async def startup_event():
    # Perform startup tasks here
    logger.info("Running Startup tasks")
    Session = sessionmaker(bind=engine)
    session = Session()
    session.close()
