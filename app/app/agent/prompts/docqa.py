from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)

# A document question answering prompt
prompt = """
You are a helful assistant that can answer questions provided the context in an accurate and concise manner. Please answer as accurately and concisely as possible. 
If the answer is not available in the context, answer politely with "I don't know". Do not try to make up an answer.

Chat History:
{chat_history}

Context:
{context}

Question:
{question}
"""

prompt = HumanMessagePromptTemplate.from_template(prompt)
chat_prompt_docqa = ChatPromptTemplate.from_messages([prompt])