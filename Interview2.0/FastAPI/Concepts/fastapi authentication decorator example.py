#decorator concept
# from functools import wraps

# def custom_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         #-------Before
#         result = func(*args, **kwargs)
#         #--------after
#         return result
#     return wrapper

# @custom_decorator
#     def greet():
#     """This function greets the user"""
#       print("Hello")

"""
╔══════════════════════════════════════════════════════════════════════╗
║         FastAPI AUTH PATTERNS — INTERVIEW PREP                       ║
║                      Author: Suvam Das                               ║
╠══════════════════════════════════════════════════════════════════════╣
║  Pattern 1 — Custom @require_login decorator                         ║
║  Pattern 2 — FastAPI Depends() (production standard)                 ║
╚══════════════════════════════════════════════════════════════════════╝

Run:   pip install fastapi uvicorn
Start: uvicorn filename:app --reload
Docs:  http://127.0.0.1:8000/docs   ← Swagger UI auto-generated
"""

# ══════════════════════════════════════════════════════════════════════
# PATTERN 1 — Custom @require_login Decorator
# ══════════════════════════════════════════════════════════════════════
#
# HOW IT WORKS:
#   - require_login wraps the route function
#   - Before the route runs, it extracts 'authorization' from kwargs
#     (FastAPI injects Header values into kwargs automatically)
#   - If token is invalid → raise 401, route never runs
#   - If token is valid   → print confirmation, run the route
#
# HOW TO EXPLAIN TO INTERVIEWER:
#   "I wrote a custom decorator that intercepts every request before
#    the route handler runs. It pulls the authorization header from
#    kwargs — FastAPI has already extracted it from the HTTP request
#    and passed it in. If the token isn't valid I raise an HTTPException
#    which FastAPI catches and returns as a 401 response automatically.
#    I use @functools.wraps so FastAPI still sees the original function
#    name and signature — without it, routing breaks."
#
# WHEN TO USE THIS PATTERN:
#   ✅ You want pure Python decorator style
#   ✅ You need to run custom logic before AND after the route
#   ⚠️  Swagger UI won't show the auth header automatically
# ══════════════════════════════════════════════════════════════════════

from fastapi import FastAPI, HTTPException, Header, Depends
from functools import wraps

app = FastAPI()

VALID_TOKENS = {"secret-token-123", "admin-token-456"}


def require_login(func):
    @wraps(func)                                 # preserves __name__ and __doc__
                                                 # FastAPI needs this for routing
    async def wrapper(*args, **kwargs):
        token = kwargs.get("authorization")      # FastAPI injects Header value here

        if token not in VALID_TOKENS:
            raise HTTPException(status_code=401, detail="Unauthorized")
                                                 # FastAPI catches this and returns
                                                 # a proper HTTP 401 response

        print(f"[AUTH] ✅ Token valid for '{func.__name__}'")
        result = await func(*args, **kwargs)     # route only runs if token is valid
        return result

    return wrapper


@app.get("/profile")
@require_login                                   # gate: checks token first
async def get_profile(user_id: int, authorization: str = Header(...)):
    # Header(...) → FastAPI extracts 'authorization' from HTTP request headers
    # This line only runs if require_login lets it through
    return {"user_id": user_id, "profile": "Jon Doe"}


@app.delete("/users/{user_id}")
@require_login                                   # same decorator reused — DRY principle
async def delete_user(user_id: int, authorization: str = Header(...)):
    return {"message": f"User {user_id} deleted"}


# ══════════════════════════════════════════════════════════════════════
# PATTERN 2 — Depends() (Production FastAPI Standard) ⭐ Recommended
# ══════════════════════════════════════════════════════════════════════
#
# HOW IT WORKS:
#   - verify_token() is a plain function — not a decorator
#   - Depends(verify_token) tells FastAPI: "call this function first,
#     inject its return value into the route parameter"
#   - FastAPI's dependency injection system handles the wiring
#   - If verify_token raises HTTPException → route never runs
#   - If verify_token returns the token → route receives it as 'token'
#
# HOW TO EXPLAIN TO INTERVIEWER:
#   "FastAPI calls verify_token() automatically before running the route.
#    If the token is invalid it raises a 401 and the route never executes.
#    If valid, the return value gets injected into the route as 'token'.
#    I write the auth logic once and reuse it across any route with just
#    Depends(verify_token) — no decorators, no copy-pasting.
#    The big advantage over a custom decorator is that FastAPI's OpenAPI
#    generator sees the dependency and shows the auth header in Swagger UI
#    automatically — so the API docs are always accurate."
#
# WHEN TO USE THIS PATTERN:
#   ✅ Production FastAPI code — this is the standard
#   ✅ Swagger UI shows auth header automatically
#   ✅ Easy to unit test — just call verify_token() directly
#   ✅ FastAPI can run multiple Depends() in parallel (async optimised)
# ══════════════════════════════════════════════════════════════════════

def verify_token(authorization: str = Header(...)):
    """
    Dependency function — FastAPI calls this automatically.
    Header(...) → FastAPI extracts 'authorization' from the HTTP request.
    The ... means it is REQUIRED — request fails if header is missing.
    """
    if authorization not in VALID_TOKENS:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return authorization                         # injected into route as 'token'


@app.get("/dashboard")
async def get_dashboard(user_id: int, token: str = Depends(verify_token)):
    # token = whatever verify_token() returned (the valid token string)
    # if verify_token raised HTTPException, this line NEVER runs
    return {"user_id": user_id, "dashboard": "welcome back"}


@app.delete("/admin/users/{user_id}")
async def admin_delete_user(user_id: int, token: str = Depends(verify_token)):
    # No decorator needed — Depends() handles everything
    return {"message": f"User {user_id} deleted by admin"}


# ══════════════════════════════════════════════════════════════════════
# COMPARISON — Decorator vs Depends()
# ══════════════════════════════════════════════════════════════════════
#
#  Feature                    @require_login        Depends(verify_token)
#  ─────────────────────────────────────────────────────────────────────
#  Where auth logic lives     Inside decorator      Standalone function
#  How FastAPI knows about it Wraps the function    Declared in signature
#  Reusability                ✅                    ✅
#  Swagger UI shows auth      ⚠️  Partial            ✅ Full (automatic)
#  Unit testable in isolation Harder                Easy (call directly)
#  FastAPI idiomatic          No                    ✅ Yes
#  Before + after logic       ✅ Easy               Harder (use middleware)
#
#  RULE OF THUMB:
#    Auth / validation        → always use Depends()
#    Logging / timing         → use a decorator (needs before + after)
#
# ══════════════════════════════════════════════════════════════════════
# TO TEST MANUALLY (with uvicorn running):
# ══════════════════════════════════════════════════════════════════════
#
#  Valid request:
#    curl -X GET "http://localhost:8000/profile?user_id=1" \
#         -H "authorization: secret-token-123"
#  Expected: {"user_id": 1, "profile": "Jon Doe"}
#
#  Invalid token:
#    curl -X GET "http://localhost:8000/profile?user_id=1" \
#         -H "authorization: wrong-token"
#  Expected: {"detail": "Unauthorized"}   ← HTTP 401
#
#  Depends() valid request:
#    curl -X GET "http://localhost:8000/dashboard?user_id=1" \
#         -H "authorization: admin-token-456"
#  Expected: {"user_id": 1, "dashboard": "welcome back"}