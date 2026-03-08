# 🎯 Interview Q&A Guide
### FastAPI · Authentication · SSO · Real-Time Communication · Kafka · OAuth · Security

> **How to use this:** Read the answer out loud once. The bold line at the top of each answer is your opening sentence. Everything after is what you add if the interviewer probes deeper.

---

## 📋 Table of Contents

| Topic | Questions |
|-------|-----------|
| [Python / FastAPI](#fastapi) | Have you used FastAPI? · How do you define APIs? |
| [Authentication & SSO](#auth) | Auth experience · SSO · What changes when API becomes authenticated |
| [SSO Integration](#sso) | How to integrate SSO into an existing app |
| [Real-Time Communication](#realtime) | Beyond WebSockets · Module communication options |
| [Kafka](#kafka) | Kafka experience · Kafka + OAuth · Securing Kafka between VMs |
| [Redis](#redis) | Are you aware of Redis? |
| [OAuth 2.0](#oauth) | OAuth experience · Which microservice · OAuth with Kafka |
| [Backend Security Design](#security) | Adding auth + persona-based access to a plain FastAPI backend |

---

<a name="fastapi"></a>
## 🐍 Python / FastAPI

---

### Q: Have you used FastAPI?

**Yes, I have worked with FastAPI to build REST APIs.**

FastAPI is a modern Python web framework for building APIs. The key reasons it's popular:

- **Fast to write** — very little boilerplate compared to Django or Flask
- **Automatic docs** — generates Swagger UI at `/docs` and ReDoc at `/redoc` out of the box, without any extra work
- **Data validation** — uses Pydantic models to validate request and response data automatically
- **Async support** — natively supports `async/await` so it handles high concurrency well
- **Type hints** — uses Python type hints everywhere, which makes code readable and catches bugs early

> **One-liner to remember:** *"FastAPI is like Express.js for Python — minimal, fast, and generates API docs automatically."*

---

### Q: How do you define APIs in FastAPI?

**You define APIs by decorating Python functions with route decorators like `@app.get()`, `@app.post()`, etc.**

Here is a complete, simple example:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Pydantic model — defines the shape of request/response data
class User(BaseModel):
    name: str
    email: str

# In-memory store (replace with DB in real app)
users = {}

# GET endpoint — fetch a user by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

# POST endpoint — create a new user
@app.post("/users")
def create_user(user: User):         # FastAPI automatically validates the body
    user_id = len(users) + 1
    users[user_id] = user
    return {"id": user_id, **user.dict()}
```

**Key points to mention:**
- The path parameters like `{user_id}` are automatically extracted and type-checked
- The `User` Pydantic model automatically validates the request body — if `email` is missing, FastAPI returns a `422` error with a clear message, no extra code needed
- You run it with: `uvicorn main:app --reload`
- Visit `http://localhost:8000/docs` and you get a full interactive Swagger UI for free

---

<a name="auth"></a>
## 🔐 Authentication

---

### Q: Have you worked on authentication in any application?

**Yes, I have implemented authentication using JWT tokens and also integrated with OAuth 2.0 based SSO providers.**

Authentication is about verifying *who* the user is. The most common approaches I have worked with:

| Method | How it works | When I used it |
|--------|-------------|----------------|
| **JWT (JSON Web Token)** | User logs in → server issues a signed token → client sends it in every request header | REST APIs, stateless auth |
| **Session-based** | Server stores session in memory/DB, client holds a session cookie | Traditional web apps |
| **OAuth 2.0 / SSO** | Delegate login to a trusted provider (Google, Azure AD, Okta) | Enterprise apps, third-party login |
| **API Keys** | A static key sent in the header | Service-to-service calls, developer APIs |

> **Follow-up ready:** If asked about JWT specifically — *"A JWT has three parts: header (algorithm), payload (user data like ID and role), and signature (to verify it wasn't tampered). The server validates the signature on every request — no DB lookup needed, which makes it stateless and fast."*

---

### Q: Are you aware of SSO authentication?

**Yes. SSO stands for Single Sign-On — it means a user logs in once and gains access to multiple applications without logging in again for each one.**

**How it works (simple flow):**

```
User visits App A (e.g., your company portal)
    │
    └── Not logged in → redirected to Identity Provider (IdP)
              │         (e.g., Okta, Azure AD, Google)
              │
         User logs in once at the IdP
              │
         IdP issues a token (SAML assertion or OAuth token)
              │
         User is redirected back to App A with the token
              │
         App A validates the token → user is in ✅
              │
    Later, user visits App B (e.g., Jira, Slack, HR portal)
              │
         App B checks with same IdP → already logged in → token issued immediately
              │
         User enters App B without logging in again ✅
```

**Protocols used for SSO:**
- **SAML 2.0** — older, XML-based, common in enterprise (banks, hospitals)
- **OpenID Connect (OIDC)** — modern, built on top of OAuth 2.0, uses JWTs
- **OAuth 2.0** — technically for authorization, but commonly used as the base for SSO

> **One-liner:** *"SSO is like a hotel key card — you check in once at the front desk (IdP) and that card opens every door in the building (all apps)."*

---

### Q: What changes when an API becomes authenticated compared to an unauthenticated one?

**Several layers change — the client must send credentials on every request, and the server must validate them before processing anything.**

Here is the before and after:

```
UNAUTHENTICATED API:
────────────────────────────────────────────
Client → HTTP Request → Server → Response
  No token needed. Anyone can call it.
  No idea who is calling.

AUTHENTICATED API:
────────────────────────────────────────────
Client → HTTP Request
         + Authorization: Bearer <token>
              │
         Server middleware intercepts
              │
         Token validated? ──No──→ 401 Unauthorized
              │ Yes
         Who is this user? (extract ID, role from token)
              │
         Does this role have permission? ──No──→ 403 Forbidden
              │ Yes
         Process the request → Response
```

**Concrete changes that happen:**

| What changes | Unauthenticated | Authenticated |
|-------------|-----------------|---------------|
| Request headers | Nothing extra | `Authorization: Bearer <jwt_token>` |
| Server middleware | None | Auth middleware runs before every route |
| Error responses | No 401/403 | 401 if no token, 403 if wrong role |
| Logging | Anonymous requests | Logs include user ID |
| Rate limiting | By IP | By user account |
| CORS | May be open | Restricted to trusted origins |
| Data returned | Same for all | Filtered by what the user is allowed to see |

**In FastAPI, authentication is added as a dependency:**

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)           # validate JWT signature + expiry
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user

# BEFORE (unauthenticated) — anyone can call this
@app.get("/reports")
def get_reports():
    return all_reports()

# AFTER (authenticated) — only valid users
@app.get("/reports")
def get_reports(current_user = Depends(get_current_user)):
    return all_reports()
```

---

<a name="sso"></a>
## 🔑 SSO Integration

---

### Q: If you plan to integrate SSO-based authentication into an app, what changes do you need to make?

**You need to change four areas: the login flow, token handling, API middleware, and role/permission mapping.**

Here is the step-by-step breakdown:

**Step 1 — Register your app with the Identity Provider (IdP)**
- Go to Okta / Azure AD / Google and register your application
- You get back: `client_id`, `client_secret`, and the IdP's `authorization_url`
- Configure which redirect URL the IdP should send the user back to after login

**Step 2 — Replace your login screen**
```
BEFORE (your own login form):
  User fills email + password → your server checks DB → session/JWT issued

AFTER (SSO):
  User clicks "Login with Company SSO"
      → Browser redirects to IdP login page (e.g., company.okta.com)
      → User authenticates at IdP (with MFA if configured)
      → IdP redirects back to your app with an auth code
      → Your backend exchanges the code for an access token + ID token
      → Your app reads user identity from the ID token
```

**Step 3 — Add a callback endpoint to your backend**
```python
# FastAPI example — SSO callback handler
from authlib.integrations.starlette_client import OAuth

oauth = OAuth()
oauth.register(
    name='okta',
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    server_metadata_url='https://yourcompany.okta.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'}
)

@app.get("/auth/callback")
async def auth_callback(request: Request):
    token = await oauth.okta.authorize_access_token(request)
    user_info = token.get('userinfo')    # contains name, email, roles
    # Create session or issue your own JWT here
    return {"user": user_info}
```

**Step 4 — Update API middleware to validate SSO tokens**
- Every API request must carry the access token in the `Authorization` header
- Your middleware validates the token against the IdP's public keys (JWKS endpoint)
- No DB lookup needed — the token itself contains the user's identity and roles

**Step 5 — Map IdP roles to your app's permissions**
```python
# IdP sends roles like: ["admin", "viewer", "editor"]
# Map them to what your app understands

def get_permissions(sso_roles: list):
    role_map = {
        "admin":  ["read", "write", "delete", "manage_users"],
        "editor": ["read", "write"],
        "viewer": ["read"],
    }
    permissions = set()
    for role in sso_roles:
        permissions.update(role_map.get(role, []))
    return permissions
```

**Summary of what changes:**

| Area | Change needed |
|------|--------------|
| Login UI | Replace form with "Login with SSO" button |
| Backend auth routes | Add `/auth/login` redirect + `/auth/callback` handler |
| Token validation | Validate against IdP's JWKS (public keys), not your own secret |
| User table | May not need passwords anymore; store SSO user ID |
| Roles/permissions | Map IdP groups/roles to your app's permission model |
| Logout | Must also call IdP logout to end the SSO session |

---

<a name="realtime"></a>
## ⚡ Real-Time Communication

---

### Q: Apart from WebSockets and REST APIs, what other options are available to send real-time data to the UI?

**The main options are Server-Sent Events (SSE), Long Polling, and push notifications via a message broker.**

| Option | How it works | Best for |
|--------|-------------|---------|
| **Server-Sent Events (SSE)** | Server pushes data to browser over a single HTTP connection. One-way (server → client only) | Live feeds, dashboards, notifications |
| **Long Polling** | Client sends a request, server holds it open until data is available, then responds. Client immediately sends next request | Chat apps, older browser support needed |
| **WebHooks** | Server calls a URL when something happens (server-to-server, not browser) | Stripe payment events, GitHub push events |
| **WebSockets** | Full duplex, two-way persistent connection | Chat, games, collaborative editing |
| **Push Notifications** | Firebase FCM / APNs sends a message to device even when app is closed | Mobile alerts |

**SSE is the most underrated option — explain it well:**

```
SSE flow:
──────────────────────────────────────────────────────
Browser opens: GET /stream (one long HTTP connection)

Server sends events whenever it has data:
  data: {"price": 102.5}\n\n
  data: {"price": 103.1}\n\n

Browser receives each event and updates the UI — no polling needed.

Key difference from WebSocket:
  SSE = one-way (server pushes only)        → simpler, works over HTTP/1.1
  WebSocket = two-way (both sides send)     → more complex, needs upgrade handshake
```

```python
# FastAPI SSE example — live stock price feed
from fastapi.responses import StreamingResponse
import asyncio, json

@app.get("/stream/prices")
async def stream_prices():
    async def event_generator():
        prices = [100, 101, 102, 103]
        for price in prices:
            yield f"data: {json.dumps({'price': price})}\n\n"
            await asyncio.sleep(1)
    return StreamingResponse(event_generator(), media_type="text/event-stream")
```

> **One-liner:** *"For one-way server-to-client updates like dashboards or notifications, SSE is simpler than WebSockets and works over standard HTTP with no special infrastructure."*

---

### Q: What other communication services are available between modules (microservices)?

**Beyond REST APIs, services communicate via message queues, event streams, and RPC — each with different trade-offs.**

```
MODULE COMMUNICATION OPTIONS:
──────────────────────────────────────────────────────────────────
1. REST API (HTTP)
   Service A ──HTTP POST──→ Service B
   Synchronous. Simple. Service B must be up when A calls it.

2. Message Queue (e.g., RabbitMQ, SQS)
   Service A ──publish──→ Queue ──consume──→ Service B
   Asynchronous. B can be down; message waits in queue.
   One producer, one consumer per message.

3. Event Stream (e.g., Kafka)
   Service A ──publish──→ Kafka Topic ──consume──→ Service B, C, D
   Asynchronous. Multiple consumers can read the same event.
   Messages are stored and replayable. High throughput.

4. gRPC (Remote Procedure Call)
   Service A ──proto call──→ Service B
   Like a REST call but uses Protocol Buffers (binary, faster than JSON).
   Strongly typed, great for internal service-to-service calls.

5. GraphQL Subscriptions
   Client subscribes to a topic, server pushes updates in real time.
   Good when the UI needs fine-grained control over what data it receives.
```

| Option | Sync/Async | Best for |
|--------|-----------|---------|
| REST / HTTP | Synchronous | Simple request-response between services |
| Message Queue (RabbitMQ) | Async | Task queues, one consumer per job |
| Kafka | Async, persistent | Event streaming, audit logs, multiple consumers |
| gRPC | Synchronous | High-performance internal calls with strict contracts |
| GraphQL Subscriptions | Async | Real-time UI data with flexible queries |

---

<a name="kafka"></a>
## 📨 Kafka

---

### Q: Have you worked on Kafka?

**Yes. Kafka is a distributed event streaming platform — producers publish messages to topics, and consumers read from those topics.**

**Core concepts in plain English:**

```
KAFKA ARCHITECTURE:
──────────────────────────────────────────────────────────────────
  Producer              Kafka Broker             Consumer
(Service A)                  │                 (Service B, C)
    │                    Topic: "orders"              │
    └──publish──→   [partition 0] [partition 1] ──read──→ multiple consumers
                    [msg1][msg2]  [msg3][msg4]
                         │
                    Messages stored on disk
                    Retained for 7 days (configurable)
                    Consumers can replay from any point
```

**Key things to mention:**
- **Topic** — a named channel (like a table in a DB). e.g., `user-signups`, `order-events`
- **Partition** — a topic is split into partitions for parallelism and scalability
- **Consumer Group** — multiple instances of the same service can share a consumer group to divide work
- **Offset** — each message has an offset (position). Consumers track which offset they've read up to
- **Retention** — messages stay in Kafka for a configured time (default 7 days), even after being consumed — unlike a queue where messages are deleted after consumption

**When to use Kafka vs a REST call:**

| Use case | Better option |
|----------|--------------|
| Order placed → notify inventory, billing, shipping (fan-out) | Kafka |
| Simple request + response needed immediately | REST |
| Audit log of all events | Kafka |
| High throughput (millions of events/sec) | Kafka |
| Quick task queue with one consumer | RabbitMQ or SQS |

---

### Q: Are you aware OAuth can also be integrated with Kafka / backend communication?

**Yes. OAuth can be used to authenticate Kafka clients — so only authorised services can produce or consume from a topic.**

Normally you think of OAuth for user-facing APIs, but in a microservice setup, Kafka itself can be secured with OAuth tokens.

**How it works:**

```
SERVICE A wants to publish to Kafka:
──────────────────────────────────────────────────────────────────
1. Service A requests an access token from the OAuth server
   (using client_credentials grant — no user involved, service-to-service)

2. OAuth server validates Service A's client_id + client_secret
   and issues an access token

3. Service A includes the token when connecting to Kafka

4. Kafka's broker validates the token against the OAuth server

5. If valid and the token has the right scope (e.g., "kafka:write:orders"),
   the connection is allowed

6. Service A can now publish to the "orders" topic ✅
```

**Kafka uses SASL/OAUTHBEARER mechanism for this:**
```
# Kafka client config (Python kafka-python or confluent-kafka)
conf = {
    'bootstrap.servers': 'kafka-broker:9093',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'OAUTHBEARER',
    'oauth_cb': fetch_oauth_token   # function that gets a token from your IdP
}
```

> **Key point to say:** *"OAuth in Kafka is about service identity, not user identity. Each microservice has its own client_id and secret. The token it gets from the OAuth server proves 'I am the Order Service' and 'I am allowed to write to the orders topic.'"*

---

### Q: If Kafka is running on one VM and another VM reads from it, how would you secure the data transfer?

**You secure it at three layers: transport (TLS), authentication (SASL), and authorisation (ACLs).**

```
VM 1 (Kafka Broker)              VM 2 (Consumer Service)
──────────────────               ──────────────────────
Kafka running on                 Python app consuming
port 9093 (TLS)                  from Kafka topic

Security layers:

LAYER 1 — TRANSPORT (TLS/SSL)
  All data between VM1 and VM2 is encrypted in transit.
  VM2 connects to 9093 (SSL port), not 9092 (plain).
  Prevents anyone sniffing the network from reading the data.

LAYER 2 — AUTHENTICATION (SASL)
  VM2 must prove its identity before it can connect.
  Options:
    SASL/PLAIN     → username + password (simple, less secure)
    SASL/SCRAM     → hashed credentials (better)
    SASL/OAUTHBEARER → OAuth token (best for microservices)
    mTLS           → mutual TLS (both sides present certificates)

LAYER 3 — AUTHORISATION (ACLs)
  Even after authenticating, VM2 is only allowed to read from
  specific topics, not produce to all topics.
  
  Example ACL:
    consumer-service → READ on topic "orders"       ✅
    consumer-service → WRITE on topic "orders"      ❌ denied
    consumer-service → READ on topic "payments"     ❌ denied
```

**Summary of what you configure:**

| Security concern | Solution |
|-----------------|---------|
| Data encrypted in transit | TLS on port 9093 |
| Only authorised services connect | SASL (SCRAM or OAuth) |
| Services can only read/write their own topics | Kafka ACLs |
| Credentials not hardcoded | Environment variables / Vault / AWS Secrets Manager |
| Kafka broker certificate is trusted | CA certificate distributed to all clients |

> **One-liner:** *"TLS encrypts the data in transit, SASL proves who is connecting, and ACLs control what they're allowed to do — these three layers together make Kafka secure between VMs."*

---

<a name="redis"></a>
## 🔴 Redis

---

### Q: Are you aware of Redis?

**Yes. Redis is an in-memory data store — it keeps data in RAM so reads and writes are extremely fast (sub-millisecond).**

**What Redis is used for:**

| Use case | How Redis helps |
|----------|----------------|
| **Caching** | Store DB query results in Redis. Next request hits Redis instead of DB — much faster |
| **Session storage** | Store user sessions in Redis instead of in-memory or DB. Works across multiple server instances |
| **Rate limiting** | Count requests per user per minute using Redis counters with expiry |
| **Pub/Sub messaging** | Services publish events, other services subscribe — lightweight alternative to Kafka for simple cases |
| **Distributed locks** | Prevent two servers from processing the same job simultaneously |
| **Leaderboards / sorted sets** | Real-time ranking with sorted sets |
| **Job queues** | Background task queues (used by Celery + Redis in Python) |

**Simple mental model:**

```
Without Redis:
  User requests profile → API → DB query (50ms) → Response

With Redis cache:
  User requests profile → API → Redis check (1ms) → found? → Response ✅
                                                  → not found? → DB (50ms) → store in Redis → Response

50x faster on cache hit. DB protected from repeated queries.
```

> **Key difference from a database:** Redis stores data in memory — it's fast but not the primary source of truth. If the Redis server restarts, cache data can be lost (unless persistence is configured). You always have the real data in your primary DB.

---

<a name="oauth"></a>
## 🔒 OAuth 2.0

---

### Q: Have you used OAuth 2.0?

**Yes. OAuth 2.0 is an authorisation framework that lets one service act on behalf of a user or another service, without sharing passwords.**

**The four OAuth grant types (flows) — know these:**

```
1. AUTHORIZATION CODE (most common — for web/mobile apps with a user)
   User clicks "Login with Google"
   → Redirected to Google → logs in → Google sends back an auth code
   → Your backend exchanges code for access token (server-to-server)
   → Use token to call APIs on user's behalf

2. CLIENT CREDENTIALS (service-to-service, no user involved)
   Service A sends: client_id + client_secret → OAuth server
   OAuth server returns: access token
   Service A uses token to call Service B
   (Used for microservice authentication, Kafka auth, etc.)

3. IMPLICIT (deprecated — was used for SPAs, no longer recommended)

4. DEVICE CODE (for TVs, CLIs)
   Device shows a code → user enters it on phone → token issued
```

**What I have used it for:**
- Integrating "Login with Google / GitHub" into web apps (Authorization Code flow)
- Service-to-service authentication in microservice architecture (Client Credentials flow)
- Calling third-party APIs (Slack, GitHub, Stripe) that require OAuth tokens

---

### Q: With which microservice did you use OAuth 2.0?

**I used the Client Credentials flow for service-to-service authentication — for example, between an API Gateway and backend services, and between a notification service and a messaging API.**

A good way to explain this in an interview:

```
Example: API Gateway → Order Service

1. API Gateway is configured with its own client_id + client_secret

2. When it needs to call Order Service, it first goes to the Auth Server:
   POST /oauth/token
   { grant_type: "client_credentials", client_id: "...", client_secret: "..." }

3. Auth Server returns: { access_token: "eyJ...", expires_in: 3600 }

4. API Gateway calls Order Service with:
   GET /orders/123
   Authorization: Bearer eyJ...

5. Order Service validates the token (checks signature, expiry, scope)
   If valid → process the request
```

**Why this is better than shared API keys:**
- Tokens expire (e.g., after 1 hour) — stolen token has a short window
- Different scopes per service — Order Service token can't access Payment Service
- Centralised revocation — if a service is compromised, revoke its client credentials at the auth server

---

<a name="security"></a>
## 🏗️ Backend Security Design

---

### Q: If you have a plain unauthenticated FastAPI backend with no persona-based operations, how would you integrate authentication and persona-based access?

**This is a three-stage migration: add authentication, then add roles, then enforce permissions per endpoint.**

---

**Stage 1 — Add authentication (verify who the user is)**

Choose your auth method (JWT is most common for APIs):

```python
# 1. Add a login endpoint that issues a JWT
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt, datetime

SECRET_KEY = "your-secret"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

app = FastAPI()

@app.post("/auth/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    # Validate username + password against your DB
    user = authenticate_user(form.username, form.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Issue a JWT with user ID and role in the payload
    token = jwt.encode({
        "sub": str(user.id),
        "role": user.role,              # e.g., "admin", "editor", "viewer"
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    }, SECRET_KEY, algorithm="HS256")

    return {"access_token": token, "token_type": "bearer"}
```

---

**Stage 2 — Add a reusable dependency to extract the current user**

```python
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("sub")
        role = payload.get("role")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"id": user_id, "role": role}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
```

---

**Stage 3 — Add persona-based access (authorisation)**

```python
from functools import wraps

# Role permission map — define who can do what
ROLE_PERMISSIONS = {
    "admin":  ["read", "write", "delete", "manage_users"],
    "editor": ["read", "write"],
    "viewer": ["read"],
}

# Reusable permission checker — returns a FastAPI dependency
def require_permission(permission: str):
    def dependency(current_user = Depends(get_current_user)):
        user_permissions = ROLE_PERMISSIONS.get(current_user["role"], [])
        if permission not in user_permissions:
            raise HTTPException(
                status_code=403,
                detail=f"Role '{current_user['role']}' does not have '{permission}' permission"
            )
        return current_user
    return dependency
```

---

**Stage 4 — Update each endpoint with the right permission**

```python
# BEFORE — unauthenticated, anyone can call
@app.get("/reports")
def get_reports():
    return fetch_all_reports()

@app.post("/reports")
def create_report(data: ReportModel):
    return save_report(data)

@app.delete("/reports/{report_id}")
def delete_report(report_id: int):
    return remove_report(report_id)


# AFTER — each endpoint enforces its required permission
@app.get("/reports")
def get_reports(user = Depends(require_permission("read"))):
    return fetch_all_reports()           # viewers, editors, admins can read

@app.post("/reports")
def create_report(data: ReportModel, user = Depends(require_permission("write"))):
    return save_report(data)             # editors and admins can write

@app.delete("/reports/{report_id}")
def delete_report(report_id: int, user = Depends(require_permission("delete"))):
    return remove_report(report_id)     # only admins can delete
```

---

**Full picture — what the request flow looks like after all stages:**

```
Client Request: DELETE /reports/5
  Authorization: Bearer eyJ...

        │
        ▼
  oauth2_scheme extracts the token from the header
        │
        ▼
  get_current_user() decodes + validates JWT
  → user = { id: "42", role: "editor" }
        │
        ▼
  require_permission("delete") checks role permissions
  → editor has ["read", "write"] — "delete" is NOT in the list
        │
        ▼
  403 Forbidden: "Role 'editor' does not have 'delete' permission"
  Request never reaches the delete_report function ✅
```

**If integrating SSO instead of your own login:**

```
The only thing that changes is Stage 1 and Stage 2.
Stage 1 — replace your login endpoint with an SSO redirect
Stage 2 — instead of decoding your own JWT secret,
           validate the token against the IdP's public keys (JWKS endpoint)

Stages 3 and 4 (roles + permissions) stay exactly the same.
The IdP sends roles in the token payload — you just map them to your
ROLE_PERMISSIONS dict as before.
```

---

**Summary — migration checklist for an unauthenticated FastAPI app:**

```
□ 1. Add /auth/login endpoint (or SSO redirect + callback)
□ 2. Create get_current_user() dependency to validate every token
□ 3. Define ROLE_PERMISSIONS map for your personas (admin, editor, viewer)
□ 4. Create require_permission() dependency factory
□ 5. Add Depends(require_permission("...")) to every existing endpoint
□ 6. Add 401 / 403 error handlers for clean error responses
□ 7. Store roles in your DB (or read them from SSO token claims)
□ 8. Add token expiry + refresh token flow for long sessions
□ 9. Enable HTTPS (never send tokens over plain HTTP)
□ 10. Log all access attempts with user ID and action for audit trail
```

---

*Study tip: For each answer, practise saying the one-liner first, then expand. Interviewers appreciate when you give a crisp answer and then offer to go deeper.*