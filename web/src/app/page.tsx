'use client';
import {
  Avatar,
  Box,
  Button,
  Flex,
  Heading,
  Menu,
  MenuButton,
  MenuItem,
  MenuList,
} from '@chakra-ui/react';
import SideNav from '@/components/SideNav';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGear } from '@fortawesome/free-solid-svg-icons';
import { ChevronDownIcon } from '@chakra-ui/icons';

export default function Home() {
  return (
    <Box>
      <Flex>
        <Box me={'8'}>
          <Flex direction={'column'} gap={'16'}>
            <Flex direction={'row'}>
              <Flex
                me={'6'}
                style={{ position: 'relative' }}
                alignItems={'center'}
              >
                <Avatar size={'lg'} />
                <FontAwesomeIcon
                  icon={faGear}
                  color="white"
                  style={{ position: 'absolute', bottom: -2, right: -2 }}
                  size="xl"
                />
              </Flex>
              <Heading color={'white'} size={'md'} lineHeight={'short'}>
                Good Morning,
                <br /> Rishabh!
              </Heading>
            </Flex>
            <Box>
              <Menu>
                <MenuButton
                  as={Button}
                  rightIcon={<ChevronDownIcon />}
                  w={'full'}
                  textAlign={'left'}
                  variant={'outline'}
                  colorScheme={'white'}
                  color={'white'}
                >
                  Geoffery
                </MenuButton>
                <MenuList>
                  <MenuItem>Download</MenuItem>
                  <MenuItem>Create a Copy</MenuItem>
                  <MenuItem>Mark as Draft</MenuItem>
                  <MenuItem>Delete</MenuItem>
                  <MenuItem>Attend a Workshop</MenuItem>
                </MenuList>
              </Menu>
            </Box>
            <SideNav />
          </Flex>
        </Box>
        <Box>Dashboard</Box>
      </Flex>
    </Box>
  );
}
