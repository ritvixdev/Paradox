"""
╔══════════════════════════════════════════════════════════════════════╗
║       PYTHON DECORATORS + FastAPI — FULL INTERVIEW PREP GUIDE        ║
║                         Author: Suvam Das                            ║
╠══════════════════════════════════════════════════════════════════════╣
║  ✅ What a decorator IS — explained from scratch                     ║
║  ✅ 5 real decorator patterns used in FastAPI interviews             ║
║  ✅ Full working FastAPI app tying everything together               ║
║  ✅ "How to explain to interviewer" for each pattern                 ║
║  ✅ Actual output shown as inline comments                           ║
║  ✅ Common interview Q&A at the end                                  ║
╚══════════════════════════════════════════════════════════════════════╝

WHAT IS A DECORATOR? (say this to the interviewer)
──────────────────────────────────────────────────
  "A decorator is a function that WRAPS another function to add
   behaviour BEFORE and/or AFTER it runs — without modifying the
   original function's code. It uses Python's first-class functions:
   functions can be passed as arguments and returned from other functions.
   The @syntax is just clean shorthand for: func = decorator(func)"

MENTAL MODEL:
  Think of a decorator like a SECURITY GUARD at a door:
    1. Guard checks your ID before you enter  (before logic)
    2. You do your thing inside               (original function)
    3. Guard logs that you left               (after logic)
  The room (original function) doesn't change — only the guard wraps it.

DECORATOR ANATOMY:
  def my_decorator(func):          # accepts the original function
      def wrapper(*args, **kwargs): # wraps it
          # --- BEFORE ---
          result = func(*args, **kwargs)  # call original
          # --- AFTER  ---
          return result
      return wrapper               # return the wrapped version

  @my_decorator                    # sugar for: greet = my_decorator(greet)
  def greet():
      print("Hello!")
"""

import time
import functools


# ══════════════════════════════════════════════════════════════════════
# PART 1 — DECORATOR BASICS (understand this first)
# ══════════════════════════════════════════════════════════════════════

print("=" * 64)
print("PART 1 — DECORATOR BASICS")
print("=" * 64)

# ── Step 1: Without decorator syntax ──────────────────────────────────
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"  [Before] calling {func.__name__}()")
        result = func(*args, **kwargs)
        print(f"  [After]  {func.__name__}() finished")
        return result
    return wrapper

def say_hello():
    print("  Hello, World!")

say_hello = simple_decorator(say_hello)   # manual wrapping (no @ syntax)
print("\n-- Manual wrapping (no @ syntax) --")
say_hello()
# Output:
#   [Before] calling say_hello()
#   Hello, World!
#   [After]  say_hello() finished

# ── Step 2: Same thing using @ syntax (cleaner) ───────────────────────
@simple_decorator                         # identical to: greet = simple_decorator(greet)
def greet():
    print("  Hi from greet()!")

print("\n-- @ syntax (same result, cleaner) --")
greet()
# Output:
#   [Before] calling greet()
#   Hi from greet()!
#   [After]  greet() finished

# ── Step 3: functools.wraps — ALWAYS use this ─────────────────────────
# Without @functools.wraps, the wrapper HIDES the original function's
# name and docstring — bad for debugging.
def proper_decorator(func):
    @functools.wraps(func)               # preserves __name__, __doc__ of original
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@proper_decorator
def my_function():
    """This is my docstring."""
    pass

print("\n-- functools.wraps preserves metadata --")
print(f"  Function name: {my_function.__name__}")   # Output: my_function (not 'wrapper')
print(f"  Docstring    : {my_function.__doc__}")    # Output: This is my docstring.


# ══════════════════════════════════════════════════════════════════════
# 1️⃣  LOGGING DECORATOR  —  @log_execution
# ══════════════════════════════════════════════════════════════════════
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS IT?
  Automatically logs every function call: which function ran,
  what arguments it received, and what it returned.
  Used in every production API to track activity.

HOW TO EXPLAIN TO INTERVIEWER:
  "In FastAPI, every route handler is just a Python function.
   I wrap it with @log_execution so every incoming request is
   automatically logged — the endpoint name, the arguments
   (like user_id or query params), and the response.
   This gives us full observability without touching each function.
   I use functools.wraps to preserve the original function's name
   so FastAPI's routing still works correctly."

