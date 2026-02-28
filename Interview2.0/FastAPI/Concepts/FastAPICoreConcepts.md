# ⚡ FastAPI Ultimate Interview Guide

> **Your complete reference to crack any Python FastAPI interview.**
> Read it once carefully. Glance through it before your interview. Built for beginners who want to become experts.

---

## 📖 Table of Contents

| # | Section | Level |
|---|---------|-------|
| 0 | [Visual Concept Diagrams](#diagrams) | 🖼️ All Levels |
| 1 | [What is an API & Why FastAPI?](#section-1) | ⭐ Beginner |
| 2 | [FastAPI Fundamentals](#section-2) | ⭐ Beginner |
| 3 | [Request Parameters (Path, Query, Body)](#section-3) | ⭐ Beginner |
| 4 | [Pydantic — Data Validation](#section-4) | ⭐⭐ Intermediate |
| 5 | [Async & Sync in FastAPI](#section-5) | ⭐⭐ Intermediate |
| 6 | [Dependency Injection](#section-6) | ⭐⭐ Intermediate |
| 7 | [Middleware](#section-7) | ⭐⭐ Intermediate |
| 8 | [Error Handling & HTTP Exceptions](#section-8) | ⭐⭐ Intermediate |
| 9 | [Security & Authentication](#section-9) | ⭐⭐⭐ Advanced |
| 10 | [Database Integration (SQLAlchemy)](#section-10) | ⭐⭐⭐ Advanced |
| 11 | [Background Tasks](#section-11) | ⭐⭐ Intermediate |
| 12 | [CORS](#section-12) | ⭐⭐ Intermediate |
| 13 | [File Uploads](#section-13) | ⭐⭐ Intermediate |
| 14 | [WebSockets](#section-14) | ⭐⭐⭐ Advanced |
| 15 | [API Documentation (Swagger / ReDoc)](#section-15) | ⭐ Beginner |
| 16 | [APIRouter — Structuring Large Apps](#section-16) | ⭐⭐ Intermediate |
| 17 | [Testing FastAPI](#section-17) | ⭐⭐ Intermediate |
| 18 | [Deployment & Production](#section-18) | ⭐⭐⭐ Advanced |
| 19 | [Quick Cheatsheet](#section-19) | 📌 Reference |
| 20 | [Interview Tips & Tricks](#section-20) | 🔥 Must Read |

---

## 🧠 How to Use This Guide

```
🎯 Night before interview:  Read sections 1–8 + Cheatsheet (Section 19)
🎯 Week before interview:   Read entire guide + try all code examples
🎯 During interview:        Use simple definitions first, then expand with examples
🎯 Memory trick:            Each section has a "1-liner" — memorise those first
```

---

<a name="section-1"></a>
## 📌 Section 1 — What is an API & Why FastAPI?

### 🔑 Core Definitions

**What is an API?**
> An API (Application Programming Interface) is a set of **endpoints on a server** that allow different applications to communicate with each other. Think of it as a **waiter in a restaurant** — you (the client) give your order (request) to the waiter (API), who takes it to the kitchen (server) and brings back your food (response).

```
Client App ──── Request ───► API Endpoint ───► Server Logic ───► Database
           ◄─── Response ─────────────────────────────────────────
```

**What is FastAPI?**
> FastAPI is a **modern, high-performance Python web framework** for building APIs with Python 3.7+, based on standard Python type hints. Its performance is **comparable to Node.js and Go**.

**One-liner for interview:** *"FastAPI is a fast, modern Python framework for building APIs with automatic validation, async support, and auto-generated documentation."*

---

### 🏆 Why FastAPI? Key Benefits

| Feature | Benefit |
|---------|---------|
| ⚡ High Performance | Built on Starlette + Pydantic — comparable to Go/Node.js |
| 📝 Auto Documentation | Swagger UI & ReDoc generated automatically |
| ✅ Auto Validation | Pydantic validates all request/response data |
| 🔄 Async Support | Native async/await for concurrent requests |
| 🔒 Built-in Security | OAuth2, JWT, API keys out of the box |
| 🐍 Type Hints | Better IDE support, fewer runtime bugs |
| 🧪 Easy Testing | Built-in TestClient with pytest |

---

### ⚖️ FastAPI vs Flask vs Django — The Big Comparison

```
┌─────────────┬──────────────────┬──────────────────┬──────────────────┐
│  Feature    │    FastAPI       │     Flask        │     Django       │
├─────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Type        │ API Framework    │ Micro Framework  │ Full-Stack       │
│ Speed       │ ⚡⚡⚡ Very Fast  │ ⚡⚡ Fast         │ ⚡ Moderate      │
│ Async       │ ✅ Native        │ ❌ Not built-in  │ ⚠️ Limited       │
│ Validation  │ ✅ Auto (Pydantic)│ ❌ Manual        │ ⚠️ Partial       │
│ ORM         │ ❌ Bring your own│ ❌ Bring your own│ ✅ Built-in      │
│ Admin Panel │ ❌               │ ❌               │ ✅ Built-in      │
│ Auto Docs   │ ✅ Swagger+ReDoc │ ❌               │ ❌               │
│ Best For    │ APIs/Microservices│ Small Apps       │ Full Web Apps    │
└─────────────┴──────────────────┴──────────────────┴──────────────────┘
```

> **Memory Trick:** "**F**astAPI = **F**ast APIs. **F**lask = **F**lexible small apps. **D**jango = **D**one for you (full stack)."

**When to choose what:**
- **FastAPI** → Building a REST API, microservice, or high-performance backend
- **Flask** → Small web app, prototype, full control over components
- **Django** → Full web application with admin, ORM, authentication all built in

---

### 🏗️ FastAPI Architecture — How It's Built

```
FastAPI Application
│
├── Built on STARLETTE (web/ASGI layer)
│   ├── Handles HTTP requests/responses
│   ├── WebSocket support
│   └── Middleware system
│
└── Built on PYDANTIC (data layer)
    ├── Data validation
    ├── Serialization (Python ↔ JSON)
    └── OpenAPI schema generation
```

**ASGI** = Asynchronous Server Gateway Interface (the modern standard replacing WSGI)

---

### 💡 Interview Tips for Section 1

> 🔥 **Hot tip:** Interviewers LOVE this question: *"Why would you choose FastAPI over Django REST Framework?"*
> **Answer:** FastAPI is faster, has native async, automatic Pydantic validation, auto-generated docs, and less boilerplate code. DRF needs manual serializers; FastAPI uses type hints.

---

<a name="section-2"></a>
## 📌 Section 2 — FastAPI Fundamentals

### 🔑 Installation & First App

```bash
# Install FastAPI + ASGI server
pip install fastapi uvicorn

# Run the app
uvicorn main:app --reload
# main = filename (main.py)
# app  = FastAPI() instance variable name
# --reload = auto-restart on code changes (dev only!)
```

### Hello World API

```python
from fastapi import FastAPI

app = FastAPI()   # Create the application instance

@app.get("/")              # Route decorator — HTTP method + path
def read_root():           # Handler function
    return {"message": "Hello, FastAPI! 🚀"}

# Access at: http://127.0.0.1:8000/
# Swagger UI: http://127.0.0.1:8000/docs
# ReDoc:      http://127.0.0.1:8000/redoc
```

---

### 📡 HTTP Methods — The CRUD Operations

> **Memory trick: CRUD = Create, Read, Update, Delete = POST, GET, PUT/PATCH, DELETE**

```
GET    → READ    → "Give me the data"        → /users, /users/1
POST   → CREATE  → "Create new data"         → /users
PUT    → UPDATE  → "Replace existing data"   → /users/1
PATCH  → UPDATE  → "Partially update data"   → /users/1
DELETE → DELETE  → "Remove this data"        → /users/1
```

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items")          # Get all items
def get_items():
    return [{"id": 1}, {"id": 2}]

@app.post("/items")         # Create new item
def create_item():
    return {"created": True}

@app.put("/items/{id}")     # Replace item
def update_item(id: int):
    return {"updated": id}

@app.delete("/items/{id}")  # Delete item
def delete_item(id: int):
    return {"deleted": id}
```

---

### 📊 HTTP Status Codes — Must Know

```
2xx = SUCCESS
  200 OK           → Standard successful response
  201 Created      → New resource created (POST)
  204 No Content   → Success but nothing to return (DELETE)

4xx = CLIENT ERROR (your fault)
  400 Bad Request  → Invalid data sent
  401 Unauthorized → Not logged in
  403 Forbidden    → Logged in but no permission
  404 Not Found    → Resource doesn't exist
  422 Unprocessable→ Validation failed (FastAPI default)

5xx = SERVER ERROR (server's fault)
  500 Internal Server Error → Something crashed on server
```

```python
# Setting custom status codes:
from fastapi import FastAPI
from fastapi import status  # import status constants

@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item():
    return {"created": True}

@app.delete("/items/{id}", status_code=204)
def delete_item(id: int):
    return None   # 204 = no content
```

---

### 💡 Interview Tips for Section 2

> 🔥 **Common question:** *"What is the difference between PUT and PATCH?"*
> **Answer:** PUT replaces the **entire** resource. PATCH updates **only the specified fields**. Example: PUT /user needs all fields; PATCH /user can send just `{"age": 30}`.

---

<a name="section-3"></a>
## 📌 Section 3 — Request Parameters

> **Big picture:** There are 3 ways to send data to a FastAPI endpoint — in the URL path, in the URL query string, or in the request body.

### 🗺️ Visual Overview

```
GET /users/42?active=true

     PATH ──► 42  (required, part of URL structure)
     QUERY──► active=true  (optional, filters/options)

POST /users
Body: {"name": "Alice", "age": 25}
     BODY ──► JSON data (complex objects)
```

---

### 1️⃣ Path Parameters — Required URL Values

> Path parameters are **part of the URL structure**, defined with `{curly_braces}`. They are always **required**.

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):   # type hint = auto validation!
    return {"user_id": user_id}

# URL: /users/42    → user_id = 42  ✓
# URL: /users/abc   → 422 Error! (not an int)
# URL: /users/      → 404 Not Found

# Multiple path params:
@app.get("/users/{user_id}/posts/{post_id}")
def get_post(user_id: int, post_id: int):
    return {"user": user_id, "post": post_id}
```

---

### 2️⃣ Query Parameters — Optional URL Filters

> Query parameters come **after the `?`** in the URL. They are **optional** (have default values) and used for filtering, sorting, pagination.

```python
@app.get("/items")
def get_items(
    skip: int = 0,          # default = 0
    limit: int = 10,        # default = 10
    active: bool = True     # default = True
):
    return {"skip": skip, "limit": limit, "active": active}

# URL: /items              → skip=0, limit=10, active=True
# URL: /items?skip=5       → skip=5, limit=10, active=True
# URL: /items?skip=5&limit=20  → skip=5, limit=20

# Making a query param REQUIRED (no default):
@app.get("/search")
def search(q: str):    # required! no default value
    return {"query": q}

# URL: /search        → 422 Error! (q is required)
# URL: /search?q=hello → OK
```

---

### 3️⃣ Request Body — Complex JSON Data

> Request body is used for **POST/PUT requests** when sending complex data (JSON objects). Define it with Pydantic models.

```python
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True   # optional with default

@app.post("/items")
def create_item(item: Item):   # FastAPI knows Item is a body param
    return {
        "name": item.name,
        "price": item.price,
        "in_stock": item.in_stock
    }

# Request body (JSON):
# {
#   "name": "Laptop",
#   "price": 999.99
# }
```

---

### 🔀 Combining All Three Types

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None

@app.put("/users/{user_id}/items/{item_id}")
def update_item(
    user_id: int,        # PATH parameter
    item_id: int,        # PATH parameter
    q: str = None,       # QUERY parameter (optional)
    item: Item = None    # BODY parameter (optional)
):
    result = {"user_id": user_id, "item_id": item_id}
    if q:
        result["q"] = q
    if item:
        result["item"] = item
    return result
```

> **Memory trick:**
> - In the URL **path**? → Path parameter
> - After the `?`? → Query parameter
> - In the **request body** (JSON)? → Body parameter (Pydantic model)

---

### 💡 Interview Tips for Section 3

> 🔥 **Common question:** *"How does FastAPI know if a parameter is a path, query, or body param?"*
> **Answer:** If it matches a `{name}` in the path → path param. If it's a simple type (int, str, bool) without a path match → query param. If it's a Pydantic BaseModel → body param.

---

<a name="section-4"></a>
## 📌 Section 4 — Pydantic: Data Validation

> **One-liner:** Pydantic uses Python type hints to automatically validate, parse, and serialize data — no manual checking needed.

### 🔑 Why Pydantic?

```
WITHOUT Pydantic:                    WITH Pydantic:
──────────────────                   ──────────────
def create_user(data: dict):         class UserCreate(BaseModel):
    name = data.get("name")              name: str
    if not name:                         age: int
        raise ValueError(...)            email: str
    age = data.get("age")
    if not isinstance(age, int):     @app.post("/users")
        raise ValueError(...)        def create_user(user: UserCreate):
    # ... 20 more lines                  # Already validated! ✓
```

---

### 📦 Pydantic BaseModel — The Foundation

```python
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class User(BaseModel):
    # Required fields (no default):
    username: str
    age: int

    # Optional fields (has default):
    email: Optional[str] = None
    is_active: bool = True

    # Field with validation rules:
    password: str = Field(
        ...,                    # ... means REQUIRED
        min_length=8,
        max_length=100,
        description="User password"
    )

    # Field with constraints:
    score: float = Field(default=0.0, ge=0.0, le=100.0)
    # ge = greater than or equal to
    # le = less than or equal to
    # gt = greater than
    # lt = less than

# Usage:
user = User(username="alice", age=25, password="secret123")
print(user.username)   # "alice"
print(user.is_active)  # True (default)
```

---

### 🔍 Pydantic Field Validators

```python
from pydantic import BaseModel, Field, field_validator

class Product(BaseModel):
    name: str
    price: float = Field(gt=0, description="Price must be positive")
    category: str

    @field_validator("name")
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("Name cannot be empty or whitespace")
        return v.title()   # Capitalise each word

    @field_validator("category")
    def category_must_be_valid(cls, v):
        valid = ["electronics", "clothing", "food"]
        if v.lower() not in valid:
            raise ValueError(f"Category must be one of: {valid}")
        return v.lower()

# Valid:
p = Product(name="laptop", price=999.99, category="Electronics")
print(p.name)      # "Laptop"  (title-cased)
print(p.category)  # "electronics" (lowercased)

# Invalid — raises ValidationError:
p = Product(name="", price=-10, category="cars")
```

---

### 🔄 Pydantic V1 vs V2 — Key Differences

| Feature | Pydantic V1 | Pydantic V2 |
|---------|------------|------------|
| Speed | Python implementation | Rust core (10x faster!) |
| Parse JSON | `.parse_obj(data)` | `.model_validate(data)` |
| To dict | `.dict()` | `.model_dump()` |
| To JSON | `.json()` | `.model_dump_json()` |
| Validator | `@validator` | `@field_validator` |
| ORM mode | `class Config: orm_mode=True` | `model_config = ConfigDict(from_attributes=True)` |

```python
# PYDANTIC V2 style:
from pydantic import BaseModel, ConfigDict

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # V2 way
    id: int
    name: str

# Parsing:
data = {"id": 1, "name": "Alice"}
user = UserOut.model_validate(data)    # V2: model_validate

# Serialising:
user.model_dump()         # V2: model_dump (was .dict() in V1)
user.model_dump_json()    # V2: model_dump_json
```

---

### 📋 Response Models — Control What Gets Returned

```python
class UserCreate(BaseModel):
    username: str
    password: str         # NEVER return this!
    email: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    # password NOT included — security!

@app.post("/users", response_model=UserOut)  # filters output!
def create_user(user: UserCreate):
    # Save to DB... (returns user with id)
    return {"id": 1, "username": user.username,
            "email": user.email, "password": "hidden"}
    # Even though password is in dict, it's filtered OUT
    # because response_model=UserOut doesn't have password
```

> **Interview tip:** `response_model` is a **security feature** — it ensures you never accidentally return sensitive fields like passwords or tokens.

---

### 🎯 Pydantic with Enums

```python
from enum import Enum
from pydantic import BaseModel

class Priority(str, Enum):   # str = values are strings
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Task(BaseModel):
    title: str
    priority: Priority = Priority.MEDIUM

@app.post("/tasks")
def create_task(task: Task):
    return task

# Valid:   {"title": "Fix bug", "priority": "high"}
# Invalid: {"title": "Fix bug", "priority": "urgent"} → 422 Error
```

---

### 💡 Interview Tips for Section 4

> 🔥 **Common question:** *"What happens if Pydantic validation fails?"*
> **Answer:** FastAPI automatically returns a `422 Unprocessable Entity` response with a detailed JSON error message showing exactly which field failed and why — no extra code needed.

> 🔥 **Common question:** *"What is `response_model` used for?"*
> **Answer:** It filters the response to only include specified fields. This is crucial for security (hiding passwords) and for controlling what the API consumer sees.

---


<a name="diagrams"></a>
## 🖼️ Visual Concept Diagrams

### Diagram 1 — FastAPI Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        FASTAPI APPLICATION                       │
│                                                                  │
│  ┌──────────────────────┐    ┌──────────────────────────────┐   │
│  │      STARLETTE        │    │          PYDANTIC             │   │
│  │   (Web/ASGI Layer)    │    │      (Data Layer)             │   │
│  │                       │    │                               │   │
│  │  • HTTP Routing        │    │  • Request Validation         │   │
│  │  • Middleware          │    │  • Response Serialization     │   │
│  │  • WebSockets          │    │  • Auto Documentation         │   │
│  │  • Static Files        │    │  • Type Enforcement           │   │
│  └──────────────────────┘    └──────────────────────────────┘   │
│                                                                  │
│  Runs on UVICORN (ASGI Server) — your app's engine               │
└─────────────────────────────────────────────────────────────────┘
```

### Diagram 2 — Request Lifecycle

```
  CLIENT SENDS REQUEST
         │
         ▼
  ┌─────────────────────────────────────────────────────┐
  │  MIDDLEWARE LAYER (runs for EVERY request)           │
  │  → CORS check → Logging → Auth → Timing              │
  └──────────────────────┬──────────────────────────────┘
                         │
                         ▼
  ┌─────────────────────────────────────────────────────┐
  │  URL ROUTING — match path + HTTP method to handler   │
  └──────────────────────┬──────────────────────────────┘
                         │
                         ▼
  ┌─────────────────────────────────────────────────────┐
  │  DEPENDENCY RESOLUTION — Depends() runs              │
  │  → DB session opened → Token verified                │
  └──────────────────────┬──────────────────────────────┘
                         │
                         ▼
  ┌─────────────────────────────────────────────────────┐
  │  PYDANTIC VALIDATION                                 │
  │  → Path params ✓  Query params ✓  Body JSON ✓        │
  │  → 422 returned automatically if invalid             │
  └──────────────────────┬──────────────────────────────┘
                         │
                         ▼
  ┌─────────────────────────────────────────────────────┐
  │  YOUR ROUTE HANDLER EXECUTES                         │
  └──────────────────────┬──────────────────────────────┘
                         │
                         ▼
  ┌─────────────────────────────────────────────────────┐
  │  RESPONSE SERIALISATION via response_model           │
  │  → Pydantic filters output → converts to JSON        │
  └──────────────────────┬──────────────────────────────┘
                         │
                         ▼
  ┌─────────────────────────────────────────────────────┐
  │  DEPENDENCY CLEANUP (yield teardown)                 │
  │  → DB session closed → Resources released            │
  └──────────────────────┬──────────────────────────────┘
                         │
                         ▼
  RESPONSE SENT TO CLIENT
                         │
                         ▼
  ┌─────────────────────────────────────────────────────┐
  │  BACKGROUND TASKS run AFTER response is sent         │
  └─────────────────────────────────────────────────────┘
```

### Diagram 3 — Async vs Sync vs Blocking

```
BLOCKING async def (❌ WRONG — time.sleep):
  Request 1: ████████████ (blocks all)
  Request 2:             ████████████ (forced to wait)
  Request 3:                         ████████████
  Time taken: 3x longer than needed!

NON-BLOCKING async def (✅ asyncio.sleep / await):
  Request 1: ████░░░░░░░░████  (░ = waiting, yields to loop)
  Request 2:      ████░░░████
  Request 3:           ████████
  Time taken: All complete in ~same time as 1 request!

REGULAR def (✅ runs in thread pool):
  Thread 1: ████████████
  Thread 2: ████████████  (parallel threads)
  Thread 3: ████████████
  Time taken: All run simultaneously in separate threads!
```

### Diagram 4 — Parameter Types

```
  REQUEST URL:  GET  /users/42?active=true&limit=5
                           │         │         │
                    ┌──────┘  ┌──────┘  ┌──────┘
                    │         │         │
               PATH PARAM  QUERY PARAM  QUERY PARAM
               (required)  (optional)   (optional)
               user_id=42  active=true  limit=5

  REQUEST BODY (POST/PUT only):
  {
    "name": "Alice",        ◄── BODY PARAM
    "email": "a@b.com",     ◄── (Pydantic BaseModel)
    "age": 25
  }
```

### Diagram 5 — Dependency Injection Flow

```
  @app.get("/users")
  async def get_users(db = Depends(get_db),           ─┐
                      user = Depends(get_current_user)):─┘
      # use db and user here                             │
                                                         │
  FastAPI automatically calls these BEFORE your handler:│
                                                         │
  ┌──────────────────────────────────────────────────┐   │
  │  1. get_db() called                               │◄──┤
  │     → opens DB session                           │   │
  │     → yields session to handler                  │   │
  │                                                   │   │
  │  2. get_current_user() called                     │◄──┘
  │     → reads token from header
  │     → validates token
  │     → returns user object
  │
  │  3. YOUR HANDLER runs with db + user ready
  │
  │  4. AFTER handler: db session closed (yield cleanup)
  └──────────────────────────────────────────────────┘
```

### Diagram 6 — Pydantic Model Inheritance Pattern

```
  ┌─────────────────────────────────┐
  │         UserBase                │  ← shared fields
  │   username: str                 │
  │   email: str                    │
  └────────────┬────────────────────┘
               │
       ┌───────┼───────────────┐
       │                       │
  ┌────▼──────────┐    ┌───────▼──────────┐
  │  UserCreate   │    │    UserOut        │
  │  (for POST)   │    │  (for response)   │
  │               │    │                  │
  │ + password    │    │ + id: int         │
  │ + (no id yet) │    │ + is_active: bool │
  └───────────────┘    │ - NO password!   │
                       └──────────────────┘
  ┌────────────────────┐
  │    UserUpdate       │  ← all optional for PATCH
  │  username?: str     │
  │  email?: str        │
  └────────────────────┘
```

### Diagram 7 — JWT Authentication Flow

```
  1. LOGIN:
     Client ──── POST /token {username, password} ────► FastAPI
     FastAPI verifies password ──────────────────────────────────┐
     FastAPI creates JWT token ◄─────────────────────────────────┘
     Client ◄─── {access_token: "eyJ...", type: "bearer"} ──── FastAPI

  2. USE TOKEN:
     Client ──── GET /profile + Header: "Authorization: Bearer eyJ..." ──► FastAPI
     FastAPI extracts token ──────────────────────────────────────────────────────┐
     FastAPI decodes + verifies JWT ◄────────────────────────────────────────────┘
     FastAPI returns user data ──────────────────────────────────────────────────►
     Client ◄─── {id: 1, username: "alice"} ──────────────────── FastAPI

  JWT TOKEN STRUCTURE:
  eyJhbGciOiJIUzI1NiJ9  .  eyJ1c2VyX2lkIjoxfQ  .  SflKxwRJSMeKKF2QT4fwp
  └────────────────────┘    └────────────────┘    └──────────────────────┘
       HEADER                    PAYLOAD               SIGNATURE
   (algorithm: HS256)        (user data +         (verifies nothing was
                               expiry time)              tampered with)
```

### Diagram 8 — Production Deployment Stack

```
  INTERNET
     │
     ▼
  ┌─────────────────────────────┐
  │  NGINX (Reverse Proxy)       │  ← HTTPS termination, load balancing
  │  Port 443 (HTTPS)            │    static files, rate limiting
  └──────────────┬──────────────┘
                 │
                 ▼
  ┌─────────────────────────────┐
  │  GUNICORN (Process Manager)  │  ← manages multiple worker processes
  └──────────────┬──────────────┘
                 │
        ┌────────┼────────┐
        │        │        │
  ┌─────▼──┐ ┌───▼───┐ ┌──▼─────┐
  │Uvicorn │ │Uvicorn│ │Uvicorn │  ← ASGI workers (2×CPU+1 recommended)
  │Worker 1│ │Worker │ │Worker N│
  └────────┘ └───────┘ └────────┘
        │        │        │
        └────────┼────────┘
                 │
                 ▼
  ┌─────────────────────────────┐
  │  POSTGRESQL DATABASE         │
  └─────────────────────────────┘
```

<a name="section-5"></a>
## 📌 Section 5 — Async & Sync in FastAPI

> **One-liner:** `async def` handles multiple requests concurrently (non-blocking). `def` runs in a separate thread (also fine but different mechanism).

### 🧠 The Big Picture — Why Async?

```
SYNCHRONOUS (blocking) — like a single-lane road:
Request 1 ──► [PROCESSING 3s] ──► Response
                                  Request 2 waits 3s...
                                                        Request 3 waits 6s...

ASYNCHRONOUS (non-blocking) — like a multi-lane highway:
Request 1 ──► [waiting for DB...] ──────────────────► Response
Request 2 ──────────► [waiting for DB...] ──────────► Response
Request 3 ──────────────────► [processing] ─────────► Response
               All handled CONCURRENTLY!
```

---

### 🔄 async def vs def — When to Use Which

```python
# Use ASYNC DEF for:
# - Database queries (with async ORM)
# - External API calls (httpx, aiohttp)
# - File I/O (aiofiles)
# - Any awaitable operation

@app.get("/users")
async def get_users():
    # Can use await here
    users = await db.execute(select(User))  # non-blocking!
    return users

# Use DEF for:
# - CPU-heavy calculations (image processing, ML inference)
# - Libraries that DON'T support async (old DB drivers)
# - Simple synchronous operations

@app.get("/calculate")
def calculate(n: int):
    # FastAPI runs this in a thread pool — doesn't block main thread
    result = heavy_calculation(n)
    return {"result": result}
```

---

### ⚠️ The Common Mistake — Blocking in Async

```python
import time
import asyncio

# ❌ WRONG — time.sleep BLOCKS the entire event loop!
@app.get("/wrong")
async def wrong_endpoint():
    time.sleep(5)   # Blocks ALL other requests for 5 seconds!
    return {"done": True}

# ✅ CORRECT — asyncio.sleep yields control to event loop
@app.get("/correct")
async def correct_endpoint():
    await asyncio.sleep(5)  # Other requests can run during wait
    return {"done": True}
```

---

### 📊 The 3 Concurrency Modes Summary

| Endpoint Type | How It Runs | Best For |
|--------------|-------------|----------|
| `async def` + `await` | Event loop (concurrent) | DB queries, API calls, I/O |
| `async def` + `time.sleep` | Sequential (blocks all!) | ❌ Never do this! |
| `def` (regular) | Thread pool (parallel) | CPU-heavy, sync libraries |

```python
# Real-world async example with multiple awaits:
import httpx

@app.get("/data")
async def get_combined_data():
    async with httpx.AsyncClient() as client:
        # Both requests fire at the same time!
        user_task = client.get("https://api.example.com/user")
        posts_task = client.get("https://api.example.com/posts")

        user_resp, posts_resp = await asyncio.gather(user_task, posts_task)

    return {
        "user": user_resp.json(),
        "posts": posts_resp.json()
    }
```

---

### 💡 Interview Tips for Section 5

> 🔥 **Classic trick question:** *"If I use `time.sleep` inside an `async def` endpoint, what happens?"*
> **Answer:** The entire event loop is blocked. ALL other concurrent requests are frozen until the sleep finishes. This completely defeats the purpose of async. Always use `await asyncio.sleep()` instead.

> 🔥 **Follow-up:** *"When should you use `def` instead of `async def`?"*
> **Answer:** When using libraries that don't support async (e.g., old database drivers, some ML libraries). FastAPI automatically runs `def` endpoints in a thread pool so they don't block the event loop either.

---

<a name="section-6"></a>
## 📌 Section 6 — Dependency Injection

> **One-liner:** Dependency Injection (DI) lets you define reusable logic once (like getting a DB session or checking auth) and automatically inject it into any route that needs it.

### 🧠 Understanding with a Simple Analogy

```
WITHOUT DI:                          WITH DI:
──────────                           ──────
@app.get("/users")                   def get_db():
def get_users():                         db = connect_to_db()
    db = connect_to_db()  ← repeated     yield db
    return db.query(User)                db.close()

@app.post("/users")                  @app.get("/users")
def create_user():                   def get_users(db = Depends(get_db)):
    db = connect_to_db()  ← repeated     return db.query(User)
    db.save(user)
                                     @app.post("/users")
                                     def create_user(db = Depends(get_db)):
                                         db.save(user)
```

---

### 🔧 Basic Dependency Example

```python
from fastapi import FastAPI, Depends

app = FastAPI()

# Step 1: Define the dependency function
def get_query_params(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# Step 2: Use it with Depends()
@app.get("/items")
def get_items(params: dict = Depends(get_query_params)):
    return {"params": params}

@app.get("/users")
def get_users(params: dict = Depends(get_query_params)):
    # Same pagination logic reused — DRY principle!
    return {"params": params}
```

---

### 🗄️ Database Session Dependency (Most Common Interview Example)

```python
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# THE DEPENDENCY — gets called for every request, cleaned up after
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session      # yield = give the session to the route
        # After yield: session is automatically closed!

# INJECT the dependency into routes:
@app.get("/users")
async def get_users(db: AsyncSession = Depends(get_db)):
    # db is already set up and ready to use
    result = await db.execute(select(User))
    return result.scalars().all()
    # db is automatically closed after this returns

@app.post("/users")
async def create_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_db)  # same dependency, fresh session
):
    db_user = User(**user.model_dump())
    db.add(db_user)
    await db.commit()
    return db_user
```

---

### 🔐 Authentication Dependency

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dependency: extracts and validates token
async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)   # your token verification logic
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    return user

# Protect any route by adding this dependency:
@app.get("/profile")
async def get_profile(current_user = Depends(get_current_user)):
    return current_user

@app.get("/settings")
async def get_settings(current_user = Depends(get_current_user)):
    return {"user": current_user}
```

---

### 🔗 Chained Dependencies (Dependencies of Dependencies)

```python
# Dependency 1 — get token from request
def get_token(token: str = Depends(oauth2_scheme)):
    return token

# Dependency 2 — depends on Dependency 1!
def get_current_user(token: str = Depends(get_token)):
    user = decode_token(token)
    return user

# Dependency 3 — depends on Dependency 2!
def get_admin_user(user = Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(403, "Admins only!")
    return user

# Route uses the final dependency — chain auto-resolves:
@app.delete("/users/{id}")
def delete_user(id: int, admin = Depends(get_admin_user)):
    # FastAPI automatically runs: get_token → get_current_user → get_admin_user
    pass
```

---

### 🧪 Overriding Dependencies in Tests

```python
# Real dependency (uses real DB):
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# Test override (uses test DB):
async def override_get_db():
    async with TestSessionLocal() as session:
        yield session

# In your test file:
from fastapi.testclient import TestClient

app.dependency_overrides[get_db] = override_get_db  # swap!
client = TestClient(app)

def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
```

---

### 💡 Interview Tips for Section 6

> 🔥 **Key question:** *"What is the difference between `yield` and `return` in a dependency?"*
> **Answer:** `return` gives the value once and that's it. `yield` gives the value AND allows cleanup code to run after the request finishes (after the `yield` line). This is perfect for DB sessions — open before yield, close after yield.

> 🔥 **Use cases to mention in interview:**
> - Database session management
> - Authentication and authorization
> - Rate limiting
> - Logging / audit trails
> - Configuration/settings injection
> - Pagination parameters

---

<a name="section-7"></a>
## 📌 Section 7 — Middleware

> **One-liner:** Middleware is a function that runs **before AND after** every single request — perfect for logging, timing, auth checks, and adding headers globally.

### 🧠 Visual Flow

```
Incoming Request
       │
       ▼
┌─────────────────┐
│   Middleware 1  │  ← runs BEFORE handler
│   (e.g., log)  │
└────────┬────────┘
         │
┌────────▼────────┐
│   Middleware 2  │  ← runs BEFORE handler
│   (e.g., auth) │
└────────┬────────┘
         │
┌────────▼────────┐
│  Route Handler  │  ← your endpoint function
└────────┬────────┘
         │
┌────────▼────────┐
│   Middleware 2  │  ← runs AFTER handler
└────────┬────────┘
         │
┌────────▼────────┐
│   Middleware 1  │  ← runs AFTER handler
└────────┬────────┘
         │
       Response
```

---

### 🔧 Creating Middleware

```python
from fastapi import FastAPI, Request
import time

app = FastAPI()

# Method 1: @app.middleware decorator (simplest)
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)   # ← run the actual endpoint

    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# Method 2: Class-based middleware (for complex logic)
from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print(f"Request: {request.method} {request.url}")
        response = await call_next(request)
        print(f"Response: {response.status_code}")
        return response

app.add_middleware(LoggingMiddleware)
```

---

### 🌟 Common Middleware Use Cases

```python
# 1. REQUEST LOGGING middleware:
@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"📥 {request.method} {request.url.path}")
    response = await call_next(request)
    print(f"📤 Status: {response.status_code}")
    return response

# 2. AUTHENTICATION middleware (check token on every request):
@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    # Skip auth for public routes:
    if request.url.path in ["/", "/docs", "/login"]:
        return await call_next(request)

    token = request.headers.get("Authorization")
    if not token:
        return JSONResponse({"error": "No token"}, status_code=401)

    return await call_next(request)

# 3. PERFORMANCE MONITORING:
@app.middleware("http")
async def monitor_performance(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    if duration > 1.0:   # alert if request takes over 1 second
        print(f"⚠️ SLOW REQUEST: {request.url.path} took {duration:.2f}s")
    return response
```

---

### ⚖️ Middleware vs Dependency Injection

```
MIDDLEWARE:
  - Runs for EVERY request (can't be selective)
  - Access to raw request/response
  - Good for: logging, timing, global headers
  - Runs OUTSIDE the route

DEPENDENCY INJECTION:
  - Runs only for specific routes (you choose)
  - Cleaner, more testable
  - Good for: auth, DB sessions, validation
  - Runs INSIDE the route context
```

---

### 💡 Interview Tips for Section 7

> 🔥 **Common question:** *"When would you use middleware instead of a dependency?"*
> **Answer:** Middleware when you need to process EVERY request globally (like logging response times). Dependency injection when you need selective, route-specific logic (like checking if a user is logged in for specific endpoints).

---

<a name="section-8"></a>
## 📌 Section 8 — Error Handling & HTTP Exceptions

> **One-liner:** Use `HTTPException` to return proper HTTP error codes. Use `@app.exception_handler` for custom global error handling.

### 🔧 Basic HTTPException

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

fake_db = {1: "Alice", 2: "Bob"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(
            status_code=404,        # HTTP status code
            detail="User not found" # Error message (returned in JSON)
        )
    return {"name": fake_db[user_id]}

# Response for /users/99:
# Status: 404 Not Found
# Body: {"detail": "User not found"}
```

---

### 🛡️ Custom Exception Classes

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Step 1: Define custom exception
class UserNotFoundException(Exception):
    def __init__(self, user_id: int):
        self.user_id = user_id

class InsufficientPermissionsError(Exception):
    def __init__(self, action: str):
        self.action = action

# Step 2: Register handlers
@app.exception_handler(UserNotFoundException)
async def user_not_found_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "error": "USER_NOT_FOUND",
            "message": f"User with ID {exc.user_id} does not exist",
            "path": str(request.url)
        }
    )

@app.exception_handler(InsufficientPermissionsError)
async def permissions_handler(request: Request, exc: InsufficientPermissionsError):
    return JSONResponse(
        status_code=403,
        content={"error": "FORBIDDEN", "action": exc.action}
    )

# Step 3: Raise in routes
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in fake_db:
        raise UserNotFoundException(user_id=user_id)  # clean!
    return {"name": fake_db[user_id]}
```

---

### 🌍 Global Exception Handler (Catch-All)

```python
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

# Handle Pydantic validation errors (422):
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "error": "VALIDATION_ERROR",
            "details": exc.errors(),   # detailed field-level errors
            "body": exc.body
        }
    )

# Handle ALL unhandled exceptions (safety net):
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "INTERNAL_SERVER_ERROR",
            "message": "Something went wrong"
            # Never expose the actual error in production!
        }
    )
```

---

### 💡 Interview Tips for Section 8

> 🔥 **Key question:** *"What is the difference between `HTTPException` and a custom exception handler?"*
> **Answer:** `HTTPException` is a quick way to return a specific HTTP status with a message for a single case. Custom exception handlers are registered globally and catch specific exception types thrown anywhere in your app — better for consistent, structured error responses across the whole API.

---

<a name="section-9"></a>
## 📌 Section 9 — Security & Authentication

> **One-liner:** FastAPI has built-in OAuth2, JWT, and API key support. Use `Depends` + `fastapi.security` for clean, reusable auth logic.

### 🔐 Authentication Methods Overview

```
METHOD          WHEN TO USE                  HOW IT WORKS
──────────────────────────────────────────────────────────
API Key         Simple, server-to-server      Key in header/query param
OAuth2 + JWT    User login, web/mobile apps   Login → token → use token
HTTP Basic      Very simple / legacy systems  Base64 username:password
OAuth2 + Cookie Browser-based SPAs            Token in httpOnly cookie
```

---

### 🎫 JWT Authentication — Full Implementation

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from pydantic import BaseModel

app = FastAPI()

# Config (in production, use environment variables!)
SECRET_KEY = "your-secret-key-keep-it-secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# ── MODELS ──────────────────────────────────────────
class User(BaseModel):
    username: str
    email: str
    disabled: bool = False

class Token(BaseModel):
    access_token: str
    token_type: str

# ── HELPER FUNCTIONS ────────────────────────────────
def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# ── DEPENDENCIES ────────────────────────────────────
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = get_user_from_db(username)   # your DB lookup
    if user is None:
        raise credentials_exception
    return user

# ── ROUTES ──────────────────────────────────────────
@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me")
async def get_my_profile(current_user = Depends(get_current_user)):
    return current_user  # Only accessible with valid token
```

---

### 🗝️ API Key Authentication

```python
from fastapi import Security
from fastapi.security import APIKeyHeader, APIKeyQuery

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)
api_key_query  = APIKeyQuery(name="api_key", auto_error=False)

VALID_API_KEYS = {"secret123", "myapikey456"}

async def get_api_key(
    header_key: str = Security(api_key_header),
    query_key:  str = Security(api_key_query),
):
    if header_key in VALID_API_KEYS:
        return header_key
    if query_key in VALID_API_KEYS:
        return query_key
    raise HTTPException(status_code=403, detail="Invalid API Key")

@app.get("/protected")
def protected_route(api_key: str = Depends(get_api_key)):
    return {"message": "You're in!", "key": api_key}
```

---

### 🛡️ Security Best Practices

```
✅ DO:
  - Store secrets in environment variables (.env files)
  - Hash passwords with bcrypt (NEVER store plain text!)
  - Use HTTPS in production
  - Set token expiry times (short-lived access tokens)
  - Use refresh tokens for long-lived sessions
  - Validate and sanitize all inputs

❌ DON'T:
  - Hardcode SECRET_KEY in source code
  - Return sensitive data in error messages
  - Use HTTP in production
  - Store passwords in plain text
  - Use * for CORS allow_origins in production
  - Log sensitive data like tokens or passwords
```

---

### 💡 Interview Tips for Section 9

> 🔥 **Common question:** *"What is JWT and how does it work?"*
> **Answer:** JWT (JSON Web Token) is a self-contained token with 3 parts: Header (algorithm), Payload (user data + expiry), Signature (verification). The server creates it at login and sends it to the client. Client sends it back with every request. Server verifies the signature — no DB lookup needed to check auth.

> **JWT = Header.Payload.Signature (Base64 encoded, dot-separated)**

---

<a name="section-10"></a>
## 📌 Section 10 — Database Integration (SQLAlchemy)

> **One-liner:** FastAPI has no built-in ORM. Use SQLAlchemy 2.0 with async support + dependency injection to manage DB sessions cleanly.

### 🏗️ Full Setup: FastAPI + SQLAlchemy 2.0 Async

```bash
pip install fastapi sqlalchemy[asyncio] aiosqlite asyncpg
# aiosqlite = async SQLite driver
# asyncpg   = async PostgreSQL driver
```

```python
# database.py — DB setup
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# SQLite (development):
DATABASE_URL = "sqlite+aiosqlite:///./app.db"

# PostgreSQL (production):
# DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False   # Don't expire objects after commit
)

class Base(DeclarativeBase):  # SQLAlchemy 2.0 style base
    pass
```

---

### 📋 Defining Models

```python
# models.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id       = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email    = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    # Relationship (one user has many posts):
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = "posts"

    id      = Column(Integer, primary_key=True, index=True)
    title   = Column(String, nullable=False)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("User", back_populates="posts")
```

---

### 🔌 DB Dependency + Startup

```python
# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import engine, AsyncSessionLocal, Base
from models import User

app = FastAPI()

# Create tables on startup:
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# THE DB DEPENDENCY — reused in every route:
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session          # ← session handed to route
        # After route finishes: session automatically closed/committed
```

---

### 📝 CRUD Operations

```python
from sqlalchemy import select
from fastapi import HTTPException

# CREATE:
@app.post("/users", response_model=UserOut, status_code=201)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = User(**user.model_dump())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)   # reload from DB to get generated id
    return db_user

# READ ALL:
@app.get("/users")
async def get_all_users(
    skip: int = 0, limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(User).offset(skip).limit(limit))
    return result.scalars().all()

# READ ONE:
@app.get("/users/{user_id}", response_model=UserOut)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# UPDATE:
@app.put("/users/{user_id}", response_model=UserOut)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    for field, value in user_update.model_dump(exclude_unset=True).items():
        setattr(user, field, value)

    await db.commit()
    await db.refresh(user)
    return user

# DELETE:
@app.delete("/users/{user_id}", status_code=204)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await db.delete(user)
    await db.commit()
```

---

### 🔗 Pydantic ↔ SQLAlchemy Bridge

```python
# schemas.py — Pydantic models for API
from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):   # for incoming POST requests
    password: str

class UserUpdate(BaseModel):  # for PATCH requests (all optional)
    username: str | None = None
    email: str | None = None

class UserOut(UserBase):      # for responses (no password!)
    model_config = ConfigDict(from_attributes=True)  # CRITICAL!
    # from_attributes=True tells Pydantic to read from ORM object attributes
    id: int
    is_active: bool
```

> **Critical note:** `from_attributes=True` (formerly `orm_mode=True` in V1) is **required** to convert SQLAlchemy ORM objects into Pydantic models. Without it, you'll get a validation error.

---

### 💡 Interview Tips for Section 10

> 🔥 **Common question:** *"Why do we use `yield` instead of `return` in the DB dependency?"*
> **Answer:** `yield` allows the cleanup code (closing the session) to run AFTER the request handler finishes. With `return`, you'd have no way to close the session cleanly after use. `yield` is basically a try/finally block.

> 🔥 **Key concept to mention:** Always use `expire_on_commit=False` in async SQLAlchemy. Without it, accessing attributes after `commit()` triggers a sync DB call which breaks async context.

---

<a name="section-11"></a>
## 📌 Section 11 — Background Tasks

> **One-liner:** Background tasks run AFTER the response is sent — perfect for sending emails, notifications, or logging without making the user wait.

### 🔧 Basic Background Task

```python
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

# Step 1: Define the task function (runs in background)
def send_welcome_email(email: str, username: str):
    # This runs AFTER the response is already sent to client
    print(f"Sending welcome email to {email}...")
    # email_client.send(to=email, subject="Welcome!", body=...)
    print(f"Email sent to {username}!")

# Step 2: Inject BackgroundTasks and add your task
@app.post("/register")
async def register_user(
    user: UserCreate,
    background_tasks: BackgroundTasks   # inject BackgroundTasks
):
    # Save user to DB...
    new_user = save_user(user)

    # Schedule email for AFTER response:
    background_tasks.add_task(
        send_welcome_email,      # function to run
        email=user.email,        # arguments
        username=user.username
    )

    return {"message": "Registered successfully!"}
    # Response sends immediately — email runs in background!
```

---

### 📊 Background Tasks vs Celery

```
FASTAPI BackgroundTasks:           CELERY + Redis/RabbitMQ:
─────────────────────────         ──────────────────────────
✅ Simple, no extra setup         ✅ Distributed, scalable
✅ Same process as app            ✅ Survives app restarts
✅ Great for lightweight tasks    ✅ Great for heavy workloads
❌ Dies if app crashes            ✅ Retry logic built-in
❌ Can't distribute across nodes  ✅ Can run on separate servers
❌ No task monitoring             ✅ Flower dashboard for monitoring

USE BackgroundTasks for: emails, logs, notifications (lightweight)
USE Celery for: video processing, bulk emails, complex pipelines
```

---

### 🔧 Multiple Background Tasks

```python
@app.post("/order")
async def create_order(
    order: OrderCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    # Create order in DB...
    new_order = await save_order(order, db)

    # Schedule multiple tasks — all run after response:
    background_tasks.add_task(send_order_confirmation, order.email, new_order.id)
    background_tasks.add_task(update_inventory, order.items)
    background_tasks.add_task(log_order_analytics, new_order)
    background_tasks.add_task(notify_warehouse, new_order)

    return {"order_id": new_order.id, "status": "confirmed"}
```

---

<a name="section-12"></a>
## 📌 Section 12 — CORS (Cross-Origin Resource Sharing)

> **One-liner:** CORS controls which external domains (like your React frontend) are allowed to call your FastAPI backend. Without it, browsers block cross-domain requests.

### 🧠 Why CORS Exists

```
Without CORS headers:
React app at http://localhost:3000
    calls → FastAPI at http://localhost:8000
         ← Browser BLOCKS response! (different origin = security risk)

With CORS headers:
React app at http://localhost:3000
    calls → FastAPI at http://localhost:8000
         ← ALLOWED! (FastAPI says "yes, 3000 is allowed")
```

---

### 🔧 Adding CORS Middleware

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# DEVELOPMENT — allow everything (⚠️ not for production!):
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # allow ALL origins
    allow_credentials=True,
    allow_methods=["*"],          # allow ALL methods
    allow_headers=["*"],          # allow ALL headers
)

# PRODUCTION — be specific:
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://myapp.com",
        "https://www.myapp.com",
        "http://localhost:3000",  # your frontend (dev only)
    ],
    allow_credentials=True,      # allow cookies/auth headers
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)
```

---

### 💡 Interview Tips for Section 12

> 🔥 **Common question:** *"What is CORS and why is it important?"*
> **Answer:** CORS is a browser security mechanism that blocks cross-origin requests by default. Your API must explicitly say which frontend domains are allowed. Using `allow_origins=["*"]` in production is a security risk — always specify exact origins.

---

<a name="section-13"></a>
## 📌 Section 13 — File Uploads

> **One-liner:** Use `UploadFile` for file uploads — it handles large files efficiently with streaming and async reading.

### 🔧 Single File Upload

```python
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {
        "filename":     file.filename,
        "content_type": file.content_type,
        "size":         file.size
    }

# Save uploaded file:
@app.post("/upload/save")
async def save_file(file: UploadFile = File(...)):
    save_path = f"uploads/{file.filename}"

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)   # efficient streaming copy

    return {"saved": save_path}

# Read file content:
@app.post("/upload/read")
async def read_file(file: UploadFile = File(...)):
    contents = await file.read()   # async read into memory
    return {"content": contents.decode("utf-8"), "size": len(contents)}
```

---

### 🔧 Multiple File Upload

```python
from typing import List

@app.post("/upload/multiple")
async def upload_multiple(files: List[UploadFile] = File(...)):
    results = []
    for file in files:
        results.append({
            "filename": file.filename,
            "size": file.size,
            "type": file.content_type
        })
    return {"files": results, "count": len(files)}
```

---

### 🔒 File Validation with Pydantic

```python
from fastapi import HTTPException

ALLOWED_IMAGE_TYPES = ["image/jpeg", "image/png", "image/gif", "image/webp"]
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

@app.post("/upload/image")
async def upload_image(file: UploadFile = File(...)):
    # Validate type:
    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Allowed: {ALLOWED_IMAGE_TYPES}"
        )

    # Validate size:
    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"File too large. Max size: {MAX_FILE_SIZE / 1024 / 1024}MB"
        )

    # Process the image...
    return {"filename": file.filename, "size": len(contents)}
```

---

<a name="section-14"></a>
## 📌 Section 14 — WebSockets

> **One-liner:** WebSockets enable real-time, two-way communication between client and server — perfect for chat apps, live notifications, and dashboards.

### 🧠 HTTP vs WebSocket

```
HTTP (Request-Response):
Client ──► Request  ──► Server
       ◄── Response ◄──
       (connection closed after each exchange)

WebSocket (Persistent Connection):
Client ◄──────────────────── Server
       ──────────────────────►
       (connection stays open, both sides can send anytime)
```

---

### 🔧 Basic WebSocket

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()   # accept the connection

    try:
        while True:
            data = await websocket.receive_text()        # wait for message
            await websocket.send_text(f"Echo: {data}")  # send reply
    except WebSocketDisconnect:
        print("Client disconnected")
```

---

### 💬 Chat Room — Managing Multiple Connections

```python
from typing import List

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/chat/{username}")
async def chat_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket)
    await manager.broadcast(f"🟢 {username} joined the chat")

    try:
        while True:
            message = await websocket.receive_text()
            await manager.broadcast(f"{username}: {message}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"🔴 {username} left the chat")
```

---

<a name="section-15"></a>
## 📌 Section 15 — API Documentation

> **One-liner:** FastAPI auto-generates interactive documentation at `/docs` (Swagger UI) and `/redoc` (ReDoc) — no extra work needed!

### 📚 Swagger UI vs ReDoc

```
SWAGGER UI (/docs):                 REDOC (/redoc):
────────────────────                ──────────────────
✅ Interactive — test endpoints     ✅ Beautiful, structured design
✅ "Try it out" button              ✅ Better for large, complex APIs
✅ Shows request/response format    ✅ Nested menu navigation
✅ Auth integration (lock icon)     ✅ Detailed specification view
Best for: developers during dev     Best for: sharing with external teams
```

---

### 🔧 Customising Documentation

```python
from fastapi import FastAPI

app = FastAPI(
    title="My Awesome API",
    description="""
    ## Features
    - User management
    - Product catalog
    - Order processing
    """,
    version="1.0.0",
    contact={
        "name": "Developer",
        "email": "dev@example.com"
    },
    license_info={
        "name": "MIT"
    }
)

# Document individual routes:
@app.get(
    "/users/{user_id}",
    summary="Get a user by ID",
    description="Retrieves a specific user by their unique ID.",
    response_description="The user object",
    tags=["Users"]      # groups routes in docs
)
def get_user(user_id: int):
    """
    Get a user with full details:
    - **user_id**: The unique identifier
    Returns the complete user profile.
    """
    pass
```

---

<a name="section-16"></a>
## 📌 Section 16 — APIRouter: Structuring Large Apps

> **One-liner:** `APIRouter` lets you split a large FastAPI app into multiple files, each handling a specific feature (users, products, orders).

### 🏗️ Project Structure

```
my_app/
├── main.py            ← app entry point
├── database.py        ← DB setup
├── models.py          ← SQLAlchemy models
├── schemas.py         ← Pydantic models
└── routers/
    ├── users.py       ← /users routes
    ├── products.py    ← /products routes
    └── orders.py      ← /orders routes
```

---

### 🔧 Router Setup

```python
# routers/users.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db

router = APIRouter(
    prefix="/users",           # all routes start with /users
    tags=["Users"],            # group in docs
    responses={404: {"description": "Not found"}}
)

@router.get("/")               # full path: GET /users/
async def get_users(db: AsyncSession = Depends(get_db)):
    pass

@router.get("/{user_id}")      # full path: GET /users/42
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    pass

@router.post("/")              # full path: POST /users/
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    pass
```

```python
# main.py
from fastapi import FastAPI
from routers import users, products, orders

app = FastAPI()

# Register all routers:
app.include_router(users.router)
app.include_router(products.router, prefix="/api/v1")  # version prefix
app.include_router(orders.router)
```

---

<a name="section-17"></a>
## 📌 Section 17 — Testing FastAPI

> **One-liner:** Use `TestClient` from FastAPI (based on httpx) to write tests for your routes — synchronous tests for sync+async endpoints.

### 🧪 Basic Tests

```python
# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test GET endpoint:
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}

# Test POST with body:
def test_create_user():
    response = client.post(
        "/users",
        json={"username": "alice", "email": "alice@example.com", "password": "pass123"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "alice"
    assert "password" not in data   # password should be hidden!

# Test 404:
def test_user_not_found():
    response = client.get("/users/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

# Test validation error:
def test_invalid_data():
    response = client.post("/users", json={"username": ""})  # missing required fields
    assert response.status_code == 422

# Test with authentication:
def test_protected_route():
    # Without token — should fail:
    response = client.get("/profile")
    assert response.status_code == 401

    # With token — should succeed:
    response = client.get(
        "/profile",
        headers={"Authorization": "Bearer your-test-token"}
    )
    assert response.status_code == 200
```

---

### 🧪 Testing with Dependency Overrides

```python
import pytest
from fastapi.testclient import TestClient
from main import app
from database import get_db

# Setup test DB:
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

TEST_DATABASE_URL = "sqlite+aiosqlite:///./test.db"
test_engine = create_async_engine(TEST_DATABASE_URL)
TestSessionLocal = sessionmaker(test_engine, class_=AsyncSession, expire_on_commit=False)

# Override the DB dependency:
async def override_get_db():
    async with TestSessionLocal() as session:
        yield session

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

@pytest.fixture(autouse=True)
async def setup_db():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
```

---

<a name="section-18"></a>
## 📌 Section 18 — Deployment & Production

> **One-liner:** Deploy FastAPI with Uvicorn/Gunicorn behind Nginx, containerised with Docker. Use env vars for secrets.

### 🚀 Production Stack

```
Internet ──► Nginx (reverse proxy, SSL)
                 │
                 ▼
            Gunicorn (process manager)
            ├── Uvicorn worker 1  ┐
            ├── Uvicorn worker 2  │ → FastAPI app
            └── Uvicorn worker N  ┘
                 │
                 ▼
            PostgreSQL Database
```

---

### 🐳 Docker Setup

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies first (Docker layer caching):
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code:
COPY . .

# Run with Uvicorn:
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```yaml
# docker-compose.yml
version: "3.8"
services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql+asyncpg://user:pass@db/mydb
      - SECRET_KEY=your-secret-key
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

---

### ⚙️ Production Uvicorn Command

```bash
# Single worker (dev):
uvicorn main:app --reload

# Multiple workers (production):
uvicorn main:app --workers 4 --host 0.0.0.0 --port 8000

# With Gunicorn (recommended for production):
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
# -w 4 = 4 worker processes (rule of thumb: 2 × CPU cores + 1)
```

---

### 🔒 Environment Variables

```python
# config.py — settings management with Pydantic
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"   # reads from .env file automatically

settings = Settings()  # auto-reads from environment

# Use in app:
from config import settings
engine = create_async_engine(settings.database_url)
```

```bash
# .env file (NEVER commit to git!):
DATABASE_URL=postgresql+asyncpg://user:password@localhost/mydb
SECRET_KEY=super-secret-random-string-here
DEBUG=false
```

---

### 💡 Production Checklist

```
Before deploying to production:
  ☑ Set DEBUG=false
  ☑ All secrets in environment variables
  ☑ HTTPS enabled (SSL certificate)
  ☑ CORS configured with specific origins (not *)
  ☑ Rate limiting enabled
  ☑ Database connection pooling configured
  ☑ Logging configured (structured JSON logs)
  ☑ Health check endpoint (/health)
  ☑ Error monitoring (Sentry, etc.)
  ☑ Gunicorn with multiple Uvicorn workers
  ☑ Nginx as reverse proxy
```

---

<a name="section-19"></a>
## 📌 Section 19 — Quick Cheatsheet

### ⚡ 30-Second Answers — Memorise These

| Question | One-Line Answer |
|----------|----------------|
| What is FastAPI? | Modern, fast Python framework for building APIs with type hints, auto-validation, auto-docs |
| FastAPI vs Flask? | FastAPI: async, auto-validation, auto-docs. Flask: lightweight, no built-in validation |
| FastAPI vs Django? | Django: full-stack, batteries included. FastAPI: API-only, faster, async-first |
| What is Pydantic? | Python library for data validation using type hints — core of FastAPI's validation |
| What is Uvicorn? | ASGI server that runs FastAPI — like the engine that powers the app |
| What is ASGI? | Asynchronous Server Gateway Interface — modern standard for Python web servers |
| What is `Depends`? | FastAPI's dependency injection system — inject reusable logic into any route |
| What is a response_model? | Pydantic model that filters/shapes what the API returns — security + consistency |
| async def vs def? | async def: concurrent via event loop. def: parallel via thread pool |
| What is CORS? | Browser security allowing specific domains to call your API |
| What are background tasks? | Functions that run after response is sent — emails, logs, notifications |
| What is JWT? | JSON Web Token — self-contained auth token with header, payload, signature |
| What is OAuth2? | Standard auth framework — FastAPI has built-in support via fastapi.security |
| Pydantic V1 vs V2? | V2: Rust-powered (10x faster), `.model_validate()` instead of `.parse_obj()` |
| What is APIRouter? | Groups related routes into separate files for cleaner code organisation |
| What is middleware? | Function that runs before/after every request — logging, timing, global auth |
| What is `yield` in dependency? | Allows cleanup code (DB session close) to run after request finishes |
| How to test FastAPI? | Use TestClient + `dependency_overrides` to inject test dependencies |

---

### 🗺️ FastAPI Request Lifecycle

```
Client sends request
       │
       ▼
┌──────────────────────────────────────────────┐
│  MIDDLEWARE STACK (runs for EVERY request)    │
│  - CORS check                                 │
│  - Logging                                    │
│  - Timing                                     │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│  ROUTE MATCHING                               │
│  URL + HTTP method → find the right function  │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│  DEPENDENCY RESOLUTION (Depends())            │
│  - DB session opened                          │
│  - Auth token verified                        │
│  - Other dependencies resolved                │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│  PYDANTIC VALIDATION                          │
│  - Path params validated                      │
│  - Query params validated                     │
│  - Request body validated                     │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│  YOUR ROUTE HANDLER RUNS                      │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│  RESPONSE SERIALISATION (response_model)      │
│  - Output filtered through response_model     │
│  - Converted to JSON                          │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│  DEPENDENCY CLEANUP (yield dependencies)      │
│  - DB session closed                          │
│  - Resources released                         │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
         Response sent to client
                   │
                   ▼
┌──────────────────────────────────────────────┐
│  BACKGROUND TASKS (if any)                    │
│  Run AFTER response is already sent           │
└──────────────────────────────────────────────┘
```

---

### 🏗️ Minimal Production-Ready App

```python
# main.py — complete minimal FastAPI app
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI(title="My API", version="1.0.0")

# CORS:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://myfrontend.com"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# SCHEMA:
class ItemCreate(BaseModel):
    name: str
    price: float

class ItemOut(ItemCreate):
    id: int
    class Config:
        from_attributes = True

# ROUTES:
@app.get("/health")             # health check
def health():
    return {"status": "ok"}

@app.get("/items", response_model=list[ItemOut])
async def get_items(db: AsyncSession = Depends(get_db)):
    pass   # your implementation

@app.post("/items", response_model=ItemOut, status_code=201)
async def create_item(item: ItemCreate, db: AsyncSession = Depends(get_db)):
    pass   # your implementation
```

---

### 🔧 Common Patterns Quick Reference

```python
# PATH PARAMETER:
@app.get("/items/{item_id}")
def f(item_id: int): pass

# QUERY PARAMETER (optional):
@app.get("/items")
def f(skip: int = 0, limit: int = 10): pass

# REQUEST BODY:
@app.post("/items")
def f(item: ItemCreate): pass   # Pydantic model = body

# INJECT DEPENDENCY:
@app.get("/items")
def f(db = Depends(get_db)): pass

# PROTECT WITH AUTH:
@app.get("/me")
def f(user = Depends(get_current_user)): pass

# BACKGROUND TASK:
@app.post("/notify")
def f(bt: BackgroundTasks):
    bt.add_task(send_email, "user@email.com")

# RAISE HTTP ERROR:
raise HTTPException(status_code=404, detail="Not found")

# CUSTOM STATUS CODE:
@app.post("/items", status_code=201)
def f(): pass

# RESPONSE MODEL (filter output):
@app.get("/users", response_model=UserOut)
def f(): pass
```

---

<a name="section-20"></a>
## 📌 Section 20 — Interview Tips, Tricks & Study Strategy

### 🎯 Most Likely Interview Questions by Level

#### 🟢 Beginner Questions (Always Asked)
1. What is FastAPI and why would you use it?
2. What is the difference between FastAPI, Flask, and Django?
3. How do you define a GET/POST endpoint in FastAPI?
4. What is Pydantic and why is it used?
5. What is path vs query vs body parameter?
6. What are HTTP methods and status codes?
7. How do you run a FastAPI app?
8. What is Swagger UI and where does it appear?

#### 🟡 Intermediate Questions (Common)
9. What is Dependency Injection and why is it useful?
10. What is the difference between `async def` and `def` in FastAPI?
11. What is middleware and when would you use it?
12. How do you handle exceptions in FastAPI?
13. What is CORS and how do you configure it?
14. What is `response_model` and why is it important?
15. What is `yield` in a dependency function?
16. How do you validate request data beyond type hints?
17. What is `Depends()` and how does it work?
18. How do you implement pagination?

#### 🔴 Advanced Questions (Senior/Experienced)
19. How do you integrate FastAPI with SQLAlchemy async?
20. How do you implement JWT authentication?
21. How would you structure a large FastAPI application?
22. How do you write tests for FastAPI with dependency overrides?
23. What is the difference between FastAPI BackgroundTasks and Celery?
24. How do you deploy FastAPI in production?
25. What is Pydantic V2 and how is it different from V1?
26. How do you implement rate limiting?
27. How would you implement WebSockets in FastAPI?

---

### 🧠 Memory Tricks — Remember These

```
FastAPI = Starlette + Pydantic
  Starlette → web layer (routing, middleware, WebSockets)
  Pydantic  → data layer (validation, serialization)

HTTP Methods = CRUD
  POST   → CREATE
  GET    → READ
  PUT    → UPDATE (full replacement)
  PATCH  → UPDATE (partial)
  DELETE → DELETE

Parameters — how to remember them:
  PATH   → "the address tells you exactly what" (required)
  QUERY  → "questions after the ?" (optional filters)
  BODY   → "the letter in the envelope" (JSON data)

Pydantic V2 new names:
  .dict()        → .model_dump()
  .parse_obj()   → .model_validate()
  orm_mode=True  → from_attributes=True

Dependency yield trick:
  yield = "give it, then clean up after"
  return = "give it once, done"

Status codes:
  200 = OK (all good)
  201 = Created (new thing made)
  204 = No Content (success, nothing to say)
  400 = Bad Request (you sent bad data)
  401 = Unauthorized (not logged in)
  403 = Forbidden (logged in but no permission)
  404 = Not Found (thing doesn't exist)
  422 = Unprocessable (validation failed — FastAPI default)
  500 = Server Error (something crashed)
```

---

### 💬 How to Answer Interview Questions — Structure

**The DECS framework (Definition → Example → Comparison → Scenario):**

```
Q: "What is Dependency Injection in FastAPI?"

D - DEFINITION:
"Dependency Injection is a design pattern where reusable logic
(like getting a DB session or verifying a user) is defined once
and FastAPI automatically injects it into any route that declares it
using the Depends() function."

E - EXAMPLE:
"For example, I define a get_db() function that opens a database session
and yields it. Then any route that needs the DB just adds
db: AsyncSession = Depends(get_db) as a parameter."

C - COMPARISON:
"Without DI, you'd copy-paste the DB setup code into every route.
With DI, you write it once and reuse it everywhere — DRY principle."

S - SCENARIO:
"In a real app, I use DI for: DB sessions, auth checking,
pagination parameters, and rate limiting logic."
```

---

### 🚀 5 Things That Impress Interviewers

1. **Mention `yield` vs `return` in dependencies** — shows deep understanding
2. **Explain `from_attributes=True`** — shows you understand Pydantic ↔ SQLAlchemy bridge
3. **Talk about `response_model` as a security feature** — not just convenience
4. **Know when to use `def` vs `async def`** — the `time.sleep` gotcha is a classic trap
5. **Mention `dependency_overrides` for testing** — shows production mindset

---

### ⚡ Last-Minute Revision — Read 30 Mins Before Interview

```
1. FastAPI = fast + automatic docs + async + Pydantic validation
2. Pydantic validates ALL request data automatically → 422 on failure
3. Depends() = inject reusable logic (DB, auth, pagination)
4. yield in dependency = setup + teardown (open DB, yield, close DB)
5. async def + await = non-blocking I/O (concurrent)
6. def = runs in thread pool (parallel, good for sync libraries)
7. time.sleep in async = BLOCKS everything (use asyncio.sleep)
8. middleware = runs for ALL requests (logging, timing, headers)
9. HTTPException = raise HTTP errors with status + message
10. response_model = filter/shape API output (hide passwords!)
11. CORS = add middleware with specific allow_origins in production
12. APIRouter = split large app into multiple files
13. TestClient + dependency_overrides = how to test FastAPI
14. Gunicorn + Uvicorn workers = production deployment
15. .env + pydantic BaseSettings = secure config management
```

---

### 📚 Bonus Questions (Extra Credit in Interview)

**Q: What is `scalar_one_or_none()` in SQLAlchemy?**
> Returns exactly one result or None. If multiple results exist, raises an error. Use it when you expect 0 or 1 result (like fetching by ID).

**Q: What is `expire_on_commit=False` in SQLAlchemy?**
> By default, SQLAlchemy expires all attributes after commit (to force re-fetch). In async, this causes issues. Setting this to False lets you access attributes after commit without another DB query.

**Q: What does `await db.refresh(obj)` do?**
> Reloads the object from the DB after an insert. Needed to get auto-generated fields like `id` and timestamps.

**Q: What is `model_dump(exclude_unset=True)` used for in PATCH endpoints?**
> Returns only the fields that were actually provided in the request, skipping fields with defaults. Perfect for PATCH (partial update) — so you don't overwrite existing values with defaults.

**Q: What is `APIRouter` prefix?**
> A string prepended to all routes in that router. `prefix="/users"` means `@router.get("/")` becomes `/users/` and `@router.get("/{id}")` becomes `/users/{id}`.

**Q: What is `on_event("startup")` used for?**
> Runs a function when the FastAPI app starts — typically used to create DB tables, load ML models, or initialise caches.

**Q: What is `include_router` with `dependencies` param?**
> Applies a dependency to ALL routes in a router. Example: `app.include_router(admin_router, dependencies=[Depends(require_admin)])` — protects ALL admin routes with one line.

---

## 🏁 Final Words

> **You're now equipped with everything needed to crack a FastAPI interview.**
>
> **The 3 concepts that appear in 90% of all FastAPI interviews:**
> 1. **Pydantic** — validation, BaseModel, response_model
> 2. **Dependency Injection** — Depends(), yield, chaining
> 3. **Async/Await** — when to use each, the time.sleep gotcha
>
> **Understand WHY, not just HOW. Interviewers can tell the difference.**
>
> **Good luck! 🚀🐍**

---

*Guide compiled from multiple YouTube FastAPI courses and interview prep resources.*
*Built for beginners aiming to become FastAPI experts.*

