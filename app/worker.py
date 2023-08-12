from datetime import timedelta
from celery import Celery
from sqlalchemy.orm import sessionmaker

from app.config import Config
from app.models.db import connect_db
from app.logger import logger

app = Celery("OBOagents", broker=Config.MQTT_BROKER_URL, backend=Config.MQTT_BACKEND_URL)
app.conf.worker_concurrency = 4
app.conf.accept_content = ['application/x-python-serialize', 'application/json']

beat_schedule = {
    'initialize-schedule-agent': {
        'task': 'initialize-schedule-agent',
        'schedule': timedelta(minutes=5),
    },
}
app.conf.beat_schedule = beat_schedule

@app.task(name="add_document", autoretry_for=(Exception,), retry_backoff=2, max_retries=5, serializer='pickle')
def add_document(agent_id: str, document_id: str):
    """Add a document in background."""
    from app.document_manager.document_loader import DocLoader
    from app.vector_store.embedding.hf_emb import HuggingfaceEmbedding
    from app.vector_store.chromadb_vs import ChromaDB

    engine = connect_db()
    Session = sessionmaker(bind=engine)
    session = Session()

    embedding_model = HuggingfaceEmbedding()
    vector_store = ChromaDB(collection_name=agent_id,
                            embedding_model=embedding_model,
                            text_field="text_content")
    docs = DocLoader(session, document_id).load_document()
    texts, metadatas = [], []
    for doc in docs:
        texts.append(doc.page_content)
        metadatas.append(doc.metadata)
    vector_store.add_texts(texts=texts, metadatas=metadatas)

    logger.info("Adding documents:" + agent_id + "," + document_id)
    session.close()

@app.task(name="remove_document", autoretry_for=(Exception,), retry_backoff=2, max_retries=5, serializer='pickle')
def remove_document(agent_id: str, document_id: str):
    """Delete a document in background."""
    from app.vector_store.embedding.hf_emb import HuggingfaceEmbedding
    from app.vector_store.chromadb_vs import ChromaDB

    engine = connect_db()
    Session = sessionmaker(bind=engine)
    session = Session()

    embedding_model = HuggingfaceEmbedding()
    vector_store = ChromaDB(collection_name=agent_id,
                            embedding_model=embedding_model,
                            text_field="text_content")
    vector_store.delete_embeddings_from_vector_db(where={"document_id": document_id})

    logger.info("Deleting documents:" + agent_id + "," + document_id)
    session.close()

@app.task(name="patch_document", autoretry_for=(Exception,), retry_backoff=2, max_retries=5, serializer='pickle')
def patch_document(agent_id: str, document_id: str):
    """Update a document in background."""
    from app.document_manager.document_loader import DocLoader
    from app.vector_store.embedding.hf_emb import HuggingfaceEmbedding
    from app.vector_store.chromadb_vs import ChromaDB

    engine = connect_db()
    Session = sessionmaker(bind=engine)
    session = Session()

    embedding_model = HuggingfaceEmbedding()
    vector_store = ChromaDB(collection_name=agent_id,
                            embedding_model=embedding_model,
                            text_field="text_content")
    vector_store.delete_embeddings_from_vector_db(where={"document_id": document_id})
    docs = DocLoader(session, document_id).load_document()
    texts, metadatas = [], []
    for doc in docs:
        texts.append(doc.page_content)
        metadatas.append(doc.metadata)
    vector_store.add_texts(texts=texts, metadatas=metadatas)


    logger.info("Updating documents:" + agent_id + "," + document_id)
    session.close()
