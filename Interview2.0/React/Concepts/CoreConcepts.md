# ⚛️ React Interview Preparation Guide

> **Covers:** Basic → Intermediate → Advanced  
> All concepts grouped by topic with definitions, key points, and code examples.

---

## 📚 Table of Contents

| # | Topic |
|---|-------|
| 1 | [React Fundamentals](#1-react-fundamentals) |
| 2 | [JSX & Babel](#2-jsx--babel) |
| 3 | [Components](#3-components) |
| 4 | [Props & Data Flow](#4-props--data-flow) |
| 5 | [State & useState](#5-state--usestate) |
| 6 | [React Hooks](#6-react-hooks) |
| 7 | [Component Lifecycle](#7-component-lifecycle) |
| 8 | [Routing](#8-routing) |
| 9 | [Forms — Controlled vs Uncontrolled](#9-forms--controlled-vs-uncontrolled) |
| 10 | [Context API](#10-context-api) |
| 11 | [Redux & State Management](#11-redux--state-management) |
| 12 | [Performance Optimization](#12-performance-optimization) |
| 13 | [Code Splitting & Lazy Loading](#13-code-splitting--lazy-loading) |
| 14 | [Higher-Order Components & Patterns](#14-higher-order-components--patterns) |
| 15 | [API Calls — fetch vs axios](#15-api-calls--fetch-vs-axios) |
| 16 | [Error Handling in React](#16-error-handling-in-react) |
| 17 | [Testing in React](#17-testing-in-react) |
| 18 | [Advanced Concepts](#18-advanced-concepts) |
| 19 | [Tricky Interview Questions](#19-tricky-interview-questions) |
| 20 | [Quick Revision Cheatsheet](#-quick-revision-cheatsheet) |

---

## 1. React Fundamentals

### What is React?

**Definition:** React is an open-source JavaScript **library** (not a framework) for building user interfaces, developed and maintained by Meta (Facebook).

- **Library** — React provides specific functions that developers import and use. Developers remain in control of the application structure.
- **Framework** — Provides a complete structure (Angular, Vue are frameworks).

### 7 Key Features of React

1. **Virtual DOM** — Efficient UI updates without re-rendering the entire page
2. **Component-Based Architecture** — Build UIs using reusable, independent pieces
3. **Reusability & Composition** — Components can be reused and combined
4. **JSX** — JavaScript XML syntax for writing HTML-like code in JS
5. **Declarative Syntax** — Describe *what* to render, not *how*
6. **React Hooks** — Add state and lifecycle to functional components
7. **Ecosystem & Community** — Large ecosystem of libraries and tools

### DOM vs Virtual DOM

**DOM (Document Object Model):** Represents the web page as a tree-like structure, allowing JS to dynamically access and manipulate content.

**Virtual DOM:** A lightweight in-memory copy of the real DOM. React uses it to calculate the minimum changes needed before updating the real DOM.

| Feature | Real DOM | Virtual DOM |
|---------|---------|-------------|
| Definition | Actual representation of the webpage | Lightweight copy of the DOM |
| On update | Re-renders the entire page | Re-renders only the changed parts |
| Speed | Slower with frequent updates | Optimized for faster rendering |
| Use case | Static websites | Dynamic SPAs with frequent updates |

**How Virtual DOM works (Reconciliation):**
1. State/props change → React creates a new Virtual DOM tree
2. React **diffs** the new Virtual DOM vs the previous one (diffing algorithm)
3. Only the changed parts are updated in the real DOM (**reconciliation**)

### SPA (Single Page Application)

**Definition:** A web application with only **one HTML page**. Content is dynamically updated without refreshing or loading a new page.

- React is commonly used to build SPAs
- URL changes are handled client-side using React Router

### Declarative vs Imperative

| | Declarative | Imperative |
|-|-------------|-----------|
| Focus | *What* the result should look like | *How* step-by-step to achieve the result |
| Example | JSX in React | Vanilla JS DOM manipulation |

```jsx
// Declarative (React JSX)
function App() {
  return <h1>Hello World</h1>;
}

// Imperative (Vanilla JS)
function App() {
  const el = document.createElement("h1");
  el.textContent = "Hello World";
  document.body.appendChild(el);
}
```

### React Project Structure

| File/Folder | Role |
|------------|------|
| `index.html` | Single HTML page; has `<div id="root">` where React mounts |
| `index.js` | Entry point; renders the root `<App />` component into `#root` |
| `App.js` | Root component; defines layout, structure, and routing |
| `src/` | All source code — components, hooks, styles |
| `public/` | Static assets served directly (images, fonts, `index.html`) |
| `node_modules/` | All installed dependencies |
| `package.json` | Lists dependencies and scripts |

```jsx
// index.html
<div id="root"></div>

// index.js
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

### ReactDOM

**Definition:** A JavaScript library that renders React components to the real DOM/browser.

- `ReactDOM.createRoot()` — Creates the root for React 18+
- `root.render()` — Mounts the component tree into the DOM

---

## 2. JSX & Babel

### JSX (JavaScript XML)

**Definition:** A syntax extension for JavaScript that lets you write HTML-like code inside JS files.

**Key points:**
- JSX stands for JavaScript XML
- Browsers do NOT understand JSX — it must be compiled to JavaScript first
- Babel converts JSX into `React.createElement()` calls
- JSX allows embedding JavaScript expressions using `{}`

```jsx
// JSX
function App() {
  const name = "Alice";
  return (
    <div>
      <h1>Hello, {name}!</h1>    {/* JS expression */}
      <p>{2 + 2} is four</p>     {/* Expression */}
    </div>
  );
}
```

### JSX Rules

- Must return a **single root element** (use `<>...</>` or `React.Fragment` for multiple)
- Use `className` instead of `class`
- Use `camelCase` for HTML attributes (`onClick`, `htmlFor`)
- Self-close tags with no children: `<img />`, `<br />`
- JavaScript expressions go in `{}`; statements (if, for) do not

```jsx
// Fragment — avoids unnecessary DOM nodes
function App() {
  return (
    <>
      <h1>Title</h1>
      <p>Paragraph</p>
    </>
  );
}
```

### Advantages of JSX

1. Improved code readability and writability
2. Type safety — catches errors at compile time
3. Supports JavaScript expressions inline
4. Better performance through Babel optimization
5. Enables code reusability through components

### Babel

**Definition:** A JavaScript transpiler that converts JSX and modern JS (ES6+) syntax into regular JavaScript that browsers can understand.

- **Transpiler** — Converts one high-level language (JSX) to another high-level language (JavaScript)
- **Compiler** — Converts high-level language (Java) to low-level machine code

```jsx
// JSX (what you write)
return <div className="App"><h1>Hello!</h1></div>;

// After Babel (what the browser sees)
return React.createElement(
  "div",
  { className: "App" },
  React.createElement("h1", null, "Hello!")
);
```

### Spread Operator in JSX

```jsx
function App() {
  const props = { name: "Alice", role: "Developer" };
  return <ChildComponent {...props} />;   // spreads all props
}

function ChildComponent({ name, role }) {
  return <div>{name} — {role}</div>;
}
// Output: Alice — Developer
```

### map() in JSX — Rendering Lists

```jsx
function App() {
  const fruits = ["Apple", "Banana", "Mango"];
  return (
    <ul>
      {fruits.map((fruit, index) => (
        <li key={index}>{fruit}</li>   // key is required!
      ))}
    </ul>
  );
}
```

> **Key prop:** Required when rendering lists. Helps React identify which items changed. Use unique IDs, not array indices when possible.

---

## 3. Components

### What is a React Component?

**Definition:** A reusable, independent building block for creating user interfaces. Each component manages its own logic and renders a piece of the UI.

```jsx
// Basic component structure
import React from "react";

function MyComponent() {
  return (
    <div>
      <h1>I am a reusable component</h1>
    </div>
  );
}

export default MyComponent;
```

### Functional vs Class Components

| Feature | Functional Component | Class Component |
|---------|---------------------|----------------|
| Syntax | JavaScript function | ES6 class extending `Component` |
| State | Via `useState` hook | Via `this.state` |
| Lifecycle | Via `useEffect` hook | Lifecycle methods |
| `this` keyword | Not used | Required |
| `render()` method | Not needed | Required |
| Readability | Concise and readable | Verbose |
| Modern usage | ✅ Preferred | Legacy code |

```jsx
// Functional Component (preferred)
function Greeting({ name }) {
  return <h1>Hello, {name}!</h1>;
}

// Arrow function shorthand
const Greeting = ({ name }) => <h1>Hello, {name}!</h1>;

// Class Component (legacy)
import React, { Component } from "react";

class Greeting extends Component {
  render() {
    return <h1>Hello, {this.props.name}!</h1>;
  }
}
```

### Reusability & Composition

- **Reusability** — Once a component is created, it can be reused anywhere in the app or other projects.
- **Composition** — Building large, complex components by combining smaller ones. A change in one small component does not impact others.

```jsx
// Composition example
function Button({ label, onClick }) {
  return <button onClick={onClick}>{label}</button>;
}

function Card({ title, children }) {
  return (
    <div className="card">
      <h2>{title}</h2>
      {children}
    </div>
  );
}

function App() {
  return (
    <Card title="Welcome">
      <p>Some content here</p>
      <Button label="Click Me" onClick={() => alert("Clicked!")} />
    </Card>
  );
}
```

### `React.Fragment`

Lets you group multiple elements without adding an extra DOM node.

```jsx
// Both are equivalent
return (
  <React.Fragment>
    <h1>Title</h1>
    <p>Paragraph</p>
  </React.Fragment>
);

// Shorthand
return (
  <>
    <h1>Title</h1>
    <p>Paragraph</p>
  </>
);
```

---

## 4. Props & Data Flow

### Props (Properties)

**Definition:** A way to pass data from a **parent component** to a **child component**. Props are **read-only** — a child cannot modify the props it receives.

```jsx
// Parent passes data via props
function App() {
  return <UserCard name="Alice" age={25} role="Developer" />;
}

// Child receives via function parameter
function UserCard({ name, age, role }) {
  return (
    <div>
      <h2>{name}</h2>
      <p>Age: {age} | Role: {role}</p>
    </div>
  );
}
```

### Default Props

```jsx
function Button({ label = "Click Me", color = "blue" }) {
  return <button style={{ backgroundColor: color }}>{label}</button>;
}

// or using defaultProps
Button.defaultProps = {
  label: "Click Me",
  color: "blue"
};
```

### Prop Drilling

**Definition:** The process of passing data through **multiple layers** of nested components via props, even when intermediate components don't need the data.

```
App (has data)
 └── Layout (passes it down)
      └── Section (passes it down)
           └── DeepChild (finally uses it) ← prop drilling!
```

**5 Ways to Avoid Prop Drilling:**
1. **Context API** — Share data globally without passing props manually
2. **Redux** — Centralized state store
3. **Component Composition** — Restructure components to avoid deep nesting
4. **Callback Functions** — Pass functions down to lift state up
5. **Custom Hooks** — Encapsulate logic in reusable hooks

### Passing Data from Child to Parent (Lifting State Up)

Parent provides a **callback function** as a prop. Child calls it with data.

```jsx
// Parent
function Parent() {
  const handleChildData = (data) => {
    console.log("Received from child:", data);
  };
  return <Child sendData={handleChildData} />;
}

// Child
function Child({ sendData }) {
  return (
    <button onClick={() => sendData("Hello from Child!")}>
      Send to Parent
    </button>
  );
}
```

### `children` Prop

Allows components to accept arbitrary JSX content between their opening and closing tags.

```jsx
function Card({ children, title }) {
  return (
    <div className="card">
      <h2>{title}</h2>
      <div className="card-body">{children}</div>
    </div>
  );
}

// Usage
<Card title="My Card">
  <p>Any content goes here</p>
  <button>Action</button>
</Card>
```

---

## 5. State & useState

### State

**Definition:** State is the current data/information that a component manages. When state changes, the component **re-renders** to reflect the updated UI.

- **Stateless** — A component that doesn't hold any state (just renders what it receives via props)
- **Stateful** — A component that manages its own state and re-renders on state changes

```jsx
// Without state — UI does NOT update
function Counter() {
  let count = 0;
  return (
    <div>
      <p>{count}</p>
      <button onClick={() => { count++; }}>+</button>
      {/* count updates in memory but UI doesn't re-render */}
    </div>
  );
}
```

### `useState` Hook

**Definition:** A React hook that enables functional components to manage state. Returns an array with the current state value and a function to update it.

```jsx
const [state, setState] = useState(initialValue);
```

- First element — current state value
- Second element — setter function to update state
- Calling the setter **triggers a re-render**

```jsx
import React, { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0); // initial state = 0

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>+</button>
      <button onClick={() => setCount(count - 1)}>-</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}
```

### Updating State Based on Previous State

When new state depends on the old state, use the **functional update form** to avoid stale state bugs.

```jsx
// Potentially buggy — may use stale state
setCount(count + 1);

// Correct — always uses latest state
setCount(prevCount => prevCount + 1);
```

### State with Objects

```jsx
function Profile() {
  const [user, setUser] = useState({ name: "Alice", age: 25 });

  const updateAge = () => {
    // Must spread to preserve other properties
    setUser(prev => ({ ...prev, age: prev.age + 1 }));
  };

  return (
    <div>
      <p>{user.name} — {user.age}</p>
      <button onClick={updateAge}>Birthday!</button>
    </div>
  );
}
```

### `useState` vs Class State

| | `useState` (Functional) | `this.state` (Class) |
|-|------------------------|---------------------|
| Initial state | `useState(initialValue)` | `this.state = { ... }` |
| Update state | `setState(newValue)` | `this.setState({ ... })` |
| Merges state? | No — replaces entirely | Yes — shallow merge |

---

## 6. React Hooks

### What are Hooks?

**Definition:** Built-in functions provided by React that allow **functional components** to use state, lifecycle features, and other React capabilities.

- Introduced in React 16.8
- Before Hooks, state and lifecycle were only possible in class components
- Hooks must be called at the **top level** (not inside conditionals or loops)
- Hooks can only be called in **functional components** or **custom hooks**

### Top React Hooks

| Hook | Purpose |
|------|---------|
| `useState` | Manage local component state |
| `useEffect` | Handle side effects (API calls, subscriptions) |
| `useContext` | Consume Context values |
| `useReducer` | Manage complex state logic |
| `useCallback` | Memoize functions |
| `useMemo` | Memoize computed values |
| `useRef` | Access DOM elements or persist values |
| `useLayoutEffect` | Synchronous side effects after DOM mutations |
| `useId` | Generate unique IDs |
| `useTransition` | Mark non-urgent state updates |

### `useEffect`

**Definition:** Used to perform **side effects** in functional components — things that happen *after* rendering (API calls, subscriptions, timers, DOM manipulation).

**Two parameters:** (effect function, dependency array)

```jsx
useEffect(() => {
  // side effect code here
  return () => { /* cleanup function (optional) */ };
}, [dependencies]);
```

| Dependency Array | Behavior |
|-----------------|----------|
| Not provided | Runs after every render |
| `[]` (empty) | Runs once after first render (like `componentDidMount`) |
| `[val]` (with values) | Runs when any of the listed values change |

```jsx
import React, { useState, useEffect } from "react";

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // Run once when component mounts
  useEffect(() => {
    setLoading(true);
    fetch(`https://api.example.com/users/${userId}`)
      .then(res => res.json())
      .then(data => {
        setUser(data);
        setLoading(false);
      });
  }, [userId]); // re-runs when userId changes

  if (loading) return <p>Loading...</p>;
  return <div>{user?.name}</div>;
}
```

**Cleanup function:** Return a function from `useEffect` to clean up subscriptions, timers, or event listeners.

```jsx
useEffect(() => {
  const timer = setInterval(() => console.log("tick"), 1000);
  return () => clearInterval(timer); // cleanup on unmount
}, []);
```

### `useContext`

**Definition:** Provides a way to consume context values without prop drilling. See [Context API section](#10-context-api) for full details.

```jsx
const theme = useContext(ThemeContext);
```

### `useReducer`

**Definition:** An alternative to `useState` for managing **complex state logic** (multiple sub-values, next state depends on previous).

```jsx
const [state, dispatch] = useReducer(reducer, initialState);
```

```jsx
const initialState = { count: 0 };

function reducer(state, action) {
  switch (action.type) {
    case "increment": return { count: state.count + 1 };
    case "decrement": return { count: state.count - 1 };
    case "reset":     return initialState;
    default: throw new Error("Unknown action");
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, initialState);
  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: "increment" })}>+</button>
      <button onClick={() => dispatch({ type: "decrement" })}>-</button>
      <button onClick={() => dispatch({ type: "reset" })}>Reset</button>
    </div>
  );
}
```

### `useRef`

**Definition:** Returns a mutable ref object whose `.current` property persists across renders. Does NOT trigger re-renders when changed.

**Two main uses:**
1. Accessing DOM elements directly
2. Storing mutable values that persist between renders without causing re-renders

```jsx
import { useRef, useEffect } from "react";

// Use 1: Access DOM element
function FocusInput() {
  const inputRef = useRef(null);

  const focusInput = () => inputRef.current.focus();

  return (
    <div>
      <input ref={inputRef} type="text" />
      <button onClick={focusInput}>Focus Input</button>
    </div>
  );
}

// Use 2: Persist value without re-render
function Timer() {
  const intervalRef = useRef(null);

  const start = () => {
    intervalRef.current = setInterval(() => console.log("tick"), 1000);
  };
  const stop = () => clearInterval(intervalRef.current);

  return (
    <div>
      <button onClick={start}>Start</button>
      <button onClick={stop}>Stop</button>
    </div>
  );
}
```

### `useMemo`

**Definition:** Memoizes the **return value** of an expensive computation. Only recalculates when dependencies change.

```jsx
import { useMemo } from "react";

function ExpensiveList({ items, filter }) {
  const filteredItems = useMemo(() => {
    console.log("Filtering..."); // only runs when items or filter change
    return items.filter(item => item.includes(filter));
  }, [items, filter]);

  return <ul>{filteredItems.map(item => <li key={item}>{item}</li>)}</ul>;
}
```

### `useCallback`

**Definition:** Memoizes a **function reference** so it doesn't get recreated on every render. Useful when passing callbacks to child components that are wrapped in `React.memo`.

```jsx
import { useCallback, useState } from "react";

function Parent() {
  const [count, setCount] = useState(0);

  // Without useCallback, new function created on every render
  const handleClick = useCallback(() => {
    console.log("Button clicked");
  }, []); // no dependencies — stable reference

  return (
    <div>
      <p>{count}</p>
      <button onClick={() => setCount(c => c + 1)}>Update Parent</button>
      <Child onClick={handleClick} />
    </div>
  );
}
```

### `useMemo` vs `useCallback`

| | `useMemo` | `useCallback` |
|-|-----------|---------------|
| Returns | Memoized **value** | Memoized **function** |
| Use for | Expensive calculations | Stable function references |
| Example | Filtered/sorted data | Event handlers passed to children |

### `useLayoutEffect`

**Definition:** Like `useEffect` but fires **synchronously** after all DOM mutations and before the browser paints. Use for DOM measurements.

```jsx
useLayoutEffect(() => {
  // runs synchronously after DOM update, before browser paint
  const height = elementRef.current.offsetHeight;
  setHeight(height);
}, []);
```

> Use `useEffect` unless you need to read DOM layout. `useLayoutEffect` can block the paint.

### Custom Hooks

**Definition:** Custom hooks are JavaScript functions whose name starts with `use` that can call other hooks — allowing you to extract and reuse stateful logic.

```jsx
// Custom hook — useFetch
function useFetch(url) {
  const [data, setData]       = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError]     = useState(null);

  useEffect(() => {
    setLoading(true);
    fetch(url)
      .then(res => {
        if (!res.ok) throw new Error("Network error");
        return res.json();
      })
      .then(data => { setData(data); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [url]);

  return { data, loading, error };
}

// Usage
function UserList() {
  const { data, loading, error } = useFetch("https://api.example.com/users");

  if (loading) return <p>Loading...</p>;
  if (error)   return <p>Error: {error}</p>;
  return <ul>{data.map(u => <li key={u.id}>{u.name}</li>)}</ul>;
}
```

---

## 7. Component Lifecycle

### Lifecycle Phases

Every React component goes through 3 lifecycle phases:

| Phase | When | Description |
|-------|------|-------------|
| **Mounting** | Component created & inserted into DOM | Initial render |
| **Updating** | Component re-renders due to state/prop change | Re-render phase |
| **Unmounting** | Component removed from DOM | Cleanup phase |

### Class Component Lifecycle Methods

**Mounting Phase:**
1. `constructor(props)` — Initialize state, bind methods
2. `getDerivedStateFromProps()` — Sync state from props (rare use)
3. `render()` — Returns JSX (only required method)
4. `componentDidMount()` — Called after first render; ideal for API calls, subscriptions

**Updating Phase:**
1. `getDerivedStateFromProps()` — Before re-render
2. `shouldComponentUpdate()` — Returns `true`/`false` to allow/block re-render (performance)
3. `render()` — Re-renders the component
4. `getSnapshotBeforeUpdate()` — Capture DOM info before update
5. `componentDidUpdate(prevProps, prevState)` — After re-render; compare with previous values

**Unmounting Phase:**
1. `componentWillUnmount()` — Cleanup: cancel timers, unsubscribe, remove event listeners

```jsx
import React, { Component } from "react";

class LifecycleExample extends Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
    console.log("1. constructor");
  }

  componentDidMount() {
    console.log("3. componentDidMount — fetch data here");
  }

  componentDidUpdate(prevProps, prevState) {
    if (prevState.count !== this.state.count) {
      console.log("componentDidUpdate — count changed");
    }
  }

  componentWillUnmount() {
    console.log("componentWillUnmount — cleanup here");
  }

  render() {
    console.log("2. render");
    return (
      <div>
        <p>{this.state.count}</p>
        <button onClick={() => this.setState({ count: this.state.count + 1 })}>
          +
        </button>
      </div>
    );
  }
}
```

### Functional Component Lifecycle with Hooks

```jsx
import { useState, useEffect } from "react";

function FunctionalLifecycle() {
  const [count, setCount] = useState(0);

  // componentDidMount
  useEffect(() => {
    console.log("Mounted — fetch data here");

    // componentWillUnmount (cleanup)
    return () => console.log("Unmounted — cleanup here");
  }, []);

  // componentDidUpdate (when count changes)
  useEffect(() => {
    console.log("count updated:", count);
  }, [count]);

  return (
    <button onClick={() => setCount(c => c + 1)}>
      Count: {count}
    </button>
  );
}
```

### Class Component State Management

```jsx
class Counter extends Component {
  constructor(props) {
    super(props); // required — calls parent constructor
    this.state = { count: 0 };
  }

  increment = () => {
    this.setState({ count: this.state.count + 1 }); // update
  };

  render() {
    return (
      <div>
        <p>Count: {this.state.count}</p>  {/* render */}
        <button onClick={this.increment}>+</button>
      </div>
    );
  }
}
```

**`super(props)`** — Must be called in the constructor before using `this`. Calls the parent class (`Component`) constructor to ensure proper initialization.

---

## 8. Routing

### React Router

**Definition:** A library for handling client-side routing in React. Enables navigation and rendering of different components based on the URL without a full page refresh.

**Installation:** `npm install react-router-dom`

### Core Routing Components

| Component | Role |
|-----------|------|
| `<BrowserRouter>` | Wraps the whole app; provides routing context |
| `<Routes>` | Container for all `<Route>` definitions |
| `<Route path="..." element={...}>` | Maps a URL path to a component |
| `<Link to="...">` | Client-side navigation (no page reload) |
| `<NavLink>` | Like `Link` but applies active class automatically |
| `<Navigate>` | Programmatic redirect |
| `<Outlet>` | Renders nested routes |

```jsx
// index.js
import { BrowserRouter as Router } from "react-router-dom";
root.render(
  <Router>
    <App />
  </Router>
);

// App.js
import { Routes, Route, Link } from "react-router-dom";

const Home    = () => <h2>Home Page</h2>;
const About   = () => <h2>About Page</h2>;
const Contact = () => <h2>Contact Page</h2>;
const NotFound = () => <h2>404 — Page Not Found</h2>;

function App() {
  return (
    <div>
      <nav>
        <Link to="/">Home</Link> |
        <Link to="/about">About</Link> |
        <Link to="/contact">Contact</Link>
      </nav>

      <Routes>
        <Route path="/"        element={<Home />} />
        <Route path="/about"   element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="*"        element={<NotFound />} />  {/* 404 */}
      </Routes>
    </div>
  );
}
```

### Route Parameters

Dynamic segments in the URL path that pass values to the component.

```jsx
// Define a route with a parameter
<Route path="/users/:userId" element={<UserProfile />} />

// Access the parameter in the component
import { useParams } from "react-router-dom";

function UserProfile() {
  const { userId } = useParams();
  return <h2>User ID: {userId}</h2>;
}
```

### Programmatic Navigation

```jsx
import { useNavigate } from "react-router-dom";

function LoginButton() {
  const navigate = useNavigate();
  const handleLogin = () => {
    // ... login logic
    navigate("/dashboard");         // go to dashboard
    // navigate(-1)                 // go back
    // navigate("/login", { replace: true }) // replace history entry
  };
  return <button onClick={handleLogin}>Login</button>;
}
```

### Query Parameters

```jsx
// URL: /search?q=react&page=2
import { useSearchParams } from "react-router-dom";

function SearchPage() {
  const [searchParams, setSearchParams] = useSearchParams();
  const query = searchParams.get("q");    // "react"
  const page  = searchParams.get("page"); // "2"
  return <p>Searching for: {query} (Page {page})</p>;
}
```

### Nested Routes

```jsx
<Routes>
  <Route path="/dashboard" element={<Dashboard />}>
    <Route index element={<Overview />} />
    <Route path="settings" element={<Settings />} />
    <Route path="profile"  element={<Profile />} />
  </Route>
</Routes>

// Dashboard component — Outlet renders child route
function Dashboard() {
  return (
    <div>
      <nav>
        <Link to="/dashboard">Overview</Link>
        <Link to="/dashboard/settings">Settings</Link>
      </nav>
      <Outlet />  {/* Child route renders here */}
    </div>
  );
}
```

### Protected Routes (Auth Guard)

```jsx
function PrivateRoute({ children }) {
  const isAuthenticated = useAuth(); // custom hook
  return isAuthenticated ? children : <Navigate to="/login" replace />;
}

<Route path="/dashboard" element={
  <PrivateRoute>
    <Dashboard />
  </PrivateRoute>
} />
```

---

## 9. Forms — Controlled vs Uncontrolled

### Controlled Components

**Definition:** Form elements whose values are **controlled by React state**. Every keystroke updates state, which then drives the input value — React is the "single source of truth."

```jsx
function ControlledForm() {
  const [name, setName]   = useState("");
  const [email, setEmail] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();  // prevent page refresh
    if (!email.includes("@")) {
      setError("Invalid email");
      return;
    }
    console.log("Submitted:", { name, email });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Name"
      />
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
      />
      {error && <p style={{ color: "red" }}>{error}</p>}
      <button type="submit">Submit</button>
    </form>
  );
}
```

### Uncontrolled Components

**Definition:** Form elements that manage their own state in the DOM. React accesses values using `useRef` only when needed.

```jsx
function UncontrolledForm() {
  const inputRef = useRef(null);

  const handleClick = () => {
    alert(`You typed: ${inputRef.current.value}`);
  };

  return (
    <div>
      <input type="text" ref={inputRef} placeholder="Type here..." />
      <button onClick={handleClick}>Read Value</button>
    </div>
  );
}
```

### Controlled vs Uncontrolled Comparison

| Feature | Controlled | Uncontrolled |
|---------|-----------|--------------|
| State managed by | React (`useState`) | DOM |
| Access value | Via state | Via `useRef` |
| Re-renders on change | Yes | No |
| Validation | Easy — check state on each change | Harder — check on submit |
| Best practice | ✅ Recommended | Use sparingly |

### Handling Multiple Inputs

```jsx
function MultiForm() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: ""
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value })); // dynamic key
  };

  return (
    <form>
      <input name="name"     value={formData.name}     onChange={handleChange} />
      <input name="email"    value={formData.email}    onChange={handleChange} />
      <input name="password" value={formData.password} onChange={handleChange} />
    </form>
  );
}
```

---

## 10. Context API

### What is Context?

**Definition:** A built-in React feature that allows sharing data across the component tree **without prop drilling**. Best for global data like theme, language, authenticated user.

**When to use Context vs Redux:**
- **Context** — Light global state (theme, locale, auth). Simpler setup, built-in.
- **Redux** — Large, complex state with many interactions. Better devtools and middleware.

### Using Context — 3 Steps

**Step 1: Create the Context**
```jsx
// ThemeContext.js
import { createContext } from "react";
const ThemeContext = createContext("light"); // default value
export default ThemeContext;
```

**Step 2: Provide the Context**
```jsx
// App.js
import ThemeContext from "./ThemeContext";

function App() {
  const [theme, setTheme] = useState("light");
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <Layout />
    </ThemeContext.Provider>
  );
}
```

**Step 3: Consume the Context**
```jsx
// DeepChild.js
import { useContext } from "react";
import ThemeContext from "./ThemeContext";

function DeepChild() {
  const { theme, setTheme } = useContext(ThemeContext);
  return (
    <div>
      <p>Current theme: {theme}</p>
      <button onClick={() => setTheme(t => t === "light" ? "dark" : "light")}>
        Toggle Theme
      </button>
    </div>
  );
}
```

### Context API Use Cases

1. **Theme Switching** — Dark/light mode across all components
2. **Localization** — Language preference
3. **Authentication** — Current user info available everywhere
4. **Configuration Settings** — API endpoints, feature flags
5. **Notification System** — Centralized notification state

### Context with `useReducer` (Mini-Redux Pattern)

```jsx
const CounterContext = createContext();

function counterReducer(state, action) {
  switch (action.type) {
    case "increment": return { count: state.count + 1 };
    case "decrement": return { count: state.count - 1 };
    default: return state;
  }
}

function CounterProvider({ children }) {
  const [state, dispatch] = useReducer(counterReducer, { count: 0 });
  return (
    <CounterContext.Provider value={{ state, dispatch }}>
      {children}
    </CounterContext.Provider>
  );
}

// Usage anywhere in the tree
function Counter() {
  const { state, dispatch } = useContext(CounterContext);
  return (
    <div>
      <p>{state.count}</p>
      <button onClick={() => dispatch({ type: "increment" })}>+</button>
    </div>
  );
}
```

---

## 11. Redux & State Management

### What is Redux?

**Definition:** An open-source JS library for **centralized state management**. All application state lives in one place (the Store), and components can read/update it in a predictable manner.

**When to use Redux:**
- Large-scale applications with complex, shared state
- Multiple components need the same piece of state
- State logic is complex (many transitions, derived state)

### Redux Core Concepts

**1. Store** — Centralized place holding the entire state of the application.

**2. Action** — A plain JS object that describes *what happened*. Must have a `type` property.

**3. Reducer** — A pure function that takes `(previousState, action)` and returns the new state. Contains the state update logic.

**4. Dispatch** — The method used to send (dispatch) an action to the store.

**5. Selector** — A function that reads a specific piece of state from the store.

### Redux Data Flow (Unidirectional)

```
User Interaction
      ↓
Component dispatches an Action
      ↓
Reducer receives (previousState, action) → returns new state
      ↓
Store updates with new state
      ↓
Component re-renders with new state
```

### Redux 3 Core Principles

1. **Single Source of Truth** — All state in one store; consistent view across the app
2. **State is Read-Only** — Can only change state by dispatching actions (no direct mutation)
3. **Changes via Pure Functions** — Reducers are pure: same input → same output; no side effects

### Redux Toolkit (RTK) — Modern Redux

```jsx
// store.js
import { configureStore } from "@reduxjs/toolkit";
import counterReducer from "./counterSlice";

const store = configureStore({
  reducer: {
    counter: counterReducer,
  },
});
export default store;

// counterSlice.js
import { createSlice } from "@reduxjs/toolkit";

const counterSlice = createSlice({
  name: "counter",
  initialState: { count: 0 },
  reducers: {
    increment: (state) => { state.count += 1; },  // RTK uses Immer — safe mutation
    decrement: (state) => { state.count -= 1; },
    incrementBy: (state, action) => { state.count += action.payload; },
  },
});

export const { increment, decrement, incrementBy } = counterSlice.actions;
export default counterSlice.reducer;

// index.js — wrap app with Provider
import { Provider } from "react-redux";
import store from "./store";

root.render(
  <Provider store={store}>
    <App />
  </Provider>
);

// CounterComponent.js
import { useSelector, useDispatch } from "react-redux";
import { increment, decrement, incrementBy } from "./counterSlice";

function Counter() {
  const count    = useSelector(state => state.counter.count);
  const dispatch = useDispatch();

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => dispatch(increment())}>+</button>
      <button onClick={() => dispatch(decrement())}>-</button>
      <button onClick={() => dispatch(incrementBy(5))}>+5</button>
    </div>
  );
}
```

### Classic Redux (without RTK)

```jsx
// reducer.js
const initialState = { count: 0 };
const counterReducer = (state = initialState, action) => {
  switch (action.type) {
    case "INCREMENT": return { count: state.count + 1 };
    case "DECREMENT": return { count: state.count - 1 };
    default: return state;
  }
};
export default counterReducer;

// actions.js
export const increment = () => ({ type: "INCREMENT" });
export const decrement = () => ({ type: "DECREMENT" });
```

### `useSelector` vs `mapStateToProps`

```jsx
// Modern (hooks) — useSelector
const count = useSelector(state => state.counter.count);

// Legacy (connect) — mapStateToProps
const mapStateToProps = (state) => ({ count: state.counter.count });
export default connect(mapStateToProps)(CounterComponent);
```

### Redux Middleware

**Definition:** Middleware adds extra functionality between dispatching an action and reaching the reducer. Used for logging, async operations (API calls), error handling.

**Common middleware:**
- **Redux Thunk** — Allows action creators to return functions (for async actions)
- **Redux Saga** — Handles side effects using generator functions
- **Redux Logger** — Logs all state changes

```jsx
// Async action with Redux Thunk
export const fetchUsers = () => async (dispatch) => {
  dispatch({ type: "FETCH_USERS_REQUEST" });
  try {
    const res  = await fetch("/api/users");
    const data = await res.json();
    dispatch({ type: "FETCH_USERS_SUCCESS", payload: data });
  } catch (error) {
    dispatch({ type: "FETCH_USERS_FAILURE", payload: error.message });
  }
};

// With RTK (createAsyncThunk)
import { createAsyncThunk } from "@reduxjs/toolkit";

export const fetchUsers = createAsyncThunk("users/fetch", async () => {
  const res  = await fetch("/api/users");
  return res.json();
});
```

### State Management — When to Use What

| Solution | Use When |
|----------|---------|
| `useState` | Simple, local component state |
| `useReducer` | Complex local state with multiple sub-values |
| Context API | Light global state (theme, auth, locale) — small/medium app |
| Redux Toolkit | Large app with complex, shared state; need for devtools |
| Zustand / Jotai | Simpler alternatives to Redux for medium apps |

---

## 12. Performance Optimization

### React.memo

**Definition:** A Higher-Order Component that memoizes a functional component. Prevents re-rendering if **props haven't changed**.

```jsx
const ExpensiveChild = React.memo(function Child({ count, name }) {
  console.log("Child rendered"); // only re-renders if count or name change
  return <div>{name}: {count}</div>;
});

function Parent() {
  const [count, setCount]     = useState(0);
  const [other, setOther]     = useState(0);

  return (
    <div>
      <ExpensiveChild count={count} name="Alice" />
      <button onClick={() => setCount(c => c + 1)}>Update Child Props</button>
      <button onClick={() => setOther(o => o + 1)}>Update Other (no re-render of child)</button>
    </div>
  );
}
```

### `useMemo` and `useCallback` for Optimization

```jsx
function ProductList({ products, category }) {
  // Only recalculates when products or category changes
  const filtered = useMemo(
    () => products.filter(p => p.category === category),
    [products, category]
  );

  // Stable function reference — won't re-create on every render
  const handleSelect = useCallback((id) => {
    console.log("Selected:", id);
  }, []);

  return filtered.map(p => (
    <ProductCard key={p.id} product={p} onSelect={handleSelect} />
  ));
}
```

### React Profiler

**Definition:** A tool for measuring the performance of a React application — how often components render and at what cost.

```jsx
// Wrap sections you want to profile
<React.Profiler id="Navigation" onRender={callback}>
  <Navigation />
</React.Profiler>

function callback(id, phase, actualDuration, baseDuration, startTime, commitTime) {
  console.log(`${id} took ${actualDuration}ms`);
}
```

> Also available as the **React DevTools Profiler** tab in browser devtools.

### Performance Best Practices

1. **`React.memo`** — Prevent unnecessary child re-renders
2. **`useMemo`** — Memoize expensive calculations
3. **`useCallback`** — Stable function references for child props
4. **Code Splitting** — Load components only when needed (`React.lazy`)
5. **Virtualization** — Only render visible items in long lists (`react-window`, `react-virtual`)
6. **Avoid anonymous functions** in render — creates new reference every time
7. **Avoid deep object comparisons** — keep state flat
8. **Use `key` correctly** — helps React's diffing algorithm
9. **Lazy load images** — use `loading="lazy"` attribute
10. **Avoid index as key** — can cause reconciliation issues with dynamic lists

---

## 13. Code Splitting & Lazy Loading

### What is Code Splitting?

**Definition:** Splitting the JS bundle into **smaller chunks** that are loaded **on demand** rather than all at once. Reduces initial bundle size and improves load time.

| Without Code Splitting | With Code Splitting |
|----------------------|---------------------|
| All code in one bundle (e.g., 500KB) | Main bundle (200KB) + chunks loaded later |
| Slower initial load | Faster initial load |
| All code loaded upfront | Code loaded only when needed |

### Implementing Code Splitting with React.lazy + Suspense

```jsx
import React, { lazy, Suspense } from "react";

// Lazy load components
const Dashboard   = lazy(() => import("./Dashboard"));
const UserProfile = lazy(() => import("./UserProfile"));
const Settings    = lazy(() => import("./Settings"));

function App() {
  return (
    <div>
      <h1>My App</h1>
      {/* Suspense shows fallback while the chunk loads */}
      <Suspense fallback={<div>Loading...</div>}>
        <Routes>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/profile"   element={<UserProfile />} />
          <Route path="/settings"  element={<Settings />} />
        </Routes>
      </Suspense>
    </div>
  );
}
```

### Key Concepts

- **`React.lazy()`** — Dynamically imports a component. Returns a lazy component.
- **`Suspense`** — Wraps lazy components. Shows `fallback` UI while loading.
- **`import()`** — Dynamic import returns a Promise. Triggers when component is needed.
- **`fallback` prop** — UI shown while the lazy component is loading.

### 5 Benefits of Code Splitting

1. **Faster initial load** — Only essential code loads first
2. **Optimized bandwidth** — Users don't download code they never use
3. **Improved caching** — Unchanged chunks stay cached
4. **Parallel loading** — Multiple small chunks can load in parallel
5. **Better maintainability** — Smaller, focused bundles

### Reactive Programming in React

**Definition:** A paradigm that focuses on **reacting to changes and events** in a declarative, asynchronous manner.

**Ways React implements reactive programming:**
1. **State & Props** — Components react to state/prop changes
2. **React Hooks** — `useState`, `useEffect` for reactive state and side effects
3. **Event Handling** — React to user interactions
4. **Context API** — Reactively share global state
5. **Redux** — Reactive state management pattern
6. **Lifecycle Methods** — React to component lifecycle events
7. **Async/Await** — Handle async operations reactively

---

## 14. Higher-Order Components & Patterns

### Higher-Order Components (HOC)

**Definition:** A function that takes a component as argument and returns a **new enhanced component** with extra features. A pattern for reusing component logic.

```jsx
// Syntax
const EnhancedComponent = HOC(OriginalComponent);
```

**Common HOC use cases:** Authentication, logging, data fetching, theming, permissions.

```jsx
// HOC: withLogger — adds logging to any component
function withLogger(WrappedComponent) {
  return function WithLogger(props) {
    console.log(`Rendering: ${WrappedComponent.displayName || WrappedComponent.name}`);
    return <WrappedComponent {...props} />;
  };
}

// HOC: withAuth — protects routes
function withAuth(WrappedComponent) {
  return function WithAuth(props) {
    const isAuthenticated = useAuth();
    if (!isAuthenticated) return <Navigate to="/login" />;
    return <WrappedComponent {...props} />;
  };
}

// Usage
const LoggedButton    = withLogger(Button);
const ProtectedDash   = withAuth(Dashboard);
```

### Render Props Pattern

**Definition:** Sharing stateful logic by passing a **function as a prop** that returns JSX. The function receives data and decides what to render.

```jsx
// Component that handles mouse position logic
function MouseTracker({ render }) {
  const [position, setPosition] = useState({ x: 0, y: 0 });

  const handleMouseMove = (e) => {
    setPosition({ x: e.clientX, y: e.clientY });
  };

  return (
    <div onMouseMove={handleMouseMove} style={{ height: "200px" }}>
      {render(position)}
    </div>
  );
}

// Usage — parent decides what to render with position data
<MouseTracker
  render={({ x, y }) => (
    <p>Mouse is at: {x}, {y}</p>
  )}
/>
```

### Compound Component Pattern

Multiple components work together to form one cohesive UI, sharing state through Context.

```jsx
// Accordion compound component
const AccordionContext = createContext();

function Accordion({ children }) {
  const [openIndex, setOpenIndex] = useState(null);
  return (
    <AccordionContext.Provider value={{ openIndex, setOpenIndex }}>
      <div>{children}</div>
    </AccordionContext.Provider>
  );
}

function AccordionItem({ children, index }) {
  const { openIndex, setOpenIndex } = useContext(AccordionContext);
  const isOpen = openIndex === index;
  return (
    <div>
      <button onClick={() => setOpenIndex(isOpen ? null : index)}>
        Toggle
      </button>
      {isOpen && <div>{children}</div>}
    </div>
  );
}

// Usage
<Accordion>
  <AccordionItem index={0}>Content 1</AccordionItem>
  <AccordionItem index={1}>Content 2</AccordionItem>
</Accordion>
```

---

## 15. API Calls — fetch vs axios

### fetch (Built-in)

```jsx
// GET request
async function getData() {
  try {
    const response = await fetch("https://api.example.com/data");
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error:", error);
  }
}

// POST request
await fetch("https://api.example.com/users", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ name: "Alice" })
});
```

### axios (Third-party library)

```jsx
// Installation: npm install axios
import axios from "axios";

// GET request
const response = await axios.get("https://api.example.com/data");
console.log(response.data); // data is already parsed!

// POST request
await axios.post("https://api.example.com/users", { name: "Alice" });

// Axios instance with base URL
const api = axios.create({
  baseURL: "https://api.example.com",
  timeout: 5000,
  headers: { "Authorization": `Bearer ${token}` }
});
const data = await api.get("/users");
```

### fetch vs axios

| Feature | fetch | axios |
|---------|-------|-------|
| Built-in | Yes — no install needed | No — third-party library |
| Response parsing | Must call `response.json()` manually | Auto-parsed (`.data`) |
| HTTP error detection | Must check `response.ok` manually | Auto-throws for 4xx/5xx |
| Request cancellation | AbortController | Built-in (`CancelToken`) |
| Interceptors | Not available | Built-in |
| Request/response transform | Manual | Built-in |
| Best for | Simple requests, minimal dependencies | Complex apps with auth, interceptors |

### API Calls in a React Component

```jsx
function UserList() {
  const [users, setUsers]     = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError]     = useState(null);

  useEffect(() => {
    let isMounted = true; // prevent state update on unmounted component

    async function fetchUsers() {
      try {
        const res  = await fetch("https://jsonplaceholder.typicode.com/users");
        if (!res.ok) throw new Error("Failed to fetch");
        const data = await res.json();
        if (isMounted) {
          setUsers(data);
          setLoading(false);
        }
      } catch (err) {
        if (isMounted) {
          setError(err.message);
          setLoading(false);
        }
      }
    }

    fetchUsers();
    return () => { isMounted = false; }; // cleanup
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error)   return <p>Error: {error}</p>;

  return (
    <ul>
      {users.map(user => <li key={user.id}>{user.name}</li>)}
    </ul>
  );
}
```

---

## 16. Error Handling in React

### Error Boundaries

**Definition:** Class components that **catch JavaScript errors** anywhere in their child component tree, log them, and display a fallback UI instead of crashing.

- Only work for render-time errors, not async errors or event handlers
- Must be **class components** (no functional equivalent yet)

```jsx
import React, { Component } from "react";

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    // Log to error monitoring service (e.g., Sentry)
    console.error("Error caught:", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div>
          <h2>Something went wrong.</h2>
          <button onClick={() => this.setState({ hasError: false })}>
            Try Again
          </button>
        </div>
      );
    }
    return this.props.children;
  }
}

