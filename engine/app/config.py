class Config:
    """Configuration class for the app."""

    DOCS_DIR = "app/docstore"
    SPLIT_CHUNK_SIZE = 500
    SPLIT_CHUNK_OVERLAP = 100

    DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost/obo"
    MQTT_BROKER_URL = "amqp://localhost"
    MQTT_BACKEND_URL = "rpc://localhost"

    EMBEDDING_MODEL = "BAAI/bge-small-en"

    VECTOR_STORE_TOPK = 3

    CHAT_HISTORY_MESSAGE_LIMIT = 4
