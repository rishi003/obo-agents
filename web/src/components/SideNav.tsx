'use client';
import { Box, Flex, Stack, Text } from '@chakra-ui/react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {
  faChartBar,
  faWrench,
  faCubesStacked,
  faBookmark,
  faRepeat,
} from '@fortawesome/free-solid-svg-icons';
import { usePathname } from 'next/navigation';

export default function SideNav() {
  const pathname = usePathname();

  return (
    <Box>
      <Stack gap={4}>
        <SideNavItem
          text={'Dashboard'}
          icon={faChartBar}
          isActive={pathname === '/'}
        />
        <SideNavItem
          text={'Tool Chain'}
          icon={faWrench}
          isActive={pathname === '/tool-chain'}
        />
        <SideNavItem
          text={'Workflows'}
          icon={faCubesStacked}
          isActive={pathname === '/workflows'}
        />
        <SideNavItem
          text={'Knowledge Bases'}
          icon={faBookmark}
          isActive={pathname === '/knowledge-bases'}
        />
        <SideNavItem
          text={'Interactions'}
          icon={faRepeat}
          isActive={pathname === '/interactions'}
        />
      </Stack>
    </Box>
  );
}

function SideNavItem({
  text,
  icon,
  isActive,
}: {
  text: string;
  icon: any;
  isActive?: boolean;
}) {
  return (
    <Flex
      alignItems={'center'}
      gap={2}
      borderRadius={'md'}
      backgroundColor={isActive ? 'whiteAlpha.400' : ''}
      py={'2'}
      px={'4'}
      cursor={'pointer'}
    >
      <FontAwesomeIcon icon={icon} color="white" />
      <Text color="white">{text}</Text>
    </Flex>
  );
}
