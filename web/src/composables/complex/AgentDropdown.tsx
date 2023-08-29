import { Dropdown } from '@/components/Dropdown';
import useAgentStore from '@/state/store/agent.store';
import { MenuItem } from '@chakra-ui/react';

const AgentsDropdown = () => {
  const agent = useAgentStore((state) => state.activeAgent);
  return (
    <Dropdown title={agent?.name || ''}>
      <MenuItem>Download</MenuItem>
      <MenuItem>Create a Copy</MenuItem>
      <MenuItem>Mark as Draft</MenuItem>
      <MenuItem>Delete</MenuItem>
      <MenuItem>Attend a Workshop</MenuItem>
    </Dropdown>
  );
};

export default AgentsDropdown;
