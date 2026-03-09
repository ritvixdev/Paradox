# Each user can make at most max_requests within window_seconds.
# If limit exceeded → return False
# Otherwise → return True
# Must support multiple users
# Timestamps are provided (no need to use real time)
# Should be optimized for high request volume
# Use sliding window.

class RateLimiter:
 
    def __init__(self, max_requests: int, window_seconds: int):
        
        pass
    def allow_request(self, user_id: str, timestamp: int) -> bool:
        
        pass

limiter = RateLimiter(3, 10)
limiter.allow_request("u1", 1)   # True
 
limiter.allow_request("u1", 2)   # True
 
limiter.allow_request("u1", 3)   # True
 
limiter.allow_request("u1", 11)  # True (old requests expired)
 
limiter.allow_request("u1", 12)  # True
 
limiter.allow_request("u1", 13)  # True
 
limiter.allow_request("u1", 14)  # False (exceeds limit)


# Answer:

from collections import deque

class RateLimiter:

    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.users = {}   # store user_id -> deque of timestamps

    def allow_request(self, user_id, timestamp):

        # If user not present, create a queue
        if user_id not in self.users:
            self.users[user_id] = deque()

        q = self.users[user_id]

        # Remove expired timestamps
        while len(q) > 0:
            oldest = q[0]

            if timestamp - oldest >= self.window_seconds:
                q.popleft()
            else:
                break

        # Check if request allowed
        if len(q) < self.max_requests:
            q.append(timestamp)
            return True
        else:
            return False



"""
Rate Limiter (Sliding Window)

Goal:
Limit how many requests a user can make in a given time window.

Example:
max_requests = 3
window_seconds = 10

Meaning:
A user can only make 3 requests in the last 10 seconds.

Idea (Sliding Window):
For each user we store timestamps of their requests.

Data Structure:
users = {
    user_id : deque([timestamps])
}

Example:
u1 -> [1,2,3]

When a new request arrives:

Step 1:
Remove all timestamps that are outside the window.

Example:
timestamp = 11
window = 10 seconds

11 - 1 >= 10 → remove 1

queue becomes:
[2,3]

Step 2:
Check if current requests < max_requests

If yes:
    allow request
    add timestamp to queue

If no:
    reject request

Example:
queue = [11,12,13]
max_requests = 3

new request at 14
queue size = 3 → reject

Why deque?
Because we need:
- fast remove from left (old requests)
- fast append to right (new request)

Time Complexity:
O(1) average per request

Space Complexity:
O(active requests per user)

This approach is used in:
API gateways
Cloudflare
AWS rate limiting
"""