// Usage
function App() {
  return (
    <ErrorBoundary>
      <MightCrash />
    </ErrorBoundary>
  );
}
```

### try/catch for Async Errors

```jsx
async function fetchData() {
  try {
    const res  = await fetch("/api/data");
    const data = await res.json();
    setData(data);
  } catch (error) {
    setError(error.message);
  }
}
```

---

## 17. Testing in React

### Types of Tests

| Type | What it tests | Tools |
|------|--------------|-------|
| Unit tests | Individual functions/components | Jest, Vitest |
| Integration tests | Multiple components together | React Testing Library |
| End-to-End (E2E) | Full user flows in browser | Cypress, Playwright |

### React Testing Library Basics

```jsx
// Button.test.jsx
import { render, screen, fireEvent } from "@testing-library/react";
import Button from "./Button";

test("renders button with correct text", () => {
  render(<Button label="Click Me" />);
  const button = screen.getByText("Click Me");
  expect(button).toBeInTheDocument();
});

test("calls onClick when clicked", () => {
  const mockFn = jest.fn();
  render(<Button label="Click" onClick={mockFn} />);
  fireEvent.click(screen.getByText("Click"));
  expect(mockFn).toHaveBeenCalledTimes(1);
});
```

---

## 18. Advanced Concepts

### Reconciliation & the Diffing Algorithm

**Definition:** The process React uses to update the DOM efficiently. When state/props change, React builds a new Virtual DOM and **diffs** it against the previous one to find the minimum set of changes.

**Key rules of the diffing algorithm:**
- Elements of different types → tear down old tree, build new tree
- Elements of the same type → update attributes only
- `key` prop helps React match list items across renders

### React Fiber

**Definition:** The reconciliation engine introduced in React 16. Fiber breaks rendering work into **units** that can be paused, resumed, or aborted — enabling features like Concurrent Mode.

**Why Fiber:** Previous reconciliation was synchronous and couldn't be interrupted. Fiber enables priority-based rendering.

### Concurrent Mode (React 18)

**Definition:** An experimental set of features enabling React to prepare multiple versions of the UI at the same time, making apps feel more responsive.

```jsx
// useTransition — mark non-urgent updates
import { useTransition, useState } from "react";

