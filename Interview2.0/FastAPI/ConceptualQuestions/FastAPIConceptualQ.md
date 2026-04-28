# ⚡ Senior FastAPI / Backend API Interview Guide
> Precise answers for scenario-based backend questions. No code. No fluff. Read once, remember forever.

---

## Table of Contents
1. [What is FastAPI and Why Use It Over Flask or Django?](#1-what-is-fastapi-and-why-use-it-over-flask-or-django)
2. [How Does Async Work in FastAPI?](#2-how-does-async-work-in-fastapi)
3. [API is Slow — How Do You Find and Fix It?](#3-api-is-slow--how-do-you-find-and-fix-it)
4. [How Do You Design a Good REST API?](#4-how-do-you-design-a-good-rest-api)
5. [How Do You Handle Authentication and Authorization?](#5-how-do-you-handle-authentication-and-authorization)
6. [What is Rate Limiting and How Do You Implement It?](#6-what-is-rate-limiting-and-how-do-you-implement-it)
7. [How Do You Handle Database Performance Issues?](#7-how-do-you-handle-database-performance-issues)
8. [What is Caching and When Do You Use It?](#8-what-is-caching-and-when-do-you-use-it)
9. [API is Throwing 500 Errors in Production — What Do You Do?](#9-api-is-throwing-500-errors-in-production--what-do-you-do)
10. [How Do You Handle Background Tasks?](#10-how-do-you-handle-background-tasks)
11. [How Do You Design for Scale and High Traffic?](#11-how-do-you-design-for-scale-and-high-traffic)
12. [What is Idempotency and Why Does It Matter?](#12-what-is-idempotency-and-why-does-it-matter)
13. [How Do You Secure an API?](#13-how-do-you-secure-an-api)
14. [Monolith vs Microservices — When Do You Use Which?](#14-monolith-vs-microservices--when-do-you-use-which)
15. [How Do You Handle Database Migrations?](#15-how-do-you-handle-database-migrations)
16. [What is the N+1 Query Problem and How Do You Fix It?](#16-what-is-the-n1-query-problem-and-how-do-you-fix-it)
17. [How Do You Version an API?](#17-how-do-you-version-an-api)
18. [How Do You Test a Backend API?](#18-how-do-you-test-a-backend-api)
19. [SQL vs NoSQL — How Do You Choose?](#19-sql-vs-nosql--how-do-you-choose)
20. [How Do You Handle Async Communication Between Services?](#20-how-do-you-handle-async-communication-between-services)
21. [Cheat Sheet — Tools and When to Use Them](#21-cheat-sheet--tools-and-when-to-use-them)

---

## 1. What is FastAPI and Why Use It Over Flask or Django?

> **Interviewer wants to hear:** You know the trade-offs, not just the buzzwords.

### Why FastAPI Stands Out
- **Performance** — built on Starlette (ASGI) and Uvicorn; one of the fastest Python frameworks, on par with Node.js and Go in benchmarks
- **Async-first** — natively supports `async/await` so it handles many concurrent requests without extra threads
- **Auto-generated docs** — Swagger UI and ReDoc come free out of the box from your code — no manual documentation needed
- **Pydantic validation** — request and response data is automatically validated and typed; bad data is rejected before it even reaches your logic
- **Type hints everywhere** — errors caught at development time, not in production

### Compared to Others

| Feature | FastAPI | Flask | Django |
|---|---|---|---|
| Performance | Very high (async) | Medium (sync) | Medium (sync) |
| Built-in validation | Yes (Pydantic) | No | Partial (Forms) |
| Auto docs | Yes | No | No |
| Best for | APIs, microservices | Small APIs, simple apps | Full-stack, admin-heavy apps |
| Learning curve | Medium | Low | High |

### When NOT to use FastAPI
- You need a full-stack web app with templates → Django is better
- Team is already deep in Flask with no async needs → migration cost is not worth it
- Very simple, one-endpoint utility → Flask is simpler

### Key Concepts
| Term | One-line meaning |
|---|---|
| ASGI | Async Server Gateway Interface — the async version of WSGI |
| Uvicorn | The server that runs FastAPI; handles async requests |
| Pydantic | Data validation library; powers FastAPI's request/response models |
| Starlette | The ASGI framework FastAPI is built on top of |

---

## 2. How Does Async Work in FastAPI?

> **Interviewer wants to hear:** You understand when to use async, when not to, and what it actually does under the hood.

### The Core Idea
- Python normally runs one thing at a time on one thread
- `async/await` lets the server **pause** a waiting task (like a DB query) and handle another request while waiting — no thread blocked
- FastAPI runs on an event loop — one thread, many tasks in flight at once

### When to Use `async def`
- Whenever the route does I/O — database queries, HTTP calls to external APIs, reading files
- The whole point: while DB is thinking, serve 10 other requests

### When to Use Regular `def`
- CPU-heavy work — image processing, number crunching
- Synchronous-only libraries that don't support async
- FastAPI runs regular `def` routes in a thread pool automatically so they don't block

### The Hidden Trap
- Doing a slow synchronous database call inside an `async def` route **blocks the entire event loop** — nothing else can run
- Always use async-compatible DB drivers: `asyncpg` for PostgreSQL, `motor` for MongoDB, `aioredis` for Redis

### Key Concepts
| Term | One-line meaning |
|---|---|
| Event loop | A loop that checks what async task to run next |
| `async def` | Marks a function as async — it can pause and resume |
| `await` | Pause here until this async operation completes |
| Blocking call | A synchronous call inside async that freezes the event loop |
| Thread pool | Where FastAPI sends regular `def` routes to avoid blocking |

---

## 3. API is Slow — How Do You Find and Fix It?

> **Interviewer wants to hear:** Systematic approach — measure first, fix second. Not guessing.

### Step 1 — Find the Bottleneck
- Check **response time distribution** — is it all requests or specific endpoints?
- Check **database slow query logs** — most slowness lives in the DB
- Use **distributed tracing** (OpenTelemetry, Datadog APM) — shows exactly where each request spends time
- Add **timing middleware** to log how long each route takes
- Check **external API calls** — a slow third-party can tank your whole response time

### Step 2 — Fix Based on What You Find

| Root Cause | Fix |
|---|---|
| Slow database queries | Add indexes, rewrite query, paginate |
| Fetching too much data | Select only columns you need, add pagination |
| N+1 query problem | Eager load with joins instead of looping queries |
| No caching | Add Redis cache for repeated identical reads |
| Synchronous code in async route | Switch to async DB driver |
| Serial external API calls | Run them in parallel with `asyncio.gather` |
| Large response payload | Compress with gzip, only return fields client needs |

### Step 3 — Prevent It From Coming Back
- Set **response time SLOs** — e.g. p95 must stay under 200ms
- Add **slow query alerts** — get notified when a query exceeds threshold
- Load test before shipping with tools like **k6** or **Locust**

### Key Concepts
| Term | One-line meaning |
|---|---|
| p95 latency | 95% of requests are faster than this number |
| Slow query log | DB feature that logs queries taking over X ms |
| Distributed tracing | Track a request across multiple services end-to-end |
| `asyncio.gather` | Run multiple async operations in parallel, not serial |
| SLO | Service Level Objective — agreed performance target |

---

## 4. How Do You Design a Good REST API?

> **Interviewer wants to hear:** You think about consistency, versioning, error handling, and the consumer's experience.

### Core Principles

**Resource-based URLs — nouns, not verbs**
- Good: `GET /users/123`, `POST /orders`, `DELETE /products/456`
- Bad: `GET /getUser`, `POST /createOrder`, `GET /deleteProduct?id=456`

**Use HTTP methods correctly**
| Method | Use for |
|---|---|
| GET | Read only — never change data |
| POST | Create a new resource |
| PUT | Replace an entire resource |
| PATCH | Update part of a resource |
| DELETE | Remove a resource |

**HTTP status codes — be precise**
| Code | When to use |
|---|---|
| 200 | Success |
| 201 | Resource created |
| 400 | Bad request (client's fault — wrong input) |
| 401 | Not authenticated — no token |
| 403 | Authenticated but not allowed — wrong permissions |
| 404 | Resource not found |
| 409 | Conflict — duplicate or version mismatch |
| 422 | Validation error (FastAPI uses this a lot) |
| 429 | Too many requests — rate limited |
| 500 | Server error (your fault) |

**Always paginate lists**
- Never return 10,000 records in one call
- Use `limit` + `offset` for simple pagination or `cursor` for large datasets

**Consistent error format**
- Every error response should have the same structure: `{ "error": "RESOURCE_NOT_FOUND", "message": "User with id 123 not found" }`
- Never return HTML error pages from an API

**HATEOAS (mention to impress)**
- Include links in responses that tell clients what they can do next
- Not always practical but shows senior-level awareness

### Key Concepts
| Term | One-line meaning |
|---|---|
| Idempotent | Same request sent multiple times = same result (GET, PUT, DELETE are idempotent; POST is not) |
| Resource | The noun in your URL — User, Order, Product |
| Pagination | Splitting large results into pages so you never return all at once |
| HATEOAS | Hypermedia links in response describing next possible actions |

---

## 5. How Do You Handle Authentication and Authorization?

> **Interviewer wants to hear:** You know the difference between authentication and authorization AND the right tool for each scenario.

### Authentication vs Authorization
- **Authentication** — who are you? Prove your identity
- **Authorization** — what are you allowed to do? Check your permissions

### JWT — Most Common for APIs

**How it works:**
- User logs in with username/password
- Server verifies credentials, generates a signed JWT token
- Client stores token, sends it in every request as `Authorization: Bearer <token>`
- Server verifies the signature on every request — no DB lookup needed
- Token has an expiry — usually 15–60 minutes

**Access Token + Refresh Token pattern:**
- Access token: short-lived (15 min) — used for API calls
- Refresh token: long-lived (7–30 days) — used only to get a new access token
- If access token is stolen, it expires quickly; refresh token is stored securely (httpOnly cookie)

**JWT weaknesses:**
- Cannot revoke a token before it expires — if token is stolen and not expired, attacker has access
- Solution: maintain a token blacklist in Redis, or use short expiry + refresh tokens

### OAuth2 — For Third-Party Login
- "Login with Google/GitHub" flows
- Your app never sees the user's password — Google handles auth, sends you a token
- FastAPI has built-in `OAuth2PasswordBearer` for this

### API Keys — For Service-to-Service
- Simple static string sent in a header: `X-API-Key: <key>`
- No expiry by default — must be manually revoked
- Good for internal services or B2B integrations

### RBAC — Role-Based Access Control
- Users have roles (admin, editor, viewer)
- Routes check if user's role allows the action
- Implemented via a dependency that reads the JWT payload and checks roles

### Key Concepts
| Term | One-line meaning |
|---|---|
| JWT | Signed token containing user data — server can verify without DB lookup |
| Access Token | Short-lived token for API requests |
| Refresh Token | Long-lived token to get a new access token |
| OAuth2 | Protocol for third-party auth (login with Google etc.) |
| RBAC | Role-based access — user's role determines what they can do |
| Token blacklist | Redis set of revoked tokens checked on every request |

---

## 6. What is Rate Limiting and How Do You Implement It?

> **Interviewer wants to hear:** You know the algorithms, the tradeoffs, and how to apply limits per user not just per IP.

### Why It Matters
- Prevents abuse — one bad actor cannot take down your API with a flood of requests
- Protects downstream services — DB, third-party APIs
- Enforces fair usage — free tier gets 100 req/min, paid gets 10,000

### Common Algorithms

**Fixed Window**
- Count requests in a fixed time window (e.g. 60 seconds)
- Simple but has a burst problem — user can send 100 requests at second 59, then 100 more at second 61
- Good enough for most cases

**Sliding Window**
- Tracks requests over a rolling time window — no burst loophole
- More accurate but slightly more complex

**Token Bucket**
- User has a bucket of tokens; each request consumes one; tokens refill at a fixed rate
- Allows short bursts while still enforcing average rate
- Used by most production systems (AWS, Stripe)

**Leaky Bucket**
- Requests drip out at a fixed rate regardless of how fast they come in
- Smooths traffic — no bursts at all

### What to Rate Limit On
- **IP address** — basic, can be defeated by rotating IPs
- **User ID / API key** — better for authenticated endpoints
- **Endpoint** — different limits for different routes (login has stricter limit than read endpoints)
- **Global** — cap total requests to protect infrastructure

### Where to Enforce It
- **API Gateway level** (Nginx, AWS API Gateway, Kong) — before request even hits your app — most efficient
- **Middleware in FastAPI** — `slowapi` library or custom middleware
- **Redis** — store counters in Redis so limits work across multiple server instances (otherwise each server has its own counter)

### Key Concepts
| Term | One-line meaning |
|---|---|
| Token Bucket | Most common algorithm — allows bursts, enforces average rate |
| Sliding Window | No burst loophole — tracks last N seconds exactly |
| 429 status code | HTTP response when rate limit is exceeded |
| Redis counter | Shared counter across multiple servers for distributed rate limiting |
| API Gateway | Layer in front of your API — best place to enforce global limits |

---

## 7. How Do You Handle Database Performance Issues?

> **Interviewer wants to hear:** Indexing, query optimization, connection pooling, read replicas — in that order.

### Common Issues and Fixes

**Slow queries — fix with indexing**
- Index the columns you filter by (`WHERE`, `JOIN`, `ORDER BY`)
- Use `EXPLAIN` / `EXPLAIN ANALYZE` to see what the DB is doing with a query
- Composite indexes for multi-column filters: `WHERE status = 'active' AND created_at > X`
- Too many indexes slow down writes — only index what you query frequently

**Fetching too much — fix with selective queries**
- Never `SELECT *` — only fetch columns you actually need
- Always paginate — never return unbounded lists
- Use `LIMIT` on every query that returns multiple rows

**N+1 problem — fix with eager loading**
- Fetching 100 users and then querying orders for each = 101 queries
- Fix: join tables in one query or use ORM eager loading (SQLAlchemy `joinedload`)

**Connection exhaustion — fix with connection pooling**
- Every request opening a new DB connection kills the DB quickly
- Connection pool keeps a fixed set of connections alive and reuses them
- FastAPI with SQLAlchemy: configure pool size, max overflow, and timeout
- For async: use `asyncpg` with its own connection pool

**Database becomes a bottleneck under read-heavy load**
- Add a **read replica** — primary handles writes, replica handles reads
- Route read queries to replica, write queries to primary
- Slight replication lag is acceptable for most reads

**Database becomes a bottleneck under write-heavy load**
- Consider **sharding** — split data across multiple DBs by a key (user_id range, geographic region)
- Last resort — very complex; exhaust caching and read replicas first

### Key Concepts
| Term | One-line meaning |
|---|---|
| Index | Pre-sorted data structure for fast column lookups |
| `EXPLAIN` | DB command that shows how a query is executed |
| N+1 problem | One query for list, then one per item — very slow |
| Connection pool | Reuse existing connections instead of opening new ones per request |
| Read replica | Copy of DB that handles read queries — reduces primary load |
| Sharding | Splitting DB across multiple servers by a partition key |

---

## 8. What is Caching and When Do You Use It?

> **Interviewer wants to hear:** You know cache strategies, invalidation, and the trade-offs — not just "add Redis."

### What Caching Solves
- Repeated identical reads hit the database every time — wasteful and slow
- Cache stores the result in memory — next request gets it in microseconds, not milliseconds

### Caching Strategies

**Cache-Aside (most common)**
- App checks cache first
- If miss → fetch from DB → store in cache → return to client
- App controls what gets cached and when
- Best for read-heavy data that changes occasionally

**Write-Through**
- On every write → update DB AND cache simultaneously
- Cache always has fresh data
- Slight write latency increase

**Write-Behind (Write-Back)**
- Write to cache immediately, write to DB asynchronously in background
- Very fast writes but risk of data loss if cache crashes before DB write

**Read-Through**
- Cache sits in front of DB transparently — app just asks cache
- Cache fetches from DB on miss automatically

### What to Cache
- Expensive DB query results — product catalogue, configuration, reference data
- Computed results — aggregations, reports
- Session data — user session tokens
- API responses from slow external services

### What NOT to Cache
- Highly personalized data — wrong user gets wrong data
- Frequently changing data with zero tolerance for staleness — bank balances
- Write-heavy data — cache invalidation becomes the problem

### Cache Invalidation — The Hard Part
- **TTL (Time to Live)** — cache expires after N seconds; simplest approach
- **Event-based** — when data changes, explicitly delete or update the cache key
- **Cache-busting** — include a version in the cache key so old entries are naturally abandoned

### Tools
- **Redis** — most popular; in-memory, supports TTL, pub/sub, atomic operations
- **Memcached** — simpler, faster for pure key-value; no persistence
- **In-memory dict in process** — fine for single-server, lost on restart

### Key Concepts
| Term | One-line meaning |
|---|---|
| Cache hit | Data found in cache — fast |
| Cache miss | Data not in cache — fetch from DB, then store |
| TTL | How long a cache entry lives before expiring |
| Cache invalidation | Removing or updating stale cache entries when source data changes |
| Eviction policy | What Redis removes when cache is full (LRU = Least Recently Used) |

---

## 9. API is Throwing 500 Errors in Production — What Do You Do?

> **Interviewer wants to hear:** Systematic incident response — calm, methodical, no panic.

### Step 1 — Contain the Damage (First 5 minutes)
- Check if this is **all requests or some requests** — if all, consider a rollback immediately
- Check **when it started** — correlate with the last deployment
- If recent deploy caused it → **rollback** first, investigate after
- Enable a **feature flag** to turn off the affected feature without full rollback

### Step 2 — Find the Root Cause
- Pull **logs** — look for the actual exception and stack trace
- Check **monitoring dashboards** — CPU, memory, DB connections, external API errors
- Check **database** — is it up? Is it under unusual load?
- Check **external dependencies** — is a third-party API the app relies on down?
- Reproduce locally if possible — same payload, same environment

### Step 3 — Fix and Verify
- Deploy the fix to **staging first** — reproduce the error there, verify fix
- Deploy to production
- Watch error rate — confirm it drops back to baseline
- Check that the fix didn't introduce new errors

### Step 4 — Post-Mortem
- Write a **post-mortem** — what happened, why, what was the impact, how was it fixed, what prevents recurrence
- Add a **test** that would have caught this bug — so it never ships again
- Add a **monitoring alert** for the specific pattern that caused this

### Key Concepts
| Term | One-line meaning |
|---|---|
| Rollback | Revert to the previous working deployment |
| Feature flag | Toggle a feature on/off without deploying new code |
| Stack trace | The exact line of code where an error occurred |
| Post-mortem | Blameless writeup of an incident — root cause + prevention |
| Error rate | Percentage of requests resulting in 5xx errors |

---

## 10. How Do You Handle Background Tasks?

> **Interviewer wants to hear:** You know the difference between lightweight background tasks and true async job queues — and when to use each.

### When to Use Background Tasks
- Sending emails after signup — user doesn't need to wait
- Generating a report — takes 10 seconds, return a job ID immediately
- Sending webhooks to third parties — fire-and-forget
- Processing uploaded files — resize images, parse CSVs
- Logging and analytics — non-critical, can be async

### Option 1 — FastAPI BackgroundTasks (Built-in, Lightweight)
- Runs after the response is sent, in the same process
- Simple to use, no extra infrastructure
- **Limitation**: if server crashes, tasks are lost — not suitable for critical work
- **Use for**: non-critical tasks like sending emails, writing logs

### Option 2 — Celery + Redis/RabbitMQ (Production-Grade)
- Tasks are put in a queue (Redis or RabbitMQ acts as the broker)
- Separate worker processes consume and run tasks independently
- Tasks survive server crashes — they wait in queue until a worker picks them up
- Supports retries, scheduling, task prioritization, result storage
- **Use for**: payment processing, report generation, any task that must not be lost

### Option 3 — Cloud-Managed Queues
- AWS SQS, Google Cloud Tasks, Azure Service Bus
- Managed — no infrastructure to maintain
- SQS is at-least-once delivery — design tasks to be idempotent (running twice = same result)

### Key Design Rule
- **Always return a response immediately** — never make the user wait for a background task
- Return a `202 Accepted` with a `job_id` — client polls or gets notified when done

### Key Concepts
| Term | One-line meaning |
|---|---|
| Message broker | Intermediary (Redis, RabbitMQ) that holds tasks between producer and worker |
| Worker | Separate process that consumes and executes tasks from the queue |
| At-least-once delivery | Task may run more than once — must be idempotent |
| 202 Accepted | HTTP status: "request received, processing in background" |
| Dead letter queue | Where failed tasks go after max retries — inspect and replay |

---

## 11. How Do You Design for Scale and High Traffic?

> **Interviewer wants to hear:** Horizontal scaling, stateless design, caching, load balancing, async queues — in layers.

### The Core Principle
- Design stateless APIs — any request can go to any server instance
- State (sessions, cache) lives in shared external storage (Redis), not in the server itself

### Scaling Layers

**Layer 1 — Scale the Application Server**
- Run **multiple instances** of FastAPI behind a load balancer
- Horizontal scaling — add more instances under load; remove them when traffic drops
- Use Docker + Kubernetes for orchestration and auto-scaling
- Each instance is stateless — no local storage, no local session

**Layer 2 — Scale the Database**
- **Read replicas** — route read queries to replicas; primary only handles writes
- **Connection pooling** — PgBouncer in front of PostgreSQL for connection management at scale
- **Caching layer** — Redis in front of DB to absorb repeated reads

**Layer 3 — Async Work**
- Move heavy or slow work off the request path into a queue (Celery, SQS)
- Keep API response times fast — the API should only coordinate, not do heavy lifting inline

**Layer 4 — CDN and Edge**
- Cache static assets and even some API responses at CDN edge nodes
- Geographic distribution — serve users from nearest server

**Layer 5 — Load Balancer**
- Nginx or AWS ALB distributes incoming traffic across all instances
- Health checks — removes unhealthy instances from rotation automatically

### Key Numbers to Know
- A single FastAPI instance can handle ~5,000–10,000 concurrent connections (async)
- PostgreSQL connection limit is usually 100–500 — use PgBouncer at scale
- Redis can handle 1M+ operations per second

### Key Concepts
| Term | One-line meaning |
|---|---|
| Stateless | Server stores nothing locally — any instance can handle any request |
| Horizontal scaling | Add more instances — cheaper than one very powerful machine |
| Load balancer | Distributes requests across multiple instances |
| PgBouncer | Connection pooler that sits in front of PostgreSQL |
| Auto-scaling | Automatically add/remove instances based on traffic |

---

## 12. What is Idempotency and Why Does It Matter?

> **Interviewer wants to hear:** You can explain it practically with a real scenario — not just the definition.

### What It Means
An operation is idempotent if performing it multiple times produces the same result as doing it once.

- **GET** — always idempotent (read-only)
- **DELETE** — idempotent (delete twice = still deleted)
- **PUT** — idempotent (replace with same data twice = same result)
- **POST** — NOT idempotent by default (create twice = two records created)

### Why It Matters
- Networks are unreliable — client may not know if request succeeded
- Client retries the request → without idempotency → operation runs twice
- Example: user clicks Pay, network drops, client retries → user charged twice

### How to Implement

**Idempotency Keys**
- Client generates a unique UUID for each operation
- Sends it as a header: `Idempotency-Key: <uuid>`
- Server checks if this key was seen before:
  - First time → process and store the result linked to the key
  - Repeat → return the stored result without re-processing
- Store in Redis with TTL (e.g. 24 hours)

**Natural idempotency through design**
- `PUT /users/123/status` with `{ "status": "active" }` — running twice sets status to active both times — same result
- Design your write endpoints to be PUT-style where possible

**Database-level idempotency**
- Use `ON CONFLICT DO NOTHING` or `UPSERT` to avoid duplicate inserts
- Unique constraints on meaningful business fields prevent duplicate records

### Key Concepts
| Term | One-line meaning |
|---|---|
| Idempotency Key | UUID sent by client; server uses it to detect and deduplicate retries |
| UPSERT | Insert if not exists, update if exists — naturally idempotent |
| `ON CONFLICT DO NOTHING` | SQL that ignores duplicate inserts gracefully |
| At-least-once delivery | Queue guarantee that a message is processed at least once — requires idempotent consumers |

---

## 13. How Do You Secure an API?

> **Interviewer wants to hear:** Layered security — authentication, authorization, input validation, transport, rate limiting, monitoring.

### Security Layers

**1. Transport — Always HTTPS**
- All traffic encrypted in transit — no exceptions
- Redirect HTTP to HTTPS automatically
- Use TLS 1.2+ only

**2. Authentication — Verify Who You Are**
- JWT tokens for stateless auth (see Q5)
- Rotate secrets regularly
- Short token expiry + refresh tokens

**3. Authorization — Verify What You Can Do**
- RBAC — roles on every protected endpoint
- Principle of least privilege — each role gets only what it needs

**4. Input Validation — Trust Nothing**
- Validate all inputs with Pydantic models — type, length, format
- Never pass raw user input to a database query
- Reject unexpected fields — don't let clients send extra data

**5. Rate Limiting — Prevent Abuse**
- Per-user limits on all endpoints
- Stricter limits on sensitive endpoints: login, password reset, OTP
- Return 429 with `Retry-After` header

**6. SQL Injection Prevention**
- Never build SQL strings by concatenating user input
- Always use parameterized queries or ORM — SQLAlchemy, Tortoise ORM handle this automatically

**7. CORS — Control Who Can Call Your API**
- Whitelist specific origins — not `*` in production
- FastAPI has `CORSMiddleware` for this

**8. Secrets Management**
- Never hardcode API keys, DB passwords, secrets in code
- Use environment variables — loaded from `.env` locally, secret manager in production (AWS Secrets Manager, Vault)

**9. Dependency Scanning**
- Run `pip audit` or Dependabot to catch vulnerabilities in third-party packages

**10. Logging and Monitoring**
- Log all authentication failures — brute force pattern
- Alert on sudden spike in 401/403 errors
- Never log passwords or tokens

### OWASP Top 10 — Know These
- Broken access control
- SQL injection
- Insecure authentication
- Sensitive data exposure
- Security misconfiguration

### Key Concepts
| Term | One-line meaning |
|---|---|
| TLS | Transport Layer Security — encrypts data in transit |
| Parameterized query | SQL query where user input is never mixed with the query string |
| CORS | Controls which browser origins can call your API |
| Least privilege | Give only the minimum permissions needed |
| OWASP Top 10 | Industry-standard list of most critical web security risks |

---

## 14. Monolith vs Microservices — When Do You Use Which?

> **Interviewer wants to hear:** You think about trade-offs and team size — not "microservices are always better."

### Monolith First
- One codebase, one deployment, one database
- Simpler to develop, test, debug, and deploy
- Lower operational overhead — no network calls between services, no distributed tracing needed
- **Start here** — most apps should stay here longer than engineers want to

### When Microservices Make Sense
- Different parts of the system need to **scale independently** — payment service gets 100x more load than user service
- Different teams need to **deploy independently** without coordinating
- Different services have **different tech requirements** — one needs Python, one needs Go
- Clear domain boundaries exist — don't split before they're obvious

### Hidden Costs of Microservices
- **Network latency** between services — a call that was in-memory now goes over the network
- **Distributed transactions** — updating two services atomically is hard (see Saga pattern)
- **Operational complexity** — logging, tracing, health checks, service discovery, per-service deployments
- **Debugging is harder** — errors span multiple services

### The Right Pattern
- Start with a **modular monolith** — clean module boundaries, separate domains internally
- Extract to a service only when you have a clear, proven reason
- "Peel off" services one at a time — don't rewrite everything at once

### Key Concepts
| Term | One-line meaning |
|---|---|
| Monolith | Single codebase and deployment unit |
| Microservice | Independent service with its own DB and deployment |
| Saga pattern | Way to handle distributed transactions across services without locking |
| Service discovery | How services find each other dynamically (Consul, Kubernetes DNS) |
| Modular monolith | Monolith with clean internal module separation — best of both worlds to start |

---

## 15. How Do You Handle Database Migrations?

> **Interviewer wants to hear:** Zero-downtime strategy, rollback plan, and expand/contract pattern.

### The Problem
- Schema changes in production can break running code — can't just `ALTER TABLE` and hope
- Need to change DB schema while the API is still running and serving traffic

### The Expand/Contract Pattern (Safe Approach)

**Step 1 — Expand (additive change)**
- Add the new column as nullable — existing rows won't break
- Both old and new code continue to work
- Deploy this migration with no app changes

**Step 2 — Migrate (dual-write or backfill)**
- New code writes to both old and new column
- Background job backfills old data into new column
- Verify data integrity — checksums, row counts

**Step 3 — Contract (cleanup)**
- Once all data is migrated and new code is fully deployed
- Remove the old column in a separate, later migration
- Only safe to do after old code is completely gone from production

### Tools
- **Alembic** — most common for SQLAlchemy — version-controlled migration files
- **Flyway / Liquibase** — Java-origin but language-agnostic
- Migrations run automatically in CI/CD before deploy, or manually with a deploy step

### Zero-Downtime Principles
- Only additive changes in the first migration — no deletes, no renames that break old code
- Never rename a column in one step — add new column → copy data → update code → remove old column
- Always have a **rollback migration** prepared before deploying

### Key Concepts
| Term | One-line meaning |
|---|---|
| Expand/Contract | Safe pattern: add first, migrate, then remove old |
| Alembic | Python migration tool for SQLAlchemy — version-controlled schema changes |
| Backfill | Populating a new column with data from existing rows in bulk |
| Rollback migration | The reverse migration that undoes a change if something goes wrong |
| Zero-downtime migration | Schema change that doesn't require stopping the API |

---

## 16. What is the N+1 Query Problem and How Do You Fix It?

> **Interviewer wants to hear:** Clear explanation of the problem and at least two fix strategies.

### What It Is
- You fetch a list of N items — 1 query
- Then for each item, you fetch related data — N more queries
- Total: N+1 database queries for one API request — gets catastrophically slow as N grows

**Example:**
- Fetch 100 users → 1 query
- For each user, fetch their orders → 100 queries
- Total: 101 queries — should have been 2 at most

### How to Fix It

**Fix 1 — Eager Loading / JOIN**
- Fetch users and their orders in a single JOIN query
- SQLAlchemy: use `joinedload()` or `selectinload()` on the relationship
- Result: 1 query (or 2 at most) instead of 101

**Fix 2 — Batch Loading (DataLoader pattern)**
- Collect all the IDs you need from step 1
- Fetch all related records in one query using `WHERE id IN (...)`
- Map results back to each parent
- Used heavily in GraphQL resolvers

**Fix 3 — Denormalization**
- Store frequently-accessed related data directly on the parent record
- Trade-off: data duplication, update complexity
- Last resort for extreme performance needs

### How to Detect It
- Count your DB queries per request in testing — anything above 5-10 for a single endpoint is suspicious
- SQLAlchemy echo mode logs every query — enable in development
- APM tools (Datadog, New Relic) show query count per request in production

### Key Concepts
| Term | One-line meaning |
|---|---|
| Eager loading | Load related data upfront in the same query |
| `joinedload` | SQLAlchemy option to join related tables automatically |
| `selectinload` | SQLAlchemy option to load relationships in a second optimised query |
| DataLoader | Batch loading pattern — collect IDs, fetch all in one query |
| `IN (...)` clause | SQL that fetches multiple rows by a list of IDs in one trip |

---

## 17. How Do You Version an API?

> **Interviewer wants to hear:** You think about backward compatibility and not breaking existing clients.

### Why Versioning Matters
- Clients (mobile apps, third parties) cannot always update immediately when you change the API
- Without versioning, a breaking change takes down all existing integrations
- With versioning, old clients use v1, new clients use v2 — no one breaks

### Versioning Strategies

**URL Path Versioning** — most common and explicit
- `GET /v1/users` and `GET /v2/users`
- Easy to see, easy to route, easy to test
- FastAPI: use APIRouter with prefix `/v1`, `/v2`

**Header Versioning**
- `Accept: application/vnd.myapi.v2+json`
- Cleaner URLs but harder to test (can't just paste URL in browser)
- Used by GitHub, Stripe

**Query Parameter Versioning**
- `GET /users?version=2`
- Simple but messy — version is data, not routing concern

### What Counts as a Breaking Change
- Removing a field from a response
- Renaming a field
- Changing a field's type
- Adding a required field to a request
- Changing behaviour of an endpoint

### What is NOT a Breaking Change (Safe to Do Without Versioning)
- Adding a new optional field to a response
- Adding a new optional query parameter
- Adding a new endpoint
- Fixing a bug (unless clients depended on the buggy behaviour)

### Supporting Multiple Versions
- Keep v1 alive until clients have migrated — set a deprecation date, communicate it
- Add `Deprecation` and `Sunset` headers to v1 responses to warn clients
- Never delete a version without giving clients adequate migration time

### Key Concepts
| Term | One-line meaning |
|---|---|
| Breaking change | Change that makes existing clients fail |
| Deprecation | Warning that a version will be removed in the future |
| Sunset header | HTTP header telling clients when a version will stop working |
| Backward compatible | New version works with old client requests without changes |

---

## 18. How Do You Test a Backend API?

> **Interviewer wants to hear:** Test pyramid, mocking external dependencies, and testing behaviour not implementation.

### Test Pyramid

**Unit Tests — most tests should be here**
- Test individual functions and business logic in isolation
- Fast — no database, no network
- Mock external dependencies (DB, Redis, external APIs)
- FastAPI: test Pydantic models, service functions, utility helpers

**Integration Tests — second layer**
- Test the full route from HTTP request to database and back
- Use a real test database (PostgreSQL in Docker) — not mocks
- FastAPI: use `TestClient` or `httpx.AsyncClient` with `app`
- Test the happy path AND error cases for each endpoint

**End-to-End Tests — few, critical paths only**
- Test the whole system as a user would — from client to production-like backend
- Slowest — run on CI, not on every local change
- Cover only the most critical user flows

### What to Test
- Every endpoint: happy path, invalid input (422), missing auth (401), wrong permissions (403)
- Pagination — does limit/offset work correctly?
- Error handling — do you get consistent error format?
- Edge cases — empty results, max limit, duplicate creates

### FastAPI Specific
- Use `pytest` with `pytest-asyncio` for async tests
- `TestClient` wraps `httpx` — use it for sync-style integration tests
- Override dependencies in tests to inject test DB or mock services

### Mocking External Services
- Never call real third-party APIs in tests — slow, unreliable, costs money
- Use `respx` to mock `httpx` calls or `unittest.mock` for function mocking
- Alternatively: `httpretty`, `responses` libraries for mocking HTTP

### Key Concepts
| Term | One-line meaning |
|---|---|
| Test pyramid | Lots of unit tests, fewer integration, very few E2E |
| TestClient | FastAPI/Starlette test helper that simulates HTTP requests |
| Mocking | Replacing real dependencies with controlled fakes in tests |
| `pytest-asyncio` | Pytest plugin enabling async test functions |
| Contract testing | Verify that two services agree on their API contract |

---

## 19. SQL vs NoSQL — How Do You Choose?

> **Interviewer wants to hear:** You choose based on data model and access patterns — not trends.

### Use SQL (PostgreSQL, MySQL) When
- Data is **relational** — users have orders, orders have items
- You need **ACID transactions** — financial data, inventory, anything where consistency is critical
- You write **complex queries** — joins, aggregations, filtering across multiple tables
- Data schema is **stable and well-defined**
- You need **strong consistency** — everyone sees the same data immediately

### Use NoSQL When

**Document DB (MongoDB)**
- Data is hierarchical or nested — store a user with their addresses, preferences all in one document
- Schema is flexible or frequently changing — different users have different fields
- Read the whole document together most of the time

**Key-Value (Redis)**
- Caching — store computed results by a key, expire after TTL
- Sessions — fast user session lookup
- Rate limiting counters
- Pub/sub messaging

**Wide-column (Cassandra, DynamoDB)**
- Massive scale — billions of rows, thousands of writes per second
- Time-series data — logs, events, IoT sensor readings
- Know your access patterns upfront — no ad-hoc queries

**Search (Elasticsearch)**
- Full-text search, fuzzy matching, autocomplete
- Complex filtering across many fields
- Not a primary database — sync data from your main DB into Elasticsearch

### Common Pattern
- PostgreSQL as the primary source of truth
- Redis for caching and sessions
- Elasticsearch for search if needed
- Never use MongoDB "because JSON" — that's not a data model reason

### Key Concepts
| Term | One-line meaning |
|---|---|
| ACID | Atomicity, Consistency, Isolation, Durability — SQL guarantees |
| CAP Theorem | Can only guarantee 2 of: Consistency, Availability, Partition tolerance |
| Eventual consistency | NoSQL trade-off — data will be consistent eventually, not immediately |
| Sharding | Splitting NoSQL data across nodes by a partition key |
| Index in NoSQL | Same concept as SQL — needed for fast lookups on non-primary-key fields |

---

## 20. How Do You Handle Async Communication Between Services?

> **Interviewer wants to hear:** Message queues, event-driven design, at-least-once delivery, and idempotent consumers.

### Why Async Communication
- Synchronous: Service A calls Service B and waits — if B is slow or down, A is slow or down too
- Async: Service A puts a message on a queue and continues — B processes when ready
- Decouples services — neither knows nor cares about the other's availability

### Message Queue vs Event Bus

**Message Queue (point-to-point)**
- One producer puts a message → one consumer processes it
- Used for: task distribution, background jobs, sending emails
- Tools: RabbitMQ, AWS SQS

**Event Bus / Event Streaming (pub/sub)**
- One producer publishes an event → many consumers can react to it
- Used for: system-wide events ("order placed" → email service, inventory service, analytics service all react)
- Tools: Kafka, AWS SNS, Google Pub/Sub

### Delivery Guarantees

**At-most-once** — message delivered once or not at all (fire and forget)
**At-least-once** — message may be delivered more than once if acknowledgement fails — most common
**Exactly-once** — guaranteed single delivery — hardest, only Kafka with transactions

### Because of At-Least-Once — Always Design Idempotent Consumers
- Your message handler must produce the same result if the same message arrives twice
- Use a unique message ID — check if already processed before acting
- Database unique constraint prevents duplicate records

### Key Concepts
| Term | One-line meaning |
|---|---|
| Producer | Service that sends messages to the queue |
| Consumer | Service that reads and processes messages from the queue |
| Acknowledgement | Consumer tells queue "I processed this" — queue then deletes it |
| Dead letter queue | Where messages go after max failed retries — inspect and replay |
| Kafka | Distributed event streaming — high throughput, ordered, replayable |
| Idempotent consumer | Handler that produces same result if same message arrives multiple times |

---

## 21. Cheat Sheet — Tools and When to Use Them

> "What stack would you use for a production FastAPI backend?"

| Category | Tool | When to Use |
|---|---|---|
| **Framework** | FastAPI | APIs, microservices, async-heavy workloads |
| **Server** | Uvicorn + Gunicorn | Uvicorn workers managed by Gunicorn for multi-process production |
| **Database (relational)** | PostgreSQL | Default choice — reliable, feature-rich, handles most use cases |
| **Database (cache)** | Redis | Caching, sessions, rate limiting, pub/sub, task queues |
| **ORM** | SQLAlchemy (async) | Models, migrations, query building — use async engine |
| **Migrations** | Alembic | Version-controlled schema changes with SQLAlchemy |
| **Validation** | Pydantic v2 | Built into FastAPI — request/response validation and serialization |
| **Auth** | JWT + OAuth2 | JWT for stateless auth; OAuth2 for third-party login |
| **Task Queue** | Celery + Redis | Background jobs that must not be lost |
| **Message Broker** | RabbitMQ / Kafka | Service-to-service async communication |
| **Search** | Elasticsearch | Full-text search, complex filtering |
| **Testing** | pytest + httpx | Unit and integration tests; httpx for async HTTP testing |
| **Monitoring** | Datadog / Prometheus + Grafana | Metrics, alerts, dashboards |
| **Tracing** | OpenTelemetry | Distributed request tracing across services |
| **Error Tracking** | Sentry | Production exceptions with full context |
| **Load Testing** | k6 / Locust | Performance testing before go-live |
| **Containerization** | Docker + Kubernetes | Packaging and orchestrating at scale |
| **API Gateway** | Nginx / AWS API Gateway | Rate limiting, SSL termination, routing |
| **Secrets** | AWS Secrets Manager / Vault | Store and rotate secrets securely |

---

## 6 Sentences to Say in Every Backend Interview

1. **"I profile before I optimize"** — never assume where the bottleneck is; measure it
2. **"I design for failure"** — retries, timeouts, circuit breakers, dead letter queues
3. **"I make operations idempotent"** — safe retries are non-negotiable in distributed systems
4. **"Database is usually the bottleneck"** — index, cache, paginate, pool connections
5. **"Stateless APIs are the foundation of horizontal scaling"** — nothing stored locally on the server
6. **"Security is layered"** — auth, input validation, rate limiting, transport, secrets — never just one layer

---

*Senior FastAPI / Backend API Interview Guide — precise, scannable, no fluff.*