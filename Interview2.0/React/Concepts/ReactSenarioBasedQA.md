# 🧠 React Scenario‑Based Interview Q&A (Explain Like an Expert)

> This file is designed for **scenario rounds** (senior / practical interviews).  
> Format for each question: **Issue → Why it happens → Best solution → Code → Pitfalls → What to say in interview**

---

## 📌 Quick Rule for Interview Answers
When interviewer asks any scenario, answer in this order:

1) **Clarify** the requirement (edge cases, constraints)  
2) **Explain mental model** (why the issue happens)  
3) **Propose a clean architecture**  
4) **Show code / pseudo code**  
5) **Mention pitfalls + tradeoffs**

---

# 1) Hooks & React Internals Scenarios

## Q1) “I want to call a hook only if some condition is true.” What’s the issue? How do you mitigate?

### ✅ The Issue
Hooks must be called in the **same order** on every render. React identifies hooks by:
- which component is rendering  
- the **call order** of hooks inside it  

If you call a hook conditionally, the order changes → React links state/effects to the **wrong hook** → bugs.

### Why it happens (simple mental model)
React stores hooks in a list like:
```
Hook #1 → useState
Hook #2 → useEffect
Hook #3 → useRef
```
If you skip a hook sometimes, everything after shifts.

### ❌ Wrong
```jsx
function Demo({ enabled }) {
  if (enabled) {
    const [x, setX] = useState(0); // ❌ conditional hook
  }
  return null;
}
```

### ✅ Bandaid fix (allowed but not always ideal)
Call the hook always, but move condition **inside**:
```jsx
function useMaybeFetch(enabled, url) {
  const [data, setData] = useState(null);

  useEffect(() => {
    if (!enabled) return;              // ✅ condition inside effect
    let cancelled = false;

    (async () => {
      const res = await fetch(url);
      const json = await res.json();
      if (!cancelled) setData(json);
    })();

    return () => { cancelled = true; };
  }, [enabled, url]);

  return enabled ? data : null;
}
```

**Tradeoff:** callers must check for `null`/`undefined`.

### ✅ Best approach (cleanest)
Split into a **conditionally rendered component**:
```jsx
function FetchUser({ url }) {
  const [data, setData] = useState(null);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      const res = await fetch(url);
      const json = await res.json();
      if (!cancelled) setData(json);
    })();
    return () => { cancelled = true; };
  }, [url]);

  return <pre>{JSON.stringify(data, null, 2)}</pre>;
}

export default function Parent({ enabled }) {
  return (
    <div>
      {enabled ? <FetchUser url="/api/user" /> : <p>Disabled</p>}
    </div>
  );
}
```

### What to say in interview
> “Hooks must be called unconditionally because React matches them by call order. If I need conditional behavior, I either keep the hook call stable and put the condition inside the hook/effect, or I split into a conditional child component. In practice, the component split usually produces cleaner separation.”

---

## Q2) You get outdated state inside useEffect (stale closures). How to fix?

### ✅ Why it happens
Each render creates a new closure. If an effect or timer captures old variables, it keeps using old values.

### Fix options (choose best for scenario)

#### ✅ Option A: Add dependencies (most common)
```jsx
useEffect(() => {
  console.log(count);
}, [count]);
```

#### ✅ Option B: Functional updates (for state setters)
```jsx
setCount(c => c + 1);
```

#### ✅ Option C: useRef to store latest value (best for intervals/events)
```jsx
import { useEffect, useRef, useState } from "react";

export default function Demo() {
  const [count, setCount] = useState(0);
  const latest = useRef(count);

  useEffect(() => { latest.current = count; }, [count]);

  useEffect(() => {
    const id = setInterval(() => {
      console.log("latest:", latest.current); // always fresh
    }, 1000);
    return () => clearInterval(id);
  }, []);

  return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
}
```

### What to say in interview
> “Stale closures happen when async callbacks capture old state. Fix is dependency array, functional updates, or storing latest state in a ref for long‑lived callbacks.”

---

# 2) Data Flow & State Management

## Q3) What is prop drilling? What’s preferred instead?

### ✅ Definition
Prop drilling is when you pass props through multiple layers of components that don’t need them, just to reach a deep child.

### Why it’s a problem
- painful refactors (change one prop → many files)
- noisy code
- hard to reuse components

### Preferred options (when to use which)