REAL USE CASE IN FastAPI:
  @app.get("/users/{user_id}")
  @log_execution
  async def get_user(user_id: int):
      return fetch_user(user_id)
  → Every GET /users/42 call is automatically logged.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  [LOG] Calling '{func.__name__}' | args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"  [LOG] '{func.__name__}' returned → {result}")
        return result
    return wrapper

@log_execution
def get_user(user_id: int):
    """Simulates a FastAPI route: GET /users/{user_id}"""
    return {"id": user_id, "name": "Suvam", "role": "admin"}

@log_execution
def create_order(product: str, quantity: int):
    """Simulates a FastAPI route: POST /orders"""
    return {"product": product, "quantity": quantity, "status": "created"}

print("\n" + "=" * 64)
print("1️⃣  LOGGING DECORATOR  —  @log_execution")
print("=" * 64)
get_user(42)
# Output:
#   [LOG] Calling 'get_user' | args=(42,) kwargs={}
#   [LOG] 'get_user' returned → {'id': 42, 'name': 'Suvam', 'role': 'admin'}

print()
create_order(product="laptop", quantity=2)
# Output:
#   [LOG] Calling 'create_order' | args=() kwargs={'product': 'laptop', 'quantity': 2}
#   [LOG] 'create_order' returned → {'product': 'laptop', 'quantity': 2, 'status': 'created'}


# ══════════════════════════════════════════════════════════════════════
# 2️⃣  AUTHENTICATION DECORATOR  —  @require_login
# ══════════════════════════════════════════════════════════════════════
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS IT?
  Guards a route so only authenticated users can access it.
  If the user is not logged in, return 401 immediately — never
  even run the actual function.

HOW TO EXPLAIN TO INTERVIEWER:
  "This is the GATE KEEPER pattern. The decorator checks if a
   valid token/session exists BEFORE running the route logic.
   In real FastAPI, authentication is done with Depends() and
   OAuth2 Bearer tokens — but the concept is identical: intercept
   the request, validate credentials, either proceed or reject.
   The key benefit is I write the auth check ONCE and apply it
   to any route with @require_login — no copy-pasting auth code
   into every function."

REAL USE CASE IN FastAPI:
  @app.delete("/users/{user_id}")
  @require_login
  async def delete_user(user_id: int, token: str):
      ...   # only runs if token is valid
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# Simulated token store (in real FastAPI: JWT validation)
VALID_TOKENS = {"secret-token-123", "admin-token-456"}

def require_login(func):
    @functools.wraps(func)
        def wrapper(*args, **kwargs):
                token = kwargs.get("token", None)        # extract token from kwargs
                        if token not in VALID_TOKENS:
                                    print(f"  [AUTH] ❌ 401 Unauthorized — invalid token: '{token}'")
                                                return {"error": "401 Unauthorized"}
                                                        print(f"  [AUTH] ✅ Token valid — proceeding to '{func.__name__}'")
                                                                return func(*args, **kwargs)
                                                                    return wrapper

                                                                    @require_login
                                                                    def get_profile(user_id: int, token: str):
                                                                        """Simulates: GET /profile (protected route)"""
                                                                            return {"user_id": user_id, "profile": "Suvam Das", "email": "suvam@dev.com"}

                                                                            @require_login
                                                                            def delete_account(user_id: int, token: str):
                                                                                """Simulates: DELETE /users/{user_id} (admin only)"""
                                                                                    return {"message": f"User {user_id} deleted successfully"}

print("\n" + "=" * 64)
print("2️⃣  AUTHENTICATION DECORATOR  —  @require_login")
print("=" * 64)

print("\n-- Valid token --")
result = get_profile(user_id=7, token="secret-token-123")
print(f"  Response: {result}")
# Output:
#   [AUTH] ✅ Token valid — proceeding to 'get_profile'
#   Response: {'user_id': 7, 'profile': 'Suvam Das', 'email': 'suvam@dev.com'}

print("\n-- Invalid token --")
result = get_profile(user_id=7, token="hacker-token")
print(f"  Response: {result}")
# Output:
#   [AUTH] ❌ 401 Unauthorized — invalid token: 'hacker-token'
#   Response: {'error': '401 Unauthorized'}

