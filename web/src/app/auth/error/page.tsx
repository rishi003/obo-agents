'use client';
import { Box, Flex, Heading, Text } from '@chakra-ui/react';

const Error = () => {
  return (
    <>
      <Flex
        alignItems={'center'}
        justifyContent={'center'}
        direction={'column'}
      >
        <Heading>Opps!</Heading>
        <Text fontSize={'xl'} fontWeight={'bold'}>
          Authentication is not working properly.
        </Text>
      </Flex>
    </>
  );
};

export default Error;
