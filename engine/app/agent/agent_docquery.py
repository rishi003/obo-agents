import uuid
from langchain.chains import LLMChain
from langchain.callbacks import get_openai_callback

from app.agent.prompts.docqa import chat_prompt_docqa
from app.llms.openai_llm import load_llm
from app.vector_store.embedding.hf_emb import HuggingfaceEmbedding
from app.vector_store.chromadb_vs import ChromaDB
from app.models.message import Message
from app.config import Config
from fastapi_sqlalchemy import db

EMBEDDING_MODEL = HuggingfaceEmbedding()

def run_query(user_id: str, chat_id: str, query: str, db_session: db) -> str:
    """
    Run a document question answering query.
    
    Args:
        user_id (str): Identifier of the associated user.
        chat_id (str): Identifier of the associated chat.
        query (str): Question to be answered.
        db_session (db): Database session
    
    Returns:
        str: Answer to the question
    """
    llm = load_llm(temperature=0.2)
    chain = LLMChain(llm=llm, prompt=chat_prompt_docqa)
    vector_store = ChromaDB(collection_name=user_id,
                            embedding_model=EMBEDDING_MODEL,
                            text_field="document_id")
    matching_docs = vector_store.get_matching_text(query)
    docs_content = [doc.page_content for doc in matching_docs]
    messages = db_session.session.query(Message).filter(Message.chatId == chat_id).all()
    # Consider the last N messages
    chat_history = ""
    if len(messages) > 1:
        messages = messages[-Config.CHAT_HISTORY_MESSAGE_LIMIT:]
        for message in messages:
            role = "AI" if message.byAgent else "USER"
            chat_history += f"{role}: {message.content}\n"
    if docs_content:
        with get_openai_callback() as cb:
            response = chain({
                "chat_history": chat_history,
                "context": "\n\n".join(docs_content),
                "question": query
            })
            input_tokens = cb.prompt_tokens
            output_tokens = cb.completion_tokens
            total_cost = cb.total_cost
    else:
        response = {"text": "I don't know"}
    db_message = Message(id=str(uuid.uuid4()), userId=user_id, chatId=chat_id, content=response["text"],
                         byAgent=True, inputTokens=input_tokens,
                         outputTokens=output_tokens, totalCost=total_cost)
    db_session.session.add(db_message)
    db_session.session.commit()
    
    return db_message
