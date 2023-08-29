import { create } from 'zustand';
import { devtools, persist } from 'zustand/middleware';

interface UserState {
  id: string;
  name: string;
  email: string;
  setUser: ({
    id,
    name,
    email,
  }: {
    id: string;
    name: string;
    email: string;
  }) => void;
}

const useUserStore = create<UserState>()(
  devtools(
    persist(
      (set) => ({
        id: '',
        name: '',
        email: '',
        setUser: ({ id, name, email }) => set({ id, name, email }),
      }),
      {
        name: 'user-store',
      }
    )
  )
);

export default useUserStore;
