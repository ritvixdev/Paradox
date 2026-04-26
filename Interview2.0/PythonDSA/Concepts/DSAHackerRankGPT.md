# Python HackerRank DSA — Built-in Methods, Tricks, and Pattern Cheat Sheet

> Goal: Solve HackerRank-style DSA questions faster using Python's accepted built-in tools and standard-library helpers, while still understanding the algorithm clearly enough to explain it in an interview.

---

## How to Use This File

Read this file in this order:

1. **Python tools cheat sheet** — know which built-in solves which pattern.
2. **Pattern recognition table** — identify the question type quickly.
3. **Pythonic templates** — use short, accepted code.
4. **Interview explanation lines** — explain why the solution works.
5. **Practice roadmap** — revise only the highest-return problems.

This file assumes HackerRank-style Python solutions where standard library usage such as `collections`, `heapq`, `bisect`, and `itertools` is normally acceptable unless the interviewer specifically says **do not use built-ins**.

---

# 1. Python Built-in / Standard Library DSA Toolkit

## 1.1 Must-Know Tools

| Tool | Import Needed? | Best For | Pattern |
|---|---:|---|---|
| `dict` | No | Frequency, index mapping, lookup | Hash Map |
| `set` | No | Duplicate check, membership, uniqueness | Hash Set |
| `Counter` | Yes | Frequency counting | Frequency Map |
| `defaultdict` | Yes | Grouping, graph adjacency list | Hash Map / Graph |
| `deque` | Yes | Queue, BFS, sliding window | Queue |
| `heapq` | Yes | Top K, min heap, priority queue | Heap |
| `bisect` | Yes | Binary search insert position | Binary Search |
| `sorted()` | No | Sorting, greedy, grouping | Sorting |
| `zip()` | No | Compare parallel arrays/strings | Pairing |
| `enumerate()` | No | Need index + value | Loop helper |
| `any()` / `all()` | No | Condition checks | Boolean logic |
| `map()` | No | Fast input conversion | Input parsing |
| `join()` | No | Build string efficiently | String |
| slicing | No | Reverse/copy/subarray | Array/String |

---

## 1.2 Import Block to Remember

Use this in HackerRank when useful:

```python
from collections import Counter, defaultdict, deque
import heapq
import bisect
import math
```

For most HackerRank DSA questions, this is enough.

---

# 2. Fast Input Tricks for HackerRank

## 2.1 Read One Integer

```python
n = int(input())
```

## 2.2 Read Space-Separated Integers

```python
arr = list(map(int, input().split()))
```

## 2.3 Read Multiple Lines into List

```python
n = int(input())
arr = []

for _ in range(n):
    arr.append(input())
```

## 2.4 Read Matrix

```python
n, m = map(int, input().split())
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
```

## 2.5 Fast Output

Instead of printing inside loop many times:

```python
result = ["Yes", "No", "Yes"]
print("\n".join(result))
```

Why?

`join()` builds one final string, which is faster and cleaner than many small prints.

---

# 3. Pattern Recognition Cheat Sheet

| Question Keywords | Pattern | Pythonic Tool |
|---|---|---|
| count, frequency, repeated | Frequency Map | `Counter` |
| duplicate, unique | Hash Set | `set` |
| anagram, same letters | Frequency Map | `Counter` |
| group by key | Grouping | `defaultdict(list)` |
| first/last occurrence | Hash Map | `dict` |
| sorted array search | Binary Search | `bisect` |
| top K, kth largest, smallest | Heap | `heapq` |
| brackets, undo, valid expression | Stack | `list` |
| queue, BFS, level order | Queue | `deque` |
| continuous subarray/substring | Sliding Window | `dict`, `Counter`, `deque` |
| range sum, subarray sum | Prefix Sum | list + dict |
| min/max after sorting | Greedy | `sorted()` |
| count ways/min cost | DP | list/dict memo |

---

# 4. Frequency Map Pattern — Pythonic Version

Use when you see:

- count frequency
- duplicate
- anagram
- pair count
- matching strings
- sock merchant
- top K frequent

## 4.1 Counter Basic

```python
from collections import Counter

arr = [1, 2, 2, 3, 3, 3]
freq = Counter(arr)

print(freq[3])  # 3
print(freq[9])  # 0, no KeyError
```

