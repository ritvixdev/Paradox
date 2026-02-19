// Code for Pagination and Seach in React
import React, { useEffect, useState } from "react";
import axios from "axios";

const LIMIT = 10;

// 🔹 Debounce Hook
const useDebounce = (value, delay = 500) => {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => clearTimeout(timer);
  }, [value, delay]);

  return debouncedValue;
};

const App = () => {

  const [products, setProducts] = useState([]);
  const [page, setPage] = useState(0);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(false);

  const debouncedSearch = useDebounce(search, 500);

  const BASE_URL = "https://dummyjson.com/products";

  // 🔹 Separate GET Function
  const getProducts = async (pageNo, query, signal) => {
    try {
      setLoading(true);

      const skip = pageNo * LIMIT;

      const res = await axios.get(`${BASE_URL}/search`, {
        params: {
          q: query,
          limit: LIMIT,
          skip
        },
        signal
      });

      setProducts(res.data.products);

    } catch (err) {
      if (err.name !== "CanceledError") {
        console.error(err);
      }
    } finally {
      setLoading(false);
    }
  };

  // 🔹 useEffect triggers GET
  useEffect(() => {

    const controller = new AbortController();

    getProducts(page, debouncedSearch, controller.signal);

    return () => controller.abort();

  }, [page, debouncedSearch]);

  return (
    <div>

      <input
        placeholder="Search product"
        value={search}
        onChange={(e) => {
          setSearch(e.target.value);
          setPage(0);   // reset page when search changes
        }}
      />

      {loading && <p>Loading...</p>}

      {products.map(p => (
        <div key={p.id}>{p.title}</div>
      ))}

      <button
        disabled={page === 0}
        onClick={() => setPage(prev => prev - 1)}
      >
        Prev
      </button>

      <button
        onClick={() => setPage(prev => prev + 1)}
      >
        Next
      </button>

    </div>
  );
};

export default App;