function SearchPage() {
  const [query, setQuery]         = useState("");
  const [results, setResults]     = useState([]);
  const [isPending, startTransition] = useTransition();

  const handleChange = (e) => {
    setQuery(e.target.value); // urgent — update input immediately

    startTransition(() => {
      setResults(search(e.target.value)); // non-urgent — can be interrupted
    });
  };

  return (
    <div>
      <input value={query} onChange={handleChange} />
      {isPending ? <p>Loading results...</p> : <ResultsList results={results} />}
    </div>
  );
}
```

### `React.StrictMode`

**Definition:** A tool for highlighting potential problems in an application. Runs extra checks in development mode (double-invokes functions, warns about deprecated APIs).

```jsx
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

### Portals

**Definition:** Render a component into a DOM node that is **outside the parent component's DOM hierarchy**. Useful for modals, tooltips, overlays.

```jsx
import { createPortal } from "react-dom";

function Modal({ children, onClose }) {
  return createPortal(
    <div className="modal-overlay">
      <div className="modal">
        {children}
        <button onClick={onClose}>Close</button>
      </div>
    </div>,
    document.getElementById("modal-root") // different DOM node
  );
}
```

### `forwardRef`

**Definition:** Passes a `ref` from a parent component to a DOM element inside a child component.

```jsx
const Input = React.forwardRef(function Input({ label }, ref) {
  return (
    <div>
      <label>{label}</label>
      <input ref={ref} />
    </div>
  );
});

// Parent
function Form() {
  const inputRef = useRef(null);
  return (
    <div>
      <Input label="Name" ref={inputRef} />
      <button onClick={() => inputRef.current.focus()}>Focus Input</button>
    </div>
  );
}
```

