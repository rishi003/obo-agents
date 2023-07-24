'use client';
import { Box } from '@chakra-ui/react';
import SideNav from '@/components/SideNav';

export default function Home() {
  return (
    <Box p={'4'} backgroundColor={'purple.600'} h="100vh">
      <SideNav />
    </Box>
  );
}