✅ **Composition (first choice)**
- Pass children/components directly instead of drilling props
```jsx
function Layout({ header, body }) {
  return (
    <>
      <div>{header}</div>
      <div>{body}</div>
    </>
  );
}
```

✅ **Context API (for app-level shared state like theme/auth)**
```jsx
const AuthContext = createContext(null);
```

✅ **Redux / Zustand / RTK Query (large apps, complex global state, caching)**
- best when many parts of app read/write same global state
- devtools / predictable updates / async middleware

✅ **Server cache libraries (React Query / RTK Query / SWR)**
- best for API data: caching, dedupe, retries, stale‑while‑revalidate

### Interview answer
> “I avoid prop drilling with composition first, then Context for cross‑cutting concerns like theme/auth, and for large shared state + complex updates I use Redux/RTK or Zustand. For server state I prefer React Query/RTK Query because caching is the real problem.”

---

## Q4) How to update parent state from child cleanly?

### ✅ Pattern 1: callback prop (most common)
```jsx
function Child({ onChangeName }) {
  return <button onClick={() => onChangeName("Suvam")}>Set Name</button>;
}

export default function Parent() {
  const [name, setName] = useState("Guest");
  return (
    <>
      <p>{name}</p>
      <Child onChangeName={setName} />
    </>
  );
}
```

### ✅ Pattern 2: Context / store (if many children need update)
Use when multiple deeply nested components need to update same state.

---

# 3) Feed / Infinite Scroll / Large Lists

## Q5) Infinite scrolling feed (LinkedIn style). How implement efficiently?

### ✅ Requirements to clarify
- page size? cursor-based or page-based API?
- should it stop at end?
- should it dedupe duplicates?
- show skeleton loading?
- handle error retry?

### ✅ Best approach
Use **IntersectionObserver** (more efficient than scroll event):
- render “sentinel” div at bottom
- when visible, load next page
- prevent duplicate fetch using `loading` / `hasMore`

```jsx
import { useEffect, useRef, useState } from "react";

export default function InfiniteFeed() {
  const [items, setItems] = useState([]);
  const [page, setPage] = useState(0);
  const [loading, setLoading] = useState(false);
  const [hasMore, setHasMore] = useState(true);
  const sentinelRef = useRef(null);

  async function loadNext() {
    if (loading || !hasMore) return;
    setLoading(true);

    const res = await fetch(`/api/feed?page=${page}`);
    const data = await res.json(); // {items:[], hasMore:true}

    setItems(prev => [...prev, ...data.items]);
    setHasMore(data.hasMore);
    setPage(p => p + 1);
    setLoading(false);
  }

  useEffect(() => { loadNext(); }, []); // initial load

  useEffect(() => {
    const el = sentinelRef.current;
    if (!el) return;

    const obs = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) loadNext();
    }, { rootMargin: "200px" });

    obs.observe(el);
    return () => obs.disconnect();
  }, [loading, hasMore, page]);

  return (
    <div>
      {items.map((x, idx) => <div key={idx}>{x.title}</div>)}

      <div ref={sentinelRef} style={{ height: 1 }} />

      {loading && <p>Loading…</p>}
      {!hasMore && <p>End of feed.</p>}
    </div>
  );
}
```

### Performance improvements
- **Virtualize** large feed (`react-window`)
- use cursor-based pagination (better than page numbers)
- use caching library (React Query)
- dedupe requests, cancel on unmount

### Interview answer
> “I use IntersectionObserver sentinel + cursor pagination and guard with loading/hasMore. For very large lists I add virtualization and cache pages.”

---

# 4) Auth / Security / Routing Scenarios

## Q6) Auto logout after 30 minutes of inactivity

### ✅ Approach
Track user activity events + reset timer:
- `mousemove`, `keydown`, `click`, `scroll`, `touchstart`
- store lastActive time
- if idle → clear token and redirect

```jsx
import { useEffect, useRef } from "react";

export default function useAutoLogout(minutes = 30) {
  const timeoutRef = useRef(null);

  useEffect(() => {
    const ms = minutes * 60 * 1000;

    const reset = () => {
      clearTimeout(timeoutRef.current);
      timeoutRef.current = setTimeout(() => {
        localStorage.removeItem("token");
        window.location.assign("/login");
      }, ms);
    };

    const events = ["mousemove", "keydown", "click", "scroll", "touchstart"];
    events.forEach(e => window.addEventListener(e, reset));

    reset(); // start timer

    return () => {
      clearTimeout(timeoutRef.current);
      events.forEach(e => window.removeEventListener(e, reset));
    };
  }, [minutes]);
}
```

