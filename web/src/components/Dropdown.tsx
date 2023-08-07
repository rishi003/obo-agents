import * as React from 'react';
import { ChevronDownIcon } from '@chakra-ui/icons';
import { Menu, MenuButton, Button, MenuList, Box } from '@chakra-ui/react';

export const Dropdown = (props: { children: React.ReactNode }) => {
  return (
    <Box>
      <Menu>
        <MenuButton
          as={Button}
          rightIcon={<ChevronDownIcon />}
          w={'full'}
          textAlign={'left'}
          variant={'outline'}
          colorScheme={'black'}
          color={'black'}
          border={'2px'}
          borderRadius={'md'}
          p={'1.4rem'}
        >
          Geoffery
        </MenuButton>
        <MenuList>{props.children}</MenuList>
      </Menu>
    </Box>
  );
};
