# Rate Limiter — Interview Cheat Sheet

> **Code in interview:** Sliding Window Log | **FAANG explain:** Token Bucket | **Distributed:** Redis

---

## 1. What is a Rate Limiter?

Controls how many requests a client can make in a given time window. Excess requests are blocked with **HTTP 429 Too Many Requests**.

**Why it matters (say this in interview):**
- Prevents DoS / DDoS attacks
- Reduces server cost
- Protects paid third-party APIs from overuse
- Prevents abuse from bots

---

## 2. The One to Code — Sliding Window Log

> Simplest + most accurate. This is what you write when asked to code a rate limiter.

**Mental model:**
1. Store → `user_id: [timestamps]`
2. Filter → remove timestamps older than 60s
3. Check → if count >= limit → block, else → append & allow

### Python
```python
import time
from collections import defaultdict

LIMIT  = 5
WINDOW = 60  # seconds

requests = defaultdict(list)  # { user_id: [timestamps] }

def is_allowed(user_id):
    now  = time.time()
    logs = requests[user_id]

    # keep only timestamps within last 60s
    requests[user_id] = [t for t in logs if now - t < WINDOW]

    if len(requests[user_id]) >= LIMIT:
        return False  # blocked

    requests[user_id].append(now)  # save timestamp
    return True


# Flask usage
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/api")
def api():
    user_id = request.args.get("user_id", "anonymous")
    if not is_allowed(user_id):
        return jsonify({"error": "Too many requests"}), 429
    return jsonify({"message": "OK"})
```

### JavaScript
```javascript
const LIMIT  = 5;
const WINDOW = 60 * 1000; // ms
const requests = new Map(); // userId → [timestamps]

function isAllowed(userId) {
  const now    = Date.now();
  const logs   = requests.get(userId) || [];
  const recent = logs.filter(t => now - t < WINDOW);

  if (recent.length >= LIMIT) return false;

  requests.set(userId, [...recent, now]);
  return true;
}

// Express usage
app.use((req, res, next) => {
  if (!isAllowed(req.user.id))
    return res.status(429).json({ error: "Too many requests" });
  next();
});
```

---

## 3. All 5 Algorithms — Quick Reference

| Algorithm | Pros | Cons |
|---|---|---|
| **Token Bucket** | Allows bursts, memory efficient | Hard to tune 2 params |
| **Leaking Bucket** | Smooth fixed output rate | Bursts fill queue, recent reqs dropped |
| **Fixed Window** | Simple, memory efficient | Spike at window edges (2x requests slip through) |
| **Sliding Window Log** | Very accurate, no edge spike | Memory heavy (stores all timestamps) |
| **Sliding Window Counter** | Smooth + memory efficient | Approximate (assumes even distribution) |

---

## 4. Token Bucket — Know for FAANG

> Used by **Amazon** and **Stripe**. Best when bursts of traffic are allowed.

- Bucket holds N tokens, refills at fixed rate (e.g. 10 tokens/sec)
- Each request consumes 1 token
- If bucket empty → request dropped
- Allows short bursts — all tokens can be used at once

```python
import time

class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity    = capacity     # max tokens
        self.tokens      = capacity     # start full
        self.refill_rate = refill_rate  # tokens per second
        self.last_refill = time.time()

    def allow(self):
        self._refill()
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False

    def _refill(self):
        now     = time.time()
        elapsed = now - self.last_refill
        added   = elapsed * self.refill_rate
        self.tokens      = min(self.capacity, self.tokens + added)
        self.last_refill = now

# usage
bucket = TokenBucket(capacity=10, refill_rate=2)  # 10 max, refill 2/sec
print(bucket.allow())  # True or False
```

---

## 5. Where to Place the Rate Limiter

| Option | When to use |
|---|---|
| Server-side middleware | Full control over algorithm, best for most cases |
| API Gateway | Already using microservices + auth + IP whitelisting |
| Client-side | ❌ NEVER — clients can be forged by malicious actors |

---

## 6. Distributed Rate Limiting — Senior Level

> If they ask *"What if multiple servers are running?"* — this is your answer.

### Problem 1: Race Condition
Two servers read counter = 3 at same time → both write 4 → should be 5.

**Fix:** Use Redis atomic `INCR + EXPIRE`

### Problem 2: Synchronization
Client hits different servers each time → no single server has full history.

**Fix:** Centralized Redis — all rate limiters share one Redis store.

### Redis-based (production pattern)
```python
import redis

r = redis.Redis(host='localhost', port=6379)

def is_allowed(user_id, limit=5, window=60):
    key   = f"rate:{user_id}"
    count = r.incr(key)           # atomic increment
    if count == 1:
        r.expire(key, window)     # set TTL on first request
    return count <= limit
```

---

## 7. HTTP Headers to Mention

| Header | Meaning |
|---|---|
| `X-RateLimit-Limit` | Max requests allowed per window |
| `X-RateLimit-Remaining` | Requests left in current window |
| `X-RateLimit-Retry-After` | Seconds until they can retry |
| `HTTP 429` | Too Many Requests — returned when blocked |

---

## 8. Follow-up Questions & Answers

**Q: What if server restarts?**
> In-memory solution is lost on restart. Use Redis with `INCR + EXPIRE` — persists across restarts and servers.

**Q: Multiple servers / distributed system?**
> Centralized Redis store. All rate limiters point to same Redis. Use atomic `INCR` to avoid race conditions.

**Q: Which algorithm is best?**
> Sliding window log for accuracy. Token bucket if bursts allowed. Sliding window counter for memory efficiency at scale (used by Cloudflare).

**Q: Hard vs soft rate limiting?**
> - **Hard:** Strictly block when limit exceeded
> - **Soft:** Allow slight overflow for short bursts

**Q: Rate limit by what?**
> - **User ID** — most common, per logged-in user
> - **IP Address** — for unauthenticated APIs
> - **API Key** — for B2B / developer APIs
> - **Global** — one shared limit across all users

---

## 9. One-Page Summary to Memorize

```
Code in interview  →  Sliding Window Log (simplest + accurate)
FAANG explanation  →  Token Bucket (bursts allowed, used by Amazon/Stripe)
Distributed fix    →  Redis INCR + EXPIRE (atomic, shared across servers)
Race condition fix →  Lua script or Redis sorted sets
HTTP response      →  429 + X-RateLimit headers
Never              →  Client-side rate limiting (can be forged)
```