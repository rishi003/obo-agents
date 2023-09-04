import { createAgent } from '@/api/actions/actions';
import Button from '@/components/Button';
import ValidatedTextField from '@/components/ValidatedTextBox';
import useAgentStore from '@/state/store/agent.store';
import useUserStore from '@/state/store/user.store';
import {
  Flex,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalFooter,
  ModalHeader,
  ModalOverlay,
} from '@chakra-ui/react';
import { faClose } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { Form, Formik } from 'formik';
import * as Yup from 'yup';

const CreateAgentForm = (props: {
  isOpen: boolean;
  onClose: () => void;
  onOpen: () => void;
}) => {
  const userId = useUserStore((state) => state.id);
  const agentStore = useAgentStore();
  const createAgentSchema = Yup.object().shape({
    name: Yup.string().required(),
  });

  const handleSubmit = (values: any, actions: any) => {
    createAgent(values.name, userId).then((res) => {
      agentStore.addAgent({ id: res.data.id, name: res.data.name });
      agentStore.setActiveAgent(res.data.id);
      props.onClose();
    });
  };

  return (
    <Modal isOpen={props.isOpen} onClose={props.onClose}>
      <ModalOverlay />
      <Formik
        initialValues={{ name: '' }}
        onSubmit={handleSubmit}
        validationSchema={createAgentSchema}
      >
        <Form>
          <ModalContent>
            <ModalHeader>Add Agent</ModalHeader>
            <ModalCloseButton />
            <ModalBody>
              <ValidatedTextField
                name="name"
                label="Agent Name"
                placeholder="Geoffery"
              />
            </ModalBody>
            <ModalFooter>
              <Flex gap={5}>
                <Button type="solid" isSubmit={true}>
                  Create
                </Button>
                <Button
                  type="outline"
                  onClick={props.onClose}
                  rightIcon={<FontAwesomeIcon icon={faClose} />}
                >
                  Cancel
                </Button>
              </Flex>
            </ModalFooter>
          </ModalContent>
        </Form>
      </Formik>
    </Modal>
  );
};

export default CreateAgentForm;
