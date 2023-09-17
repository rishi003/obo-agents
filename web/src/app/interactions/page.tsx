'use client';
import {
  createChat,
  createMessage,
  getChatsForUser,
} from '@/api/actions/actions';
import Button from '@/components/Button';
import TextBox from '@/components/TextBox';
import ValidatedTextField from '@/components/ValidatedTextBox';
import PrimaryContainer from '@/composables/containers/PrimaryContainer';
import useChatStore from '@/state/store/chat.store';
import useUserStore from '@/state/store/user.store';
import { Box, Flex, List, ListItem } from '@chakra-ui/react';
import {
  faComment,
  faCommentAlt,
  faCommentDots,
  faPlug,
  faPlus,
} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { Form, Formik } from 'formik';
import { useEffect, useState } from 'react';
import * as Yup from 'yup';

interface Message {
  content: string;
  byAgent: boolean;
}

const Interactions = () => {
  const [message, setMessage] = useState('');
  const [messages, setMessages] = useState<Message[]>([]);
  const userId = useUserStore((state) => state.id);
  const { chats, setActiveChat, setChats, activeChat } = useChatStore();

  const fetchChats = async () => {
    const res = await getChatsForUser(userId);
    if (res.status === 200) {
      setChats(res.data);
    }
  };

  useEffect(() => {
    fetchChats();
  }, []);

  const messageSubmit = () => {
    setMessages((prev) => [...prev, { content: message, byAgent: false }]);
    activeChat?.id &&
      createMessage(activeChat?.id, message, userId).then((res) => {
        setMessages((prev) => [
          ...prev,
          { content: res.data.content, byAgent: true },
        ]);
        setMessage('');
      });
  };

  const createChatSubmit = (values: any, actions: any) => {
    createChat(userId).then((res) => {});
  };

  return (
    <PrimaryContainer>
      <Box w={'full'} h={'full'}>
        <Flex w={'full'} h={'full'}>
          <Box flex={1.5}>
            <List>
              <ListItem key={'create-chat'} mb={12}>
                <Formik initialValues={{}} onSubmit={createChatSubmit}>
                  <Form>
                    <Flex gap={2} direction={'column'}>
                      <Button
                        type="solid"
                        isSubmit={true}
                        rightIcon={<FontAwesomeIcon icon={faPlus} />}
                      >
                        New Chat
                      </Button>
                    </Flex>
                  </Form>
                </Formik>
              </ListItem>
              {chats.map((chat) => (
                <ChatItem
                  key={chat.id}
                  active={chat.active}
                  onClick={() => setActiveChat(chat.id)}
                >
                  {chat.name}
                </ChatItem>
              ))}
            </List>
          </Box>
          <Box flex={10} h={'full'} ms={6}>
            <Flex direction={'column'} h={'full'}>
              <Box
                flex={10}
                bgColor={'blackAlpha.100'}
                m={2}
                p={2}
                borderRadius={'md'}
              >
                {messages.map((message, index) => (
                  <Flex alignItems={'center'}>
                    <Box me={2}>{message.byAgent ? '' : 'You: '}</Box>
                    <Box
                      key={index}
                      bgColor={message.byAgent ? 'blackAlpha.300' : ''}
                      padding={'2'}
                      borderRadius={'md'}
                    >
                      {message.content}
                    </Box>
                  </Flex>
                ))}
              </Box>
              <Box flex={1}>
                <Flex direction={'row'} gap={2} alignItems={'center'} mb={6}>
                  <TextBox
                    name="message"
                    type="text"
                    onChange={setMessage}
                    value={message}
                  />
                  <Button
                    type="solid"
                    isSubmit={true}
                    onClick={() => {
                      messageSubmit();
                    }}
                  >
                    Send
                  </Button>
                </Flex>
              </Box>
            </Flex>
          </Box>
        </Flex>
      </Box>
    </PrimaryContainer>
  );
};

const ChatItem = (props: {
  children: React.ReactNode;
  active?: boolean;
  onClick: () => void;
}) => {
  return (
    <ListItem
      cursor={'pointer'}
      py={'2.5'}
      px={'3'}
      my={'2'}
      bgColor={props.active ? 'blackAlpha.800' : ''}
      color={props.active ? 'white' : 'black'}
      borderRadius={'md'}
      onClick={props.onClick}
    >
      <Flex justifyContent={'flex-start'} alignItems={'center'} gap={2}>
        <FontAwesomeIcon icon={faCommentAlt} />
        {props.children}
      </Flex>
    </ListItem>
  );
};

export default Interactions;
