import React, { useEffect, useState } from "react";
import axios from "axios";

const LIMIT = 10;
const API = "https://dummyjson.com/products/search";

const useDebounce = (value, delay = 500) => {
  const [debounced, setDebounced] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);

  return debounced;
};

const App = () => {
  const [products, setProducts] = useState([]);
  const [total, setTotal] = useState(0);
  const [page, setPage] = useState(0);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const debouncedSearch = useDebounce(search);

  useEffect(() => {
    const controller = new AbortController();

    const fetchProducts = async () => {
      setLoading(true);
      setError("");
      try {
        const res = await axios.get(API, {
          params: { q: debouncedSearch, limit: LIMIT, skip: page * LIMIT },
          signal: controller.signal,
        });
        setProducts(res.data.products);
        setTotal(res.data.total);
      } catch (err) {
        if (!axios.isCancel(err)) setError("Something went wrong.");
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
    return () => controller.abort();
  }, [page, debouncedSearch]);

  const isLastPage = (page + 1) * LIMIT >= total;

  return (
    <div>
      <input
        placeholder="Search products..."
        value={search}
        onChange={(e) => { setSearch(e.target.value); setPage(0); }}
      />

      {loading && <p>Loading...</p>}
      {error && <p>{error}</p>}
      {!loading && !error && products.length === 0 && <p>No products found.</p>}

      {products.map((p) => (
        <div key={p.id}>{p.title}</div>
      ))}

      <button disabled={page === 0} onClick={() => setPage(page - 1)}>Prev</button>
      <span> Page {page + 1} </span>
      <button disabled={isLastPage} onClick={() => setPage(page + 1)}>Next</button>
    </div>
  );
};

export default App;