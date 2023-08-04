'use client';
import {
  Flex,
  Box,
  Heading,
  Stack,
  Text,
  useMediaQuery,
} from '@chakra-ui/react';
import { signIn } from 'next-auth/react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {
  faGithub,
  faMicrosoft,
  faGoogle,
} from '@fortawesome/free-brands-svg-icons';
import { EnvelopeIcon } from '@heroicons/react/24/outline';
import { useSearchParams } from 'next/navigation';
import Button from '@/components/Button';
import TextBox from '@/components/TextBox';
const SignIn = () => {
  const searchParams = useSearchParams();
  const callbackUrl = (searchParams.get('callbackUrl') as string) ?? '/';
  return (
    <>
      <Heading>Log In</Heading>
      <Stack width={'100%'}>
        <TextBox
          type="email"
          placeholder="Email"
          leftIcon={<EnvelopeIcon height={'20'} />}
        />
        <TextBox type="password" />
      </Stack>
      <Stack width={'100%'}>
        <Button
          type={'outline'}
          onClick={() => {
            console.log('click');
          }}
        >
          Log In
        </Button>
        <Text align={'center'} fontWeight={'bold'}>
          or
        </Text>
        <Button
          leftIcon={<FontAwesomeIcon icon={faGithub} />}
          type={'solid'}
          onClick={() => {
            signIn('github', { callbackUrl: callbackUrl });
          }}
        >
          Sign In with Github
        </Button>
        <Button
          leftIcon={<FontAwesomeIcon icon={faMicrosoft} />}
          type={'solid'}
          onClick={() => {
            signIn('github', { callbackUrl: callbackUrl });
          }}
        >
          Sign In with Microsoft
        </Button>
        <Button
          leftIcon={<FontAwesomeIcon icon={faGoogle} />}
          type={'solid'}
          onClick={() => {
            signIn('github', { callbackUrl: callbackUrl });
          }}
        >
          Sign In with Google
        </Button>
      </Stack>
    </>
  );
};

export default SignIn;
