import Button from '@/components/Button';
import { Dropdown } from '@/components/Dropdown';
import useAgentStore from '@/state/store/agent.store';
import { MenuItem, useDisclosure } from '@chakra-ui/react';
import { faPlus } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import CreateAgentForm from '../forms/CreateAgentForm';

const AgentsDropdown = () => {
  const agent = useAgentStore((state) => state.activeAgent);

  console.log(agent);

  const { isOpen, onClose, onOpen } = useDisclosure();

  if (agent?.name) {
    return (
      <Dropdown title={agent.name}>
        <MenuItem>Change</MenuItem>
      </Dropdown>
    );
  } else {
    return (
      <>
        <Button
          rightIcon={<FontAwesomeIcon icon={faPlus} />}
          type="solid"
          onClick={onOpen}
        >
          Add Agent
        </Button>
        <CreateAgentForm isOpen={isOpen} onClose={onClose} onOpen={onOpen} />
      </>
    );
  }
};

export default AgentsDropdown;