### `useImperativeHandle`

**Definition:** Customizes the instance value that is exposed when using `ref` with `forwardRef`. Lets you control what the parent can access via ref.

```jsx
const FancyInput = React.forwardRef((props, ref) => {
  const inputRef = useRef();

  useImperativeHandle(ref, () => ({
    focus: () => inputRef.current.focus(),
    clear: () => { inputRef.current.value = ""; }
  }));

  return <input ref={inputRef} />;
});

// Parent can now call ref.current.focus() and ref.current.clear()
```

### Server-Side Rendering (SSR) vs Client-Side Rendering (CSR)

| | CSR (React default) | SSR (Next.js) |
|-|--------------------|----|
| HTML generated | On the client browser | On the server |
| Initial load | Blank page → JS loads → renders | Full HTML sent immediately |
| SEO | Poor (content not in initial HTML) | Good (content in HTML) |
| Performance | Slower TTFB | Faster TTFB |
| Framework | React | Next.js, Remix |

---

## 19. Tricky Interview Questions

### 1. Why can't you call hooks inside conditions?

```jsx
// ❌ Wrong
if (condition) {
  const [value, setValue] = useState(0); // breaks rules of hooks!
}

// ✅ Correct — hooks always in same order
const [value, setValue] = useState(0);
if (condition) { /* use value here */ }
```

