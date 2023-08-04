'use client';
import theme from '@/theme';
import { CacheProvider } from '@chakra-ui/next-js';
import { ChakraProvider, Box } from '@chakra-ui/react';

export default function StyleProvider({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <CacheProvider>
      <ChakraProvider theme={theme}>
        <Box h="100vh">{children}</Box>
      </ChakraProvider>
    </CacheProvider>
  );
}
