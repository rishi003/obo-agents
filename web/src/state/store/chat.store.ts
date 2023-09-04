import { create } from 'zustand';
import { devtools } from 'zustand/middleware';

interface Chat {
  id: string;
  name: string;
  active: boolean;
}

interface ChatState {
  chats: Chat[];
  activeChat: Chat | undefined;
  setActiveChat: (id: string) => void;
  setChats: (chats: Chat[]) => void;
}

const useChatStore = create<ChatState>()(
  devtools((set) => ({
    chats: [],
    activeChat: undefined,
    setChats: (chats) => set({ chats }),
    setActiveChat: (id) =>
      set((state) => ({
        chats: state.chats.map((chat) => ({ ...chat, active: chat.id === id })),
        activeChat: state.chats.find((chat) => chat.id === id),
      })),
  }))
);

export default useChatStore;
