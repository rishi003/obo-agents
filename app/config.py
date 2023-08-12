class Config:
    """Configuration class for the app."""

    DOCS_DIR = "app/docstore"

    DATABASE_URL = "sqlite:///obo-agents.db"
    MQTT_BROKER_URL = "amqp://localhost"
    MQTT_BACKEND_URL = "rpc://localhost"

    EMBEDDING_MODEL = "BAAI/bge-small-en"
