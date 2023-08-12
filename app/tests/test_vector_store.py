from app.vector_store.chromadb_vs import ChromaDB
from app.vector_store.embedding.hf_emb import HuggingfaceEmbedding
from sentence_transformers import util

def test_hf_emb():
    embedding_model = HuggingfaceEmbedding()
    query_1 = "The man is playing the piano"
    query_2 = "The man is playing the guitar"
    embed_1 = embedding_model.get_embedding_query(query_1)
    embed_2 = embedding_model.get_embedding_query(query_2)
    score = util.cos_sim(embed_1, embed_2)
    print(score)
    assert score > 0.7, "Embeddings are not similar, use a different model"

def test_chroma():
    embedding_model = HuggingfaceEmbedding()
    chroma_db = ChromaDB(
        collection_name="test_collection",
        embedding_model=embedding_model,
        text_field="test_field",
        namespace="test_namespace",
    )
    print(chroma_db.collection)
    docs = [
        "A man is playing the piano",
        "A man is playing the violin",
        "The sky is blue",
        "The sun is shining"
    ]
    # ids = chroma_db.add_texts(docs)
    matching_docs = chroma_db.get_matching_text("A man is playing the guitar")
    print(matching_docs)
    assert docs[0] in [doc.page_content for doc in matching_docs]
    matching_docs = chroma_db.get_matching_text("The sky is yellow")
    print(matching_docs)
    assert docs[2] in [doc.page_content for doc in matching_docs]
    
def test_chroma_deletion():
    embedding_model = HuggingfaceEmbedding()
    chroma_db = ChromaDB(
        collection_name="test_collection",
        embedding_model=embedding_model,
        text_field="test_field",
    )
    docs = [
        "A man is playing the piano",
        "A man is playing the violin",
        "The sky is blue",
        "The sun is shining"
    ]
    metadatas = [{"test_field": "test_id"} for _ in docs]
    ids = chroma_db.add_texts(docs, metadatas)
    emb_count = chroma_db.get_index_stats()
    print(emb_count)
    chroma_db.delete_embeddings_from_vector_db(where={"test_field": "test_id"})
    emb_count = chroma_db.get_index_stats()
    print(emb_count)
    assert emb_count["embeddings_count"] == 0, "Embeddings are not deleted"
