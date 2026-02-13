// useCallback

// useCallback memoizes a function so that it does not get recreated on every render unless its dependencies change.

// Interview Perfect Answer (MEMORIZE)

// useCallback memoizes a function so that it maintains the same reference between renders unless dependencies change. 
// It is mainly used to prevent unnecessary child re-renders when passing functions as props.

// Basic Example of useCallback


import React, { useState, useCallback } from "react";

const App = () => {
  const [count, setCount] = useState(0);

  const increment = useCallback(() => {
    setCount(prev => prev + 1);
  }, []);

  return (
    <div>
      <p>{count}</p>
      <button onClick={increment}>Increment</button>
    </div>
  );
};

export default App;

// increment will not be recreated on every render.

// Real Interview Example (Parent → Child Optimization)

const handleClick = useCallback(() => {
  console.log("Clicked");
}, []);

// 🧠 Important Interview Concept

// useCallback only matters when:

// Passing function to child
// Using React.memo
// Using dependency arrays


// 3️⃣ useCallback + useEffect Example

import React, { useState, useEffect, useCallback } from "react";

const App = () => {
  const [count, setCount] = useState(0);

  const fetchData = useCallback(() => {
    console.log("Fetching with count:", count);
  }, [count]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  return (
    <button onClick={() => setCount(count + 1)}>
      Count {count}
    </button>
  );
};

// 🧠 Why this is important?

// If you define fetchData normally,
// useEffect may re-run every render. useCallback stabilizes the reference.

// Common Interview Mistake

// Many people think: useCallback prevents re-render ❌ Wrong
// It only prevents function recreation, not component re-render.