React tracks hooks by **call order**. Conditional calls break this order between renders.

### 2. What is the difference between `state` and `props`?

| | `state` | `props` |
|-|---------|---------|
| Owner | Component itself | Parent component |
| Mutable | Yes — via `setState` | No — read-only |
| Purpose | Internal data | External configuration |
| Re-render | Yes, on change | Yes, on change |

### 3. What causes a component to re-render?

1. **State changes** — `setState` or `useState` setter called
2. **Props change** — Parent passes new prop values
3. **Parent re-renders** — All children re-render (unless `React.memo`)
4. **Context changes** — Context value changes

### 4. What is the `key` prop and why is it important?

```jsx
// ❌ Using index as key — can cause bugs with dynamic lists
items.map((item, index) => <li key={index}>{item}</li>)

// ✅ Using stable unique ID
items.map(item => <li key={item.id}>{item.name}</li>)
```

`key` helps React identify which items in a list changed, were added, or removed during reconciliation.

### 5. `useEffect` cleanup — why is it needed?

```jsx
useEffect(() => {
  const subscription = subscribeToData(handleData);

  // Without cleanup, subscription leaks when component unmounts!
  return () => subscription.unsubscribe();
}, []);
```

Without cleanup: memory leaks, duplicate subscriptions, state updates on unmounted components.

