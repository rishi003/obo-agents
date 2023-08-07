'use client';
import Button from '@/components/Button';
import TextBox from '@/components/TextBox';
import { Flex, Heading, Stack, Text } from '@chakra-ui/react';
import { useSession } from 'next-auth/react';
import { useState } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';
import { updateUserName } from './update-user-action';

const NewUser = () => {
  const { data: session } = useSession();
  const [username, setUsername] = useState('');
  const router = useRouter();
  const searchParams = useSearchParams();
  const callbackUrl = (searchParams.get('callbackUrl') as string) ?? '/';

  return (
    <>
      <Flex justifyContent={'center'} direction={'column'}>
        <Heading>Hold On!</Heading>
        <Text fontSize={'xl'} fontWeight={'bold'}>
          What should we call you?
        </Text>
        <Stack>
          <TextBox name="name" type="text" onChange={setUsername} />
          <Button
            type="outline"
            onClick={() => {
              updateUserName(username, session?.user?.email as string).then(
                () => {
                  router.push(callbackUrl);
                }
              );
            }}
          >
            {"Let's Go!"}
          </Button>
        </Stack>
      </Flex>
    </>
  );
};

export default NewUser;