print("\n-- No token at all --")
result = delete_account(user_id=7, token=None)
print(f"  Response: {result}")
# Output:
#   [AUTH] ❌ 401 Unauthorized — invalid token: 'None'
#   Response: {'error': '401 Unauthorized'}


# ══════════════════════════════════════════════════════════════════════
# 3️⃣  TIMING DECORATOR  —  @measure_time
# ══════════════════════════════════════════════════════════════════════
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS IT?
  Measures how long a function takes to execute.
  Used to detect slow API endpoints and performance bottlenecks.

HOW TO EXPLAIN TO INTERVIEWER:
  "I record time.time() before and after the function runs, then
   print the difference. In FastAPI production systems, this feeds
   into monitoring tools like Prometheus or Datadog — if an endpoint
   suddenly takes 3 seconds instead of 50ms, we get an alert.
   The decorator approach means I add timing to any slow endpoint
   with a single line — @measure_time — without touching the
   business logic inside the function."

REAL USE CASE IN FastAPI:
  @app.get("/reports/annual")
  @measure_time              ← flag slow endpoints instantly
  async def annual_report():
      return run_heavy_db_query()
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start  = time.time()                     # snapshot before
        result = func(*args, **kwargs)
        end    = time.time()                     # snapshot after
        elapsed = (end - start) * 1000           # convert to milliseconds
        print(f"  [TIMER] '{func.__name__}' took {elapsed:.2f} ms")
        return result
    return wrapper

@measure_time
def fetch_products():
    """Simulates: GET /products (fast DB query)"""
    time.sleep(0.05)                             # simulate 50ms DB call
    return [{"id": 1, "name": "Laptop"}, {"id": 2, "name": "Mouse"}]

@measure_time
def generate_report():
    """Simulates: GET /reports (heavy computation)"""
    time.sleep(0.2)                              # simulate 200ms heavy query
    return {"report": "Q4 Annual Summary", "rows": 50000}

print("\n" + "=" * 64)
print("3️⃣  TIMING DECORATOR  —  @measure_time")
print("=" * 64)

print("\n-- Fast endpoint --")
products = fetch_products()
print(f"  Returned: {products}")
# Output:
#   [TIMER] 'fetch_products' took ~50.xx ms
#   Returned: [{'id': 1, 'name': 'Laptop'}, {'id': 2, 'name': 'Mouse'}]

print("\n-- Slow endpoint --")
report = generate_report()
print(f"  Returned: {report}")
# Output:
#   [TIMER] 'generate_report' took ~200.xx ms
#   Returned: {'report': 'Q4 Annual Summary', 'rows': 50000}


# ══════════════════════════════════════════════════════════════════════
# 4️⃣  CACHING DECORATOR  —  @lru_cache  (VERY common in interviews)
# ══════════════════════════════════════════════════════════════════════
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS IT?
  Store the result of expensive function calls and return the cached
  result when called again with the same arguments.
  LRU = Least Recently Used (evicts oldest entries when cache is full).

HOW TO EXPLAIN TO INTERVIEWER:
  "Caching is critical for API performance. If 1000 users all request
   GET /products/categories, I don't want to hit the database 1000
   times — I compute it once, cache it, and serve from memory.
   Python's @functools.lru_cache does this automatically using the
   function arguments as the cache key.
   I also show a manual cache using a dict — same concept, more
   control (useful when you need TTL or cache invalidation).
   In FastAPI production: use Redis for distributed caching across
   multiple servers, but lru_cache is perfect for in-process caching."

LRU vs Manual dict cache:
  @lru_cache    → built-in, thread-safe, has maxsize, tracks hit/miss stats
  Manual dict   → more control: add TTL, custom keys, explicit invalidation

REAL USE CASE IN FastAPI:
  @lru_cache(maxsize=128)
  def get_exchange_rates():    ← called thousands of times, hits API once
      return requests.get("https://api.rates.com").json()
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

from functools import lru_cache

# ── Approach A: Built-in @lru_cache ───────────────────────────────────
@lru_cache(maxsize=128)                          # cache up to 128 unique calls
def get_product_details(product_id: int):
    """Simulates: GET /products/{id} — expensive DB call."""
    print(f"  [DB HIT] Fetching product {product_id} from database...")
    time.sleep(0.1)                              # simulate slow DB query
    return {"id": product_id, "name": f"Product-{product_id}", "price": product_id * 10}

