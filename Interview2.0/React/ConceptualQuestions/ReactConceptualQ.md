# 🚀 Senior React Interview Guide
> Precise answers for scenario-based questions. No fluff. Read once, remember forever.

---

## Table of Contents
1. [API is Slow](#1-api-is-slow)
2. [Page is Getting Slow](#2-page-is-getting-slow)
3. [Page is Not Responsive](#3-page-is-not-responsive)
4. [User Hitting a Button Too Many Times](#4-user-hitting-a-button-too-many-times)
5. [API is Flaky — Sometimes Works, Sometimes Doesnt](#5-api-is-flaky--sometimes-works-sometimes-doesnt)
6. [1000 Chats in a Chat App — Its Lagging](#6-1000-chats-in-a-chat-app--its-lagging)
7. [Best React App Architecture](#7-best-react-app-architecture)
8. [How to Prevent Extra Re-renders](#8-how-to-prevent-extra-re-renders)
9. [Page is Re-rendering Too Many Times](#9-page-is-re-rendering-too-many-times)
10. [When to Use Redux vs React Query](#10-when-to-use-redux-vs-react-query)
11. [Design a React App for Millions of Users](#11-design-a-react-app-for-millions-of-users)
12. [Handling Concurrent Users](#12-handling-concurrent-users)
13. [Lazy Loading, Code Splitting and Suspense](#13-lazy-loading-code-splitting-and-suspense)
14. [User Clicks Edit — Idempotency Problem](#14-user-clicks-edit--idempotency-problem)
15. [Library Cheat Sheet](#15-library-cheat-sheet)

---

## 1. API is Slow

> **Interviewer wants to hear:** You think about user experience during the wait AND reducing unnecessary calls.

### What You Should Do

**Hide the wait from the user:**
- Show **skeleton / shimmer UI** — user feels progress, not a blank screen
- Use **optimistic updates** — update UI instantly, rollback if API fails
- Show **cached old data** while fresh data loads in background *(stale-while-revalidate)*
- **Prefetch data** on hover before user even clicks a link

**Reduce unnecessary API calls:**
- **Debounce** search inputs — wait until user stops typing, then call
- **Cancel stale requests** with `AbortController` — old slow responses never overwrite new ones
- **Paginate** — never fetch 1000 items if user only sees 20

**Without libraries:**
- Cache responses in a plain JS `Map` — check map first, fetch only if missing
- Write a `useDebounce` hook using `setTimeout` + `clearTimeout` in `useEffect`
- Native `AbortController` + `fetch` — no axios needed

### Key Concepts
| Term | One-line meaning |
|---|---|
| Skeleton UI | Placeholder shaped like the real content |
| Optimistic Update | Update UI first, rollback on failure |
| Stale-While-Revalidate | Show old data, silently fetch new in background |
| AbortController | Native API to cancel a pending fetch |
| Debounce | Fire only after user stops for X ms |

---

## 2. Page is Getting Slow

> **Interviewer wants to hear:** Measure first, then fix — not randomly add React.memo everywhere.

### Step 1 — Find the Problem First
- **Chrome DevTools → Performance tab** — record and see what takes long
- **React DevTools Profiler** — which components render and how long
- **Lighthouse** — overall score, flags big issues
- `console.time()` around suspect code for rough timing

### Step 2 — Fix Based on What You Find

| Problem | Fix |
|---|---|
| Bundle too large | Code split with `React.lazy` + `Suspense` |
| Too many DOM nodes | Virtualize long lists |
| Components re-rendering too often | `React.memo`, `useMemo`, `useCallback` |
| Fetching too much data | Paginate, cursor-based loading |
| Heavy images | Use WebP/AVIF format, add `loading="lazy"` |
| Scripts blocking page render | Add `defer` or `async` on script tags |

### Step 3 — Monitor in Production
- Track **LCP, FID, CLS** with `web-vitals` library
- **Sentry** for error tracking, **Datadog** for performance metrics

### Key Concepts
| Term | One-line meaning |
|---|---|
| LCP | How long before main content appears |
| FID | How long before first click is responded to |
| CLS | Does page jump around during load |
| Code Splitting | Only ship JS needed for current page |
| Tree Shaking | Remove unused code from final bundle automatically |

---

## 3. Page is Not Responsive

> **Interviewer wants to hear:** You know about the JS main thread being blocked and React's concurrent features.

### Root Cause
JavaScript runs on a **single main thread**. If it's busy with a heavy render or big computation, the browser cannot respond to clicks or keystrokes — page feels frozen.

### Fixes

**Using React 18 built-in features:**
- **`useTransition`** — mark heavy updates as non-urgent; user interactions always interrupt them
- **`useDeferredValue`** — defer updating an expensive list until urgent work like typing is done first

**Without React 18 / without libraries:**
- Process data in **chunks using `setTimeout(fn, 0)`** — do a chunk, yield to browser, continue
- Move heavy computation to a **Web Worker** — separate thread entirely, UI thread stays free

### Key Concepts
| Term | One-line meaning |
|---|---|
| Main thread | The one JS thread — block it and the page freezes |
| `useTransition` | Marks update as non-urgent; React pauses it for user input |
| `useDeferredValue` | Defers an expensive value until higher-priority work is done |
| Web Worker | Background thread for heavy JS — never blocks UI |
| `setTimeout(fn, 0)` | Old-school way to yield control between chunks of work |

---

## 4. User Hitting a Button Too Many Times

> **Interviewer wants to hear:** Race conditions, deduplication, backend safety — not just "disable the button."

### Multi-Layer Solution

**Layer 1 — Disable the button immediately**
- Set `isLoading = true` on first click, disable button until response comes back
- Re-enable in `finally` block — works for both success and error

**Layer 2 — Guard with a ref**
- Use `useRef` as an "is request in flight?" flag
- Doesn't cause re-renders unlike state — perfect for a silent guard
- Return early if ref is already `true`

**Layer 3 — Debounce or throttle the handler**
- **Debounce** — fires after user stops clicking (good for search)
- **Throttle** — fires at most once per interval no matter how many clicks
- Both can be written manually with `setTimeout` + `clearTimeout` — no lodash needed

**Layer 4 — Tell the backend (idempotency)**
- Send a **UUID** per request as an `Idempotency-Key` header
- Backend recognises duplicate requests and returns the same result without re-processing

### Key Concepts
| Term | One-line meaning |
|---|---|
| Debounce | Fire after user *stops* — best for inputs |
| Throttle | Fire at most once per interval — best for buttons/scroll |
| Race condition | Multiple async calls completing in unpredictable order |
| Idempotency | Same request sent twice = same effect as one |
| `useRef` guard | Mutable flag that does not trigger re-renders |

---

## 5. API is Flaky — Sometimes Works, Sometimes Doesnt

> **Interviewer wants to hear:** Retry logic, timeouts, fallbacks, circuit breaker, and clear UX communication.

### Strategy — Layer by Layer

**Retry with Exponential Backoff**
- Try up to 3 times — wait 1s → 2s → 4s between each attempt
- Increasing delays prevent hammering an already-struggling server
- Writeable manually in a loop with `setTimeout` — no library needed

**Timeout**
- Set a maximum wait time using `AbortController` + `setTimeout`
- If no response in 5s → abort and show an error — never leave user with an infinite spinner

**Serve stale cache while retrying**
- Return last successful response from cache while new fetch is retrying in background

**Circuit Breaker pattern**
- After 3 consecutive failures → stop making requests for 30 seconds
- Show "Service temporarily unavailable" — better UX than an endless spinner
- Reset automatically after cooldown

**Always show clear UI state**
- Never leave a blank screen or frozen spinner
- Show: retry progress → number of attempts → manual "Try Again" button

### Key Concepts
| Term | One-line meaning |
|---|---|
| Exponential Backoff | Retry delays double each attempt — 1s, 2s, 4s |
| Circuit Breaker | Stop calling a failing service; let it recover first |
| Stale Cache Fallback | Serve old data while retrying for fresh |
| `Promise.race` | Whichever promise resolves first wins — useful for timeouts |

---

## 6. 1000 Chats in a Chat App — Its Lagging

> **Interviewer wants to hear:** Virtualization first, normalized state, then real-time batching.

### Root Cause
Rendering 1000 DOM nodes when only 15–20 are visible — browser wastes time on elements the user cannot even see.

### Fix in Priority Order

**1. Virtualize the list** *(most important)*
- Only render items visible in the viewport
- DOM node count stays constant (~20 nodes) regardless of 100 or 100,000 messages
- With library: `react-window` `FixedSizeList`
- Without library: calculate `scrollTop`, slice only visible items, use a ghost div for correct scrollbar height

**2. Normalize state**
- Store messages as `{ byId: {id: message}, allIds: [ids] }` — not a flat array
- Updates to one message are O(1) and do not cause other messages to re-render

**3. Memoize each message component**
- Wrap `ChatMessage` in `React.memo` — only re-renders when its own props change

**4. Batch incoming real-time events**
- Do not call `setState` on every single WebSocket message
- Buffer messages and flush to state every 100ms

**5. Paginate — do not load all at once**
- Load last 50 messages on open, load more as user scrolls up
- Use `IntersectionObserver` on a sentinel element — no library needed

### Key Concepts
| Term | One-line meaning |
|---|---|
| Virtualization | Only render visible items — rest are virtual |
| Normalized State | Map-based structure — O(1) lookups and updates |
| `React.memo` | Skip re-render if props did not change |
| `IntersectionObserver` | Native API to detect when element enters viewport |
| Batching | Merge multiple state updates into one render |

---

## 7. Best React App Architecture

> **Interviewer wants to hear:** Feature-based structure, separation of concerns, lazy-loaded routes, clear data flow.

### Folder Structure — Feature-based, Not Type-based

```
src/
├── features/
│   ├── auth/
│   │   ├── components/   ← UI only, no logic
│   │   ├── hooks/        ← all business logic
│   │   └── api.ts        ← all fetch calls
│   └── chat/
│       ├── components/
│       ├── hooks/
│       └── api.ts
├── shared/
│   ├── components/       ← Button, Modal, Input
│   ├── hooks/            ← useDebounce, useLocalStorage
│   └── utils/            ← pure helper functions
└── app/
    ├── router.tsx         ← routes with lazy loading
    └── App.tsx
```

> Do NOT group by type at root level (`/components`, `/hooks`, `/pages`) — breaks down as app grows

### Architecture Layers
- **UI Components** — only render, no API calls, no business logic
- **Custom Hooks** — all logic lives here, extracted and reusable
- **API Layer** — all fetch calls in one place, never inside components directly
- **State Management** — global only for truly global things; local state everywhere else

### Key Principles
- **Colocation** — component, its styles, and its tests live together
- **Single Responsibility** — one component or hook does one thing
- **Lazy load every route** — each page is a separate JS chunk, downloaded only when visited

**In Next.js** — route splitting is automatic per file in `/pages` or `/app`

**In plain React** — wrap each page import in `React.lazy()`, wrap routes in `<Suspense>`

### Key Concepts
| Term | One-line meaning |
|---|---|
| Feature-based structure | Group files by feature, not by file type |
| Container/Presenter | Hook fetches data, component only renders |
| Colocation | Keep related files together |

---

## 8. How to Prevent Extra Re-renders

> **Interviewer wants to hear:** Profile first. Pick the right tool — not useCallback on everything blindly.

### Find Re-renders First, Then Fix
- **React DevTools Profiler** — flame graph of renders and their durations
- Temporary `console.log('rendered')` in suspect components
- `why-did-you-render` library in dev — logs exactly which prop changed
- Without the library: write a `useWhyDidYouRender` hook using `useRef` to compare prev vs current props

### Common Causes and Fixes

| Cause | Fix |
|---|---|
| Parent re-renders → child gets same props | Wrap child in `React.memo` |
| New object/array created every render | `useMemo` to stabilise the reference |
| New function created every render | `useCallback` to stabilise the reference |
| Context value changes → all consumers re-render | Split contexts or `useMemo` the context value |
| Inline `style={{ }}` object in JSX | Move to a constant outside the component |
| State higher than it needs to be | Move state down closer to where it is used |

### Important Caveat
`React.memo`, `useMemo`, `useCallback` all have a cost — memory and comparison work every render. Only use them when a component renders frequently, receives the same props, and re-rendering is measurably expensive.

### Key Concepts
| Term | One-line meaning |
|---|---|
| `React.memo` | Skip re-render if props are shallowly equal |
| `useMemo` | Cache a computed value between renders |
| `useCallback` | Cache a function reference between renders |
| Referential equality | `{} !== {}` even with identical content — React compares by reference |
| Shallow comparison | `React.memo` checks each prop with `===`, not deeply |

---

## 9. Page is Re-rendering Too Many Times

> **Interviewer wants to hear:** You know all four triggers and diagnose each one systematically.

### The 4 Triggers of Re-renders
1. **State changes**
2. **Props change**
3. **Context changes**
4. **Parent re-renders**

Check each one in order.

### Common Causes and Fixes

**State updating too rapidly**
- Check for state being set in loops or scroll handlers without throttling
- React 18 auto-batches — multiple `setState` calls in one event = one render

**Wrong `useEffect` dependency array**
- Object or function as dependency creates a new reference every render → effect fires every render
- Fix: stabilise with `useMemo` or `useCallback`

**Context too broad**
- One large context updating frequently → all consumers re-render on every change
- Fix: split into multiple contexts grouped by update frequency — theme (never), user (on login), data (often)

**State too high in the tree**
- Input state in a parent re-renders every sibling on every keystroke
- Fix: move input state down into its own component — siblings are completely unaffected

### Key Concepts
| Term | One-line meaning |
|---|---|
| State colocation | Keep state as local as possible |
| Derived state | Compute from existing state with `useMemo` — do not store separately |
| Batching | React 18 merges multiple setState calls into one render |

---

## 10. When to Use Redux vs React Query

> **Interviewer wants to hear:** You know the difference between server state and client state — this is the most important distinction in modern React.

### The Core Distinction

| State Type | What It Is | Best Tool |
|---|---|---|
| **Server State** | Data from an API — users, posts, products | React Query / TanStack Query |
| **Client State** | UI-only — modal open, selected tab, form draft | Zustand / useState / useReducer |

> Most teams use Redux for everything including server data. That is the wrong approach.

### React Query — For Server Data
- Handles caching, loading states, error states, background refresh, polling, pagination, optimistic updates
- `staleTime` — how long before data is considered outdated
- `queryKey` — cache key; change it to trigger a new fetch
- `useMutation` — for POST/PUT/DELETE with automatic cache invalidation on success

### Redux or Zustand — For Client State
- Theme, auth session, shopping cart, multi-step form state
- When multiple disconnected parts of the app share the same state
- **Zustand** is the modern preference — no boilerplate, no Provider wrapper needed

### Without Libraries
- **Custom `useFetch` hook** using `useEffect` + `useState` handles simple cases
- **`Context + useReducer`** replaces Redux for simple global state — zero extra packages

### My Recommended Architecture
- React Query → all server/API data
- Zustand → complex global UI state
- `useState` / `useReducer` → local component state

### Key Concepts
| Term | One-line meaning |
|---|---|
| Server state | Lives on the server — needs fetching, caching, syncing |
| Client state | Lives only in the browser — no network involved |
| `staleTime` | How long before React Query considers cached data outdated |
| `queryKey` | Cache key — changing it triggers a new fetch |
| Redux Toolkit | Modern Redux — significantly less boilerplate |

---

## 11. Design a React App for Millions of Users

> **Interviewer wants to hear:** CDN, rendering strategy, code splitting, performance budgets, monitoring.

### Rendering Strategy — Pick the Right One

| Strategy | When to Use |
|---|---|
| **SSG** | Content rarely changes — blogs, marketing pages — pre-render at build, serve from CDN |
| **SSR** | Personalised or frequently changing + needs SEO — Next.js; plain React needs Express server |
| **CSR** | Internal tools, SEO does not matter — default React behaviour |

### Other Key Pillars

**Get code closer to the user**
- Serve all JS, CSS, images from a **CDN**
- Use **Edge Functions** (Cloudflare Workers, Vercel Edge) — SSR runs from the nearest server

**Shrink what the browser downloads**
- Every route is a separate chunk — `React.lazy` in plain React, automatic in Next.js
- Analyse bundle with `webpack-bundle-analyzer` or `vite-bundle-visualizer`
- Set a **performance budget** — fail CI build if bundle exceeds e.g. 200KB

**Images**
- Use WebP or AVIF — much smaller than JPEG/PNG
- Lazy load with `loading="lazy"` or `IntersectionObserver`
- Next.js `<Image>` component handles all of this automatically

**Caching**
- Static assets cached for 1 year — filenames include a content hash so cache busting is safe
- React Query for client-side API caching
- Service Workers for offline support

**Monitor in production**
- `web-vitals` library for LCP, FID, CLS
- Sentry for errors — Datadog for performance APM

### Key Concepts
| Term | One-line meaning |
|---|---|
| TTFB | Time to First Byte — SSG has the lowest |
| Edge rendering | SSR runs near the user, not on a distant origin server |
| Performance budget | Max allowed bundle size — CI fails if exceeded |
| Content hash | File names change on deploy, so long cache headers are safe |
| Hydration | React attaches to server HTML on the client to make it interactive |

---

## 12. Handling Concurrent Users

> **Interviewer wants to hear:** Real-time sync options, optimistic updates, conflict detection, multi-tab awareness.

### Real-Time Options

| Method | Best For |
|---|---|
| **WebSockets** | Bidirectional — chat, live collaboration, gaming |
| **Server-Sent Events** | Server-to-client only — notifications, live feeds |
| **Polling** | Simplest fallback — `setInterval` to refetch every N seconds |

### Handling Conflicts

**Optimistic Updates**
- Apply change in UI immediately — do not wait for server confirmation
- If server rejects → roll back to snapshot + show error

**Optimistic Locking (version numbers)**
- Every record has a version number
- Save request includes the version the edit was based on
- Server responds 409 Conflict if someone else already updated it
- Frontend shows: "Someone else updated this — see latest or save anyway"

**CRDTs / Operational Transformation**
- For real-time collaborative editing like Google Docs or Figma
- Algorithms that auto-merge concurrent edits without conflicts
- Complex to implement — mention it to signal awareness

**Multi-tab sync**
- **BroadcastChannel API** — native, no library needed
- User logs out in one tab → broadcast to all other tabs → all log out

### Without Libraries
- Native `WebSocket` constructor — no Socket.io needed
- `setInterval` + `fetch` for polling
- `BroadcastChannel` for cross-tab messaging

### Key Concepts
| Term | One-line meaning |
|---|---|
| Optimistic locking | Save includes version seen; server rejects if version advanced |
| 409 Conflict | HTTP status: "your request conflicts with current server state" |
| CRDT | Data structure that auto-merges concurrent edits |
| BroadcastChannel | Native browser API for messaging between tabs |
| Lost Update | Two users edit same record; second save silently overwrites first |

---

## 13. Lazy Loading, Code Splitting and Suspense

> **Interviewer wants to hear:** You understand the mechanism, what Suspense does, and the key difference between plain React and Next.js.

### The Problem
Default React build = one giant JS file. User visiting the homepage downloads code for every page — most of it never used on that visit.

### The Mechanism
- **Dynamic `import()`** returns a Promise — code downloads only when that line runs
- Build tool (Webpack / Vite) sees it and automatically creates a **separate JS chunk** for that module
- This is the foundation of all lazy loading and code splitting

### In Plain React — Manual

**Component-level splitting:**
- Wrap dynamic import in `React.lazy()`
- Wrap the component in `<Suspense fallback={...}>` — required, shows fallback while chunk downloads
- `React.lazy` only works with **default exports** — named exports need a `.then()` workaround

**Route-level splitting:**
- Lazy-import every page component separately
- Wrap the Routes block in `<Suspense>`
- Each route's chunk downloads only when that URL is first visited

### In Next.js — Mostly Automatic
- Every file in `/pages` or `/app` folder is automatically a separate chunk — you do nothing
- Use `next/dynamic` for component-level splitting with extra options:
  - `ssr: false` — skip server rendering for browser-only components like map libraries
  - Named export support built in — no workaround needed
- `<Link>` automatically prefetches the next page chunk on hover

### What Suspense Actually Does
- Catches a "pending" signal from a lazy component or async data source
- Shows your fallback UI (spinner, skeleton) until the chunk or data is ready
- In React 18 + Next.js App Router: also works for async data fetching, not just lazy loading

### Preloading — Bonus Pattern
- Call `import('./SomePage')` on hover of a navigation link — chunk starts downloading early
- By the time user clicks, chunk is already loaded — navigation feels instant

### Key Concepts
| Term | One-line meaning |
|---|---|
| Dynamic `import()` | Returns a Promise; build tool splits it into a separate file |
| `React.lazy` | Wraps dynamic import for JSX use; requires Suspense parent |
| Suspense | Shows fallback while lazy component or async data is pending |
| `next/dynamic` | Next.js version of React.lazy with SSR control |
| Prefetching | Download chunk before user navigates — feels instant |

---

## 14. User Clicks Edit — Idempotency Problem

> **Interviewer wants to hear:** You think beyond the happy path — race conditions, duplicate saves, concurrent editors, stale forms.

### The Real Question Behind This
When interviewer says "user clicks Edit" they are really asking about failure modes:
- User double-clicks Save → two identical requests race to server
- Two users edit same record → one silently overwrites the other
- User edits, walks away, comes back → data changed, they overwrite new changes
- Network is slow, user retries → operation runs twice (e.g. payment charged twice)

### Layer 1 — Control Edit State on the Frontend

Model the edit as a **state machine** — never allow overlapping states:

**`idle` → `editing` → `saving` → `idle` or `error`**

- While in `saving`: disable all inputs and the Save button
- On success: back to `idle`
- On error: back to `editing` with message shown — user can retry
- Keep a **draft copy** locally — do not mutate real data until Save is confirmed
- Reset draft to latest server data every time user opens the edit form

### Layer 2 — Idempotency Keys (Prevent Duplicate Writes)

- Generate a **UUID** once when user opens the edit form
- Send it as a request header: `Idempotency-Key: <uuid>`
- If user retries or double-submits → same key arrives at server again
- Server returns the stored result from the first request — **operation runs only once**
- This is how Stripe, PayPal, and banking APIs prevent double-charges

### Layer 3 — Conflict Detection (Prevent Lost Updates)

- Every record has a `version` number on the server
- When user opens form → frontend reads current version (e.g. `5`)
- Save request includes: `version: 5` — "I based my edit on version 5"
- If another user already saved (now version `6`) → server responds **409 Conflict**
- Frontend shows options:
  - See latest version (discard your changes)
  - Force save anyway (overwrite)
  - Show diff and let user merge

### Layer 4 — Optimistic UI (Fast Feel)

- Apply the edit in UI immediately — do not wait for server
- Save a snapshot of data before the update
- If server rejects → restore the snapshot + show error toast
- React Query `useMutation` has `onMutate`, `onError`, `onSettled` for this pattern built-in

### Without Libraries — useRef Guard
- Use `useRef` as an "is saving in progress?" flag instead of `useState`
- `useRef` does not cause re-renders when changed — perfect for a silent guard
- Check the ref at the top of the save handler — if already `true`, return early immediately

### The One Sentence to Say in the Interview
> "The frontend controls UX. The backend guarantees correctness."

Meaning — you disable buttons and show spinners for fast feedback, but the real safety against duplicates and conflicts lives on the server with idempotency keys and version locking.

### Key Concepts
| Term | One-line meaning |
|---|---|
| Idempotency | Same request sent N times = same result as once |
| Idempotency Key | UUID per operation; backend deduplicates on it |
| Optimistic Locking | Save includes version seen; server rejects if version advanced |
| 409 Conflict | Server says: "your edit is based on stale data" |
| Lost Update | Two users edit same record; second save overwrites first silently |
| Draft State | Local copy of data being edited; separate from real data until saved |
| `useRef` guard | Mutable flag across renders that does not trigger re-renders |
| State machine | Explicit states: idle → editing → saving → done or error |

---

## 15. Library Cheat Sheet

> "If you were starting a new React project today, what stack would you pick?"

| Category | Pick | Why |
|---|---|---|
| **Framework** | Next.js | Auto code splitting, SSR/SSG, image optimization, edge support |
| **Server State** | TanStack Query | Caching, background sync, pagination, optimistic updates — all built in |
| **Client State** | Zustand | Zero boilerplate, no Provider needed |
| **Forms** | React Hook Form | Uncontrolled inputs = zero re-renders per keystroke |
| **Validation** | Zod | TypeScript-first, pairs perfectly with React Hook Form |
| **Styling** | Tailwind CSS | No CSS sprawl, purges unused styles automatically |
| **Components** | shadcn/ui | Accessible, you own the code — copy-paste not npm install |
| **Routing** | React Router v6 / Next.js | Nested routes, lazy loading, data loaders |
| **Testing** | Vitest + RTL | Fast, tests behavior not implementation details |
| **Lists** | react-window | Virtualize huge lists efficiently |
| **Errors** | Sentry | Production error tracking with full stack traces |
| **Bundle Analysis** | bundle-analyzer | See exactly what is making the bundle fat |

---

## 6 Sentences to Say in Every Senior Interview

1. **"I measure before I optimize"** — profiling first, guessing never
2. **"I keep state as local as possible"** — global state only when truly needed
3. **"Server state and client state are different problems"** — React Query for API, Zustand for UI
4. **"The frontend controls UX, the backend guarantees correctness"** — for edit/save flows
5. **"I know how to do it without libraries too"** — proves you understand fundamentals, not just tools
6. **"Every decision has a trade-off"** — memoization adds complexity, SSR adds infrastructure

---

*Senior React Interview Guide — precise, scannable, no fluff.*