### Interview answer
> “I attach global listeners to detect activity and reset a timeout. On timeout I clear auth and redirect. I cleanup listeners and timers on unmount.”

---

## Q7) Role-based protected routes in React Router (Admins only)

### ✅ Idea
- Keep auth + roles in Context/store
- Create `ProtectedRoute` wrapper that checks role and redirects

```jsx
import { Navigate, Outlet } from "react-router-dom";

export function ProtectedRoute({ allowedRoles }) {
  const user = JSON.parse(localStorage.getItem("user") || "null"); // {role:"admin"}

  if (!user) return <Navigate to="/login" replace />;

  if (allowedRoles && !allowedRoles.includes(user.role)) {
    return <Navigate to="/403" replace />;
  }

  return <Outlet />;
}
```

Usage:
```jsx
<Route element={<ProtectedRoute allowedRoles={["admin"]} />}>
  <Route path="/admin" element={<AdminPage />} />
</Route>
```

### Interview answer
> “I handle authorization in route guards. Auth state comes from context/store; route wrapper checks roles and redirects to login/403.”

---

# 5) SEO / SSR / Indexing Problems

## Q8) Google isn’t indexing your React SPA. How do you solve it?

### Why it happens
A pure SPA renders most content only after JS loads. Search bots may not execute JS fully, so pages appear empty.

### Solutions (best order)
1) ✅ **SSR framework (Next.js)** → best solution  
2) ✅ **Static Site Generation (SSG)** for marketing pages  
3) ✅ **Dynamic rendering / prerendering** (Rendertron / Prerender.io)  
4) ✅ Ensure metadata: title, meta tags, canonical, sitemap, robots.txt

### Interview answer
> “For SEO pages I move to SSR/SSG (Next.js). If migration is slow, I use prerendering. And I ensure correct meta tags, sitemap and canonical URLs.”

---

# 6) Large File Uploads / Network Scenarios

## Q9) Upload 100MB+ files without timeouts

### ✅ Best practices
- Use **chunked uploads** (split file into parts)
- Upload parts with retry/resume
- Use presigned URLs (S3) or backend upload session
- Show progress using `xhr.upload.onprogress`

### Chunk upload example (simplified)
```jsx
async function uploadChunked(file) {
  const chunkSize = 5 * 1024 * 1024; // 5MB
  let offset = 0;
  let part = 0;

  while (offset < file.size) {
    const chunk = file.slice(offset, offset + chunkSize);

    const form = new FormData();
    form.append("chunk", chunk);
    form.append("part", String(part));
    form.append("name", file.name);

    const res = await fetch("/api/upload/chunk", { method: "POST", body: form });
    if (!res.ok) throw new Error("chunk failed");

    offset += chunkSize;
    part += 1;
  }

  await fetch("/api/upload/complete", { method: "POST", body: JSON.stringify({ name: file.name }) });
}
```

### Interview answer
> “I implement chunked uploads with retry/resume, or use S3 multipart uploads via presigned URLs. This avoids timeouts and supports progress.”

---

# 7) Internationalization (i18n)

## Q10) Support multiple languages in React

### ✅ Approach
Use i18n library + translation files per locale.
- `react-i18next` is common
- store selected language in localStorage
- support RTL if needed

Example (react-i18next style)
```js
// translations/en.json
{ "hello": "Hello", "logout": "Logout" }
```

```jsx
// usage
import { useTranslation } from "react-i18next";

function Header() {
  const { t, i18n } = useTranslation();
  return (
    <div>
      <h2>{t("hello")}</h2>
      <button onClick={() => i18n.changeLanguage("hi")}>Hindi</button>
    </div>
  );
}
```

### Interview answer
> “I use react-i18next with JSON translation files, lazy-load languages, store preference, and handle pluralization/formatting properly.”

---

# 8) Bundle Size / Performance / Loading

## Q11) Bundle too large. How to reduce it?

