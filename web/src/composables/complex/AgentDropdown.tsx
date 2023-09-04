import Button from '@/components/Button';
import { Dropdown } from '@/components/Dropdown';
import useAgentStore from '@/state/store/agent.store';
import { MenuItem, useDisclosure } from '@chakra-ui/react';
import { faPlus } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import CreateAgentForm from '../forms/CreateAgentForm';
import { useEffect, useState } from 'react';

const AgentsDropdown = () => {
  const agent = useAgentStore((state) => state.activeAgent);
  const [ready, setReady] = useState(false);

  useEffect(() => {
    if (agent?.name) {
      setReady(true);
    }
  }, [agent]);

  const { isOpen, onClose, onOpen } = useDisclosure();

  return ready ? (
    <Dropdown title={agent?.name}>
      <MenuItem>Change</MenuItem>
    </Dropdown>
  ) : (
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
};

export default AgentsDropdown;