### 6. When does `useEffect` run with `[]` vs no dependency array?

```jsx
useEffect(() => { /* runs on EVERY render */ });
useEffect(() => { /* runs ONCE after mount */ }, []);
useEffect(() => { /* runs when count changes */ }, [count]);
```

### 7. What is the difference between `React.memo`, `useMemo`, and `useCallback`?

| | `React.memo` | `useMemo` | `useCallback` |
|-|-------------|-----------|---------------|
| Memoizes | Component | Value | Function |
| Prevents | Component re-render | Expensive recalculation | Function re-creation |

### 8. Can you update state directly in React?

```jsx
// ❌ Never mutate state directly
this.state.count = 5;           // Class component
state.items.push(newItem);      // Functional component

// ✅ Always use setter
this.setState({ count: 5 });    // Class
setItems(prev => [...prev, newItem]); // Functional
```

Direct mutation doesn't trigger a re-render. React doesn't know the state changed.

### 9. What is the difference between Context and Redux?

| | Context API | Redux |
|-|------------|-------|
| Setup | Simple, built-in | More setup needed |
| Dev Tools | No | Excellent Redux DevTools |
| Middleware | No | Yes (thunk, saga) |
| Performance | Re-renders all consumers | Selective re-renders |
| Best for | Light global state | Large, complex state |