Important: `Counter` returns `0` for missing keys.

---

## 4.2 Contains Duplicate

```python
def contains_duplicate(nums):
    return len(nums) != len(set(nums))
```

### Interview explanation

> I convert the array into a set because a set stores only unique values. If the set length is smaller than the original length, duplicates exist.

Time: `O(n)`  
Space: `O(n)`

---

## 4.3 Valid Anagram

```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
```

### Interview explanation

> Two strings are anagrams if every character appears the same number of times in both strings. Counter gives a frequency map, so comparing two Counters solves it directly.

Time: `O(n)`  
Space: `O(k)` where `k` is number of unique characters.

---

## 4.4 Sock Merchant

```python
from collections import Counter

def sock_merchant(n, ar):
    freq = Counter(ar)
    pairs = 0

    for count in freq.values():
        pairs += count // 2

    return pairs
```

### Key trick

Every `2` same socks make one pair.

---

## 4.5 Matching Strings / Sparse Arrays

```python
from collections import Counter

def matching_strings(strings, queries):
    freq = Counter(strings)
    return [freq[q] for q in queries]
```

### Why this is fast

Without `Counter`, for every query you may scan all strings. With `Counter`, each query is `O(1)` average lookup.

---

## 4.6 Most Common Elements

```python
from collections import Counter

def top_k_frequent(nums, k):
    freq = Counter(nums)
    common = freq.most_common(k)
    return [num for num, count in common]
```

### Interview explanation

> I count occurrences using Counter, then use `most_common(k)` to return the highest frequency elements.

Time: usually efficient for interview use. For strict optimization, mention heap or bucket sort.

---

# 5. Hash Set Pattern

Use when:

- need fast lookup
- duplicate check
- intersection
- unique values
- seen before

## 5.1 Two Sum — Fast Pythonic Version

```python
def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        need = target - num

        if need in seen:
            return [seen[need], i]

        seen[num] = i

    return []
```

### Interview explanation

> I store each number and its index in a dictionary. For every number, I check whether `target - current` was already seen. This avoids the nested loop.

Time: `O(n)`  
Space: `O(n)`

---

## 5.2 Missing Number

```python
def missing_number(nums):
    n = len(nums)
    expected = n * (n + 1) // 2
    actual = sum(nums)
    return expected - actual
```

### Interview explanation

> Numbers should be from `0` to `n`. The expected sum is `n(n+1)/2`. The difference between expected and actual sum is the missing number.

Time: `O(n)`  
Space: `O(1)`

---

## 5.3 Intersection of Two Arrays

```python
def intersection(a, b):
    set_a = set(a)
    result = []

    for x in b:
        if x in set_a:
            result.append(x)
            set_a.remove(x)  # avoid duplicate output

    return result
```

---

# 6. Sorting Pattern

Use when:

- need minimum/maximum after arranging
- interval problems
- greedy choices
- anagram by sorting
- closest pair

## 6.1 Sort Numbers

```python
arr.sort()
```

or

```python
arr = sorted(arr)
```

Difference:

| Method | Changes Original? | Returns |
|---|---:|---|
| `arr.sort()` | Yes | `None` |
| `sorted(arr)` | No | new sorted list |

---

## 6.2 Sort Descending

```python
arr.sort(reverse=True)
```

---

## 6.3 Sort List of Pairs by Second Value

```python
pairs = [("a", 3), ("b", 1), ("c", 2)]
pairs.sort(key=lambda x: x[1])
```

---

## 6.4 Minimum Absolute Difference

```python
def minimum_absolute_difference(arr):
    arr.sort()
    best = float("inf")

    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if diff < best:
            best = diff

    return best
```

### Why sorting helps

The closest numbers will be adjacent after sorting.

Time: `O(n log n)`

---

## 6.5 Group Anagrams

```python
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)

    for word in words:
        key = "".join(sorted(word))
        groups[key].append(word)

    return list(groups.values())
```

### Interview explanation

> Anagrams become the same string after sorting their characters, so I use the sorted version as the dictionary key.

---

# 7. defaultdict Pattern

Use when:

