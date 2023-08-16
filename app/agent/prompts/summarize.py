from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

system_message = "You are a helpful assistant that Summarizes the conversation provided between a buyer and seller from the chat history. The summary should be from {role} point of view in first person. The summary should be detailed and precise."
system_message_prompt = SystemMessagePromptTemplate.from_template(system_message)

human_message = "Summarize the following conversation.\nCHAT HISTORY:\n{chat_history}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_message)

summarize_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

# Usage
# summarize_prompt.format_prompt(role="", chat_history="").to_messages()
