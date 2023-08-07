from sqlalchemy import create_engine
from app.logger import logger

database_url = "sqlite:///obo-agents.db"
engine = None

def connect_db():
    """
    Connects to the Sqlite database using SQLAlchemy.

    Returns:
        engine: The SQLAlchemy engine object representing the database connection.
    """
    global engine
    if engine is not None:
        return engine

    engine = create_engine(database_url,
                           pool_size=20,  # Maximum number of database connections in the pool
                           max_overflow=50,  # Maximum number of connections that can be created beyond the pool_size
                           pool_timeout=30,  # Timeout value in seconds for acquiring a connection from the pool
                           pool_recycle=1800,  # Recycle connections after this number of seconds (optional)
                           pool_pre_ping=False,  # Enable connection health checks (optional)
                           )

    # Test the connection
    try:
        connection = engine.connect()
        logger.info("Connected to the database! @ " + database_url)
        connection.close()
    except Exception as error:
        logger.error(f"Unable to connect to the database:{error}")
    return engine
