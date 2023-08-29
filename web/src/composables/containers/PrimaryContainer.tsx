'use client';
import { Box, Flex, MenuItem } from '@chakra-ui/react';
import SideNav from '@/components/SideNav';
import { Avatar } from '@/components/Avatar';
import { useSession } from 'next-auth/react';
import AgentsDropdown from '@/composables/complex/AgentDropdown';

const PrimaryContainer = ({ children }: { children: React.ReactNode }) => {
  const { data: session } = useSession();
  return (
    <Box p={4}>
      <Flex>
        <Box me={'8'}>
          <Flex direction={'column'} gap={'16'}>
            <Avatar
              username={session?.user?.name || ''}
              image={session?.user?.image || ''}
            />
            <AgentsDropdown />
            <SideNav />
          </Flex>
        </Box>
        <Box w="100%">{children}</Box>
      </Flex>
    </Box>
  );
};

export default PrimaryContainer;