- grouping values
- adjacency list graph
- collecting indexes
- avoiding `if key not in dict`

## 7.1 Group Items by Key

```python
from collections import defaultdict

def group_by_first_letter(words):
    groups = defaultdict(list)

    for word in words:
        groups[word[0]].append(word)

    return groups
```

Without `defaultdict`, you write extra checks. With `defaultdict(list)`, an empty list is created automatically.

---

## 7.2 Graph Adjacency List

```python
from collections import defaultdict

def build_graph(edges):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    return graph
```

---

# 8. Stack Pattern Using List

Python list works as stack:

```python
stack = []
stack.append(10)
stack.append(20)
last = stack.pop()
```

## 8.1 Balanced Brackets

```python
def is_balanced(s):
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack:
                return False

            if stack.pop() != pairs[ch]:
                return False

    return not stack
```

### Interview explanation

> I push opening brackets. When I see a closing bracket, it must match the latest opening bracket. That is why stack works.

---

## 8.2 Next Greater Element

```python
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []  # indexes

    for i, num in enumerate(nums):
        while stack and num > nums[stack[-1]]:
            index = stack.pop()
            result[index] = num

        stack.append(i)

    return result
```

---

# 9. Queue Pattern Using deque

Use `deque` instead of list for queue because popping from the left of a list is slow.

```python
from collections import deque

q = deque()
q.append(10)
q.append(20)
first = q.popleft()
```

## 9.1 BFS Template

```python
from collections import deque, defaultdict

def bfs(start, graph):
    visited = set()
    q = deque([start])
    visited.add(start)

    while q:
        node = q.popleft()

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)

    return visited
```

### Interview explanation

> BFS explores level by level, so I use a queue. `deque.popleft()` is efficient for removing from the front.

---

## 9.2 Queue Using Two Stacks

HackerRank has this style question.

```python
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x):
        self.in_stack.append(x)

    def transfer(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def dequeue(self):
        self.transfer()
        return self.out_stack.pop()

    def peek(self):
        self.transfer()
        return self.out_stack[-1]
```

---

# 10. Sliding Window Pattern — Pythonic Version

Use when:

- longest substring
- max sum of fixed window
- smallest window
- continuous subarray

## 10.1 Fixed Window Maximum Sum

```python
def max_sum_k(nums, k):
    window_sum = sum(nums[:k])
    best = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right - k]
        best = max(best, window_sum)

    return best
```

---

## 10.2 Longest Substring Without Repeating Characters

```python
def longest_unique_substring(s):
    last_seen = {}
    left = 0
    best = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1

        last_seen[ch] = right
        best = max(best, right - left + 1)

    return best
```

### Interview explanation

> I keep a window with unique characters. If a character repeats inside the current window, I move the left pointer after its last position.

---

# 11. Prefix Sum Pattern

Use when:

- range sum
- subarray sum
- array manipulation
- difference array

## 11.1 Prefix Sum Array

```python
def build_prefix(nums):
    prefix = [0]

    for num in nums:
        prefix.append(prefix[-1] + num)

    return prefix
```

Range sum from `l` to `r`:

```python
sum_l_r = prefix[r + 1] - prefix[l]
```

---

## 11.2 Subarray Sum Equals K

```python
from collections import defaultdict

def subarray_sum(nums, k):
    count = 0
    current = 0
    freq = defaultdict(int)
    freq[0] = 1

    for num in nums:
        current += num
        count += freq[current - k]
        freq[current] += 1

    return count
```

### Interview explanation

> If current prefix sum is `current`, then I need an earlier prefix sum equal to `current - k`. The difference gives a subarray sum of `k`.

---

## 11.3 Array Manipulation / Difference Array

HackerRank-style range update optimization.

```python
def array_manipulation(n, queries):
    diff = [0] * (n + 2)

    for a, b, k in queries:
        diff[a] += k
        diff[b + 1] -= k

    best = 0
    current = 0

    for value in diff:
        current += value
        best = max(best, current)

    return best
```

### Why this works

Instead of updating every element from `a` to `b`, mark only:

- start point: `+k`
- after end point: `-k`

Then prefix sum reconstructs final values.

---

# 12. Binary Search with bisect

Use when:

