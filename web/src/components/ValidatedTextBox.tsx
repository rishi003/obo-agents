import {
  FormControl,
  Input,
  FormLabel,
  FormErrorMessage,
  Text,
} from '@chakra-ui/react';
import { Field } from 'formik';
import React from 'react';

interface ValidatedTextFieldProps {
  name: string;
  label: string;
  placeholder?: string;
}

const ValidatedTextField: React.FC<ValidatedTextFieldProps> = ({
  name,
  label,
  placeholder,
}) => {
  return (
    <Field name={name}>
      {({ field, form, meta }: any) => (
        <FormControl isInvalid={form.errors[name] && form.touched[name]}>
          <FormLabel htmlFor={name}>{label}</FormLabel>
          <Input
            {...field}
            id={name}
            placeholder={placeholder}
            focusBorderColor="blackAlpha.800"
            errorBorderColor="crimson"
          />
          <FormErrorMessage>
            <Text fontSize={'xs'} textColor={'crimson'}>
              {form.errors[name]}
            </Text>
          </FormErrorMessage>
        </FormControl>
      )}
    </Field>
  );
};

export default ValidatedTextField;
