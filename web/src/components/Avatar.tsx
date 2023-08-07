import { Flex, Heading, Avatar as ChakraAvatar } from '@chakra-ui/react';
import { faPowerOff } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { signOut } from 'next-auth/react';
import * as React from 'react';

export const Avatar = () => {
  return (
    <Flex direction={'row'}>
      <Flex me={'6'} style={{ position: 'relative' }} alignItems={'center'}>
        <ChakraAvatar size={'lg'} />
        <FontAwesomeIcon
          icon={faPowerOff}
          style={{
            position: 'absolute',
            bottom: -2,
            right: -2,
            cursor: 'pointer',
          }}
          size="xl"
          onClick={() => signOut()}
        />
      </Flex>
      <Heading color={'black'} size={'md'} lineHeight={'short'}>
        Good Morning,
        <br /> Rishabh!
      </Heading>
    </Flex>
  );
};
