// creating useFecth

import { useEffect, useState } from "react";
import axios from "axios";

const useFetch = (url) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const controller = new AbortController();

    const fetchData = async () => {
      try {
        setLoading(true);
        setError(null);

        const response = await axios.get(url, {
          signal: controller.signal
        });

        setData(response.data);
      } catch (err) {
        if (err.name !== "CanceledError") {
          setError(err.message);
        }
      } finally {
        setLoading(false);
      }
    };

    if (url) fetchData();

    return () => controller.abort();
  }, [url]);

  return { data, loading, error };
};

export default useFetch;


// Using the Custom Hook

import React from "react";
import useFetch from "./useFetch";

const App = () => {
  const { data, loading, error } = useFetch(
    "https://jsonplaceholder.typicode.com/users"
  );

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div>
      {data &&
        data.map(user => (
          <p key={user.id}>{user.name}</p>
        ))}
    </div>
  );
};

export default App;

// It shows:

// ✔ Reusability
// ✔ Separation of concerns
// ✔ Proper cleanup
// ✔ State management
// ✔ Dependency handling

// Interview Explanation (MEMORIZE THIS)
// I created a custom hook to abstract API logic so that components remain clean and reusable. 
// The hook manages loading, error, and data states internally and returns them to the component.


// Advanced Version (With Manual Refetch) and useCallback

import { useEffect, useState, useCallback } from "react";
import axios from "axios";

const useFetch = (url, options = {}) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchData = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);

      const response = await axios.get(url, options);
      setData(response.data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, [url, options]);

  useEffect(() => {
    if (url) fetchData();
  }, [fetchData]);

  return { data, loading, error, refetch: fetchData };
};

export default useFetch;


// Usage with Refetch Button
const { data, loading, error, refetch } = useFetch(
  "https://jsonplaceholder.typicode.com/users"
);

<button onClick={refetch}>Refetch</button>

// I used useCallback to memoize the fetch function and exposed a refetch method to allow manual re-triggering of the API call.

// Why useCallback?
// To prevent unnecessary re-renders or effect re-triggers.