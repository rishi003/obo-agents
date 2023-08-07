'use client';
import { Heading, Stack, Text } from '@chakra-ui/react';
import { signIn, useSession } from 'next-auth/react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {
  faGithub,
  faMicrosoft,
  faGoogle,
} from '@fortawesome/free-brands-svg-icons';
import { EnvelopeIcon } from '@heroicons/react/24/outline';
import { useRouter, useSearchParams } from 'next/navigation';
import Button from '@/components/Button';
import TextBox from '@/components/TextBox';
import { useState } from 'react';
const SignIn = () => {
  const [email, setEmail] = useState('');
  const { status: status } = useSession();
  const router = useRouter();
  const searchParams = useSearchParams();
  const callbackUrl = (searchParams.get('callbackUrl') as string) ?? '/';
  if (status === 'authenticated') {
    router.push(callbackUrl);
  }
  return (
    <>
      <Heading>Log In</Heading>
      <Stack width={'100%'}>
        <TextBox
          type="email"
          placeholder="Email"
          name="email"
          leftIcon={<EnvelopeIcon height={'20'} />}
          onChange={(value) => setEmail(value)}
        />
        <Button
          type={'outline'}
          onClick={() => {
            signIn('email', { email, callbackUrl });
          }}
        >
          Log In
        </Button>
      </Stack>
      <Text align={'center'} fontWeight={'bold'} w={'100%'}>
        or
      </Text>
      <Stack width={'100%'}>
        <Button
          leftIcon={<FontAwesomeIcon icon={faGoogle} />}
          type={'solid'}
          onClick={() => {
            signIn('github', { callbackUrl: callbackUrl });
          }}
        >
          Sign In with Google
        </Button>
        <Button
          leftIcon={<FontAwesomeIcon icon={faMicrosoft} />}
          type={'solid'}
          onClick={() => {
            signIn('github', { callbackUrl: callbackUrl });
          }}
        >
          Sign In with Outlook
        </Button>
        <Button
          leftIcon={<FontAwesomeIcon icon={faGithub} />}
          type={'solid'}
          onClick={() => {
            signIn('github', { callbackUrl: callbackUrl });
          }}
        >
          Sign In with Github
        </Button>
      </Stack>
    </>
  );
};

export default SignIn;
