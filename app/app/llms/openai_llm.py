from typing import Any, Dict
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

def load_llm(model: str='gpt-3.5-turbo', temperature: float=0.7, **kwargs: Dict[str, Any]) -> ChatOpenAI:
    llm = ChatOpenAI(model=model, temperature=temperature, **kwargs)
    return llm
    