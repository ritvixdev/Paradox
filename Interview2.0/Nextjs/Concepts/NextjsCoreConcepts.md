# ⚡ Next.js Ultimate Interview Guide (React dev → Next.js interview ready)

This guide **assumes you already know React**. It focuses on what interviewers actually test in Next.js:
- **Routing mental model (App Router vs Pages Router)**
- **Rendering choices (SSR / SSG / ISR / CSR)**
- **Data fetching + caching**
- **API endpoints (Route Handlers / API Routes)**
- **Performance features (Image, code-splitting, prefetch)**
- **Env vars, deployment, TypeScript**

---

## How to study (fast)
1) Read the **One‑liner** of each section.  
2) Practice the **code snippets** (copy → run → modify).  
3) Before interview: revise the **Cheat Sheet** at the end.

---

## The 30‑second mental model
Next.js is a React framework that can render pages:
- **on the server** (SSR),
- **at build time** (SSG),
- **incrementally** (ISR),
- or **on the client** (CSR),
and it gives you **file-based routing**, **backend endpoints**, and **performance optimizations** out of the box.

> Modern Next.js uses the **App Router** (`/app`) built on **React Server Components**; it can exist alongside the old **Pages Router** (`/pages`) for gradual migration. citeturn5search0

---

# 1) What is Next.js + Main features (must-know)

## What is Next.js?
**Answer:** Next.js is a React framework for building full-stack web apps. It adds file-based routing, server rendering, API endpoints, and production optimizations so you don’t have to assemble everything manually. citeturn5search0turn4search1

## Main features (interview bullets)
- **App Router** (`/app`) with nested layouts + Server Components by default. citeturn5search0  
- **File-based routing** (both App Router and Pages Router). citeturn5search0turn3search1  
- **Data fetching + caching + revalidation** (server-side). citeturn0search3turn0search1  
- **Route Handlers** (API endpoints in `app/`). citeturn1search0  
- **Built-in performance**: automatic code-splitting by route segments + prefetching + Image optimization. citeturn4search1turn0search2turn3search3  

---

# 2) Next.js vs Create React App (CRA)

## Key difference (One‑liner)
**CRA is client-only**, while **Next.js is full-stack** and supports server rendering + routing + APIs + optimizations.

## Interview points
- CRA: mostly CSR; SEO and first-load performance often require extra work.
- Next.js: can SSR/SSG/ISR and also serve APIs + optimize assets.

---

# 3) Create a new Next.js app (commands + minimum requirements)

## Command to create an app
```bash
npx create-next-app@latest my-app
cd my-app
npm run dev
```
The official CLI is `create-next-app`. citeturn2search2

## System requirement you can mention
Next.js docs list a **minimum Node.js version** requirement (example: Node 20.9+ in the current installation guide). citeturn2search8

---

# 4) App Router vs Pages Router (the #1 interview topic)

## App Router (modern)
**One‑liner:** Uses `/app`, built on React Server Components, supports nested layouts, loading/error boundaries, and colocated data fetching. citeturn5search0turn4search1

**Key facts**
- Files like `app/page.tsx`, `app/layout.tsx` define UI.
- Components in `/app` are **Server Components by default** (great for performance). citeturn5search0  
- App Router takes priority over Pages Router if both define same path (it’s an error). citeturn5search0

## Pages Router (still used in many companies)
**One‑liner:** Uses `/pages` where each file becomes a route. citeturn3search1

**Key fact**
- Pages are `.js/.jsx/.ts/.tsx` files inside `pages/`. citeturn3search1

---

# 5) Routing essentials (file-based routing + dynamic routes)

## App Router: static route
**File:** `app/about/page.tsx` → URL: `/about`

```tsx
// app/about/page.tsx
export default function AboutPage() {
  return <h1>About</h1>;
}
```

## App Router: dynamic route
**File:** `app/blog/[slug]/page.tsx` → `/blog/:slug`

```tsx
// app/blog/[slug]/page.tsx
type Props = { params: { slug: string } };

export default function BlogPostPage({ params }: Props) {
  return <h1>Post: {params.slug}</h1>;
}
```

## Pages Router: dynamic route
**File:** `pages/blog/[slug].tsx` → `/blog/:slug`

```tsx
// pages/blog/[slug].tsx
import { useRouter } from "next/router";

export default function BlogPost() {
  const router = useRouter();
  const { slug } = router.query;
  return <h1>Post: {String(slug)}</h1>;
}
```

---

# 6) The Link component (navigation + prefetch)

**One‑liner:** `<Link />` enables client-side navigation and can prefetch routes/data for faster navigation (prefetching happens only in production). citeturn2search1

```tsx
import Link from "next/link";

export default function Home() {
  return (
    <div>
      <Link href="/dashboard">Go Dashboard</Link>
      <Link href="/admin" prefetch={false}>No Prefetch</Link>
    </div>
  );
}
```

**Interview tip:** Mention that Next prefetch behavior is configurable and differs by router / route type. citeturn2search1

---

# 7) Rendering modes (SSR / SSG / ISR / CSR) — explain clearly

