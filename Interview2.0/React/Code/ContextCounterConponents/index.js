import React, { useState, StrictMode } from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import CounterContext from "./CounterContext";
import "./style.css";

const CounterProvider = ({ children }) => {
  const [count, setCount] = useState(0);

  const increment = () => {
    setCount(prev => prev + 1);
  };

  const decrement = () => {
    setCount(prev => prev - 1);
  };

  return (
    <CounterContext.Provider value={{ count, increment, decrement }}>
      {children}
    </CounterContext.Provider>
  );
};

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <StrictMode>
    <CounterProvider>
      <App />
    </CounterProvider>
  </StrictMode>
);