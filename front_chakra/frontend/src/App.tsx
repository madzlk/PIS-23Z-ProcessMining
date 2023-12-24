import React from "react";
import { Button, ButtonGroup, Grid, GridItem, Heading } from "@chakra-ui/react";
import { Show, Hide } from "@chakra-ui/react";
import NavBar from "./components/NavBar";
import RegisterUser from "./components/RegisterUser";
import UsersTable from "./components/UsersTable";
import useUsers, { User } from "./hooks/useUsers";

const App = () => {
  const { users, error, isLoading, onDeleteUser, onRegisterUser } = useUsers();

  return (
    <Grid
      templateAreas={{
        base: '"nav" "main"',
        lg: `"nav nav" "aside main"`,
      }}
    >
      <GridItem h="" area="nav">
        <NavBar>Users panel</NavBar>
      </GridItem>

      <Show above="lg">
        <GridItem area="aside" width={300} padding={"20px"}>
          <RegisterUser onRegisterUser={onRegisterUser}></RegisterUser>
        </GridItem>
      </Show>

      <GridItem area="main">
        <UsersTable onDeleteUser={onDeleteUser} users={users}></UsersTable>
      </GridItem>
    </Grid>
  );
};

export default App;
