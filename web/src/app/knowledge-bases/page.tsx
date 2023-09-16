'use client';
import { uploadDocument } from '@/api/actions/actions';
import Button from '@/components/Button';
import PrimaryContainer from '@/composables/containers/PrimaryContainer';
import useUserStore from '@/state/store/user.store';
import {
  Box,
  FormControl,
  Grid,
  Input,
  Tab,
  TabList,
  TabPanel,
  TabPanels,
  Tabs,
} from '@chakra-ui/react';
import { useFormik } from 'formik';
import { useState } from 'react';

const KnowledgeBases = () => {
  const userId = useUserStore((state) => state.id);
  const [fileName, setFileName] = useState('');
  const [fileType, setFileType] = useState('');
  const formik = useFormik({
    initialValues: {
      file: '',
    },
    onSubmit: (values) => {
      uploadDocument(userId, values.file, fileName, fileType);
    },
  });

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
              <Box>
                <Box>
                  <form onSubmit={formik.handleSubmit}>
                    <FormControl>
                      <Input
                        type="file"
                        name="file"
                        onChange={(e) => {
                          formik.setFieldValue('file', e.target.files![0]);
                          setFileName(e.target.files![0].name);
                          setFileType(e.target.files![0].type.split('/')[1]);
                        }}
                      />
                    </FormControl>

                    <Button isSubmit type="solid">
                      Upload
                    </Button>
                  </form>
                </Box>
                <Grid></Grid>
              </Box>
            </TabPanel>
          </TabPanels>
        </Tabs>
      </Box>
    </PrimaryContainer>
  );
};

export default KnowledgeBases;
