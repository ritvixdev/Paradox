# ⚛️ React — Complete Interview Verbal Answers Guide
### No code. Pure understanding. Every question answered with depth.

> **How to use this:** The **bold sentence** after each question is your opening line — say that first, pause, then expand. The 🎤 blocks are follow-up counter questions — answer them confidently. Read every section out loud before the interview.

---

## 📋 Table of Contents

| Section | Topics |
|---------|--------|
| [React Fundamentals](#fundamentals) | What is React · JSX · Virtual DOM · Components · State & Props |
| [Class vs Functional Components](#components) | Experience · Differences · When to use |
| [React Hooks](#hooks) | Which hooks · useEffect · useMemo · useCallback · useReducer · Custom hooks |
| [Context API & State Management](#context) | Context structure · Provider · useContext · vs Redux |
| [Redux](#redux) | Flow · Reducers · Actions · vs Context |
| [Rendering & Re-rendering](#rendering) | How React renders · Reconciliation · Virtual DOM diffing |
| [Performance Optimization](#performance) | Bundle size · Lazy loading · Suspense · Code splitting · useMemo |
| [Authentication & Storage](#auth) | Token storage · localStorage · sessionStorage · Auth vs Authz |
| [Controlled vs Uncontrolled](#controlled) | Forms · Refs · Differences |
| [HOC — Higher Order Components](#hoc) | What it is · Real examples · vs Hooks |
| [Prop Drilling](#propdrilling) | What it is · Why avoid it · Solutions |
| [Fragments](#fragments) | What they are · Why use them |
| [Data Passing & Hierarchy](#data) | Props · Context · Child to parent |
| [Infinite Scroll](#infinitescroll) | Approach · Debounce · Throttle |
| [CSS & Styling](#css) | Flexbox · MUI · Styling approaches |
| [TypeScript](#typescript) | type vs interface · Generics |
| [Testing](#testing) | Jest · Mocha · Chai · Unit testing |
| [Next.js & Tooling](#nextjs) | Build tools · Next.js basics |
| [Quick Recall Cheatsheet](#cheatsheet) | Opening lines for every topic |

---

<a name="fundamentals"></a>
## 1️⃣ React Fundamentals

---

### Q: What is React?

**React is a JavaScript library for building user interfaces — specifically for building component-based UIs where the view automatically updates when the underlying data changes.**

React was created by Facebook and solves a very specific, very real problem. Before React, when your data changed you had to manually update the DOM — find the right elements, change their text, toggle classes, remove nodes, add nodes. For complex UIs with lots of data and lots of interactions, this manual DOM manipulation became incredibly error-prone and hard to reason about.

React introduced a fundamentally different mental model. Instead of thinking about how to update the UI when data changes, you just describe what the UI should look like for any given state of data, and React handles all the updating automatically. You write components that return descriptions of what should be on screen, and React takes responsibility for making the actual DOM match that description at all times.

The key concepts that make React powerful are its component model — breaking the UI into small, reusable, composable pieces — and its reconciliation system, where React intelligently figures out the minimum number of DOM changes needed to bring the actual DOM in line with your description. This makes updates efficient without you having to think about it.

---

🎤 **"Is React a framework or a library?"**

> React is a library — specifically a UI library. It handles only the view layer. It does not come with built-in routing, data fetching, form handling, or state management solutions. You assemble those from other libraries. A framework like Angular gives you all of that in one package with strong opinions about how to do each thing. React's philosophy is to be minimal and composable — you pick the pieces you need. Next.js could be called a React framework because it adds all those missing pieces on top of React.

---

### Q: What is JSX?

**JSX is a syntax extension for JavaScript that lets you write HTML-like markup directly inside your JavaScript code — it is not HTML, it is syntactic sugar that compiles to plain JavaScript function calls.**

When you write JSX, you are not writing actual HTML that the browser understands. You are writing a special syntax that a build tool like Babel transforms into JavaScript calls — specifically calls to `React.createElement`. Each JSX tag becomes a function call that creates a description of a UI element with its type, its properties, and its children. This description is a plain JavaScript object.

The reason JSX exists is that it makes the relationship between your data and your UI visually clear. When you look at a component, the JSX reads almost like the HTML output it produces, which makes it intuitive to understand what is being rendered. Writing the same thing as raw function calls would be verbose and hard to read.

---

🎤 **"Can you use React without JSX?"**

> Yes, absolutely. JSX is purely a convenience. The underlying reality is just JavaScript function calls. You could write every component using `React.createElement` directly. In practice no one does this for complex UIs because JSX is so much more readable. But understanding that JSX is compiled to function calls is important — it explains why you can only return a single root element from a component, why you need `key` attributes in lists, and why certain JavaScript rules apply to JSX expressions.

---

### Q: What is the virtual DOM?

**The virtual DOM is a lightweight in-memory representation of the actual DOM — it is a JavaScript object tree that mirrors the structure of the real DOM but exists only in memory, not in the browser.**

The real DOM is slow to work with directly. Every time you change it, the browser has to recalculate styles, layout, and repaint the screen — these operations are expensive. If you were naively updating the DOM on every state change, even small data updates could cause significant performance problems.

React's solution is to keep its own description of what the DOM should look like — the virtual DOM. When your state changes, React creates a new virtual DOM tree representing the updated UI. It then compares this new tree against the previous virtual DOM tree — a process called diffing or reconciliation. From this comparison, React determines the minimum set of actual DOM operations needed to bring the real DOM in line with the new description. Only those specific operations are applied to the real DOM. This batching and minimisation of DOM operations is what makes React fast.

---

🎤 **"Can you see the virtual DOM?"**

> You cannot see the virtual DOM the way you can inspect the real DOM in browser DevTools. The virtual DOM is just JavaScript objects living in memory — there is no browser panel for it. You can see the real DOM by opening browser DevTools and going to the Elements or Inspector tab. The real DOM reflects what React has ultimately applied. React DevTools — a browser extension — lets you inspect React's component tree and state, which is the closest you can get to seeing the virtual DOM's logical structure.

---

🎤 **"How does React know which part of the DOM got updated?"**

> React knows through its diffing algorithm. When state changes, React re-runs the affected components and builds a new virtual DOM tree. It then compares this new tree against the snapshot of the previous tree it kept in memory. The algorithm compares nodes level by level — if a node's type changes, React discards the whole subtree and rebuilds it. If the type is the same, React compares the attributes and updates only the changed ones. For lists, React uses the `key` attribute you provide to match old and new list items correctly, which is why keys matter — without them, React has to guess, and it can make wrong assumptions that cause incorrect re-renders or lost state.

---

### Q: What are state and props?

**State is data that a component owns and can change — it is internal and private. Props are data passed into a component from outside — they are external and read-only from the component's perspective.**

State represents the dynamic data that makes a component interactive. When state changes, React re-renders the component to reflect the new data. State is owned by the component that declares it — other components cannot directly read or modify it unless you pass it to them. State is for things that change over time: whether a modal is open, what text is in an input, whether data is loading.

Props are the mechanism for passing data from a parent component to a child component. They are like function arguments — the parent decides what to pass, and the child receives and uses them. A component should never modify its own props. They are read-only. If you need to respond to something in the child that changes the parent's data, you pass a callback function as a prop, and the child calls it.

---

🎤 **"What happens when state changes in a parent component?"**

> When a parent's state changes, React re-renders the parent component and, by default, all of its child components — even if those children did not receive any changed props. This is one of the reasons React performance optimisation matters. `React.memo` is the tool for preventing unnecessary child re-renders by telling React to skip re-rendering a child if its props have not changed.

---

### Q: What is a component?

**A component is the fundamental building block of a React application — it is a self-contained piece of UI that encapsulates its own structure, logic, and potentially its own state.**

Everything in a React application is a component or is built from components. A component takes in some data — props — and returns a description of what should appear on screen. Components are composable, meaning you build complex UIs by nesting and combining smaller components. A button is a component. A form is a component made of smaller components. A whole page is a component made of many section components.

The power of the component model is reusability and separation of concerns. You write a component once and use it in many places. Each component is responsible only for its own piece of the UI. Changes to one component do not accidentally affect others.

---

🎤 **"What are stateful and stateless components?"**

> A stateful component is one that manages its own state — it holds data that can change and drives re-renders when it does. A stateless component, also called a presentational or dumb component, simply receives props and renders based on them. It has no internal state. Stateless components are simpler, easier to test, and more reusable because their output is entirely predictable from their input — given the same props, they always render the same thing. A good architectural practice is to push state as high as it needs to be and keep components stateless wherever possible.

---

🎤 **"What is the simplest form of a React component?"**

> The simplest form is a plain function that takes no arguments and returns JSX. No state, no props, no hooks — just a function that returns a description of some UI. This is a stateless, presentational component in its purest form, and it demonstrates that React components are ultimately just functions. You can make them as simple or as complex as your use case requires.

---

🎤 **"If there is no state change and no data change, is React still a good fit?"**

> React can still be used for fully static content — it will render once and never re-render, which means you lose none of the performance benefits you would otherwise enjoy. The component model still provides organisational value even for static UIs. However, for truly static pages with no interactivity, React may be overkill — a simpler approach like plain HTML or a template engine might be more appropriate. Where React shines is when interactivity, dynamic data, or complex UI state is involved. For purely static pages, Next.js's static site generation — which uses React but pre-renders everything to plain HTML — is often the right middle ground.

---

### Q: How does React work?

**React works by maintaining a virtual representation of the UI in memory, re-running components when their data changes, comparing the new description to the old one, and applying only the necessary changes to the real browser DOM.**

The lifecycle of a React application looks like this. You write components that describe the UI as a function of data. When the application starts, React renders the root component, which renders its children, which render their children, building a complete virtual DOM tree. This tree is then used to paint the real DOM for the first time.

When something changes — a user clicks a button, data arrives from an API, a timer fires — state is updated. React then re-renders the components whose state changed, plus their descendants. It builds a new virtual DOM tree from these re-renders. It compares the new tree to the previous one through reconciliation, identifies what changed, and makes the smallest possible set of real DOM updates.

From the developer's perspective, you never touch the DOM directly. You just update state and trust React to reflect it correctly in the UI. This separation between "what the UI should look like" and "how to update the DOM to match" is what makes React so powerful and why complex UIs remain manageable.

---

<a name="components"></a>
## 2️⃣ Class vs Functional Components

---

### Q: Are you hands-on with class-based or functional components?

**I am primarily experienced with functional components, which is the current standard, but I understand class-based components well enough to read, work with, and maintain them.**

Functional components combined with hooks are the modern way of writing React. They are simpler, more concise, and more composable. Hooks allow functional components to do everything class components could do — manage state, handle side effects, access context — without the complexity of the class syntax. The React team has recommended functional components and hooks as the preferred approach since React 16.8.

Class components are still fully supported and you encounter them in older codebases. They work by extending `React.Component` and implementing lifecycle methods — `componentDidMount`, `componentDidUpdate`, `componentWillUnmount` — to handle different phases of a component's life. The main pain point with class components was that logic related to the same concern — for example, setting up and tearing down a subscription — was split across different lifecycle methods, making it harder to organise code by feature rather than by lifecycle phase.

---

🎤 **"What is the key difference between class and functional components?"**

> Class components manage state through `this.state` and update it through `this.setState`. They handle side effects and lifecycle events through explicit lifecycle methods. Functional components manage state through the `useState` hook and side effects through `useEffect`. The most significant architectural difference is that hooks let you extract and reuse stateful logic across components — you can pull a piece of behaviour into a custom hook and use it anywhere. With class components, sharing stateful logic required patterns like higher-order components or render props, which were more complex and harder to compose cleanly.

---

🎤 **"Have you actually worked with class-based components or only know the concept?"**

> I have worked primarily with functional components in my projects, which is the modern standard. I am familiar with class component syntax, lifecycle methods, and how they map to hooks — `componentDidMount` maps to a `useEffect` with an empty dependency array, `componentDidUpdate` maps to a `useEffect` with dependencies, and `componentWillUnmount` maps to the cleanup function returned inside `useEffect`. If I were working on a legacy codebase with class components, I could read and maintain them confidently.

---

<a name="hooks"></a>
## 3️⃣ React Hooks

---

### Q: Which React hooks have you used?

**I have used most of the core hooks — useState, useEffect, useContext, useRef, useMemo, useCallback, and useReducer — and I have also written custom hooks.**

Each hook solves a specific problem. `useState` is for local component state. `useEffect` is for side effects — things that happen outside the render cycle like API calls, subscriptions, and timers. `useContext` is for reading from a Context without prop drilling. `useRef` is for holding a mutable value that does not trigger re-renders, typically used for DOM references or storing interval IDs. `useMemo` is for expensive calculations you want to cache. `useCallback` is for caching function references to avoid unnecessary child re-renders. `useReducer` is for complex state logic that involves multiple values or complex transitions.

---

🎤 **"What are hooks and why do we use them?"**

> Hooks are functions that let functional components tap into React features that previously required class components — things like state, lifecycle events, and context. We use hooks because they solve the biggest organisational problem with class components: that related logic was scattered across different lifecycle methods. Hooks let you organise code by concern — all the logic for a feature lives together, rather than being split between `componentDidMount` and `componentWillUnmount`. They also enable the powerful pattern of custom hooks — packaging reusable stateful logic as a function you can share across components.

---

### Q: If you use setInterval inside useEffect, where should you clear it?

**You clear it in the cleanup function that you return from inside the same useEffect — this ensures the interval is stopped when the component unmounts or before the effect runs again.**

`useEffect` has a built-in mechanism for cleanup. When you return a function from inside a `useEffect`, React calls that function before the component is removed from the screen and also before re-running the effect if the dependencies change. If you set up a `setInterval` and never clear it, the interval keeps firing even after the component is gone. This is a classic memory leak. The interval's callback may try to update state on a component that no longer exists, causing errors.

The rule is simple: whatever you set up in a `useEffect`, you must clean up in the return function of that same effect. Subscriptions, event listeners, timers, WebSocket connections — all of them should be torn down in the cleanup to prevent memory leaks and ghost callbacks.

---

🎤 **"What happens if you pass an empty dependency array to useEffect?"**

> With an empty dependency array, the effect runs exactly once — after the component first mounts — and the cleanup runs exactly once — when the component unmounts. This is the equivalent of `componentDidMount` and `componentWillUnmount` combined. The empty array tells React that this effect does not depend on any changing data, so there is no reason to run it again. This is the correct pattern for initial data fetching, setting up a subscription once, or starting a timer that should persist for the component's entire lifetime.

---

🎤 **"What happens if you completely remove the dependency array?"**

> Without any dependency array, the effect runs after every single render — not just the first. This means every time the component re-renders for any reason — any state change, any props change — the effect fires again. For most effects, this is not what you want. It can lead to infinite loops if the effect itself causes a state update, or to performance problems if the effect makes an API call. Removing the dependency array is rarely intentional in production code.

---

### Q: In what scenario have you used useMemo?

**I have used useMemo when I have an expensive computation that takes input data and produces derived output — useMemo caches the result and only recomputes it when the inputs actually change.**

The classic scenario is filtering or transforming a large list. Imagine you have a list of thousands of products that you need to filter by a search term and sort by price. This filtering and sorting logic runs every render. If the parent component re-renders for any unrelated reason — maybe a loading spinner state changes — the filtering and sorting would run again even though the product data and search term have not changed at all. That wasted computation is exactly what `useMemo` prevents. You tell React: run this computation, cache the result, and only re-run it when these specific values change.

---

🎤 **"What is the difference between useMemo and useCallback?"**

> Both are caching hooks but they cache different things. `useMemo` caches the result of a function — a value. `useCallback` caches the function itself — a reference. The reason `useCallback` exists is that functions in JavaScript are recreated fresh on every render. If you pass a function as a prop to a child component, the child receives a new function reference on every parent render, and if the child is wrapped in `React.memo` to prevent unnecessary re-renders, that memo becomes ineffective because the prop technically changed — even though the function does the same thing. `useCallback` ensures the function reference stays stable between renders so memoised children are not unnecessarily re-rendered.

---

🎤 **"Is useMemo always beneficial? Should you use it everywhere?"**

> No, and this is an important nuance. `useMemo` itself has a cost — React has to store the cached value, compare dependencies on every render, and manage the cache. For simple computations, this overhead can actually be more expensive than just recomputing the value. `useMemo` is worth using when the computation is genuinely expensive and runs frequently. A good mental model is: profile first, optimise second. If you have not measured a performance problem, do not add `useMemo` speculatively. Premature memoisation adds complexity without clear benefit.

---

### Q: Have you worked with custom hooks?

**Yes. A custom hook is a regular JavaScript function whose name starts with "use" and that can call other hooks inside it — it is the pattern for extracting and reusing stateful logic across components.**

The problem custom hooks solve is code duplication for stateful behaviour. Suppose you need to track whether the window is currently online or offline in multiple components. Without custom hooks, you would duplicate the same `useState` and `useEffect` logic in every component that needs it. With a custom hook, you extract that logic into a single function and call it from any component. The component does not know or care about the implementation — it just gets the value it needs.

Custom hooks are powerful because they can call any other hooks, including other custom hooks, and they maintain their own separate state per component that uses them. Two components calling the same custom hook do not share state — each gets its own instance.

---

🎤 **"How is a custom hook different from a regular utility function?"**

> A regular utility function cannot call hooks. That is the defining constraint. If your shared logic needs to use `useState`, `useEffect`, or any other hook, it must be a custom hook — a function whose name starts with "use". React's linting rules enforce this. A custom hook also participates in React's lifecycle — its effects mount and unmount with the component that uses it. A regular utility function is just pure logic with no connection to React's state or lifecycle system.

---

<a name="context"></a>
## 4️⃣ Context API and State Management

---

### Q: What is the basic structure of Context API and how do you manage state inside it?

**Context API has three parts: creating the context with createContext, wrapping the component tree with a Provider to supply the data, and consuming the data with useContext in any descendant component.**

Context was created to solve prop drilling — the pattern where you have to pass data through many intermediate components just to get it to a deeply nested component that actually needs it. Instead of passing props down through every layer, you put the data in a context, wrap your tree with the Provider, and any component anywhere in that tree can read the data directly without any component in between needing to know about it.

The Provider is the broadcaster. It holds the data and makes it available to its entire subtree. You typically keep the actual state management — the `useState` or `useReducer` calls — inside the component that renders the Provider, and pass the state and the update functions through the context value. Any consumer lower in the tree gets both the current value and the ability to update it.

---

🎤 **"Are you using pure Context API or the useContext hook?"**

> `useContext` is how you consume a context inside a functional component — they go together. You create a context with `createContext`, provide it with a Provider, and then consume it with `useContext` in any functional component that needs the value. The `useContext` hook is the clean, modern way to read from context. Before hooks, you used the Context Consumer component with a render prop pattern, which was more verbose.

---

🎤 **"What happens if you do not wrap components with the Provider?"**

> If a component tries to read from a context but is not inside the corresponding Provider, it receives the default value you specified when you created the context with `createContext`. If you did not specify a default value, it receives `undefined`. This can lead to silent bugs where the component seems to work but is using undefined data. It is a common mistake when refactoring — you forget to wrap a part of your app with the Provider and wonder why the context value is not showing up.

---

<a name="redux"></a>
## 5️⃣ Redux

---

### Q: Do you understand the Redux flow?

**Redux follows a strict unidirectional data flow — state lives in a single global store, components dispatch actions describing what happened, reducers handle those actions and return new state, and connected components re-render with the updated state.**

The flow always goes one direction and never backwards. A user does something in the UI — clicks a button, submits a form. The component dispatches an action — a plain object that describes what happened, with a type field like "ADD_TO_CART" and any relevant data as the payload. This action is sent to the store, which passes it to the reducer. The reducer is a pure function — given the current state and the action, it returns the new state. The store saves this new state, and any component that is subscribed to the relevant part of the state is notified and re-renders.

The beauty of this system is predictability. Because state only changes through reducers, and reducers are pure functions, you can trace every state change back to a specific action. Redux DevTools lets you time-travel through every action that was dispatched, see exactly what state looked like before and after each one, and even replay sequences of actions.

---

🎤 **"What are the different functions or methods used in Redux?"**

> The core Redux concepts are the store, actions, action creators, and reducers. `createStore` or the modern `configureStore` from Redux Toolkit creates the store. `dispatch` is called on the store to send an action. `getState` reads the current state. `subscribe` listens for state changes. Action creators are functions that return action objects, which keeps action creation consistent. Reducers are the pure functions that specify how state transitions in response to actions. With Redux Toolkit, `createSlice` combines action creators and reducers into one definition, which significantly reduces boilerplate.

---

🎤 **"Do you know about reducers?"**

> A reducer is a pure function that takes two arguments — the current state and an action — and returns the next state. It must be pure: given the same state and the same action, it always returns the same result. It never modifies the existing state directly — it returns a new state object. It never has side effects — no API calls, no logging, no randomness inside the reducer. The name comes from the functional programming concept of a reduce operation — folding a list of actions over an initial state to arrive at the current state.

---

🎤 **"What is the difference between Redux and Context API?"**

> Context API is a built-in React mechanism for sharing data across a component tree without prop drilling. It is excellent for simple global data that does not update frequently — things like the current user, theme, or language preference. Redux is a full state management library with a strict, predictable update pattern, middleware support, and powerful DevTools. Redux is better suited for complex, frequently changing state across a large application — particularly when multiple parts of the app interact with the same state, when you need to trace and debug state changes, or when you need to handle complex async flows with middleware like Redux Thunk or Redux Saga. Context re-renders every subscriber whenever the value changes — Redux has more granular subscriptions and optimisations.

---

<a name="rendering"></a>
## 6️⃣ Rendering and Re-rendering

---

### Q: What is reconciliation?

**Reconciliation is React's process of comparing the new virtual DOM tree it just built against the previous one and figuring out the minimum set of actual DOM changes needed to bring them into sync.**

When state changes and React re-renders a component, it creates a new virtual DOM tree. It does not just throw away the old real DOM and rebuild everything — that would be extremely slow. Instead it runs a diffing algorithm that walks both trees in parallel and identifies what is different. Where nodes are the same type with the same props, nothing changes. Where props are different, React updates only those attributes. Where a node type has changed entirely, React removes the old DOM subtree and replaces it. Where list items change, React uses the `key` attribute to match old and new items and move or update only the necessary ones.

The end result is that user interaction and data updates feel instant because React applies surgical, minimal changes to the DOM rather than wholesale rebuilding it.

---

🎤 **"Will a child component re-render on every click of a button in the parent?"**

> By default, yes. When a parent component's state changes and it re-renders, all of its children re-render too — regardless of whether their props changed. React re-renders the entire subtree rooted at the component that had the state change. This is the default behaviour and is usually fine because React's virtual DOM diffing makes the actual DOM changes efficient. However, if a child is expensive to render, you can wrap it in `React.memo`, which makes React skip re-rendering that child unless its props actually changed. `React.memo` does a shallow comparison of props.

---

🎤 **"Why might a child still re-render even when wrapped in React.memo?"**

> Because of referential equality. `React.memo` does a shallow comparison of props. If a parent passes a function or an object as a prop, a new function or object is created on every render, and even though the values are the same, the reference is different — so the shallow comparison sees a change and re-renders the child. This is why `useCallback` exists for functions and `useMemo` exists for objects — to keep references stable between renders so that `React.memo` can do its job correctly.

---

<a name="performance"></a>
## 7️⃣ React Performance Optimization

---

### Q: If a React app takes 10 seconds for first paint with a 7-8 MB JS bundle, how would you optimise it?

**The first step is identifying what is taking time, and the most useful tool for that is Lighthouse in Chrome DevTools and the Network tab — then you address the bundle size through code splitting, lazy loading, and tree shaking.**

A 7-8 MB JavaScript bundle is very large. The browser has to download all of that, parse it, and execute it before anything can render. The whole bundle is not necessary for the first page the user sees — you are loading code for every page and feature simultaneously.

The diagnosis phase comes first. I would open the Network tab to see which JavaScript files are being loaded and their sizes. I would use the Coverage tab in Chrome DevTools to see how much of the loaded JavaScript is actually being used on the initial page — you often find that 60-70% of the code loaded is not needed right away. Webpack Bundle Analyzer or Vite's bundle visualiser gives a visual breakdown of what is inside the bundle and which packages are contributing the most.

The optimisation phase addresses what you found. Code splitting with dynamic imports breaks the bundle into smaller chunks that are loaded on demand rather than all at once. Lazy loading React components — using `React.lazy` — means component code is only fetched when that component is actually about to be rendered. Tree shaking eliminates dead code — making sure your build tool removes code that is imported but never used. Replacing large utility libraries with smaller alternatives — for example, using specific lodash functions rather than importing the entire library — can dramatically reduce size. Image optimisation, compression, and CDN delivery are also important. Server-side rendering or static generation with Next.js can provide meaningful content before any JavaScript loads.

---

🎤 **"How would you first identify what exactly is taking time to load?"**

> I would start with Lighthouse in Chrome DevTools — it gives a performance score and specific metrics like First Contentful Paint, Time to Interactive, and Total Blocking Time, along with actionable recommendations. The Network tab shows exactly what assets are being fetched, their sizes, and how long each takes. The Performance tab lets you record a session and see a flame chart of what JavaScript is executing and when. The Coverage tool shows dead code. Webpack Bundle Analyzer gives the visual breakdown of what is in the bundle. Together, these tools tell you whether the problem is download time (bundle size), parse time (too much JavaScript), render time (slow component tree), or network time (slow API calls).

---

🎤 **"What is lazy loading in React?"**

> Lazy loading in React means deferring the loading of a component's code until it is actually needed — typically until the user navigates to a page that uses that component. React provides `React.lazy` for this. You wrap the dynamic import in `React.lazy`, and React handles fetching the component's code only when it is first about to be rendered. This works together with `Suspense`, which lets you show a fallback — a loading spinner, a skeleton screen — while the component's code is being fetched. The result is a much smaller initial bundle because you are not loading everything upfront.

---

🎤 **"What is Suspense?"**

> Suspense is a React mechanism for handling asynchronous operations in the component tree in a declarative way. You wrap a part of your component tree in a `Suspense` boundary, provide a `fallback` prop with what to show while waiting, and React automatically shows that fallback whenever any component inside the boundary is waiting for something — whether that is lazy-loaded code or asynchronous data in newer React versions. It decouples the loading state logic from the component that is loading, making the code cleaner and giving you centralised control over loading experiences.

---

### Q: How do you optimise a React project generally?

**React optimisation falls into four areas: reducing unnecessary re-renders, minimising the JavaScript bundle, deferring work that is not immediately needed, and optimising how data is fetched and cached.**

Reducing unnecessary re-renders involves `React.memo` for components, `useCallback` for function props, `useMemo` for expensive computed values, and lifting state only as high as it needs to go — state that lives very high causes re-renders very deep.

Minimising bundle size involves code splitting, lazy loading routes and heavy components, tree shaking, analysing and replacing large dependencies, and enabling compression on the server.

Deferring non-critical work involves lazy loading images, using intersection observers for below-the-fold content, and deferring analytics or non-critical scripts.

Data optimisation involves avoiding over-fetching, caching API responses, using pagination or infinite scroll instead of loading everything at once, and potentially using a data-fetching library like React Query that handles caching, deduplication, and background updates intelligently.

---

🎤 **"What debugging points would you check first?"**

> My first checks would be: is the bundle size within reason, is there unnecessary re-rendering visible in React DevTools Profiler, are there network requests that are slow or redundant, are images unoptimised, and is there any synchronous JavaScript execution blocking the main thread. The React DevTools Profiler is particularly useful because it shows you exactly which components re-rendered on each interaction, how long each render took, and why it re-rendered. This tells you precisely where to apply memoisation.

---

### Q: What is prop drilling and should we avoid it?

**Prop drilling is the pattern of passing data through multiple layers of components that do not need the data themselves, purely to get it to a deeply nested component that does — and yes, it should generally be avoided for global or widely shared data.**

Imagine an application with five levels of components. The top-level component has the user's name. A component five levels deep needs to display it. With prop drilling, every component in between has to accept and pass the `userName` prop, even though they have no interest in it. This creates unnecessary coupling — every intermediate component now depends on this prop existing, which makes refactoring brittle and components harder to reuse.

The solution depends on the scope of the data. For truly global data — current user, theme, language — Context API is appropriate. For complex shared state with frequent updates and many interactions — use Redux or another state management library. For data specific to a feature subtree — consider whether state can be lifted to the nearest common ancestor, or use a more targeted context scoped to that feature.

---

🎤 **"Is prop drilling always bad?"**

> No. For shallow hierarchies — one or two levels — prop drilling is perfectly fine and often preferable to introducing context or global state, which adds complexity. Context and Redux have their own overhead. The rule is to start simple with props, and only reach for context or state management when prop drilling becomes genuinely painful — when you are passing props through more than three or four levels or when many unrelated components need the same data.

---

<a name="auth"></a>
## 8️⃣ Authentication, Storage, and Roles

---

### Q: After login, where would you store a token and user details so they survive a page refresh?

**I would store the token in an httpOnly cookie for security, and store non-sensitive user details like name, role, and display preferences in localStorage or sessionStorage depending on how long the session should last.**

The reason httpOnly cookies are preferred for tokens is security. A cookie marked as httpOnly cannot be accessed by JavaScript at all — it is automatically sent with every HTTP request but is invisible to your JavaScript code. This protects against XSS attacks where malicious scripts injected into your page try to steal the token from JavaScript-accessible storage. `localStorage` and `sessionStorage`, while convenient, can be read by any JavaScript running on the page.

`localStorage` persists indefinitely until explicitly cleared — the data survives closing the browser tab, closing the browser, and restarting the computer. Use it for preferences or data that should genuinely persist long-term.

`sessionStorage` lives only for the duration of the browser tab session — it is cleared when the tab is closed. Use it for session-specific data that should not persist after the user closes their session.

For sensitive information like the authentication token itself, httpOnly cookies are the gold standard. For user profile data that is needed in the UI — the user's name to display in the header, their role to control what UI they see — `localStorage` is commonly used with the understanding that this is display data, not security-critical data.

---

🎤 **"What is the difference between authentication and authorisation?"**

> Authentication is the process of verifying who you are — proving your identity. Logging in with a username and password, or using SSO, is authentication. The question being answered is "are you who you claim to be?" Authorisation is what happens after authentication — it determines what you are allowed to do. The question being answered is "now that I know who you are, what are you permitted to access?" A user might be successfully authenticated — the system knows they are Alice — but not authorised to access the admin panel because Alice's role does not grant that permission. Authentication is always a prerequisite for authorisation.

---

🎤 **"If you need to store confidential information but don't want other users to access it, how would you manage that?"**

> Confidential data should never be stored in the browser at all if it is truly sensitive. The browser environment is not a secure vault — `localStorage`, `sessionStorage`, and cookies are all accessible in some form to anyone with physical access to the device. Truly confidential data should remain on the server and only be fetched by an authenticated and authorised request at the moment it is needed. On the frontend, you store only what is necessary for the UI to function — identifiers, display names, role information — not the sensitive data itself.

---

<a name="controlled"></a>
## 9️⃣ Controlled vs Uncontrolled Components

---

### Q: Have you heard about controlled and uncontrolled components?

**Yes — a controlled component is one where React manages the form element's value through state. An uncontrolled component is one where the DOM itself manages the value and React reads it on demand through a ref.**

In a controlled component, the input's value is always driven by state. When the user types, an event handler updates the state, and React re-renders the input with the new value. React is the single source of truth. This gives you complete control — you can validate on every keystroke, format input as the user types, and always know the current value from state.

In an uncontrolled component, the input manages its own internal value just like in plain HTML. You use a `ref` to read the value when you need it — typically on form submission. React is not involved in every keystroke. This is simpler for basic forms but gives you less control over the value moment to moment.

---

🎤 **"When would you choose an uncontrolled component?"**

> For simple, non-interactive forms where you only need the value at submission time and do not need to validate or manipulate input as the user types, uncontrolled components are simpler and involve less code. They are also useful for file inputs, which cannot be controlled in React — file input values can only be read, not set programmatically. For complex forms with validation, dynamic fields, or inter-field dependencies, controlled components are the right choice because you have full access to the current values at all times.

---

<a name="hoc"></a>
## 🔟 Higher-Order Components (HOC)

---

### Q: Have you used HOC in React? Can you explain it?

**A higher-order component is a function that takes a component and returns a new, enhanced component — it is a pattern for reusing component logic without modifying the original component.**

The name comes from functional programming's concept of higher-order functions — functions that take or return other functions. A HOC takes a component as input and returns a new component that wraps the original, adding some extra behaviour or injecting additional props.

The classic real-world use cases are adding authentication protection to a route — where the HOC checks if the user is logged in and either renders the component or redirects to login — adding error boundaries around components, injecting analytics tracking, or providing theme props. The component being wrapped does not need to know it is inside a HOC — it just receives the props it needs.

---

🎤 **"Can you give a real-world example of where you would use a HOC?"**

> A very common real-world use case is route protection. You have a HOC called `withAuth` that wraps any page component. Inside the HOC, before rendering the wrapped component, it checks whether the user is authenticated. If they are, it renders the original component and passes through all the props. If they are not, it redirects to the login page. You apply this HOC to every protected route in your application. The page components themselves have no authentication logic — that concern is entirely handled by the HOC. This is separation of concerns — keeping authentication logic in one place rather than duplicating it in every protected page.

---

🎤 **"How do HOCs compare to hooks for code reuse?"**

> HOCs were the primary code-reuse pattern before hooks. They work but have drawbacks — they add layers of wrapping to your component tree which can make it harder to read in DevTools, and they can create "wrapper hell" when you stack multiple HOCs. They can also cause prop name collisions. Hooks solve the same code-reuse problem more cleanly because they extract logic into a function without adding any wrapper component to the tree. For most new code, I would reach for a custom hook rather than a HOC. HOCs still make sense for certain patterns — particularly when you need to wrap a component declaratively in JSX, or when working with class components that cannot use hooks.

---

<a name="propdrilling"></a>
## 1️⃣1️⃣ Prop Drilling

---

### Q: What is prop drilling and is it a good practice?

**Prop drilling is passing data through multiple intermediate components that do not use it themselves, just to get it to a deeply nested child that does — and while not inherently wrong, it becomes a problem at scale.**

The issue is coupling. Every component in the middle of the chain now depends on a prop it does not care about, purely for the sake of passing it along. This makes those components harder to reuse — you cannot drop a middle component somewhere else without also providing the prop it is just passing through. It makes refactoring more fragile — if you rename the prop, you have to update every component in the chain. And it makes the code harder to reason about because the data flow is obscured.

The remedy depends on the scale. For one or two levels, prop drilling is fine — use it. For three or more levels, consider lifting state to the nearest common ancestor and then using Context to make it available without threading it through every layer. For application-wide state used in many places, a state management library like Redux may be appropriate.

---

<a name="fragments"></a>
## 1️⃣2️⃣ React Fragments

---

### Q: What is the use of React Fragment, and why use it instead of a div?

**A Fragment is a way to group multiple elements without adding an extra DOM node — it lets a component return multiple children without wrapping them in a real HTML element.**

React requires components to return a single root element. Without fragments, developers would wrap everything in an extra `div`. The problem is that this extra `div` pollutes the DOM structure — it adds nodes that serve no semantic or styling purpose. This can break CSS layouts like flexbox or grid where the relationship between parent and child elements matters. It can also interfere with tables, lists, and other HTML structures that have strict rules about which elements can be children.

A Fragment returns multiple children as a group without producing any real DOM node. The rendered HTML contains only the children — no wrapper element appears in the browser's DOM. This keeps your markup clean, preserves the intended HTML structure, and avoids accidental layout breakage from unnecessary wrapper elements.

---

🎤 **"Are you aware of the shorthand syntax for Fragment?"**

> Yes — empty angle brackets are the shorthand for a Fragment. Instead of writing out the full `React.Fragment` component, you can just use empty opening and closing brackets as the wrapper. The only difference between the shorthand and the full syntax is that the full syntax can accept a `key` attribute, which is needed when rendering a list of Fragments. The shorthand cannot take any attributes.

---

<a name="data"></a>
## 1️⃣3️⃣ Data Passing and State Sharing

---

### Q: Given Company → Department → Employee → Employee Details hierarchy, how would you pass data from Company down to Employee Details?

**For data needed only at one or two levels down, I would use props directly. For data needed deep in the tree by many components, I would use Context API to make the data available throughout the subtree without threading it through every layer.**

The key decision is whether the intermediate components — Department and Employee — actually need the data. If they do, props are completely appropriate. If they are purely acting as passthrough channels for data they do not need themselves, Context eliminates the unnecessary coupling.

In practice, I would look at what the data represents. If it is company-wide information like the company name, the current user's role, or organisation-wide settings — that is a perfect use case for Context. You create a CompanyContext, wrap the tree from the Company component downward with its Provider, and Employee Details reads directly from the context with `useContext` without involving Department or Employee at all.

---

🎤 **"How would you update data from child to parent?"**

> By passing a callback function from the parent down to the child as a prop. The parent defines a function that updates its own state, and passes that function to the child. The child calls the function with the new data as an argument whenever something happens — a button click, a form submission. React's data flow is always top-down — data flows down through props, events flow up through callbacks. This is the only correct way for a child to communicate with a parent. The parent retains ownership of the state; the child is just requesting a change.

---

🎤 **"If every page header needs to show the same user name and department, how would you handle that?"**

> I would store the user's name and department in a global context or state management solution — whichever is already in use in the project. After login, I would populate that context with the user details from the API response. Every header component reads from that context. Because the context is available throughout the application, every page's header automatically shows the correct data without any prop passing between pages. If I also need it to survive refresh, I would persist it in `localStorage` and restore it into context when the app loads.

---

<a name="infinitescroll"></a>
## 1️⃣4️⃣ Infinite Scroll

---

### Q: How would you implement infinite loading on a product listing page?

**I would use an IntersectionObserver to detect when the user has scrolled to the bottom of the list, trigger an API call to load the next page of products, append them to the existing list, and prevent duplicate calls while a request is already in progress.**

The IntersectionObserver API watches a target element and fires a callback when that element enters or exits the viewport. I would place a sentinel element — an invisible div — at the very bottom of the product list. The IntersectionObserver watches this sentinel. When it becomes visible, it means the user has scrolled to the bottom and it is time to load more data.

The logic flow is: user scrolls → sentinel becomes visible → observer callback fires → check if a request is already loading → if not, set a loading flag and call the API → append new products to the existing array → clear the loading flag when done. The loading flag is the critical guard against multiple simultaneous requests.

---

🎤 **"How would you prevent multiple API calls while the user keeps scrolling?"**

> With a boolean flag — commonly called `isLoading` or `isFetching`. Before making an API call, you check this flag. If it is already true, you return early without making another request. After the response comes back, you reset the flag. This ensures that no matter how many times the scroll event or intersection observer fires while a request is in progress, only one request is alive at a time.

---

🎤 **"Can you use debounce or throttle for this?"**

> You could, and they both reduce the frequency of function calls, but they work differently. Debounce delays execution until the user has stopped scrolling for a specified time — useful for search inputs where you want to wait until the user finishes typing. Throttle limits a function to run at most once per specified time interval — regardless of how many times it is triggered. For infinite scroll, the IntersectionObserver approach is generally cleaner and more semantically correct than debouncing scroll events, because it fires only once when the target actually enters the viewport rather than continuously as the user scrolls. If using scroll event listeners instead of IntersectionObserver, throttle is the more appropriate choice over debounce — you want periodic checks, not a delay until scrolling stops.

---

<a name="css"></a>
## 1️⃣5️⃣ CSS and Styling

---

### Q: What is the flex model?

**Flexbox is a CSS layout model designed for one-dimensional layouts — arranging items in a row or a column with flexible sizing, alignment, and distribution of space between them.**

The flex model works through a parent-child relationship. The parent becomes the flex container by setting `display: flex`. This gives you control over how its direct children — the flex items — are laid out. The main axis is the direction items flow (row by default). The cross axis is perpendicular to it.

The power of flexbox is in the alignment and distribution properties. `justify-content` controls how items are distributed along the main axis. `align-items` controls how items are aligned along the cross axis. `flex-grow`, `flex-shrink`, and `flex-basis` control how individual items size themselves relative to available space. This replaces older techniques like floats and inline-block for the vast majority of UI layout scenarios.

---

🎤 **"What is the difference between relative and absolute positioning?"**

> Relative positioning moves an element from where it would naturally appear in the document flow, using top, right, bottom, left — but it still occupies its original space. The document layout is not affected by the visual shift. Absolute positioning removes an element completely from the document flow — it no longer occupies space — and positions it relative to the nearest ancestor that has any positioning other than static. If no such ancestor exists, it positions relative to the initial containing block, usually the viewport. Relative and absolute positioning are often used together: set a parent to `position: relative` to create an anchor, then position children absolutely within it.

---

### Q: What is MUI?

**MUI — Material UI — is a React component library that implements Google's Material Design system, providing pre-built, themeable, accessible components so you can build consistent UIs without designing from scratch.**

MUI gives you a comprehensive set of ready-to-use components — buttons, forms, modals, tables, navigation — all styled to Material Design specifications with built-in accessibility. Beyond the visual components, MUI provides a powerful theming system where you define your brand colours, typography, and spacing in one place and every component inherits those values. This ensures visual consistency across the entire application. The trade-off is bundle size — MUI is a large library, so tree shaking and proper imports are important for performance.

---

### Q: What are the different ways to style a React component?

**There are several approaches: plain CSS files, CSS modules, styled-components or Emotion for CSS-in-JS, utility-first frameworks like Tailwind CSS, and component libraries like MUI.**

Plain CSS files work and are familiar but can lead to class name collisions in large applications. CSS Modules scope class names to the component automatically, preventing global leakage. CSS-in-JS libraries like styled-components or Emotion let you write CSS inside JavaScript with dynamic styling based on props — components are self-contained with their styles colocated. Tailwind provides utility classes you compose directly in JSX, which trades semantic class names for faster styling without leaving the markup. Each approach has trade-offs between developer experience, performance, and maintainability, and the right choice depends on the project and team preferences.

---

<a name="typescript"></a>
## 1️⃣6️⃣ TypeScript

---

### Q: What is the difference between type and interface in TypeScript?

**Both `type` and `interface` are used to describe the shape of objects in TypeScript, but interfaces are extendable and mergeable while types are more flexible and support a broader range of use cases including union types and computed types.**

`interface` is designed specifically for describing the shape of objects and classes. It supports declaration merging — you can declare the same interface in multiple places and TypeScript merges them into one, which is useful for extending third-party library types. Interfaces are also the preferred choice for class contracts because they align with how object-oriented programming typically describes behaviour.

`type` is more flexible — it can describe objects, but also unions of types, intersections, tuples, and more complex type expressions. You cannot declaration-merge a `type`. For describing the shape of a plain object, both work and the difference is mostly stylistic. The general community convention is to use `interface` for objects and class contracts, and `type` for everything else — unions, function types, utility types, and complex type manipulations.

---

🎤 **"Do you know generics in TypeScript?"**

> Generics allow you to write flexible, reusable code that works with multiple types without losing type safety. Instead of specifying a concrete type, you use a type parameter — a placeholder that is filled in when the generic is used. The canonical example is a function that returns what it receives — without generics, you would have to choose between making it accept `any`, which loses type information, or writing separate versions for every type. With generics, you write it once with a type parameter, and TypeScript infers or you explicitly specify the type at each usage. Generics are also essential for typed collections, API response wrappers, and utility types.

---

<a name="testing"></a>
## 1️⃣7️⃣ Testing

---

### Q: When should one use Mocha vs Chai, and what different use cases do they provide?

**Mocha is a test runner — it provides the structure for organising and running tests. Chai is an assertion library — it provides the vocabulary for expressing what you expect to be true. They are complementary and are commonly used together.**

Mocha handles the mechanics of testing: defining test suites with `describe`, individual test cases with `it`, hooks like `before`, `after`, `beforeEach`, and `afterEach` for setup and teardown, and running those tests with reporting. It does not care what your assertions look like or what library you use for them.

Chai provides the assertions themselves — the actual checks. It offers three styles. The `assert` style is similar to Node's built-in assert module — `assert.equal(a, b)`. The `expect` style is chainable and reads like natural language — `expect(a).to.equal(b)`. The `should` style extends objects — `a.should.equal(b)`. Many teams prefer the `expect` style for its readability.

The reason they are separate is philosophical — a test runner and an assertion library are different concerns, and keeping them separate gives you flexibility to swap one without changing the other.

---

🎤 **"Do you have experience with Jest?"**

> Jest is a testing framework from Meta that combines a test runner, assertion library, and mocking capabilities in one package. It is the most common choice for React testing because it comes pre-configured with Create React App and works seamlessly with React Testing Library. Unlike using Mocha and Chai separately, Jest provides everything out of the box with zero configuration for most projects. It has a very fast watch mode, excellent snapshot testing for React components, and built-in code coverage reporting. For React projects specifically, Jest plus React Testing Library is the standard stack.

---

<a name="nextjs"></a>
## 1️⃣8️⃣ Next.js and Build Tooling

---

### Q: Was your frontend stack React with Next.js?

**Yes. Next.js adds a production-grade layer on top of React, providing server-side rendering, static site generation, file-based routing, API routes, and optimised performance out of the box.**

Plain React is purely client-side by default — the browser downloads a JavaScript bundle and builds the UI entirely on the client. Next.js changes this by allowing pages to be pre-rendered — either at build time as static HTML, or on the server at request time. This dramatically improves first-paint performance and search engine optimisation because the browser receives actual HTML content immediately, before any JavaScript executes.

File-based routing in Next.js means you create files in the pages directory and they automatically become routes — no routing configuration needed. API routes allow you to write backend endpoints in the same codebase. Image optimisation, font optimisation, and automatic code splitting are all handled automatically.

---

🎤 **"Which build tool were you using on the frontend?"**

> The build tool in Next.js is Webpack under the hood, though Next.js 12 and onwards introduced Rust-based SWC as the compiler, replacing Babel, for significantly faster build and refresh times. For standalone React projects, Vite has largely displaced Create React App as the preferred development tool because it starts up almost instantly using native ES modules, and hot module replacement is much faster than Webpack during development. Vite uses Rollup for production builds, which produces well-optimised output.

---

<a name="cheatsheet"></a>
## 🧠 Quick Recall — Opening Lines for Every Topic

> Say this first. Pause. Expand with detail. These first sentences signal to the interviewer that you understand the concept before going deeper.

---

| Topic | Your Opening Line |
|-------|------------------|
| **What is React** | "React is a JavaScript library for building component-based UIs where the view automatically updates when data changes." |
| **JSX** | "JSX is a syntax extension that lets you write HTML-like markup inside JavaScript — it compiles to plain React.createElement calls." |
| **Virtual DOM** | "The virtual DOM is React's in-memory representation of the UI — it compares old and new descriptions to find the minimum real DOM changes needed." |
| **Reconciliation** | "Reconciliation is React's diffing algorithm — comparing the new virtual DOM tree to the old one and applying only the necessary real DOM changes." |
| **State vs Props** | "State is data the component owns and can change. Props are data passed in from outside — read-only from the component's perspective." |
| **Component** | "A component is a self-contained piece of UI — a function that takes props and returns a description of what should appear on screen." |
| **Class vs Functional** | "Functional components with hooks are the modern standard. Class components use lifecycle methods and this.state — I can work with both." |
| **Hooks** | "Hooks are functions that let functional components use React features like state and lifecycle events without needing class syntax." |
| **useEffect cleanup** | "The cleanup for a setInterval goes in the function you return from useEffect — React calls it before unmounting and before re-running the effect." |
| **useMemo** | "useMemo caches the result of an expensive computation and only recomputes it when its specified dependencies change." |
| **useCallback** | "useCallback caches a function reference so it stays stable between renders — important for preventing unnecessary re-renders of memoised children." |
| **Custom hooks** | "A custom hook is a function starting with 'use' that calls other hooks — it extracts reusable stateful logic without adding wrapper components." |
| **Context API** | "Context has three parts: createContext to create it, a Provider to supply the data, and useContext to consume it anywhere in the subtree." |
| **Provider** | "The Provider is the broadcaster — it wraps the component tree and makes the context value available to every descendant that wants it." |
| **Without Provider** | "Without a Provider, consumers receive the default value from createContext — usually undefined, which causes silent bugs." |
| **Redux flow** | "Redux is unidirectional — component dispatches an action, the store passes it to a reducer, the reducer returns new state, subscribers re-render." |
| **Reducer** | "A reducer is a pure function — takes current state and an action, returns new state — no mutations, no side effects." |
| **Redux vs Context** | "Context is for simple, infrequently updated global data. Redux is for complex, frequently changing state with tracing, middleware, and DevTools." |
| **Re-rendering** | "By default, all child components re-render when a parent re-renders — React.memo prevents this if props have not changed." |
| **React.memo** | "React.memo does a shallow prop comparison — if a parent passes new function or object references on every render, memo breaks without useCallback or useMemo." |
| **Performance — bundle** | "A large bundle means slow parse time — fix with code splitting, lazy loading, tree shaking, and replacing large dependencies." |
| **Lazy loading** | "React.lazy defers loading a component's code until it is about to render — combined with Suspense, it shows a fallback while loading." |
| **Suspense** | "Suspense wraps a tree and shows a fallback automatically whenever any component inside it is waiting for async work — lazy loading or async data." |
| **Token storage** | "Tokens belong in httpOnly cookies for security. Non-sensitive user details for the UI go in localStorage to survive refresh." |
| **Auth vs Authz** | "Authentication is proving who you are. Authorisation is determining what you are allowed to do — auth always comes first." |
| **Controlled component** | "A controlled component has its value driven by React state — React is the single source of truth for the input's value." |
| **Uncontrolled component** | "An uncontrolled component lets the DOM manage its own value — you read it via a ref when needed, typically on submit." |
| **HOC** | "A higher-order component is a function that takes a component and returns a new enhanced component — for reusing logic without modifying the original." |
| **Prop drilling** | "Prop drilling passes data through intermediate components that do not need it — fine for shallow hierarchies, problematic at depth." |
| **Fragment** | "A Fragment groups multiple elements without adding a real DOM node — avoids unnecessary divs that break layouts or pollute markup." |
| **Infinite scroll** | "Use IntersectionObserver on a sentinel element at the bottom — when it enters the viewport, load the next page and guard with an isLoading flag." |
| **Debounce vs Throttle** | "Debounce delays until activity stops. Throttle limits to once per interval. For infinite scroll, throttle is better — you want periodic checks, not a delay." |
| **Flexbox** | "Flexbox is a one-dimensional layout model — the parent becomes a flex container and controls how its children are sized, ordered, and aligned." |
| **type vs interface** | "Both describe object shapes. Interface supports declaration merging and class contracts. Type is more flexible — supports unions, intersections, and complex expressions." |
| **Generics** | "Generics are type placeholders — they let you write code that works with multiple types while keeping full type safety at each usage." |
| **Mocha vs Chai** | "Mocha is the test runner — it structures and runs tests. Chai is the assertion library — it expresses what you expect to be true. They complement each other." |
| **Jest** | "Jest is an all-in-one testing framework — test runner, assertions, and mocking in one package. It is the standard for React testing." |
| **useReducer** | "useReducer is like Redux in a single component — you define a reducer function and dispatch actions to it, useful for complex interrelated state." |
| **useMemo for search** | "useMemo is effective for frontend search — the filtering runs only when the data or search term changes, not on every unrelated re-render." |
| **Backend search useMemo** | "For backend search, useMemo is less useful — the data itself changes with every request, so there is nothing stable to cache on the frontend." |
| **What is state** | "State is the dynamic data in your application — anything that changes over time and needs to be reflected in the UI." |