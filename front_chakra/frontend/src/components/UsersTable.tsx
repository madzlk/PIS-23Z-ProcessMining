import useUsers, { User } from "../hooks/useUsers";
import { FaTrash } from "react-icons/fa";
import {
  Table,
  Thead,
  Tbody,
  Tfoot,
  Tr,
  Th,
  Td,
  TableCaption,
  TableContainer,
  Wrap,
} from "@chakra-ui/react";

const UsersTable = ({
  users,
  onDeleteUser,
}: {
  users: User[];
  onDeleteUser: (deletedUser: User) => void;
}) => {
  return (
    <div>
      <Wrap>
        <TableContainer>
          <Table variant="simple">
            <TableCaption>unauthorized users</TableCaption>
            <Thead>
              <Tr>
                <Th isNumeric>id</Th>
                <Th>Username</Th>
                <Th>email</Th>
              </Tr>
            </Thead>
            <Tbody>
              {users.map((user) => (
                <Tr key={user.user_uid}>
                  <Td>{user.user_uid}</Td>
                  <Td>{user.username}</Td>
                  <Td>{user.email}</Td>
                  <Td>
                    <FaTrash onClick={() => onDeleteUser(user)} />
                  </Td>
                </Tr>
              ))}
            </Tbody>
          </Table>
        </TableContainer>
      </Wrap>
    </div>
  );
};

export default UsersTable;
