// USeEffect examples

// Basic API Fetch on Mount

import React, { useEffect, useState } from "react";
import axios from "axios";

const App = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        setLoading(true);
        const res = await axios.get(
          "https://jsonplaceholder.typicode.com/users"
        );
        setUsers(res.data);
      } catch (err) {
        console.error("Error fetching users:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchUsers();
  }, []); // run once on mount

  return (
    <div>
      {loading && <p>Loading...</p>}
      {users.map(user => (
        <p key={user.id}>{user.name}</p>
      ))}
    </div>
  );
};

export default App;

// I use useEffect with an empty dependency array to fetch data once when the component mounts. Axios simplifies JSON parsing and error handling.


// API Fetch Based on Dependency Change

useEffect(() => {
  const fetchUser = async () => {
    try {
      const res = await axios.get(
        `https://jsonplaceholder.typicode.com/users/${userId}`
      );
      setUser(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  if (userId) fetchUser();
}, [userId]);

// The effect re-runs whenever userId changes, ensuring the UI stays in sync with dynamic route or state changes.


// Search + Debounce

useEffect(() => {
  const timer = setTimeout(async () => {
    try {
      const res = await axios.get(
        "https://dummyjson.com/products/search",
        {
          params: { q: search }
        }
      );
      setProducts(res.data.products);
    } catch (err) {
      console.error(err);
    }
  }, 500);

  return () => clearTimeout(timer);
}, [search]);

// API with Cleanup (AbortController)

// Prevent memory leaks if component unmounts.

useEffect(() => {
  const controller = new AbortController();

  const fetchData = async () => {
    try {
      const res = await axios.get(
        "https://dummyjson.com/products",
        { signal: controller.signal }
      );
      setData(res.data);
    } catch (err) {
      if (err.name !== "CanceledError") {
        console.error(err);
      }
    }
  };

  fetchData();

  return () => {
    controller.abort();
  };
}, []);

// I use AbortController to cancel the request during cleanup to avoid memory leaks and unwanted state updates.

// Why useEffect instead of calling API directly?
// Answer: Because side effects should be handled after render and controlled through lifecycle behavior.

// What happens if you forget dependency array?
// Answer: The API will fire on every render, possibly causing infinite loops.

// Why do we need cleanup?
// Answer: To avoid memory leaks and cancel ongoing async tasks.

// Difference between fetch and axios here?
// Answer: Axios automatically parses JSON and throws on HTTP errors, while fetch requires manual checks.