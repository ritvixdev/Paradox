// Code for Pagination and Seach in React

import React, { useEffect, useState } from "react";
import axios from "axios";

const LIMIT = 10;

const App = () => {
  const [products, setProducts] = useState([]);
  const [page, setPage] = useState(0);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const controller = new AbortController();

    const fetchProducts = async () => {
      try {
        setLoading(true);

        const skip = page * LIMIT;

        const res = await axios.get(
          "https://dummyjson.com/products/search",
          {
            params: {
              q: search,
              limit: LIMIT,
              skip
            },
            signal: controller.signal
          }
        );

        setProducts(res.data.products);
      } catch (err) {
        if (err.name !== "CanceledError") {
          console.error(err);
        }
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();

    return () => controller.abort();
  }, [page, search]);

  return (
    <div>
      <input
        placeholder="Search product"
        value={search}
        onChange={(e) => {
          setSearch(e.target.value);
          setPage(0);
        }}
      />

      {loading && <p>Loading...</p>}

      {products.map(p => (
        <div key={p.id}>{p.title}</div>
      ))}

      <button disabled={page === 0} onClick={() => setPage(page - 1)}>
        Prev
      </button>

      <button onClick={() => setPage(page + 1)}>
        Next
      </button>
    </div>
  );
};

export default App;
