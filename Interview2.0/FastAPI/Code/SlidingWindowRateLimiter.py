# Each user can make at most max_requests within window_seconds.
# If limit exceeded → return False
# Otherwise → return True
# Must support multiple users
# Timestamps are provided (no need to use real time)
# Should be optimized for high request volume
# Use sliding window.

# What to say when you present it:

"""I used a deque because removing from the front is O(1) compared to O(n) with a list. 
The class takes timestamp as a parameter rather than calling time.time() internally so it's easy to unit test. 
Each user gets their own deque storing only the timestamps within the current window."""

from collections import deque, defaultdict

class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.users = defaultdict(deque)   # user_id -> deque of timestamps

    def allow_request(self, user_id: str, timestamp: int) -> bool:
        q = self.users[user_id]

        # Remove expired requests
        while q and timestamp - q[0] >= self.window_seconds:
            q.popleft()

        # Reject if limit already reached
        if len(q) >= self.max_requests:
            return False

        # Allow and record current request
        q.append(timestamp)
        return True


# Example
limiter = RateLimiter(3, 10)

print(limiter.allow_request("u1", 1))   # True
print(limiter.allow_request("u1", 2))   # True
print(limiter.allow_request("u1", 3))   # True
print(limiter.allow_request("u1", 11))  # True
print(limiter.allow_request("u1", 12))  # True
print(limiter.allow_request("u1", 13))  # True
print(limiter.allow_request("u1", 14))  # False




# Rate Limiter — How to Explain to Interviewer

> **One-line summary to open or close with:**
> *"It's a sliding window log rate limiter. I store request timestamps per user in a deque, remove expired timestamps on every request, and reject when the number of requests in the current rolling window reaches the limit. I use deque because front-removal is efficient, and I take timestamp as input so the code is easy to unit test."*

---

## Step 1 — Start with the Problem (30 seconds)

> "A rate limiter controls how many requests a user can make in a given time window. If the limit is exceeded, we reject the request, typically with HTTP 429. Here I'm using the **Sliding Window Log** algorithm because it enforces a true rolling window accurately."

---

## Step 2 — Explain the Data Structure Choice

> "I used a `defaultdict(deque)` — a dictionary mapping each `user_id` to a deque of timestamps.
>
> I chose **deque over list** because removing from the front is **O(1)** with `popleft()`, but **O(n)** with a list's `pop(0)`. Since we're constantly removing expired timestamps from the front, this matters at scale."

```python
self.users = defaultdict(deque)  # user_id -> deque of timestamps
```

---

## Step 3 — Walk Through `allow_request` Line by Line

> "Every time a request comes in, I do three things:"

### Step A — Clean up expired timestamps

```python
while q and timestamp - q[0] >= self.window_seconds:
    q.popleft()
```

> "I remove all timestamps from the front that fall outside the current window. I use `while` not `if` because multiple timestamps could be expired at once. `q[0]` is always the oldest — deque is ordered."

### Step B — Check the limit

```python
if len(q) >= self.max_requests:
    return False
```

> "After cleaning, if the remaining count already hits the limit, I reject the request. No timestamp is stored for rejected requests — important for memory efficiency."

### Step C — Allow and record

```python
q.append(timestamp)
return True
```

> "If allowed, I append the current timestamp to the right of the deque and return True."

---

## Step 4 — Trace Through the Example

> "Let me trace through with `max_requests=3, window=10`:"

| Call | Timestamp | Queue before | Action | Result |
|---|---|---|---|---|
| 1 | 1 | `[]` | append 1 | ✅ True |
| 2 | 2 | `[1]` | append 2 | ✅ True |
| 3 | 3 | `[1,2]` | append 3 | ✅ True |
| 4 | 11 | `[1,2,3]` | remove 1 (11-1=10 ≥ 10), queue=[2,3], append 11 | ✅ True |
| 5 | 12 | `[2,3,11]` | remove 2 (12-2=10 ≥ 10), queue=[3,11], append 12 | ✅ True |
| 6 | 13 | `[3,11,12]` | remove 3 (13-3=10 ≥ 10), queue=[11,12], append 13 | ✅ True |
| 7 | 14 | `[11,12,13]` | nothing expired (14-11=3), len=3 >= 3 | ❌ False |

---

## Step 5 — Time and Space Complexity

> "They will definitely ask this."

