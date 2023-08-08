'use client';
import { Box, Flex, useMediaQuery } from '@chakra-ui/react';
import React from 'react';

export default function AuthLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const [isMobile] = useMediaQuery('(max-width: 768px)');
  return (
    <Flex direction={'row'} justifyContent={'space-between'}>
      <Box
        width={{
          xl: '38vw',
          lg: '68vw',
          md: '100vw',
          sm: '100vw',
          xs: '100vw',
        }}
      >
        <Flex
          alignItems={'start'}
          justifyContent={'center'}
          height={'100vh'}
          mx={isMobile ? '8' : '36'}
          direction={'column'}
          rowGap={'8'}
        >
          {children}
        </Flex>
      </Box>

      <Box
        bgImage="url('/images/login-signup.jpg')"
        bgPosition="center"
        bgSize={'cover'}
        bgRepeat="no-repeat"
        width={'65vw'}
        height={'100vh'}
        display={isMobile ? 'none' : 'block'}
      >
        <Box></Box>
      </Box>
    </Flex>
  );
}
