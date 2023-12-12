import {
  ColorModeContext,
  HStack,
  Heading,
  Image,
  Text,
  Wrap,
} from "@chakra-ui/react";
import logo from "../assets/react.svg";
import ColorModeSwitch from "./ColorModeSwitch";
import { ReactNode } from "react";
import { Avatar, AvatarBadge, AvatarGroup } from "@chakra-ui/react";

interface Pros {
  children: string;
}

const NavBar = ({ children }: Pros) => {
  return (
    <HStack justifyContent="space-between" padding="15px">
      <HStack>
        <Image ml={10} src={logo} boxSize="40px"></Image>
        <Heading padding={"10px"}>{children}</Heading>
      </HStack>
      <Wrap mr={10}>
        <ColorModeSwitch></ColorModeSwitch>
        <Avatar name="Dan Abrahmov" src="https://bit.ly/dan-abramov"></Avatar>
      </Wrap>
    </HStack>
  );
};

export default NavBar;
