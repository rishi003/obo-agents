'use client';
import PrimaryContainer from '@/composables/containers/PrimaryContainer';
import {
  Box,
  Heading,
  Tab,
  TabList,
  TabPanel,
  TabPanels,
  Tabs,
} from '@chakra-ui/react';

const KnowledgeBases = () => {
  return (
    <PrimaryContainer>
      <Box>
        <Tabs isFitted>
          <TabList>
            <Tab
              _selected={{
                color: 'black',
                borderBottom: '2px solid black',
              }}
            >
              Files
            </Tab>
            <Tab
              _selected={{
                color: 'black',
                borderBottom: '2px solid black',
              }}
            >
              Web
            </Tab>
          </TabList>
          <TabPanels>
            <TabPanel>
              <Box></Box>
            </TabPanel>
          </TabPanels>
        </Tabs>
      </Box>
    </PrimaryContainer>
  );
};

export default KnowledgeBases;