### 10. Why shouldn't you use index as key in lists?

```jsx
// Problem with index as key + dynamic lists
// If you add/remove items, React maps wrong elements
// Can cause incorrect UI and broken animations

// Safe: use item.id or any stable unique identifier
{users.map(user => <UserCard key={user.id} user={user} />)}
```

### 11. What is the difference between `useEffect` and `useLayoutEffect`?

- `useEffect` — Runs **asynchronously** after the browser has painted
- `useLayoutEffect` — Runs **synchronously** after DOM mutations, before the browser paints

Use `useLayoutEffect` for DOM measurements that need to happen before the user sees anything.

### 12. How does React handle synthetic events?

**Synthetic Events:** React wraps native browser events in a cross-browser compatible `SyntheticEvent` object. In React 17+, events are attached to the root element, not `document`.

```jsx
function Button() {
  const handleClick = (e) => {
    console.log(e.type);        // "click"
    console.log(e.target);      // the DOM element
    e.preventDefault();         // works cross-browser
    e.stopPropagation();        // works cross-browser
  };
  return <button onClick={handleClick}>Click</button>;
}
```

---

## 📝 Quick Revision Cheatsheet

### Core Definitions — One Line Each

| Concept | Definition |
|---------|-----------|
| **React** | JS library for building UIs using reusable components |
| **Virtual DOM** | Lightweight in-memory copy of real DOM; React diffs it to minimize updates |
| **Reconciliation** | Process of comparing old vs new Virtual DOM to find minimum changes |
| **JSX** | JavaScript XML — HTML-like syntax compiled to `React.createElement()` by Babel |
| **Component** | Reusable, independent UI building block that returns JSX |
| **Props** | Read-only data passed from parent to child component |
| **State** | Mutable data managed within a component; changes trigger re-render |
| **Hooks** | Functions that add state and lifecycle to functional components |
| **useState** | Hook to add local state to a functional component |
| **useEffect** | Hook for side effects (API calls, subscriptions); runs after render |
| **useContext** | Hook to consume Context values without prop drilling |
| **useReducer** | Hook for complex state logic with action-based updates |
| **useMemo** | Memoizes a computed value; recalculates only when dependencies change |
| **useCallback** | Memoizes a function reference; prevents re-creation on re-render |
| **useRef** | Access DOM elements or persist values without triggering re-renders |
| **Prop drilling** | Passing props through multiple intermediate components that don't need them |
| **Context API** | Built-in React way to share state globally without prop drilling |
| **Redux** | External state management library with centralized store |
| **Reducer** | Pure function `(state, action) => newState` — handles state transitions |
| **HOC** | Function that takes a component and returns an enhanced component |
| **React.memo** | Wraps a component to prevent re-render when props haven't changed |
| **Code Splitting** | Breaking bundle into smaller chunks loaded on demand |
| **React.lazy** | Dynamically imports a component for code splitting |
| **Suspense** | Shows fallback UI while lazy component or async data is loading |
| **Error Boundary** | Class component that catches errors in child tree and shows fallback |
| **Lifecycle** | Mounting → Updating → Unmounting phases of a component's existence |
| **Controlled component** | Form input whose value is driven by React state |
| **Uncontrolled component** | Form input managed by DOM; accessed via `useRef` |
| **React Fiber** | Reconciliation engine enabling interruptible, prioritized rendering |
| **Portal** | Renders component outside parent DOM hierarchy |

### Most Commonly Asked Topics by Level

```
Basic:        JSX rules, props vs state, functional vs class components,
              useState, useEffect basics, list rendering with key

Intermediate: Lifecycle methods, useEffect dependencies, controlled forms,
              useContext, useRef, useReducer, React Router, prop drilling,
              React.memo, custom hooks

Advanced:     Redux + middleware, code splitting, HOC patterns, 
              useCallback/useMemo optimization, Error Boundaries,
              Portals, forwardRef, Concurrent Mode, Fiber architecture,
              SSR vs CSR, performance profiling
```

---

> **Study Tip:** Focus most on **Hooks** (especially `useEffect` edge cases), **State management patterns**, **Component re-render behavior**, and **Redux data flow** — these are the most frequently tested areas in React interviews from junior to senior level.
