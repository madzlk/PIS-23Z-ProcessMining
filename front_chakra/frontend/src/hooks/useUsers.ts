import React, { useEffect, useState } from "react";
import apiClient from "../services/api-client";
import { CanceledError } from "axios";

export interface User {
  user_uid: number;
  username: string;
  email: string;
}

const useUsers = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [error, setError] = useState();
  const [isLoading, setLoading] = useState(false);

  const onRegisterUser = async (newUser: User) => {
    try {
      const response = await apiClient.post("/users", newUser);
      console.log("User successfully added:", response.data);

      // Fetch the updated user list after registering a new user
      setLoading(true);
      const res = await apiClient.get<User[]>("/users");
      setUsers(res.data);
    } catch (error) {
      console.error("Error adding user:", error);
    } finally {
      setLoading(false);
    }
  };

  const onDeleteUser = (deletedUser: User) => {
    // Make an API request to delete the user
    apiClient
      .delete(`/users/${deletedUser.user_uid}`)
      .then(() => {
        // If the deletion is successful, update the state
        const updatedUsers = users.filter(
          (user) => user.user_uid !== deletedUser.user_uid
        );
        setUsers(updatedUsers);
      })
      .catch((error) => {
        // Handle errors, e.g., log them or show a notification
        console.error("Error deleting user:", error);
      });
  };

  const onFetchData = async () => {
    try {
      setLoading(true);
      const res = await apiClient.get<User[]>("/users");
      setUsers(res.data);
    } catch (err) {
      if (err instanceof CanceledError) return;
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    const controller = new AbortController();

    setLoading(true);
    apiClient
      .get<User[]>("/users", { signal: controller.signal })
      .then((res) => {
        setUsers(res.data), setLoading(false);
      })
      .catch((err) => {
        if (err instanceof CanceledError) return;
        setError(err.message);
        setLoading(false);
      });

    return () => controller.abort();
  }, [setUsers]);
  return { users, error, isLoading, onDeleteUser, onRegisterUser };
};

export default useUsers;