### ✅ Checklist
- Route-level code splitting (`React.lazy`)
- Remove unused libraries, use smaller alternatives
- Tree shaking + ESM builds
- Analyze bundle (Webpack bundle analyzer / Vite visualize)
- Deduplicate dependencies
- Load heavy libs only when needed (dynamic import)

### Example: route-level lazy
```jsx
import { lazy, Suspense } from "react";
const Admin = lazy(() => import("./Admin"));

export default function App() {
  return (
    <Suspense fallback={<p>Loading…</p>}>
      <Admin />
    </Suspense>
  );
}
```

### Interview answer
> “I analyze the bundle, split routes, lazy-load heavy features, remove unused deps, and ensure tree-shaking works.”

---

## Q12) Reduce unnecessary re-renders

### ✅ Tools
- `React.memo` for child components
- `useCallback` for stable function props
- `useMemo` for expensive computations
- avoid inline objects as props
- split Context to reduce blast radius

Mini example:
```jsx
const Child = React.memo(function Child({ onClick }) {
  return <button onClick={onClick}>Child</button>;
});

function Parent() {
  const [count, setCount] = useState(0);

  const handler = useCallback(() => {
    console.log("clicked");
  }, []);

  return <Child onClick={handler} />;
}
```

---

# 9) Animations / UI Motion Scenarios

## Q13) Smooth page transitions & animations

### ✅ Approach
- Use CSS transitions for simple animations
- Use Framer Motion for route transitions / layout animations
- Keep animations GPU-friendly (transform/opacity)
- Avoid layout thrash (width/height repeatedly)

Interview answer:
> “I use CSS for simple transitions and Framer Motion for route transitions. I animate transform/opacity, not layout properties.”

---

# 10) Rate Limiting / Throttling

## Q14) API calls frequently hit rate limit. How throttle?

### Options
- **Debounce** for search input (wait after typing)
- **Throttle** for scroll events (max once per interval)
- Request queue + retry with backoff (429)
- Cache and dedupe requests (React Query)

### Throttle function (simple)
```js
export function throttle(fn, wait = 500) {
  let last = 0;
  return (...args) => {
    const now = Date.now();
    if (now - last >= wait) {
      last = now;
      fn(...args);
    }
  };
}
```

### Interview answer
> “For user events I throttle/debounce. For 429 responses I retry with exponential backoff and caching to reduce calls.”

---

# 11) Forms & Inputs Scenarios

## Q15) Search filter with debounce input

```jsx
import { useEffect, useState } from "react";

function useDebounce(value, delay = 400) {
  const [v, setV] = useState(value);
  useEffect(() => {
    const id = setTimeout(() => setV(value), delay);
    return () => clearTimeout(id);
  }, [value, delay]);
  return v;
}

export default function Search() {
  const [q, setQ] = useState("");
  const debounced = useDebounce(q);

  useEffect(() => {
    if (!debounced) return;
    fetch(`/api/search?q=${encodeURIComponent(debounced)}`);
  }, [debounced]);

  return <input value={q} onChange={e => setQ(e.target.value)} placeholder="Search..." />;
}
```

---

# 12) API Integration & Side Effects

## Q16) Fetch multiple APIs concurrently and merge results (Promise.all)

```jsx
useEffect(() => {
  let cancelled = false;

  async function run() {
    const [a, b] = await Promise.all([
      fetch("/api/a").then(r => r.json()),
      fetch("/api/b").then(r => r.json()),
    ]);
    if (!cancelled) setData({ a, b });
  }

  run();
  return () => { cancelled = true; };
}, []);
```

## Q17) Retry logic for rate limits (429) with backoff
```js
async function fetchWithRetry(url, tries = 3) {
  let delay = 500;

  for (let i = 0; i < tries; i++) {
    const res = await fetch(url);

    if (res.status !== 429) return res;
    await new Promise(r => setTimeout(r, delay));
    delay *= 2;
  }

  throw new Error("Rate limited too many times");
}
```

---

# 13) Component Design Scenarios

## Q18) Build reusable Modal using Portal + Context

### Idea
- Portal renders modal into `document.body`
- Context provides open/close API

