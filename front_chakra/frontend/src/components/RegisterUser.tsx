import {
  FormControl,
  FormLabel,
  FormHelperText,
  Input,
  Button,
  Heading,
  InputGroup,
  InputRightElement,
} from "@chakra-ui/react";
import { FieldValues, useForm } from "react-hook-form";
import apiClient from "../services/api-client";
import { User } from "../hooks/useUsers";
import React from "react";

const RegisterUser = ({
  onRegisterUser,
}: {
  onRegisterUser: (newUser: User) => void;
}) => {
  const [show, setShow] = React.useState(false);
  const handleClick = () => setShow(!show);

  const { register, handleSubmit } = useForm();

  const onSubmit = (data: FieldValues) => {
    const user: User = {
      email: data.email,
      username: data.username,
      user_uid: parseInt(data.id),
    };

    onRegisterUser(user);
  };

  return (
    <>
      <Heading mb={5} ml={10} size={"md"}>
        Register
      </Heading>

      <form onSubmit={handleSubmit(onSubmit)}>
        <FormControl ml={10}>
          <FormLabel>Email address</FormLabel>
          <Input type="email" mb={4} id="email" {...register("email")} />
          <FormLabel>Username</FormLabel>
          <Input type="text" id="username" {...register("username")} />
          <FormHelperText mb={4}>Username must be unique.</FormHelperText>
          <InputGroup mb={5} size="md">
            <Input
              pr="4.5rem"
              type={show ? "text" : "password"}
              placeholder="Enter password"
            />
            <InputRightElement width="4.5rem">
              <Button h="1.75rem" size="sm" onClick={handleClick}>
                {show ? "Hide" : "Show"}
              </Button>
            </InputRightElement>
          </InputGroup>

          <Button type="submit">register</Button>
        </FormControl>
      </form>
    </>
  );
};

export default RegisterUser;