- sorted list
- find insert position
- count numbers less/greater
- lower bound / upper bound

## 12.1 Basic bisect

```python
import bisect

arr = [1, 3, 5, 7]
print(bisect.bisect_left(arr, 5))   # 2
print(bisect.bisect_right(arr, 5))  # 3
```

Difference:

| Function | Meaning |
|---|---|
| `bisect_left(arr, x)` | first position where `x` can go |
| `bisect_right(arr, x)` | position after last `x` |

---

## 12.2 Count Occurrences in Sorted Array

```python
import bisect

def count_occurrences(arr, x):
    left = bisect.bisect_left(arr, x)
    right = bisect.bisect_right(arr, x)
    return right - left
```

---

## 12.3 Count Numbers <= X

```python
import bisect

def count_less_equal(arr, x):
    return bisect.bisect_right(arr, x)
```

---

# 13. Heap Pattern Using heapq

Use when:

- top K
- kth largest/smallest
- priority queue
- merge sorted lists
- scheduling

Python `heapq` is a min-heap.

## 13.1 Kth Largest

```python
import heapq

def kth_largest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]
```

### Why this works

Keep only `k` largest elements in a min-heap. The smallest among those `k` is the kth largest.

Time: `O(n log k)`

---

## 13.2 Top K Frequent Elements

```python
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    freq = Counter(nums)
    heap = []

    for num, count in freq.items():
        heapq.heappush(heap, (count, num))

        if len(heap) > k:
            heapq.heappop(heap)

    return [num for count, num in heap]
```

---

## 13.3 Min Heap Example

```python
import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 10)

print(heapq.heappop(heap))  # 2
```

---

# 14. Math Tricks

## 14.1 Sum from 1 to N

```python
total = n * (n + 1) // 2
```

## 14.2 Sum from 0 to N

Same formula:

```python
total = n * (n + 1) // 2
```

## 14.3 Check Even / Odd

```python
if n % 2 == 0:
    print("even")
else:
    print("odd")
```

## 14.4 Check Prime

```python
def is_prime(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True
```

## 14.5 GCD

```python
import math

def gcd_of_two(a, b):
    return math.gcd(a, b)
```

---

# 15. String Tricks

## 15.1 Reverse String

```python
s[::-1]
```

## 15.2 Palindrome

```python
def is_palindrome(s):
    return s == s[::-1]
```

## 15.3 Join Characters / Words

```python
chars = ['a', 'b', 'c']
word = ''.join(chars)
```

## 15.4 Split Words

```python
words = sentence.split()
```

## 15.5 Count Characters

```python
from collections import Counter

freq = Counter(s)
```

---

# 16. List Tricks

## 16.1 Reverse List

```python
arr[::-1]
```

## 16.2 Copy List

```python
copy_arr = arr[:]
```

## 16.3 List Comprehension

```python
squares = [x * x for x in arr]
```

## 16.4 Filter Values

```python
evens = [x for x in arr if x % 2 == 0]
```

## 16.5 Flatten 2D List

```python
flat = [x for row in matrix for x in row]
```

---

# 17. Dictionary Tricks

## 17.1 Safe Get

```python
freq[num] = freq.get(num, 0) + 1
```

## 17.2 Iterate Key and Value

```python
for key, value in freq.items():
    print(key, value)
```

## 17.3 Sort Dictionary by Value

```python
items = sorted(freq.items(), key=lambda x: x[1])
```

Descending:

```python
items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
```

---

# 18. Dynamic Programming Pythonic Templates

## 18.1 Climbing Stairs

```python
def climb_stairs(n):
    if n <= 2:
        return n

    a, b = 1, 2

    for _ in range(3, n + 1):
        a, b = b, a + b

    return b
```

---

## 18.2 Coin Change

```python
def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for value in range(1, amount + 1):
        for coin in coins:
            if value - coin >= 0:
                dp[value] = min(dp[value], dp[value - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1
```

### Interview explanation

> `dp[x]` means the minimum coins needed to make amount `x`. For each amount, I try every coin and choose the minimum.

---

## 18.3 Memoization with Dictionary

```python
def fib(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
```

Note: In production code, avoid mutable default arguments. In interview quick code, it may pass, but safer version:

```python
def fib(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
```

---

# 19. Greedy Templates

## 19.1 Luck Balance Style

```python
def luck_balance(k, contests):
    important = []
    luck = 0

    for l, t in contests:
        if t == 0:
            luck += l
        else:
            important.append(l)

    important.sort(reverse=True)

    for i, value in enumerate(important):
        if i < k:
            luck += value
        else:
            luck -= value

    return luck
```

### Pattern

Sort by benefit, take the best allowed items, subtract the rest.

---

## 19.2 Minimum Jumps Style

```python
def jumping_on_clouds(c):
    jumps = 0
    i = 0

    while i < len(c) - 1:
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
        else:
            i += 1

        jumps += 1

    return jumps
```

---

# 20. Common HackerRank Problems and Best Python Trick

| Problem | Pattern | Best Python Tool |
|---|---|---|
| Sock Merchant | Frequency | `Counter` |
| Counting Valleys | State counter | loop |
| Jumping on Clouds | Greedy | loop |
| Repeated String | Math + count | `s.count('a')` |
| Sparse Arrays | Frequency | `Counter` |
| Left Rotation | Slicing | `arr[d:] + arr[:d]` |
| Array Manipulation | Difference array | list |
| Balanced Brackets | Stack | list |
| Queue using Two Stacks | Stack/Queue | list |
| Minimum Absolute Difference | Sort | `sort()` |
| Luck Balance | Greedy sort | `sort(reverse=True)` |
| Sherlock and Anagrams | Frequency of substrings | `Counter` |
| Roads and Libraries | Graph/BFS/DFS | `defaultdict`, `deque` |
| Top K Frequent | Heap/Frequency | `Counter`, `heapq` |

---

# 21. HackerRank Pythonic Solutions

## 21.1 Repeated String

```python
def repeated_string(s, n):
    full = n // len(s)
    rem = n % len(s)

    return full * s.count('a') + s[:rem].count('a')
```

### Explanation

Count how many full copies of `s` fit in `n`, then count extra `a`s in the remaining prefix.

---

## 21.2 Left Rotation

```python
def rotate_left(d, arr):
    d = d % len(arr)
    return arr[d:] + arr[:d]
```

---

## 21.3 Counting Valleys

```python
def counting_valleys(steps, path):
    level = 0
    valleys = 0

    for step in path:
        if step == 'U':
            level += 1
            if level == 0:
                valleys += 1
        else:
            level -= 1

    return valleys
```

---

## 21.4 Making Anagrams

```python
from collections import Counter

def make_anagram(a, b):
    ca = Counter(a)
    cb = Counter(b)

    deletions = 0

    all_chars = set(ca.keys()) | set(cb.keys())

    for ch in all_chars:
        deletions += abs(ca[ch] - cb[ch])

    return deletions
```

---

## 21.5 Sherlock and Valid String

```python
from collections import Counter

def is_valid_string(s):
    char_count = Counter(s)
    freq_count = Counter(char_count.values())

    if len(freq_count) == 1:
        return "YES"

    if len(freq_count) > 2:
        return "NO"

    items = list(freq_count.items())
    f1, c1 = items[0]
    f2, c2 = items[1]

    # one char occurs once, remove it completely
    if f1 == 1 and c1 == 1:
        return "YES"
    if f2 == 1 and c2 == 1:
        return "YES"

    # one frequency is exactly 1 higher and occurs once
    if abs(f1 - f2) == 1:
        if f1 > f2 and c1 == 1:
            return "YES"
        if f2 > f1 and c2 == 1:
            return "YES"

    return "NO"
```

---

# 22. When Built-ins Are Safe vs Risky

## Usually Safe in HackerRank

```python
Counter
set
defaultdict
deque
heapq
bisect
sorted
sum
max
min
map
join
split
```

## Explain Clearly in Interview

If you use a built-in, explain what it does algorithmically.

Example:

> “I use `Counter`, which internally creates a frequency dictionary. So conceptually it is the same as looping through the array and counting each value.”

## If Interviewer Says “Do Not Use Built-ins”

Then switch to the manual version from the previous file.

---

# 23. Python Tricks You Should Memorize

## 23.1 Swap Values

```python
a, b = b, a
```

