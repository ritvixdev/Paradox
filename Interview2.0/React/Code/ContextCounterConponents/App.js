import React, { useContext } from "react";
import CounterContext from "./CounterContext";
import "./style.css";

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

export default App;