## SSR (Server-Side Rendering)
**One‑liner:** HTML is generated **on every request**.
- Best for data that must always be fresh (e.g., personalized dashboards, prices).  
- Pages Router uses `getServerSideProps`. citeturn1search8

## SSG (Static Site Generation)
**One‑liner:** HTML generated **at build time**.
- Best for marketing pages, docs, blogs that change rarely.

## ISR (Incremental Static Regeneration)
**One‑liner:** Static page is served, but it can be **re-generated after a revalidate window** (so you don’t rebuild the whole app).  
- In Pages Router, `revalidate` in `getStaticProps` enables ISR; dynamic routes often use `getStaticPaths` with `fallback`. citeturn5search1  
- In App Router, you can use caching/revalidation options like `revalidate` config or `fetch(..., { next: { revalidate }})`. citeturn0search3turn0search1

## CSR (Client-Side Rendering)
**One‑liner:** Browser fetches data after load (like classic React SPA).
- Still possible in Next using client components + useEffect/SWR/React Query.

---

# 8) Data fetching: Pages Router (classic interview questions)

## getStaticProps (SSG / ISR)
**One‑liner:** Runs on server at build time (and can revalidate for ISR).  
Example uses are shown in Next learn docs. citeturn1search6turn5search1

```tsx
// pages/index.tsx
import type { GetStaticProps, InferGetStaticPropsType } from "next";

type Props = { time: string };

export const getStaticProps: GetStaticProps<Props> = async () => {
  return {
    props: { time: new Date().toISOString() },
    revalidate: 60, // ISR: rebuild at most once per 60s
  };
};

export default function Page({ time }: InferGetStaticPropsType<typeof getStaticProps>) {
  return <p>Built at: {time}</p>;
}
```

## getServerSideProps (SSR)
**One‑liner:** Runs on server **every request** and pre-renders page with returned props. citeturn1search8

```tsx
// pages/ssr.tsx
import type { GetServerSideProps, InferGetServerSidePropsType } from "next";

export const getServerSideProps: GetServerSideProps<{ now: string }> = async () => {
  return { props: { now: new Date().toISOString() } };
};

export default function SSRPage({
  now,
}: InferGetServerSidePropsType<typeof getServerSideProps>) {
  return <p>SSR time: {now}</p>;
}
```

## getStaticPaths + fallback (dynamic SSG)
**One‑liner:** Defines which dynamic paths to pre-render. `fallback` controls behavior for other paths. citeturn5search1

```tsx
// pages/posts/[id].tsx
import type { GetStaticPaths, GetStaticProps } from "next";

export const getStaticPaths: GetStaticPaths = async () => {
  return { paths: [{ params: { id: "1" } }], fallback: "blocking" };
};

export const getStaticProps: GetStaticProps = async ({ params }) => {
  const id = params?.id as string;
  return { props: { id }, revalidate: 30 };
};

export default function Post({ id }: { id: string }) {
  return <h1>Post {id}</h1>;
}
```

---

# 9) Data fetching: App Router (modern interview questions)

## Server Component fetch
**One‑liner:** In App Router, you can fetch directly inside server components and control caching/revalidation. citeturn0search3turn0search1

```tsx
// app/page.tsx (Server Component by default)
export default async function Page() {
  const res = await fetch("https://jsonplaceholder.typicode.com/posts/1", {
    cache: "force-cache",          // cache this request
    next: { revalidate: 60 },      // revalidate at most every 60s
  });
  const post = await res.json();

  return <pre>{JSON.stringify(post, null, 2)}</pre>;
}
```

## Opting out of caching
Use `cache: 'no-store'` for always-fresh data. citeturn0search1turn0search3

```ts
await fetch("https://api.example.com/live", { cache: "no-store" });
```

---

# 10) API endpoints: API Routes vs Route Handlers

## Route Handlers (App Router)
**One‑liner:** Route Handlers live inside `app/**/route.ts` and use Web Request/Response APIs. They are the App Router equivalent of Pages API Routes. citeturn1search0

```ts
// app/api/hello/route.ts
export async function GET() {
  return Response.json({ message: "Hello from Route Handler" });
}
```

## API Routes (Pages Router)
**One‑liner:** API Routes live under `pages/api/*` (common in older projects).

```ts
// pages/api/hello.ts
import type { NextApiRequest, NextApiResponse } from "next";

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  res.status(200).json({ message: "Hello from API Route" });
}
```

**Interview tip:** Don’t mix both for the same endpoint unless you’re migrating. (Route Handlers are only in `app/`.) citeturn1search0

---

# 11) Middleware (auth, redirects, rewrites)

**One‑liner:** Middleware runs **before a request is completed** and can redirect/rewrite/modify headers. It uses `middleware.ts` and `matcher` rules. citeturn4search5turn4search4

```ts
// middleware.ts
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function middleware(req: NextRequest) {
  const isLoggedIn = req.cookies.get("token")?.value;

  if (!isLoggedIn && req.nextUrl.pathname.startsWith("/dashboard")) {
    return NextResponse.redirect(new URL("/login", req.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/dashboard/:path*"],
};
```

