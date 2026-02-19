import React, { useState, useEffect } from "react";
import axios from "axios";

const App = () => {

  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [newTitle, setNewTitle] = useState("");   // 🔹 Input State

  const BASE_URL = "https://dummyjson.com/products";

  // 🔹 GET ALL PRODUCTS
  const getProducts = async () => {
    try {
      setLoading(true);

      const res = await axios.get(BASE_URL);

      setProducts(res.data.products);

    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // 🔹 POST (ADD PRODUCT from input)
  const addProduct = async () => {

    if (!newTitle) return;

    try {
      setLoading(true);

      const res = await axios.post(`${BASE_URL}/add`, {
        title: newTitle,
        price: 500
      });

      setProducts(prev => [...prev, res.data]);

      setNewTitle("");   // clear input

    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // 🔹 PUT (UPDATE PRODUCT)
  const updateProduct = async (id) => {
    try {
      setLoading(true);

      const res = await axios.put(`${BASE_URL}/${id}`, {
        title: "Updated Product"
      });

      setProducts(prev =>
        prev.map(p => p.id === id ? res.data : p)
      );

    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // 🔹 DELETE PRODUCT
  const deleteProduct = async (id) => {
    try {
      setLoading(true);

      await axios.delete(`${BASE_URL}/${id}`);

      setProducts(prev =>
        prev.filter(p => p.id !== id)
      );

    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // 🔹 GET on mount
  useEffect(() => {
    getProducts();
  }, []);

  return (
    <div>

      {/* 🔹 INPUT FIELD */}
      <input
        type="text"
        placeholder="Enter product title..."
        value={newTitle}
        onChange={(e) => setNewTitle(e.target.value)}
      />

      <button onClick={addProduct}>
        Add Product
      </button>

      {loading && <p>Loading...</p>}

      {products.map(p => (
        <div key={p.id}>
          <p>{p.title}</p>

          <button onClick={() => updateProduct(p.id)}>
            Update
          </button>

          <button onClick={() => deleteProduct(p.id)}>
            Delete
          </button>
        </div>
      ))}

    </div>
  );
};

export default App;
