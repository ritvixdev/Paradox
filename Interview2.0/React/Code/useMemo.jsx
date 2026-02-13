// useMemo

// 🧠 What is useMemo?
// useMemo memoizes a computed value and only recalculates it when its dependencies change.

// 🎯 Interview Explanation (MEMORIZE THIS)

// I use useMemo to memoize expensive calculations so they only recompute when their dependencies change, improving performance.

// useMemo → memoizes values
// React.memo → memoizes components

// Basic Example (Expensive Calculation) With useMemo (Correct)

import React, { useState, useMemo } from "react";

const App = () => {
  const [count, setCount] = useState(0);
  const [text, setText] = useState("");

  const result = useMemo(() => {
    console.log("Calculating...");
    return count * 2;
  }, [count]); // only runs when count changes

  return (
    <div>
      <p>Result: {result}</p>
      <button onClick={() => setCount(count + 1)}>Increase</button>
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
    </div>
  );
};

export default App;

// 🧠 What’s Happening Internally?

// Stores previous value
// Compares dependencies
// If unchanged → returns cached value
// If changed → recalculates

// Real Interview Example (Filtering Large List)

import React, { useState, useMemo } from "react";

const App = () => {
  const [search, setSearch] = useState("");
  const [users] = useState([
    "Alice",
    "Bob",
    "Charlie",
    "David"
  ]);

  const filteredUsers = useMemo(() => {
    console.log("Filtering...");
    return users.filter(user =>
      user.toLowerCase().includes(search.toLowerCase())
    );
  }, [search, users]);

  return (
    <div>
      <input
        placeholder="Search..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      {filteredUsers.map(user => (
        <p key={user}>{user}</p>
      ))}
    </div>
  );
};

export default App;

// 🚀 Advanced Interview Example (Derived Object)

// Without useMemo:
const options = { page: 1 };
// Object recreated every render → child re-renders.

// With useMemo:
const options = useMemo(() => ({ page: 1 }), []);

// 🧠 Common Interview Follow-Ups

// ❓ Does useMemo prevent re-render?
// No. It only memoizes value.

// ❓ Is useMemo always beneficial?
// No. Overusing it adds overhead.


// ✅ Optimized Version (useMemo + React.memo)

import React, { useState, useMemo } from "react";

const Child = React.memo(({ items }) => {
  console.log("Child re-rendered");
  return (
    <div>
      {items.map(item => (
        <p key={item}>{item}</p>
      ))}
    </div>
  );
});

const App = () => {
  const [count, setCount] = useState(0);
  const [search, setSearch] = useState("");

  const users = ["Alice", "Bob", "Charlie", "David"];

  const filteredUsers = useMemo(() => {
    console.log("Filtering...");
    return users.filter(user =>
      user.toLowerCase().includes(search.toLowerCase())
    );
  }, [search]);

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>
        Increase Count: {count}
      </button>

      <input
        placeholder="Search"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      <Child items={filteredUsers} />
    </div>
  );
};

export default App;

// 🧠 What Happens Now?

// count changes → parent re-renders
// BUT search didn't change
// useMemo returns cached array
// Same reference
// React.memo sees no prop change
// ✅ Child does NOT re-render

// 🎯 Interview Explanation (MEMORIZE THIS)

// I used useMemo to memoize the derived filtered list and React.memo to prevent the child from re-rendering unless its props change. 
// This avoids unnecessary re-renders caused by new object references.

// 🔍 Why This Works

// React.memo does:
// Object.is(previousProps, nextProps)

// If reference changes → re-render
// If reference same → skip

// ⚠️ Important Interview Clarification
// ❓ Does useMemo prevent parent re-render?
// ❌ No.

// ❓ Does React.memo prevent parent re-render?
// ❌ No.

// They only optimize child rendering.


// 🏆 Final Comparison
// Hook	Purpose
// useMemo	Memoizes computed value
// React.memo	Memoizes component render
// useCallback	Memoizes function reference