## 23.2 Track Index and Value

```python
for i, value in enumerate(arr):
    print(i, value)
```

## 23.3 Reverse Loop

```python
for i in range(len(arr) - 1, -1, -1):
    print(arr[i])
```

## 23.4 Multiple Assignment

```python
a, b = 0, 1
```

## 23.5 Infinity

```python
best = float("inf")
worst = float("-inf")
```

## 23.6 Sort by Multiple Keys

```python
arr.sort(key=lambda x: (x[0], x[1]))
```

## 23.7 Descending First, Ascending Second

```python
arr.sort(key=lambda x: (-x[0], x[1]))
```

## 23.8 Convert String Digits to Integers

```python
digits = list(map(int, "12345"))
# [1, 2, 3, 4, 5]
```

---

# 24. Complexity Cheat Sheet

| Operation | Average Time |
|---|---:|
| `x in set` | `O(1)` |
| `x in dict` | `O(1)` |
| `list.append()` | `O(1)` amortized |
| `list.pop()` from end | `O(1)` |
| `list.pop(0)` | `O(n)` |
| `deque.popleft()` | `O(1)` |
| `sort()` / `sorted()` | `O(n log n)` |
| `heapq.heappush()` | `O(log n)` |
| `heapq.heappop()` | `O(log n)` |
| `bisect_left()` | `O(log n)` |
| `Counter(arr)` | `O(n)` |
| `sum(arr)` | `O(n)` |
| `max(arr)` / `min(arr)` | `O(n)` |

---

# 25. Final Interview Answer Template

Use this structure for every problem:

```text
1. I identify this as a <pattern> problem.
2. I will use <Python tool>, which represents <underlying logic>.
3. I process the input once / sort first / use a window.
4. The time complexity is <...> and space complexity is <...>.
```

Example:

```text
This is a frequency counting problem. I use Counter, which internally builds a dictionary where each key is an element and value is its frequency. Then I use those counts to compute the answer. This takes O(n) time and O(n) space.
```

---

# 26. 3-Day Emergency HackerRank Plan

## Day 1 — Python Tools + Easy Patterns

- `Counter`
- `set`
- `dict`
- `sort`
- string slicing
- Problems: Sock Merchant, Repeated String, Sparse Arrays, Left Rotation

## Day 2 — Stack, Queue, Sliding Window, Prefix Sum

- `deque`
- stack with list
- prefix sum
- difference array
- Problems: Balanced Brackets, Queue using Two Stacks, Array Manipulation, Longest Unique Substring

## Day 3 — Greedy, Binary Search, Heap, DP

- `sorted()`
- `bisect`
- `heapq`
- DP list
- Problems: Luck Balance, Minimum Absolute Difference, Top K Frequent, Coin Change

---

# 27. One-Page Final Cheat Sheet

```python
from collections import Counter, defaultdict, deque
import heapq
import bisect
import math
```

```python
# Frequency
freq = Counter(arr)

# Unique / duplicate
unique = set(arr)
has_duplicate = len(arr) != len(unique)

# Grouping
groups = defaultdict(list)
for x in arr:
    groups[key].append(x)

# Stack
stack = []
stack.append(x)
stack.pop()

# Queue
q = deque()
q.append(x)
q.popleft()

# Sort
arr.sort()
arr.sort(reverse=True)
arr.sort(key=lambda x: x[1])

# Heap
heapq.heappush(heap, x)
heapq.heappop(heap)

# Binary search position
idx = bisect.bisect_left(arr, x)

# String reverse
s[::-1]

# List rotation
arr[d:] + arr[:d]

# Fast input
arr = list(map(int, input().split()))
```

---

# 28. Most Important Mindset

Python built-ins are not cheating in HackerRank. They are part of the language. But in interviews, you should always know the underlying pattern.

For example:

- `Counter` = frequency map
- `set` = hash set
- `deque` = efficient queue
- `heapq` = priority queue
- `bisect` = binary search
- `sorted` = `O(n log n)` sorting

So your answer should sound like:

> “I am using Python’s built-in tool for this pattern, but algorithmically this is still a frequency map / heap / binary search solution.”

That is the safest and fastest way to solve HackerRank DSA in Python.

