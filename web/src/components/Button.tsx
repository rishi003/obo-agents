import { Button as ChakraButton } from '@chakra-ui/react';
import { MouseEventHandler } from 'react';
export default function Button(props: {
  leftIcon?: any;
  rightIcon?: any;
  type: 'solid' | 'outline';
  children: any;
  onClick: MouseEventHandler;
}) {
  return (
    <ChakraButton
      leftIcon={props.leftIcon ? props.leftIcon : ''}
      rightIcon={props.rightIcon ? props.rightIcon : ''}
      bgColor={props.type === 'solid' ? 'blackAlpha.800' : 'white'}
      color={props.type === 'solid' ? 'white' : 'blackAlpha.800'}
      border={'2px'}
      borderRadius={'md'}
      p={'1.4rem'}
      borderColor={props.type === 'solid' ? '' : 'blackAlpha.800'}
      _hover={{
        bgColor: props.type === 'solid' ? 'white' : 'blackAlpha.800',
        color: props.type === 'solid' ? 'blackAlpha.800' : 'white',
        borderColor: props.type === 'solid' ? 'blackAlpha.800' : '',
      }}
      onClick={props.onClick}
    >
      {props.children}
    </ChakraButton>
  );
}
