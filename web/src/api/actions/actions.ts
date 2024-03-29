import client from '../client';

export const getUserFromEmail = (email: string) => {
  return client.get(`/users/get/${email}`);
};

export const createAgent = (name: string, userId: string) => {
  return client.post(`/agents/add`, {
    name: name,
    userId: userId,
  });
};

export const getAgent = (agentId: string) => {
  return client.get(`/agents/get/${agentId}`);
};

export const deleteAgent = (agentId: string) => {
  return client.put(`/agents/delete/${agentId}`);
};

export const downloadDocument = (documentId: string) => {
  return client.get(`/documents/get/${documentId}`);
};

export const getAllDocumentsForUser = (userId: string) => {
  return client.get(`/documents/get/all/${userId}`);
};

export const uploadDocument = (
  userId: string,
  file: string,
  fileName: string,
  fileType: string
) => {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('name', fileName);
  formData.append('type', fileType);

  return client.post(`/documents/upload/${userId}`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
};

export const updateDocument = (
  documentId: string,
  userId: string,
  file: string,
  fileName: string,
  fileType: string
) => {
  return client.put(`/documents/update/${documentId}?user_id=${userId}`, {
    file: file,
    name: fileName,
    type: fileType,
  });
};

export const deleteDocument = (documentId: string, userId: string) => {
  return client.delete(`/documents/delete/${documentId}?user_id=${userId}`);
};

export const createChat = (userId: string) => {
  return client.post(`/chats/add`, {
    user_id: userId,
  });
};

export const getChatsForUser = (userId: string) => {
  return client.get(`/chats/get?user_id=${userId}`);
};

export const getChatMessages = (chatId: string) => {
  return client.get(`/chats/get/${chatId}/messages/`);
};

export const createMessage = (
  chatId: string,
  message: string,
  userId: string
) => {
  return client.post(`/chats/add/${chatId}/message/`, {
    user_id: userId,
    chat_id: chatId,
    content: message,
  });
};