# ── Approach B: Manual dict cache (more control) ───────────────────────
_manual_cache = {}

def manual_cache(func):
    @functools.wraps(func)
    def wrapper(*args):
        if args in _manual_cache:
            print(f"  [CACHE HIT]  '{func.__name__}' args={args} → served from cache")
            return _manual_cache[args]
        print(f"  [CACHE MISS] '{func.__name__}' args={args} → computing...")
        result = func(*args)
        _manual_cache[args] = result
        return result
    return wrapper

@manual_cache
def get_user_permissions(user_id: int):
    """Simulates fetching permissions — slow auth check."""
    time.sleep(0.05)
    return {"user_id": user_id, "permissions": ["read", "write", "delete"]}

print("\n" + "=" * 64)
print("4️⃣  CACHING DECORATOR  —  @lru_cache  (VERY common)")
print("=" * 64)

print("\n-- @lru_cache: first call hits DB, second call is instant --")
r1 = get_product_details(101)
print(f"  Result: {r1}")
# Output:
#   [DB HIT] Fetching product 101 from database...
#   Result: {'id': 101, 'name': 'Product-101', 'price': 1010}

r2 = get_product_details(101)                   # same args → cache hit, no DB call
print(f"  Result (cached): {r2}")
# Output:
#   Result (cached): {'id': 101, 'name': 'Product-101', 'price': 1010}

r3 = get_product_details(202)                   # different args → new DB call
print(f"  Result (new):    {r3}")
# Output:
#   [DB HIT] Fetching product 202 from database...
#   Result (new): {'id': 202, 'name': 'Product-202', 'price': 2020}

print(f"\n  Cache stats: {get_product_details.cache_info()}")
# Output: CacheInfo(hits=1, misses=2, maxsize=128, currsize=2)

print("\n-- Manual cache decorator --")
get_user_permissions(99)
# Output: [CACHE MISS] 'get_user_permissions' args=(99,) → computing...
get_user_permissions(99)
# Output: [CACHE HIT]  'get_user_permissions' args=(99,) → served from cache
get_user_permissions(55)
# Output: [CACHE MISS] 'get_user_permissions' args=(55,) → computing...


# ══════════════════════════════════════════════════════════════════════
# 5️⃣  FastAPI ROUTING DECORATOR  —  @app.get / @app.post
# ══════════════════════════════════════════════════════════════════════
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS IT?
  @app.get("/users") IS a decorator. FastAPI uses it to register
  the function as the handler for that HTTP method + URL path.
  Under the hood it calls app.add_api_route("/users", get_users, methods=["GET"])

HOW TO EXPLAIN TO INTERVIEWER:
  "FastAPI routing decorators are just Python decorators — they
   take the function and register it in FastAPI's router table.
   When a GET /users request comes in, FastAPI looks up its router,
   finds get_users() is registered for that path, and calls it.
   I can STACK decorators: @app.get first (routing), then
   @require_login (auth), then @measure_time (performance).
   They execute bottom-up during decoration and top-down during
   the actual request — so auth runs before the function body."

STACKING ORDER (important for interviews!):
  @app.get("/users")         ← applied LAST  (outermost wrapper)
  @log_execution             ← applied second
  @require_login             ← applied FIRST (innermost, closest to function)
  async def get_users():...

  Execution order on request:
    app.get wrapper → log_execution wrapper → require_login → get_users()
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# Minimal FastAPI simulation (no server needed — shows the pattern)
class MockFastAPI:
    """Simulates FastAPI's app object to show routing decorator concept."""
    def __init__(self):
        self.routes = {}

    def get(self, path: str):
        def decorator(func):
            self.routes[("GET", path)] = func
            print(f"  [ROUTER] Registered: GET {path} → {func.__name__}()")
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator

    def post(self, path: str):
        def decorator(func):
            self.routes[("POST", path)] = func
            print(f"  [ROUTER] Registered: POST {path} → {func.__name__}()")
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator

    def simulate_request(self, method: str, path: str, **kwargs):
        handler = self.routes.get((method, path))
        if handler:
            print(f"\n  → Incoming: {method} {path}")
            return handler(**kwargs)
        return {"error": "404 Not Found"}

