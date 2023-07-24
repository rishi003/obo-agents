'use client';
import {
  Flex,
  Box,
  Heading,
  Stack,
  InputGroup,
  InputLeftElement,
  Input,
  InputRightElement,
  Button,
} from '@chakra-ui/react';
import { signIn } from 'next-auth/react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGithub } from '@fortawesome/free-brands-svg-icons';
import {
  EnvelopeIcon,
  KeyIcon,
  EyeSlashIcon,
  EyeIcon,
} from '@heroicons/react/24/outline';
import { useState } from 'react';
import Link from 'next/link';
import { useSearchParams } from 'next/navigation';
export default function SignIn() {
  const [visible, setVisible] = useState(false);
  const searchParams = useSearchParams();
  const callbackUrl = (searchParams.get('callbackUrl') as string) ?? '/';
  return (
    <Flex direction={'row'}>
      <Box width={'35vw'}>
        <Flex
          alignItems={'start'}
          justifyContent={'center'}
          height={'100vh'}
          mx={'52'}
          direction={'column'}
          rowGap={'8'}
        >
          <Heading>Log In</Heading>
          <Stack width={'100%'}>
            <InputGroup>
              <InputLeftElement pointerEvents="none">
                <EnvelopeIcon height={'20'} />
              </InputLeftElement>
              <Input type="email" placeholder="Email" />
            </InputGroup>
            <InputGroup>
              <InputLeftElement pointerEvents="none">
                <KeyIcon height={'20'} />
              </InputLeftElement>
              <InputRightElement
                onClick={() => setVisible((visible) => !visible)}
              >
                {visible ? (
                  <EyeSlashIcon height={'20'} />
                ) : (
                  <EyeIcon height={'20'} />
                )}
              </InputRightElement>
              <Input
                type={visible ? 'text' : 'password'}
                placeholder="Password"
              />
            </InputGroup>
          </Stack>
          <Stack width={'100%'}>
            <Button background={'purple.600'} color={'white'}>
              Log In
            </Button>
            <Button
              leftIcon={<FontAwesomeIcon icon={faGithub} />}
              background={'white'}
              color={'black'}
              border={'1px'}
              borderColor={'gray.200'}
              onClick={() => {
                signIn('github', { callbackUrl: callbackUrl });
              }}
            >
              Sign In with Github
            </Button>
          </Stack>
        </Flex>
      </Box>
      <Box
        bgImage="url('/images/login-signup.jpg')"
        bgPosition="center"
        bgSize={'cover'}
        bgRepeat="no-repeat"
        width={'65vw'}
        height={'100vh'}
      >
        <Box></Box>
      </Box>
    </Flex>
  );
}
