// Create useDebounce Hook

import { useEffect, useState } from "react";

const useDebounce = (value, delay = 500) => {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => {
      clearTimeout(timer); // cleanup
    };
  }, [value, delay]);

  return debouncedValue;
};

export default useDebounce;

// 🧠 What this does

// Waits delay milliseconds
// If user types again before delay ends → clears timer
// Only updates when user stops typing

// Use it with API (Axios + Search)

import React, { useState, useEffect } from "react";
import axios from "axios";
import useDebounce from "./useDebounce";

const App = () => {
  const [search, setSearch] = useState("");
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(false);

  // Debounced value
  const debouncedSearch = useDebounce(search, 500);

  useEffect(() => {
    if (!debouncedSearch) return;

    const fetchProducts = async () => {
      try {
        setLoading(true);

        const res = await axios.get(
          "https://dummyjson.com/products/search",
          {
            params: { q: debouncedSearch }
          }
        );

        setProducts(res.data.products);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, [debouncedSearch]);

  return (
    <div>
      <input
        placeholder="Search products..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      {loading && <p>Loading...</p>}

      {products.map(p => (
        <p key={p.id}>{p.title}</p>
      ))}
    </div>
  );
};

export default App;

// 🎯 Interview Explanation (MEMORIZE THIS)

// I created a reusable useDebounce hook to delay value updates. 
// It prevents excessive API calls by waiting for the user to stop typing before triggering the request.

// Why not debounce inside useEffect directly?
// Answer: Using a custom hook makes the logic reusable and keeps components clean.

// What happens without debounce?
// API fires on every keystroke → performance issues.

// What is the cleanup doing?
// It clears the previous timer to prevent outdated updates.


// Debounce vs Throttle — Clear Difference

// Debounce waits until the user stops triggering the event.
// Throttle limits how often the function runs within a time interval.