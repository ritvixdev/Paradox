import React, { useState, useEffect } from "react";
import axios from "axios";

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
  const [data, setData] = useState([]);
  const [search, setSearch] = useState("");

  const debouncedSearch = useDebounce(search, 500);

  useEffect(() => {
    const fetchData = async () => {
      if (!debouncedSearch.trim()) {
        setData([]);
        return;
      }

      try {
        const response = await axios.get("https://dummyjson.com/products/search", {
          params: { q: debouncedSearch },
        });
        setData(response.data.products);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, [debouncedSearch]);

  return (
    <div>
      <input
        type="text"
        value={search}
        placeholder="Search products..."
        onChange={(e) => setSearch(e.target.value)}
      />
      <ul>
        {data.map((item) => (
          <li key={item.id}>{item.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default App;