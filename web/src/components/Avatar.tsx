import {
  Flex,
  Heading,
  Avatar as ChakraAvatar,
  SkeletonCircle,
  Skeleton,
} from '@chakra-ui/react';
import { faPowerOff } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { signOut } from 'next-auth/react';
import * as React from 'react';

export const Avatar = ({
  username,
  image,
}: {
  username: string;
  image: string;
}) => {
  return (
    <Flex direction={'row'}>
      <Flex me={'6'} style={{ position: 'relative' }} alignItems={'center'}>
        <ChakraAvatar size={'lg'} src={image} />

        <FontAwesomeIcon
          icon={faPowerOff}
          style={{
            position: 'absolute',
            bottom: -2,
            right: -2,
            cursor: 'pointer',
            backgroundColor: 'white',
            borderRadius: '50%',
            padding: 3,
          }}
          size="xl"
          onClick={() => signOut()}
        />
      </Flex>
      <Heading color={'black'} size={'md'} lineHeight={'short'}>
        {getGreeting()}
        <br />
        {username.split(' ')[0]}
      </Heading>
    </Flex>
  );
};

const getGreeting = () => {
  var now = new Date();
  var hour = now.getHours();

  if (hour >= 5 && hour < 12) {
    return 'Good morning,';
  } else if (hour >= 12 && hour < 18) {
    return 'Good afternoon,';
  } else {
    return 'Good evening,';
  }
};
