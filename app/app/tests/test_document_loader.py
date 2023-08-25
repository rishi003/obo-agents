from sqlalchemy.orm import sessionmaker

from app.document_manager.document_loader import DocLoader
from app.models.db import connect_db

def test_doc_loader():
    engine = connect_db()
    Session = sessionmaker(bind=engine)
    session = Session()
    doc_id = "90f1698c-9cc3-434d-89c6-519babbe0e6f"
    docs = DocLoader(session, doc_id).load_document()
    print(docs)
    assert docs[0].metadata["document_id"] == doc_id