(High-level snippet)
```jsx
import { createContext, useContext, useState } from "react";
import { createPortal } from "react-dom";

const ModalCtx = createContext(null);

export function ModalProvider({ children }) {
  const [content, setContent] = useState(null);

  const open = (node) => setContent(node);
  const close = () => setContent(null);

  return (
    <ModalCtx.Provider value={{ open, close }}>
      {children}
      {content ? createPortal(
        <div role="dialog" aria-modal="true" style={{ position:"fixed", inset:0, background:"rgba(0,0,0,.5)" }}>
          <div style={{ background:"#fff", margin:"10% auto", padding:16, width:320 }}>
            {content}
            <button onClick={close}>Close</button>
          </div>
        </div>,
        document.body
      ) : null}
    </ModalCtx.Provider>
  );
}

export function useModal() {
  const ctx = useContext(ModalCtx);
  if (!ctx) throw new Error("useModal must be used within ModalProvider");
  return ctx;
}
```

---

# 14) Error Handling

## Q19) Error boundaries & fallback UI

### Key points
- Catch render errors in subtree
- Only class components can be error boundaries
- Doesn’t catch errors in async events automatically

---

# 15) DOM Manipulation (when necessary)

## Q20) Using useRef to manage focus or integrate a 3rd party library
- Focus input
- Store timer id
- Integrate chart libs, map libs, editors

---


# 16) More Scenario Questions (Extra Practice)

Use these to test yourself (**with short expected answers**):

### 1) Your list is reordering but items show wrong state—why? (keys)
**Short answer:** Your keys are not stable (often using index as key), so React “reuses” the wrong DOM/component instance when items move.  
**Fix:** Use a **stable unique id** as `key`, and avoid index keys for reorderable/filterable lists.

### 2) How to prevent double API calls in React 18 StrictMode?
**Short answer:** In **development**, StrictMode can intentionally mount/unmount and re-run effects to detect unsafe side effects, so your fetch runs twice.  
**Mitigation:** Make effects **idempotent** + cancel/ignore duplicates using `AbortController`, or use a data-fetching cache (React Query/RTK Query) that **dedupes** requests. Don’t “hack around” it in production code—fix the effect logic.

### 3) How to cancel fetch requests on unmount?
**Short answer:** Use `AbortController` and abort in the `useEffect` cleanup to avoid setting state after unmount.  
**Pattern:** create controller → pass `signal` → `return () => controller.abort()`.

### 4) How to handle optimistic updates for likes/comments?
**Short answer:** Update UI immediately, keep a snapshot of previous state, send request, and **rollback** if it fails (or reconcile with server response).  
**Best practice:** Use a mutation helper (React Query `onMutate/onError/onSettled` or RTK Query optimistic updates) for clean rollback logic.

### 5) How to implement “undo” feature? (state history)
**Short answer:** Maintain history: `past[]`, `present`, `future[]`.  
**Undo:** move `present` to `future`, pop from `past` into `present`.  
**Redo:** reverse the operation. `useReducer` is ideal for this.

### 6) How to design a table with sorting + filtering + pagination?
**Short answer:** Keep UI state: `sortKey`, `sortDir`, `filters`, `page`, `pageSize`. Derive rows with `useMemo` (filter → sort → paginate).  
**Scaling:** For large datasets, do **server-side** pagination/sorting/filtering and keep client state for controls + query params.

### 7) How to store auth tokens securely?
**Short answer:** Prefer **HttpOnly + Secure + SameSite cookies** for tokens so JS can’t read them (reduces XSS risk).  
If you must store client-side: keep access token **in memory** (not localStorage), rotate frequently, and use a refresh token in cookie + CSRF protection.

### 8) How to handle websocket updates + state consistency?
**Short answer:** Use a single websocket connection in `useEffect`, update state with **functional updates / reducer**, and dedupe messages by id.  
Add reconnect with backoff, and handle out-of-order events using timestamps/sequence numbers.

### 9) How to reduce context re-render blast radius?
**Short answer:** Split contexts (don’t put everything in one), memoize provider value, and avoid passing new objects/functions each render.  
If still heavy: use selector-based context patterns or move frequently-changing state to a store (Redux/Zustand) with selectors.

### 10) How to handle skeleton loading & error retry UX?
**Short answer:** Show skeletons for initial load, keep previous data while refetching, and show an inline error with a **Retry** button.  
For flaky APIs: implement exponential backoff retries (or use React Query/RTK Query) and clearly communicate “loading / error / success” states.

---

## ✅ Final “What interviewer wants”
If you answer each scenario with:
- root cause
- clean solution
- code snippet
- tradeoffs

…you will sound like a senior React engineer.

