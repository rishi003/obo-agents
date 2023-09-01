import { create } from 'zustand';
import { persist, devtools } from 'zustand/middleware';

interface Agent {
  id: string;
  name: string;
}

interface AgentState {
  agents: Agent[];
  activeAgent: Agent | undefined;
  addAgent: (agent: Agent) => void;
  removeAgent: (id: string) => void;
  setActiveAgent: (id: string) => void;
}

const useAgentStore = create<AgentState>()(
  devtools(
    persist(
      (set) => ({
        agents: [],
        activeAgent: undefined,
        addAgent: (agent) =>
          set((state) => ({ agents: [...state.agents, agent] })),
        removeAgent: (id) =>
          set((state) => ({
            agents: state.agents.filter((a) => a.id !== id),
          })),
        setActiveAgent: (id) =>
          set((state) => ({
            activeAgent: state.agents.find((a) => a.id === id),
          })),
      }),
      { name: 'agent-store' }
    )
  )
);

export default useAgentStore;