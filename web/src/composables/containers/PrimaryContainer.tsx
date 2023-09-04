'use client';
import { Box, Flex, MenuItem } from '@chakra-ui/react';
import SideNav from '@/components/SideNav';
import { Avatar } from '@/components/Avatar';
import { useSession } from 'next-auth/react';
import AgentsDropdown from '@/composables/complex/AgentDropdown';
import useUserStore from '@/state/store/user.store';
import { useEffect } from 'react';
import { getUserFromEmail } from '@/api/actions/actions';

const PrimaryContainer = ({ children }: { children: React.ReactNode }) => {
  const { data: session } = useSession();
  const setUser = useUserStore((state) => state.setUser);

  const getUserDetails = async (email: string) => {
    const res = await getUserFromEmail(email);
    const user = {
      id: res.data.id,
      name: res.data.name,
      email: res.data.email,
    };
    return user;
  };
  useEffect(() => {
    if (session) {
      getUserDetails(session?.user?.email as string).then((user) =>
        setUser({ ...user })
      );
    }
  }, [session]);
  return (
    <Box p={4} minH="100vh">
      <Flex minH="100vh">
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
