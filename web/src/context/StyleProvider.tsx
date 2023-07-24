'use client';
import { CacheProvider } from '@chakra-ui/next-js';
import { ChakraProvider, Box } from '@chakra-ui/react';

export default function StyleProvider({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <CacheProvider>
      <ChakraProvider>
      <Box p={'4'} backgroundColor={'purple.600'} h="100vh">
              {children}
            </Box>
      </ChakraProvider>
    </CacheProvider>
  );
}
