'use client';
import { Flex, Heading, Text } from '@chakra-ui/react';

const VerifyRequest = () => {
  return (
    <>
      <Flex
        alignItems={'center'}
        justifyContent={'center'}
        direction={'column'}
      >
        <Heading>Check your email</Heading>
        <Text fontSize={'xl'} fontWeight={'bold'}>
          Your Verification is pending.
        </Text>
      </Flex>
    </>
  );
};

export default VerifyRequest;
