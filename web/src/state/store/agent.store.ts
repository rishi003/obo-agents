import { create } from 'zustand';
import { persist, devtools } from 'zustand/middleware';

interface AgentState {
  agents: any[];
  activeAgent: any;
  addAgent: (agent: any) => void;
  removeAgent: (agent: any) => void;
  setActiveAgent: (agent: any) => void;
}

const useAgentStore = create<AgentState>()(
  devtools(
    persist(
      (set) => ({
        agents: [],
        activeAgent: {},
        addAgent: (agent) =>
          set((state) => ({ agents: [...state.agents, agent] })),
        removeAgent: (agent) =>
          set((state) => ({
            agents: state.agents.filter((a) => a.id !== agent.id),
          })),
        setActiveAgent: (agent) => set({ activeAgent: agent }),
      }),
      { name: 'agent-store' }
    )
  )
);

export default useAgentStore;
