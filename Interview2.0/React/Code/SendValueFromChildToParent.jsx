import React, { useState } from "react";

// Child component — no state, just calls the callback
const Child = ({ onNameChange }) => {
  return (
    <input
      type="text"
      placeholder="Type your name..."
      onChange={(e) => onNameChange(e.target.value)}
    />
  );
}

// Parent component — owns the state
const App = () => {
  const [name, setName] = useState("");

  return (
    <div>
      <h2>Parent Component</h2>
      <Child onNameChange={setName} />
      <p>Hello, {name || "stranger"}!</p>
    </div>
  );
}

export default App;


// ============ COUNTER Child to Parent Example =====================


import React, { useState } from "react";

// Child 1 — only knows how to increment
const IncrBtn = ({ onIncrement }) => {
  return <button onClick={onIncrement}>+ Increment</button>;
}

// Child 2 — only knows how to decrement
const DecrBtn = ({ onDecrement }) => {
  return <button onClick={onDecrement}>− Decrement</button>;
}

// Child 3 — only knows how to reset
const ResetBtn = ({ onReset }) => {
  return <button onClick={onReset}>Reset</button>;
}

// Parent — single source of truth for count
const Parent = () => {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h2>Parent Component</h2>
      <p>Count: {count}</p>

      <IncrBtn onIncrement={() => setCount((c) => c + 1)} />
      <DecrBtn onDecrement={() => setCount((c) => c - 1)} />
      <ResetBtn onReset={() => setCount(0)} />
    </div>
  );
}

// export default Parent;