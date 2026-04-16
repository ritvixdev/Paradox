import React, { createContext, useContext, useState } from "react";

// 1️⃣ Create Context
const CounterContext = createContext();

// 2️⃣ Provider Component
const CounterProvider = ({ children }) => {
  const [count, setCount] = useState(0);

  const increment = () => setCount(prev => prev + 1);
  const decrement = () => setCount(prev => prev - 1);

  return (
    <CounterContext.Provider value={{ count, increment, decrement }}>
      {children}
    </CounterContext.Provider>
  );
};

// 3️⃣ Consumer Component
const App = () => {
  const { count, increment, decrement } = useContext(CounterContext);

  return (
    <>
      <p>Current Count : {count}</p>
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
    </>
  );
};

// 4️⃣ Wrap App with Provider
const ContextAPI = () => {
  return (
    <CounterProvider>
      <App />
    </CounterProvider>
  );
};

export default ContextAPI;