---

# 12) Environment variables (server vs browser)

**One‑liner:** Next loads `.env*` into `process.env`. Variables are server-only by default; to expose to browser, prefix with `NEXT_PUBLIC_` (inlined at build time). citeturn1search4turn1search5

```bash
# .env.local
DB_URL="postgres://..."
NEXT_PUBLIC_API_BASE="https://api.example.com"
```

```ts
// server-only
console.log(process.env.DB_URL);

// client-safe (inlined at build)
console.log(process.env.NEXT_PUBLIC_API_BASE);
```

---

# 13) Image optimization (next/image)

**One‑liner:** `next/image` optimizes images (size, lazy loading, stability to reduce layout shift) and supports remote images via allowlisting patterns. citeturn0search2turn3search3turn3search4

```tsx
import Image from "next/image";

export default function Avatar() {
  return (
    <Image
      src="/profile.png"
      width={160}
      height={160}
      alt="Profile"
      priority
    />
  );
}
```

### Remote images allowlist
Use `remotePatterns` in `next.config.*` to allow safe remote optimization. citeturn3search4turn3search3

```ts
// next.config.ts
import type { NextConfig } from "next";

const config: NextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: "https",
        hostname: "s3.amazonaws.com",
        pathname: "/my-bucket/**",
        search: "",
      },
    ],
  },
};
export default config;
```

---

# 14) Performance: code splitting + prefetch

## Automatic code splitting
**One‑liner:** In App Router, code is automatically split by **route segments**; navigation loads only what changes. citeturn4search1

## Lazy loading / dynamic import
Use `next/dynamic` to avoid shipping a heavy component in the initial bundle. citeturn4search10

```tsx
import dynamic from "next/dynamic";

const HeavyChart = dynamic(() => import("../components/HeavyChart"), {
  loading: () => <p>Loading chart…</p>,
  ssr: false, // if chart needs browser APIs
});

export default function Page() {
  return <HeavyChart />;
}
```

## Prefetching
Next prefetches linked routes in the background to speed up client navigation; configurable via `<Link prefetch={...} />`. citeturn2search1turn4search1

---

# 15) Deployment: Vercel + custom server

## Vercel (what to say)
**One‑liner:** Vercel is the “default happy path” for Next apps (edge/network optimizations, serverless support, easy previews).  
(Interviewers mainly want to hear that you understand hosting choices and tradeoffs.)

## Custom server (rare; know the downsides)
**One‑liner:** You can run a custom server when Next’s integrated router/server can’t meet requirements, but it can remove important optimizations (e.g., Automatic Static Optimization) and has deployment caveats. citeturn4search0turn4search3

---

# 16) TypeScript essentials (enough for interviews)

## Turn on TypeScript
In new projects, `create-next-app` supports TS by default and can prompt for it. citeturn2search2

## Type page props (Pages Router)
Use `GetServerSideProps`, `InferGetServerSidePropsType`, etc. (shown in official docs). citeturn1search8

## Type Route Handlers (App Router)
Route handlers use `Request`/`Response` types:
```ts
export async function POST(req: Request) {
  const body = await req.json();
  return Response.json({ ok: true, body });
}
```
(Concept matches route handler docs). citeturn1search0

---

# 17) Security best practices (short but strong)

**What to say in interview**
- Never expose secrets to client: only `NEXT_PUBLIC_*` is public. citeturn1search4turn1search5
- Use middleware/route handlers for auth checks; validate input in APIs.
- Use secure headers (CSP), cookies (`HttpOnly`, `Secure`, `SameSite`), and rate limiting.
- Sanitize any user-generated HTML (avoid XSS).

---

# 18) Common interview traps (avoid these)

- Confusing **SSR** (per-request HTML) with **Server Components** (component type in App Router).
- Forgetting that public env vars are **inlined at build time** (changing them later won’t affect the client bundle). citeturn1search4turn1search5
- Using remote images in `<Image>` without configuring allowlist patterns (`remotePatterns`). citeturn3search4turn3search3
- Mixing API Routes + Route Handlers without a plan (migration confusion). citeturn1search0

---

# ✅ Next.js Interview Cheat Sheet (15-minute revision)

## If interviewer asks “What is Next.js?”
> “Next.js is a React framework for full-stack apps: file-based routing, SSR/SSG/ISR, API endpoints, and performance optimizations like code splitting and image optimization.”

## If asked “App Router vs Pages Router?”
> “App Router (`/app`) is modern and uses Server Components; Pages Router (`/pages`) is older but common. App Router supports nested layouts and colocated data fetching, and it takes priority over Pages Router.”

## If asked “When to use SSR vs SSG vs ISR?”
- SSR: always-fresh per request
- SSG: build-time static
- ISR: static but revalidates over time

## If asked “How do you build an API in Next?”
- App Router: `app/api/.../route.ts` Route Handlers
- Pages Router: `pages/api/*.ts` API Routes

---

If you want, I can also generate a **scenario-based Next.js** file (SSR indexing issue, cache bugs, auth redirects, ISR content update, etc.) in the same style you liked for React/Redux.