app = MockFastAPI()

print("\n" + "=" * 64)
print("5️⃣  FastAPI ROUTING DECORATOR  —  @app.get / @app.post")
print("=" * 64)
print("\n-- Registering routes with decorators --")

@app.get("/users")
@log_execution
def get_users():
    """GET /users — list all users"""
    return [{"id": 1, "name": "Suvam"}, {"id": 2, "name": "Riya"}]

@app.get("/users/{user_id}")
@require_login
@measure_time
def get_user_by_id(user_id: int, token: str):
    """GET /users/{user_id} — protected + timed route"""
    return {"id": user_id, "name": "Suvam Das", "email": "suvam@dev.com"}

@app.post("/products")
@log_execution
@require_login
def create_product(name: str, price: float, token: str):
    """POST /products — log + auth protected"""
    return {"id": 99, "name": name, "price": price, "created": True}

print("\n-- Simulating HTTP requests --")
app.simulate_request("GET", "/users")
# Output:
#   → Incoming: GET /users
#   [LOG] Calling 'get_users' | args=() kwargs={}
#   [LOG] 'get_users' returned → [{'id': 1, ...}, {'id': 2, ...}]

print()
app.simulate_request("GET", "/users/{user_id}", user_id=42, token="secret-token-123")
# Output:
#   → Incoming: GET /users/{user_id}
#   [AUTH] ✅ Token valid — proceeding to 'get_user_by_id'
#   [TIMER] 'get_user_by_id' took ~0.xx ms

print()
app.simulate_request("POST", "/products", name="Keyboard", price=89.99, token="hacker!")
# Output:
#   → Incoming: POST /products
#   [LOG] Calling 'create_product' ...
#   [AUTH] ❌ 401 Unauthorized — invalid token: 'hacker!'


# ══════════════════════════════════════════════════════════════════════
# FULL PICTURE — STACKING ALL DECORATORS TOGETHER
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 64)
print("🔥 FULL STACK — All decorators on one route")
print("=" * 64)

@log_execution
@require_login
@measure_time
def delete_product(product_id: int, token: str):
    """
    Simulates: DELETE /products/{product_id}
    Stack: log → auth → time → function
    """
    return {"deleted": True, "product_id": product_id}

print("\n-- Valid request (all decorators pass) --")
result = delete_product(product_id=55, token="admin-token-456")
print(f"  Final response: {result}")
# Output:
#   [LOG] Calling 'delete_product' | args=() kwargs={'product_id': 55, 'token': 'admin-token-456'}
#   [AUTH] ✅ Token valid — proceeding to 'delete_product'
#   [TIMER] 'delete_product' took ~0.xx ms
#   [LOG] 'delete_product' returned → {'deleted': True, 'product_id': 55}
#   Final response: {'deleted': True, 'product_id': 55}

print("\n-- Invalid token (auth blocks everything) --")
result = delete_product(product_id=55, token="bad-token")
print(f"  Final response: {result}")
# Output:
#   [LOG] Calling 'delete_product' | ...
#   [AUTH] ❌ 401 Unauthorized — invalid token: 'bad-token'
#   [LOG] 'delete_product' returned → {'error': '401 Unauthorized'}
#   Final response: {'error': '401 Unauthorized'}


# ══════════════════════════════════════════════════════════════════════
# REAL FastAPI CODE (what you'd actually write with FastAPI installed)
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 64)
print("📄 REAL FastAPI CODE (copy-paste ready)")
print("=" * 64)
print('''
# pip install fastapi uvicorn

from fastapi import FastAPI, HTTPException, Depends, Header
from functools import lru_cache, wraps
import time

app = FastAPI()

# ── Custom decorators ──────────────────────────────────────────────
def measure_time(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = await func(*args, **kwargs)
        print(f"[TIMER] {func.__name__} → {(time.time()-start)*1000:.1f}ms")
        return result
    return wrapper

def log_execution(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} args={args} kwargs={kwargs}")
        result = await func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

# ── Auth via FastAPI Depends (production pattern) ──────────────────
def verify_token(authorization: str = Header(...)):
    if authorization != "Bearer secret-token-123":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return authorization

# ── Caching with lru_cache ─────────────────────────────────────────
@lru_cache(maxsize=128)
def get_product_from_db(product_id: int):
    # Simulates DB call — cached after first call
    return {"id": product_id, "name": f"Product-{product_id}"}

# ── Routes ─────────────────────────────────────────────────────────
@app.get("/users")
@log_execution
async def get_users():
    return [{"id": 1, "name": "Suvam"}, {"id": 2, "name": "Riya"}]

@app.get("/products/{product_id}")
@measure_time
async def get_product(product_id: int, token: str = Depends(verify_token)):
    return get_product_from_db(product_id)   # lru_cache handles repeat calls

@app.post("/products")
@log_execution
@measure_time
async def create_product(name: str, price: float,
                          token: str = Depends(verify_token)):
    return {"id": 99, "name": name, "price": price, "created": True}

@app.delete("/products/{product_id}")
@log_execution
@require_login
@measure_time
async def delete_product(product_id: int,
                          token: str = Depends(verify_token)):
    return {"deleted": True, "product_id": product_id}

# Run: uvicorn main:app --reload
# Docs: http://127.0.0.1:8000/docs  (auto-generated Swagger UI!)
''')


