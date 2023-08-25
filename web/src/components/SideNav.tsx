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
import Link from 'next/link';

export default function SideNav() {
  const pathname = usePathname();

  return (
    <Box>
      <Stack gap={4}>
        <SideNavItem
          text={'Dashboard'}
          link={'/'}
          icon={faChartBar}
          isActive={pathname === '/'}
        />
        <SideNavItem
          text={'Tool Chain'}
          link={'/tool-chain'}
          icon={faWrench}
          isActive={pathname === '/tool-chain'}
        />
        <SideNavItem
          text={'Workflows'}
          link={'/workflows'}
          icon={faCubesStacked}
          isActive={pathname === '/workflows'}
        />
        <SideNavItem
          text={'Knowledge Bases'}
          link={'/knowledge-bases'}
          icon={faBookmark}
          isActive={pathname === '/knowledge-bases'}
        />
        <SideNavItem
          text={'Interactions'}
          link={'/interactions'}
          icon={faRepeat}
          isActive={pathname === '/interactions'}
        />
      </Stack>
    </Box>
  );
}

function SideNavItem({
  text,
  link,
  icon,
  isActive,
}: {
  text: string;
  link :string
  icon: any;
  isActive?: boolean;
}) {
  return (
    <Flex
      alignItems={'center'}
      gap={2}
      borderRadius={'md'}
      backgroundColor={isActive ? 'black' : ''}
      py={'2'}
      px={'4'}
      cursor={'pointer'}
      _hover={{
        backgroundColor: isActive ? '' : 'blackAlpha.300',
      }}
    >
      <FontAwesomeIcon icon={icon} color={isActive ? 'white' : 'black'} />
      <Link href={link}>
        <Text color={isActive ? 'white' : 'black'}>{text}</Text>
      </Link>
    </Flex>
  );
}