**Time:** Worst-case O(k) per request if many timestamps expire at once, but **amortized O(1)** since each timestamp is appended once and removed once.

**Space:** O(total active timestamps across all users). In practice if each user can have at most `max_requests` accepted timestamps in the window, it's **O(number_of_users × max_requests)**. Rejected requests take no space.

---

## Step 6 — Answer Follow-up Questions

**Q: Why take `timestamp` as a parameter instead of `time.time()`?**
> "Makes it deterministic and fully testable without mocking. I can pass any timestamp in unit tests and verify exact behavior."

**Q: Is this thread-safe?**
> "No, not as written. For concurrent access I'd add synchronization per user's deque. In a distributed system I'd move to Redis sorted sets or a Lua script so the remove-old, count, and add-new steps are atomic."

**Q: What's the weakness of this algorithm?**
> "Memory — we store every accepted request timestamp inside the current window. If a user makes 10,000 requests per window, we store 10,000 timestamps. Token Bucket is more memory efficient for that case."

**Q: How would you scale this to multiple servers?**
> "For distributed systems I'd use Redis sorted sets — timestamps as scores, `ZREMRANGEBYSCORE` to remove expired entries, `ZCARD` to count, and add the new one atomically. All servers share one Redis instance."

**Q: Hard vs soft rate limiting?**
> "This implementation is a strict sliding-window limiter. Some other algorithms like token bucket allow controlled bursts, which can feel softer from a traffic-shaping perspective."
















"""
Why this is the best one for interview
What it does

For each user, we store only the timestamps that are still inside the current sliding window.

When a new request comes:

remove old timestamps
check how many valid requests are left
if count is below limit, allow
otherwise reject
Why deque is important

Use this line in interview:

I use deque because I need fast removal from the left for expired requests and fast append to the right for new requests.

That sounds strong.

popleft() → efficient
append() → efficient
Time complexity

Say this clearly:

Average time: O(1) per request
Worst case: O(k) when many old timestamps expire at once
Space: O(active requests per user)

This is a very good interview answer.

How to explain it in simple words

Imagine:

u1 -> [1, 2, 3]

Now request comes at time 11, window is 10.

Check oldest:

11 - 1 = 10 → expired, remove it

Now queue becomes:

[2, 3]

Now size is less than 3, so add 11:

[2, 3, 11]

Allowed.

Why this is better than fixed window

This is a very common follow-up.

You can say:

Fixed window has boundary problem. For example, user can send requests at the end of one window and again at the start of the next window, which can allow bursts. Sliding window is more accurate because it always checks the last N seconds from the current request.

That is one of the best answers you can give.

Counter questions they may ask and how to answer
1. Why not use a list?

Answer:
A list is slower for removing from the front. deque is better because popleft() is efficient.

2. Why sliding window instead of fixed window?

Answer:
Sliding window is more accurate and avoids the fixed-window boundary burst problem.

3. Is this optimized for multiple users?

Answer:
Yes. I use a dictionary mapping user_id -> deque, so each user has independent request tracking.

4. What is the space complexity?

Answer:
Space is proportional to the number of active requests stored inside the current window across users.

5. Can this work in distributed systems?

Answer:
This in-memory version works for a single process. In distributed systems, I would move the counters/timestamps to Redis and use sorted sets or Lua scripts for atomic operations. The design material you shared also points toward Redis-based centralized coordination for distributed rate limiting.

6. What happens under very high traffic?

Answer:
This is efficient for in-memory single-machine use, but for very high scale I would use Redis, API gateway rate limiting, or token bucket/sliding window counter depending on memory and burst requirements. The design notes also compare sliding window log with token bucket and fixed window approaches.

Best short interview explanation

You can say this almost exactly:

I used a sliding window rate limiter with a dictionary of deques. For each user, I store request timestamps. When a new request arrives, I remove expired timestamps outside the time window. If the remaining request count is below the limit, I allow the request and append the new timestamp; otherwise I reject it. I chose deque because it gives efficient popleft() and append(). This approach is more accurate than fixed window because it avoids boundary spikes.

If interviewer asks for production improvements

Say:

use Redis
use sorted set or Lua script
return HTTP 429
add headers:
X-RateLimit-Limit
X-RateLimit-Remaining
Retry-After

These are also part of the broader rate limiting design ideas in the material you provided.
"""