# ══════════════════════════════════════════════════════════════════════
# COMMON INTERVIEW Q&A
# ══════════════════════════════════════════════════════════════════════
print("=" * 64)
print("COMMON INTERVIEW Q&A")
print("=" * 64)
print("""
Q1: "What is a decorator in Python?"
A:  "A decorator is a function that wraps another function to add
     behaviour before/after it — without changing the original code.
     @decorator is syntactic sugar for: func = decorator(func).
     It works because Python treats functions as first-class objects
     — they can be passed as arguments and returned from functions."

Q2: "What is functools.wraps and why do you need it?"
A:  "When you wrap a function, the wrapper hides the original's
     __name__ and __doc__. This breaks FastAPI routing and debugging.
     @functools.wraps(func) copies the original's metadata to the
     wrapper — so the function still reports its real name.
     I always use it. Forgetting it is a common interview mistake."

Q3: "How does FastAPI's @app.get() work under the hood?"
A:  "It's a decorator factory — app.get('/users') returns a decorator
     which registers the function in FastAPI's router table, mapping
     GET + /users to that function. When a real HTTP request arrives,
     FastAPI looks up the router, finds the handler, and calls it.
     The function itself is unchanged — the decorator just registers it."

Q4: "What's the execution order when you stack decorators?"
A:  "Decorators apply bottom-up but execute top-down at call time.
       @log_execution      ← 3rd to apply, 1st to run on request
       @require_login      ← 2nd to apply, 2nd to run
       @measure_time       ← 1st to apply, 3rd to run
       def my_func(): ...
     So the request flows: log → auth check → timing → my_func()
     This matters because auth should reject bad requests BEFORE
     timing starts, so I put @require_login closer to the function."

Q5: "What is lru_cache and when would you use it in FastAPI?"
A:  "lru_cache stores return values keyed by function arguments.
     LRU (Least Recently Used) evicts the oldest entry when maxsize
     is reached. In FastAPI I use it for:
       - DB lookups that rarely change (product catalogue, config)
       - External API calls (exchange rates, weather data)
       - Heavy computations (report generation)
     For multi-server deployments I'd use Redis instead — lru_cache
     is in-process memory, so each server has its own cache."
""")


# ══════════════════════════════════════════════════════════════════════
# FINAL CHEAT SHEET
# ══════════════════════════════════════════════════════════════════════
print("=" * 64)
print("FINAL CHEAT SHEET")
print("=" * 64)
print("""
  Decorator          What it does                    FastAPI use case
  ─────────────────────────────────────────────────────────────────────
  @log_execution     Logs calls, args, return vals   Audit trail, debugging
  @require_login     Blocks unauthenticated calls     Protect private routes
  @measure_time      Prints execution duration        Find slow endpoints
  @lru_cache         Stores results by args           Avoid repeat DB hits
  @app.get(path)     Registers HTTP route handler     Every API endpoint

  ALWAYS say to interviewer:
    ✔ "I use @functools.wraps to preserve the original function's metadata"
    ✔ "Decorators apply bottom-up, execute top-down"
    ✔ "In real FastAPI, auth is handled by Depends() — same decorator concept"
    ✔ "For distributed caching across servers, I'd use Redis over lru_cache"
""")
