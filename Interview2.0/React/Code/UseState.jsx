// interview example of useState()

// useState is a React Hook used to add state to functional components. It returns the current state value and a setter function to update it. 
// Updating state triggers a re-render of the component.

import React, { useState } from "react";

const App = () => {
  const [count, setCount] = useState(0);

  const increment = () => {
    setCount(prev => prev + 1); // safer version
  };

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={increment}>Click Me</button>
    </div>
  );
};

export default App;

// ----------------------------------------------------

// Use prev => prev + 1 to avoid stale state issues.

// Form Handling Example

import React, { useState } from "react";

const App = () => {
  const [form, setForm] = useState({
    name: "",
    email: ""
  });

  const handleChange = (e) => {
    setForm(prev => ({
      ...prev,
      [e.target.name]: e.target.value
    }));
  };

  const handleSubmit = () => {
    console.log("Form submitted:", form);
  };

  return (
    <div>
      <input
        name="name"
        value={form.name}
        onChange={handleChange}
        placeholder="Name"
      />

      <input
        name="email"
        value={form.email}
        onChange={handleChange}
        placeholder="Email"
      />

      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
};

export default App;

//Why this is better in interview?

// Shows object state
// Shows spread operator
// Shows dynamic keys
// Shows controlled components

// Toggle + Conditional Rendering

import React, { useState } from "react";

const App = () => {
  const [isVisible, setIsVisible] = useState(false);

  return (
    <div>
      <button onClick={() => setIsVisible(prev => !prev)}>
        Toggle
      </button>

      {isVisible && <p>Hello! I am visible.</p>}
    </div>
  );
};

export default App;

// Important Interview Concepts About useState

// 1. State updates are asynchronous

// 2. Functional update form prevents stale closures
setCount(prev => prev + 1);

// 3. Updating state triggers re-render


// What happens internally when setState runs?
// Answer: React schedules a re-render. During the next render cycle, the new state value is used.