import * as React from 'react';
import {
  Flex,
  Input,
  InputGroup,
  InputLeftElement,
  InputRightElement,
  Text,
} from '@chakra-ui/react';
import { EyeIcon, EyeSlashIcon, KeyIcon } from '@heroicons/react/24/outline';
import { useState } from 'react';

export default function TextBox(props: {
  isInValid?: boolean;
  type: 'email' | 'password' | 'text';
  name: string;
  onChange?: (value: string) => void;
  placeholder?: string;
  leftIcon?: any;
  rightIcon?: any;
  state?: 'error' | 'success';
  errorText?: string;
}) {
  const [visible, setVisible] = useState(false);
  const [errorTextVisible, setErrorTextVisible] = useState(true);
  const onFocusChange = () => {
    setErrorTextVisible((errorTextVisible) => !errorTextVisible);
  };

  const leftIcon = React.cloneElement(props.leftIcon, {
    height: 23,
  });

  const rightIcon =
    props.rightIcon &&
    React.cloneElement(props.rightIcon, {
      height: 23,
    });

  if (props.type === 'password') {
    return (
      <Flex direction={'column'}>
        <InputGroup>
          <InputLeftElement pointerEvents="none">
            <KeyIcon height={'23'} />
          </InputLeftElement>
          <InputRightElement onClick={() => setVisible((visible) => !visible)}>
            {visible ? (
              <EyeSlashIcon height={'23'} />
            ) : (
              <EyeIcon height={'23'} />
            )}
          </InputRightElement>
          <Input
            isInvalid={props.isInValid}
            type={visible ? 'text' : 'password'}
            placeholder="Password"
            focusBorderColor="blackAlpha.800"
            errorBorderColor="crimson"
            onFocus={onFocusChange}
            onBlur={onFocusChange}
            onChange={(e) => {
              props.onChange?.(e.target.value);
            }}
            name={props.name}
          />
        </InputGroup>
        {props.isInValid && errorTextVisible ? (
          <Text fontSize={'xs'} textColor={'crimson'} p={1}>
            {props.errorText}
          </Text>
        ) : null}
      </Flex>
    );
  } else {
    return (
      <Flex direction={'column'}>
        <InputGroup>
          {props.leftIcon ? (
            <InputLeftElement pointerEvents="none" py={'6'}>
              {leftIcon}
            </InputLeftElement>
          ) : null}
          <Input
            isInvalid={props.isInValid}
            type={props.type}
            placeholder={props.placeholder}
            focusBorderColor="blackAlpha.800"
            errorBorderColor="crimson"
            onFocus={onFocusChange}
            onBlur={onFocusChange}
            name={props.name}
            onChange={(e) => {
              props.onChange?.(e.target.value);
            }}
            py={'6'}
          />
        </InputGroup>
        {props.isInValid && errorTextVisible ? (
          <Text fontSize={'xs'} textColor={'crimson'} p={1}>
            {props.errorText}
          </Text>
        ) : null}
      </Flex>
    );
  }
}
