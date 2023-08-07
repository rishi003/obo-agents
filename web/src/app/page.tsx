'use client';
import { Box, Flex, MenuItem } from '@chakra-ui/react';
import SideNav from '@/components/SideNav';
import { Dropdown } from '@/components/Dropdown';
import { Avatar } from '@/components/Avatar';

export default function Home() {
  return (
    <Box p={4}>
      <Flex>
        <Box me={'8'}>
          <Flex direction={'column'} gap={'16'}>
            <Avatar />
            <Dropdown>
              <MenuItem>Download</MenuItem>
              <MenuItem>Create a Copy</MenuItem>
              <MenuItem>Mark as Draft</MenuItem>
              <MenuItem>Delete</MenuItem>
              <MenuItem>Attend a Workshop</MenuItem>
            </Dropdown>
            <SideNav />
          </Flex>
        </Box>
        <Box>Dashboard</Box>
      </Flex>
    </Box>
  );
}
