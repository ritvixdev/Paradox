# Python DSA — HackerRank Edition (Pythonic & Built-ins)
> Use every Python weapon available. HackerRank accepts all built-ins. Write less, think faster.

---

## Why This File Exists

HackerRank is NOT a coding interview where your interviewer watches your every keystroke.  
It is a **pass/fail test** — correct output wins. Speed wins. Clarity is a bonus.

**Rule:** Use every Python built-in, trick, and one-liner you know.  
This file teaches you the Pythonic way to solve every DSA pattern — fast to write, easy to read once you know the tricks.

---

## Table of Contents

1. [Python Power Tools — Know These Cold](#0-python-power-tools--know-these-cold)
2. [Input/Output Tricks for HackerRank](#1-inputoutput-tricks-for-hackerrank)
3. [Frequency / Counter](#2-frequency--counter)
4. [Two Pointers — Pythonic Style](#3-two-pointers--pythonic-style)
5. [Sliding Window — Pythonic](#4-sliding-window--pythonic)
6. [Binary Search — bisect module](#5-binary-search--bisect-module)
7. [Stack — Pythonic](#6-stack--pythonic)
8. [Queue / BFS — deque](#7-queue--bfs--deque)
9. [Sorting — Python Superpowers](#8-sorting--python-superpowers)
10. [Linked List — Pythonic](#9-linked-list--pythonic)
11. [Recursion + Backtracking — Pythonic](#10-recursion--backtracking--pythonic)
12. [Tree Traversal — Pythonic](#11-tree-traversal--pythonic)
13. [Dynamic Programming — Pythonic](#12-dynamic-programming--pythonic)
14. [Prefix Sum — Pythonic](#13-prefix-sum--pythonic)
15. [String Tricks](#14-string-tricks)
16. [List Comprehensions — DSA Superpower](#15-list-comprehensions--dsa-superpower)
17. [Python One-Liners for Common DSA Problems](#16-python-one-liners-for-common-dsa-problems)
18. [HackerRank-Specific Patterns](#17-hackerrank-specific-patterns)
19. [Collections Module Cheatsheet](#18-collections-module-cheatsheet)
20. [itertools Cheatsheet](#19-itertools-cheatsheet)
21. [Complexity Quick Reference](#20-complexity-quick-reference)

---

## 0. Python Power Tools — Know These Cold

These are the building blocks used throughout every section below.

### Data structures in one line
```python
# List (dynamic array)
arr = [1, 2, 3, 4, 5]

# Dict (hash map)
freq = {}
freq = {'a': 1, 'b': 2}

# Set (unique elements, O(1) lookup)
seen = set()
seen = {1, 2, 3}

# Defaultdict — never KeyError
from collections import defaultdict
freq = defaultdict(int)     # missing key returns 0
graph = defaultdict(list)   # missing key returns []

# Counter — frequency map in one line
from collections import Counter
freq = Counter("banana")    # Counter({'a': 3, 'n': 2, 'b': 1})
freq = Counter([1,1,2,3])   # Counter({1: 2, 2: 1, 3: 1})

# deque — O(1) append and pop from both ends
from collections import deque
q = deque()
q.append(1)       # right push
q.appendleft(0)   # left push
q.pop()           # right pop
q.popleft()       # left pop  ← use this for BFS queue

# heapq — min-heap (priority queue)
import heapq
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
smallest = heapq.heappop(heap)   # returns 1
```

### Python tricks every DSA coder needs
```python
# Swap without temp variable
a, b = b, a

# Multiple assignment
left, right = 0, len(arr) - 1

# Negative indexing
arr[-1]   # last element
arr[-2]   # second to last

# Slice a list
arr[1:4]    # elements at index 1, 2, 3
arr[::-1]   # reversed list
arr[::2]    # every other element

# Unpack a list
first, *rest = [1, 2, 3, 4]   # first=1, rest=[2,3,4]

# Ternary (one-line if-else)
result = a if a > b else b

# Integer division and modulo
17 // 5   # = 3  (floor division)
17 % 5    # = 2  (remainder)
mid = (left + right) // 2

# Infinity
float('inf')    # larger than any number
float('-inf')   # smaller than any number

# Check membership
if x in my_dict:   # O(1)
if x in my_set:    # O(1)
if x in my_list:   # O(n) — avoid for large lists

# Enumerate — get index AND value
for i, val in enumerate(arr):
    print(i, val)

# Zip — iterate two lists together
for a, b in zip(list1, list2):
    print(a, b)

# Sorted with custom key
arr.sort(key=lambda x: x[1])           # sort by second element
arr.sort(key=lambda x: (-x[0], x[1]))  # sort descending by first, then asc by second

# String to list and back
chars = list("hello")         # ['h','e','l','l','o']
word = "".join(chars)         # "hello"

# ord and chr — character ↔ number
ord('a')    # 97
chr(97)     # 'a'
ord('z') - ord('a')   # 25  (useful for alphabet indexing)
```

---

## 1. Input/Output Tricks for HackerRank

HackerRank problems almost always start with reading input. Get fast at this.

### Reading different input formats
```python
# Single integer
n = int(input())

# Single line of space-separated integers → list
arr = list(map(int, input().split()))

# Multiple values on one line
a, b = map(int, input().split())

# Multiple lines of integers into a 2D list
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Even faster with list comprehension
matrix = [list(map(int, input().split())) for _ in range(n)]

# Read until EOF (when you don't know how many lines)
import sys
data = sys.stdin.read().split()
# then use an index pointer to consume values
idx = 0
n = int(data[idx]); idx += 1
arr = [int(data[idx+i]) for i in range(n)]; idx += n
```

### Output tricks
```python
# Print list as space-separated
print(*arr)               # same as print(' '.join(map(str, arr)))

# Print list one per line
print('\n'.join(map(str, arr)))

# Print YES/NO (common in HackerRank)
print("YES" if condition else "NO")

# Suppress trailing newline
print(result, end='')
```

### Fast I/O template (copy this for every HackerRank problem)
```python
import sys
input = sys.stdin.readline   # faster than input() for large inputs

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # your solution here
    print(result)

solve()
```

---

## 2. Frequency / Counter

### The Counter object — your best friend

```python
from collections import Counter

# Create frequency map
freq = Counter([1, 2, 2, 3, 3, 3])
# Counter({3: 2, 2: 2, 1: 1}) — wait, 3 appears 3 times

# Access like a dict — missing key returns 0 (no KeyError!)
freq[99]   # 0  ← this is the magic

# Most common elements
freq.most_common(2)     # [(3, 3), (2, 2)] — top 2

# Total count
sum(freq.values())      # total elements counted

# Subtract counts
c1 = Counter("aab")
c2 = Counter("ab")
c1.subtract(c2)         # c1 becomes Counter({'a': 1, 'b': 0})

# Add two counters
c1 + c2                 # merges, sums counts
c1 & c2                 # intersection (min of counts)
c1 | c2                 # union (max of counts)

# Elements — expands back to list
list(Counter({'a': 2, 'b': 1}).elements())  # ['a', 'a', 'b']
```

### Classic problems — Pythonic solutions

**Find duplicate in array**
```python
from collections import Counter
def has_duplicate(arr):
    return max(Counter(arr).values()) > 1

# Even shorter using set:
def has_duplicate(arr):
    return len(arr) != len(set(arr))
```

**First non-repeating character**
```python
from collections import Counter
def first_unique(s):
    freq = Counter(s)
    for ch in s:
        if freq[ch] == 1:
            return ch
    return -1
```

**Check anagram**
```python
from collections import Counter
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

# Or even shorter:
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
```

**Most frequent element**
```python
from collections import Counter
def most_frequent(arr):
    return Counter(arr).most_common(1)[0][0]
```

**Top K frequent elements**
```python
from collections import Counter
def top_k(arr, k):
    return [item for item, count in Counter(arr).most_common(k)]
```

**Group anagrams**
```python
from collections import defaultdict
def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))   # "eat","tea","ate" → ('a','e','t')
        groups[key].append(word)
    return list(groups.values())
```

**Ransom note — can you build string A from string B's characters?**
```python
from collections import Counter
def can_construct(note, magazine):
    mag_count = Counter(magazine)
    for ch, cnt in Counter(note).items():
        if mag_count[ch] < cnt:
            return False
    return True
```

---

## 3. Two Pointers — Pythonic Style

Python tricks make two pointers cleaner but the logic is the same.

### Pythonic swaps and moves
```python
# Pythonic swap
arr[left], arr[right] = arr[right], arr[left]

# Multiple assignments at once
left, right = 0, len(arr) - 1
```

### Classic problems — Pythonic

**Check palindrome**
```python
def is_palindrome(s):
    return s == s[::-1]

# With two pointers (cleaner in interviews)
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left, right = left + 1, right - 1
    return True
```

**Reverse array**
```python
# Pythonic one-liner
def reverse_array(arr):
    return arr[::-1]

# In-place
def reverse_inplace(arr):
    arr.reverse()   # modifies in place
```

**Two sum on sorted array**
```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return [left + 1, right + 1]   # 1-indexed for HackerRank
        elif s < target:
            left += 1
        else:
            right -= 1
    return []
```

**Remove duplicates from sorted array**
```python
# Pythonic — use dict.fromkeys to preserve order, then list
def remove_duplicates(arr):
    return list(dict.fromkeys(arr))

# Or with set (doesn't preserve order):
def remove_duplicates_unordered(arr):
    return list(set(arr))
```

**Three sum**
```python
def three_sum(arr):
    arr.sort()   # built-in sort is fine on HackerRank
    result = []
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        left, right = i + 1, len(arr) - 1
        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if s == 0:
                result.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return result
```

---

## 4. Sliding Window — Pythonic

### Python built-ins that help
```python
sum(arr[i:i+k])      # sum of window — but O(k), use running sum instead
max(arr[i:i+k])      # max of window — O(k), use deque for O(1)
```

### Classic problems — Pythonic

**Max sum subarray of size k**
```python
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])    # build first window with sum()
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)   # max() built-in is fine
    return max_sum
```

**Longest substring without repeating chars**
```python
def longest_unique(s):
    seen = {}
    left = max_len = 0
    for right, ch in enumerate(s):      # enumerate gives index + value
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```

**Sliding window maximum (using deque)**
```python
from collections import deque
def sliding_max(arr, k):
    dq = deque()   # stores indices, front always has max index
    result = []
    for i, val in enumerate(arr):
        # remove indices outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # remove smaller values from back
        while dq and arr[dq[-1]] < val:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(arr[dq[0]])
    return result
```

**Count anagram occurrences in string**
```python
from collections import Counter
def count_anagrams(s, pattern):
    k = len(pattern)
    need = Counter(pattern)
    window = Counter(s[:k])
    count = 1 if window == need else 0
    for i in range(k, len(s)):
        window[s[i]] += 1
        old = s[i - k]
        window[old] -= 1
        if window[old] == 0:
            del window[old]
        if window == need:
            count += 1
    return count
```

---

## 5. Binary Search — bisect module

### The bisect module — O(log n) search on sorted lists
```python
import bisect

arr = [1, 3, 5, 7, 9]

# Find insertion point (leftmost position where x could go)
bisect.bisect_left(arr, 5)    # returns 2 (arr[2] == 5)
bisect.bisect_left(arr, 4)    # returns 2 (between 3 and 5)

# Find insertion point (rightmost)
bisect.bisect_right(arr, 5)   # returns 3 (after the 5)
bisect.bisect(arr, 5)         # same as bisect_right

# Insert and keep sorted
bisect.insort(arr, 4)         # arr becomes [1, 3, 4, 5, 7, 9]
bisect.insort_left(arr, 4)    # inserts to the left of any existing 4s

# Check if element exists (search)
def exists(arr, target):
    i = bisect.bisect_left(arr, target)
    return i < len(arr) and arr[i] == target
```

### Classic problems — Pythonic

**Search in sorted array**
```python
import bisect
def binary_search(arr, target):
    i = bisect.bisect_left(arr, target)
    return i if i < len(arr) and arr[i] == target else -1
```

**First and last position**
```python
import bisect
def first_last(arr, target):
    left = bisect.bisect_left(arr, target)
    if left == len(arr) or arr[left] != target:
        return [-1, -1]
    right = bisect.bisect_right(arr, target) - 1
    return [left, right]
```

**Count of smaller numbers before each element**
```python
import bisect
def count_smaller(nums):
    sorted_list = []
    result = []
    for num in reversed(nums):
        pos = bisect.bisect_left(sorted_list, num)
        result.append(pos)
        bisect.insort(sorted_list, num)
    return result[::-1]
```

**Manual binary search — still useful**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

---

## 6. Stack — Pythonic

Python list is already a stack. `append()` = push, `pop()` = pop, `[-1]` = peek.

### Pythonic stack patterns
```python
stack = []
stack.append(x)         # push — O(1)
stack.pop()             # pop last — O(1)
stack[-1]               # peek — O(1)
bool(stack)             # True if non-empty (Pythonic empty check)
```

### Classic problems — Pythonic

**Valid parentheses**
```python
def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack        # empty stack = balanced
```

**Next greater element**
```python
def next_greater(arr):
    result = [-1] * len(arr)
    stack = []
    for i, val in enumerate(arr):
        while stack and arr[stack[-1]] < val:
            result[stack.pop()] = val
        stack.append(i)
    return result
```

**Daily temperatures**
```python
def daily_temperatures(temps):
    result = [0] * len(temps)
    stack = []   # stores indices
    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
    return result
```

**Largest rectangle in histogram**
```python
def largest_rectangle(heights):
    stack = []
    max_area = 0
    heights = heights + [0]    # sentinel to flush remaining stack
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx
        stack.append((start, h))
    return max_area
```

**Min stack — O(1) getMin**
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val):
        self.stack.append(val)
        self.mins.append(min(val, self.mins[-1] if self.mins else val))

    def pop(self):
        self.stack.pop()
        self.mins.pop()

    def get_min(self):
        return self.mins[-1]
```

---

## 7. Queue / BFS — deque

### deque is the right tool — O(1) popleft
```python
from collections import deque

q = deque()
q.append(item)      # enqueue right — O(1)
q.popleft()         # dequeue left — O(1)  ← never use list.pop(0)
q[0]                # peek front — O(1)
bool(q)             # True if non-empty
len(q)              # size
```

### BFS template — memorize this
```python
from collections import deque

def bfs(start):
    visited = set()
    q = deque([start])
    visited.add(start)
    while q:
        node = q.popleft()
        # process node
        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
```

### Classic problems — Pythonic

**Level order traversal**
```python
from collections import deque
def level_order(root):
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):    # process exactly one level
            node = q.popleft()
            level.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        result.append(level)
    return result
```

**BFS shortest path on grid**
```python
from collections import deque
def shortest_path(grid, sr, sc, er, ec):
    rows, cols = len(grid), len(grid[0])
    q = deque([(sr, sc, 0)])
    visited = {(sr, sc)}
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    while q:
        r, c, dist = q.popleft()
        if r == er and c == ec:
            return dist
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#' and (nr,nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc, dist + 1))
    return -1
```

**Number of islands (BFS)**
```python
from collections import deque
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0
    def bfs(r, c):
        q = deque([(r, c)])
        visited.add((r, c))
        while q:
            row, col = q.popleft()
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1' and (nr,nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                bfs(r, c)
                count += 1
    return count
```

---

## 8. Sorting — Python Superpowers

### Python sort is Timsort — O(n log n), stable, fast
```python
arr.sort()                      # in-place
sorted(arr)                     # returns new list
arr.sort(reverse=True)          # descending
arr.sort(key=lambda x: x[1])   # by second element
arr.sort(key=len)               # by length
arr.sort(key=lambda x: (x[0], -x[1]))  # multi-key sort
```

### Sorting tricks
```python
# Sort strings as if they were sorted chars (for anagram grouping)
sorted("listen")   # ['e', 'i', 'l', 'n', 's', 't']
"".join(sorted("listen"))  # 'eilnst'  — same for "silent" = anagram!

# Sort by frequency (most frequent first)
from collections import Counter
arr = [3, 1, 1, 2, 2, 2]
arr.sort(key=lambda x: -Counter(arr)[x])  # [2,2,2,1,1,3]

# Custom object sort
people = [('Alice', 30), ('Bob', 25), ('Charlie', 30)]
people.sort(key=lambda x: (x[1], x[0]))  # by age, then name

# Stable sort guarantee — equal elements keep original order
scores = [(85, 'Alice'), (90, 'Bob'), (85, 'Charlie')]
scores.sort(key=lambda x: x[0])  # Alice comes before Charlie (stable)

# Argsort — get sorted indices
arr = [30, 10, 20]
indices = sorted(range(len(arr)), key=lambda i: arr[i])  # [1, 2, 0]
```

### Heap / Priority Queue
```python
import heapq

# Min heap (Python default)
heap = [3, 1, 4, 1, 5]
heapq.heapify(heap)           # O(n) — converts list to heap in-place
heapq.heappush(heap, 2)       # O(log n) push
smallest = heapq.heappop(heap) # O(log n) pop smallest
heap[0]                        # peek smallest — O(1)

# Max heap — negate values
heap = []
heapq.heappush(heap, -10)
heapq.heappush(heap, -5)
largest = -heapq.heappop(heap)  # 10

# K largest elements — O(n log k)
def k_largest(arr, k):
    return heapq.nlargest(k, arr)   # built-in!

# K smallest elements
def k_smallest(arr, k):
    return heapq.nsmallest(k, arr)  # built-in!

# Merge k sorted lists
import heapq
def merge_k_sorted(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    result = []
    while heap:
        val, i, j = heapq.heappop(heap)
        result.append(val)
        if j + 1 < len(lists[i]):
            heapq.heappush(heap, (lists[i][j+1], i, j+1))
    return result
```

---

## 9. Linked List — Pythonic

In HackerRank the Node class is usually given. Focus on the algorithm.

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### Pythonic linked list tricks
```python
# Build from list quickly (for testing)
def build_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Convert to list (for printing/checking)
def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
```

### Classic problems — Pythonic

**Reverse linked list**
```python
def reverse_list(head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
        # three-way swap: save next, reverse pointer, advance both
    return prev
```

**Detect cycle**
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False
```

**Find middle**
```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow
```

**Merge two sorted lists**
```python
def merge_sorted(l1, l2):
    dummy = Node(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next, l1 = l1, l1.next
        else:
            curr.next, l2 = l2, l2.next
        curr = curr.next
    curr.next = l1 or l2    # attach remaining
    return dummy.next
```

---

## 10. Recursion + Backtracking — Pythonic

### Python recursion tricks
```python
import sys
sys.setrecursionlimit(10000)   # raise limit for deep recursion in HackerRank

# functools.lru_cache — automatic memoization decorator
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
# That's it. No manual memo dict needed.
```

### Classic problems — Pythonic

**Fibonacci with lru_cache**
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
```

**All subsets — Pythonic**
```python
def subsets(arr):
    result = [[]]
    for num in arr:
        result += [sub + [num] for sub in result]
    return result
# Explanation: start with [[]], for each number add it to every existing subset
```

**All subsets — using itertools (HackerRank-safe)**
```python
from itertools import combinations
def subsets(arr):
    result = []
    for r in range(len(arr) + 1):
        result.extend(combinations(arr, r))
    return [list(s) for s in result]
```

**All permutations — using itertools**
```python
from itertools import permutations
def all_perms(arr):
    return [list(p) for p in permutations(arr)]
```

**Combination sum — backtracking**
```python
def combination_sum(candidates, target):
    result = []
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])
            path.pop()
    candidates.sort()
    backtrack(0, [], target)
    return result
```

**Power set using bit manipulation**
```python
def subsets_bitmask(arr):
    n = len(arr)
    result = []
    for mask in range(1 << n):   # 0 to 2^n - 1
        subset = [arr[i] for i in range(n) if mask & (1 << i)]
        result.append(subset)
    return result
```

---

## 11. Tree Traversal — Pythonic

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Pythonic traversals
```python
# Inorder — Left Root Right
def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

# Preorder — Root Left Right
def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []

# Postorder — Left Right Root
def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []
```

### Classic problems — Pythonic

**Max depth**
```python
def max_depth(root):
    if not root: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

**Level order — grouped by level**
```python
from collections import deque
def level_order(root):
    if not root: return []
    result, q = [], deque([root])
    while q:
        level = [q.popleft() for _ in range(len(q))]  # snapshot one level
        # Oops — popleft inside comprehension empties q. Use this instead:
        result.append([])
        for _ in range(len(q) + len(result[-1])):  # safer pattern below

# SAFE version:
def level_order(root):
    if not root: return []
    result, q = [], deque([root])
    while q:
        level_size = len(q)
        level = []
        for _ in range(level_size):
            node = q.popleft()
            level.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        result.append(level)
    return result
```

**Diameter of binary tree**
```python
def diameter(root):
    max_d = [0]
    def depth(node):
        if not node: return 0
        left, right = depth(node.left), depth(node.right)
        max_d[0] = max(max_d[0], left + right)
        return 1 + max(left, right)
    depth(root)
    return max_d[0]
```

**Lowest common ancestor (general binary tree)**
```python
def lca(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    return root if left and right else left or right
```

---

## 12. Dynamic Programming — Pythonic

### lru_cache makes DP trivial
```python
from functools import lru_cache

# Any recursive DP — just add the decorator
@lru_cache(maxsize=None)
def dp(state):
    # base cases
    # recursive calls
    pass
```

### Classic problems — Pythonic

**Climbing stairs**
```python
from functools import lru_cache
@lru_cache(maxsize=None)
def climb(n):
    if n <= 2: return n
    return climb(n-1) + climb(n-2)

# Or bottom-up one-liner style:
def climb(n):
    a, b = 1, 2
    for _ in range(n - 2):
        a, b = b, a + b
    return b if n >= 2 else n
```

**Coin change (minimum coins)**
```python
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], dp[a - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
```

**House robber — elegant**
```python
def rob(nums):
    prev2, prev1 = 0, 0
    for num in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + num)
    return prev1
```

**Knapsack**
```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = max(
                dp[i-1][w],
                values[i-1] + dp[i-1][w - weights[i-1]] if weights[i-1] <= w else 0
            )
    return dp[n][capacity]
```

**Longest increasing subsequence — O(n log n) with bisect**
```python
import bisect
def lis(nums):
    tails = []
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)
```

**Word break**
```python
from functools import lru_cache
def word_break(s, word_dict):
    word_set = set(word_dict)
    @lru_cache(maxsize=None)
    def can_break(start):
        if start == len(s): return True
        return any(s[start:end] in word_set and can_break(end)
                   for end in range(start + 1, len(s) + 1))
    return can_break(0)
```

---

## 13. Prefix Sum — Pythonic

### Python makes prefix sums elegant
```python
import itertools

# Build prefix sum
arr = [3, 1, 4, 1, 5, 9]
prefix = list(itertools.accumulate(arr))
# [3, 4, 8, 9, 14, 23]

# With leading zero for range queries
prefix = [0] + list(itertools.accumulate(arr))
# [0, 3, 4, 8, 9, 14, 23]

# Range sum [left, right]
def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]
```

### Classic problems — Pythonic

**Range sum query**
```python
import itertools
def range_sum_queries(arr, queries):
    prefix = [0] + list(itertools.accumulate(arr))
    return [prefix[r+1] - prefix[l] for l, r in queries]
```

**Subarray sum equals k**
```python
from collections import defaultdict
def subarray_sum_k(arr, k):
    count = 0
    prefix = 0
    seen = defaultdict(int)
    seen[0] = 1
    for num in arr:
        prefix += num
        count += seen[prefix - k]
        seen[prefix] += 1
    return count
```

**Max subarray sum — Kadane's**
```python
def max_subarray(arr):
    current = best = arr[0]
    for num in arr[1:]:
        current = max(num, current + num)
        best = max(best, current)
    return best
```

**Product of array except self (no division)**
```python
def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result
```

---

## 14. String Tricks

Strings come up constantly in HackerRank. Master these.

```python
s = "Hello World"

# Case
s.lower()          # "hello world"
s.upper()          # "HELLO WORLD"

# Split and strip
s.split()          # ['Hello', 'World']
s.split(',')       # split by comma
"  hi  ".strip()   # "hi"
"  hi  ".lstrip()  # "hi  "
"  hi  ".rstrip()  # "  hi"

# Check type
"abc".isalpha()    # True — all letters
"123".isdigit()    # True — all digits
"abc123".isalnum() # True — letters or digits
" ".isspace()      # True

# Replace
s.replace("World", "Python")  # "Hello Python"

# Find
s.find("World")    # 6  (index) or -1 if not found
s.index("World")   # 6  (index) or raises ValueError
"World" in s       # True

# Count
s.count("l")       # 3

# Join
", ".join(["a", "b", "c"])   # "a, b, c"
"".join(["a", "b", "c"])     # "abc"

# Starts/ends
s.startswith("Hello")   # True
s.endswith("World")     # True

# Reverse a string
s[::-1]            # "dlroW olleH"

# Check palindrome
s == s[::-1]

# Character manipulation
ord('a')     # 97
chr(97)      # 'a'
ord(ch) - ord('a')   # 0 for 'a', 25 for 'z'  — great for alphabet indexing

# String multiplication
"ab" * 3   # "ababab"

# f-strings for output
name = "Alice"
score = 95
print(f"{name} scored {score}")
```

### String DSA patterns

**Check if string has all unique chars**
```python
def all_unique(s):
    return len(s) == len(set(s))
```

**Longest common prefix**
```python
def longest_common_prefix(strs):
    if not strs: return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
        if not prefix: return ""
    return prefix
```

**Count vowels**
```python
def count_vowels(s):
    return sum(1 for ch in s if ch.lower() in 'aeiou')
```

**Reverse words in sentence**
```python
def reverse_words(s):
    return ' '.join(s.split()[::-1])
```

**Roman numeral to integer**
```python
def roman_to_int(s):
    val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and val[s[i]] < val[s[i+1]]:
            result -= val[s[i]]
        else:
            result += val[s[i]]
    return result
```

---

## 15. List Comprehensions — DSA Superpower

List comprehensions replace loops, filters, and maps in one clean line.

```python
# Basic — square each number
squares = [x**2 for x in range(10)]

# With condition — only even
evens = [x for x in range(20) if x % 2 == 0]

# Transform — double if positive, zero otherwise
result = [x*2 if x > 0 else 0 for x in arr]

# Flatten 2D list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [x for row in matrix for x in row]   # [1,2,3,4,5,6,7,8,9]

# Dict comprehension
freq = {ch: s.count(ch) for ch in set(s)}

# Set comprehension
unique_lengths = {len(word) for word in words}

# Generator expression — lazy (memory efficient)
total = sum(x**2 for x in range(1000000))   # doesn't build list in memory

# 2D list initialization — IMPORTANT: don't use [[0]*n]*m (shares rows!)
matrix = [[0]*n for _ in range(m)]   # CORRECT
matrix = [[0]*n]*m                    # WRONG — all rows are same object
```

### DSA examples using comprehensions

```python
# Prefix sum
prefix = [sum(arr[:i+1]) for i in range(len(arr))]

# Count elements matching condition
count = sum(1 for x in arr if x > 0)

# Find all indices of a value
indices = [i for i, x in enumerate(arr) if x == target]

# Zip two lists into dict
d = {k: v for k, v in zip(keys, values)}

# Transpose a matrix
transposed = [[matrix[r][c] for r in range(rows)] for c in range(cols)]

# Filter and transform in one line
positive_squares = [x**2 for x in arr if x > 0]
```

---

## 16. Python One-Liners for Common DSA Problems

These are patterns you'll use repeatedly on HackerRank.

```python
# Reverse a list / string
arr[::-1]
s[::-1]

# Check palindrome
s == s[::-1]

# Max / min of list
max(arr)
min(arr)
max(arr, key=lambda x: abs(x))   # max by absolute value

# Sum of list
sum(arr)

# Flatten a list
flat = [x for row in matrix for x in row]

# Remove duplicates (preserving order)
list(dict.fromkeys(arr))

# Sort by multiple criteria
arr.sort(key=lambda x: (x[0], -x[1]))

# Count elements satisfying condition
sum(1 for x in arr if x > 0)

# All elements satisfy condition
all(x > 0 for x in arr)

# Any element satisfies condition
any(x > 0 for x in arr)

# Zip two lists — stops at shorter
list(zip(arr1, arr2))

# Enumerate — get index and value
list(enumerate(arr))       # [(0, val0), (1, val1), ...]
list(enumerate(arr, 1))    # [(1, val0), (2, val1), ...]  — 1-indexed

# Map — apply function to all elements
list(map(int, ['1','2','3']))   # [1, 2, 3]
list(map(str, [1, 2, 3]))       # ['1', '2', '3']

# Filter
list(filter(lambda x: x > 0, arr))

# Reduce (fold left)
from functools import reduce
product = reduce(lambda a, b: a * b, arr)

# Find index of max/min
arr.index(max(arr))
arr.index(min(arr))

# GCD and LCM
from math import gcd
gcd(12, 8)     # 4
lcm = lambda a, b: a * b // gcd(a, b)

# Power with modulo (HackerRank loves this)
pow(base, exp, mod)   # same as (base ** exp) % mod but MUCH faster

# Check if number is prime
def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

# Generate primes up to n (Sieve of Eratosthenes)
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i in range(2, n+1) if is_prime[i]]

# Binary representation
bin(10)        # '0b1010'
bin(10)[2:]    # '1010'
int('1010', 2) # 10  — binary string to int

# Bit tricks
n & (n-1)      # removes lowest set bit (0 if n is power of 2)
n & 1          # 1 if n is odd, 0 if even
n >> 1         # floor divide by 2
n << 1         # multiply by 2
```

---

## 17. HackerRank-Specific Patterns

These patterns appear in HackerRank problems constantly.

### Counting pairs
```python
# Count pairs with sum = target (sorted array)
from collections import Counter
def count_pairs(arr, target):
    freq = Counter(arr)
    count = 0
    for num in freq:
        complement = target - num
        if complement in freq:
            if complement == num:
                count += freq[num] * (freq[num] - 1) // 2
            elif complement > num:
                count += freq[num] * freq[complement]
    return count
```

### Modular arithmetic — very common
```python
MOD = 10**9 + 7

# Fast modular exponentiation
pow(2, 100, MOD)   # Python built-in handles this perfectly

# Sum with mod
total = sum(x % MOD for x in arr) % MOD

# Always apply mod BEFORE numbers get too large
result = (a * b) % MOD
result = (a + b) % MOD
```

### Graph patterns
```python
from collections import defaultdict, deque

# Build adjacency list
def build_graph(edges, directed=False):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph

# DFS (recursive)
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

# BFS — connected component
def bfs_component(graph, start):
    visited = {start}
    q = deque([start])
    while q:
        node = q.popleft()
        for nb in graph[node]:
            if nb not in visited:
                visited.add(nb)
                q.append(nb)
    return visited

# Count connected components
def count_components(n, edges):
    graph = build_graph(edges)
    visited = set()
    count = 0
    for node in range(n):
        if node not in visited:
            visited |= bfs_component(graph, node)
            count += 1
    return count
```

### Two-sum variants — all on one pattern
```python
# Two sum — unsorted, return indices
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []

# Two sum — count pairs
def count_two_sum_pairs(arr, target):
    seen = {}
    count = 0
    for num in arr:
        if target - num in seen:
            count += seen[target - num]
        seen[num] = seen.get(num, 0) + 1
    return count
```

### Matrix operations
```python
# Transpose
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

# Rotate 90° clockwise
def rotate_90(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

# Spiral order traversal
def spiral(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)              # top row
        matrix = list(zip(*matrix))[::-1]   # rotate remaining
    return result

# Diagonal traversal
def diagonals(matrix):
    rows, cols = len(matrix), len(matrix[0])
    return [[matrix[r][c] for r in range(rows) for c in range(cols) if r - c == d]
            for d in range(-(cols-1), rows)]
```

### Bit manipulation patterns
```python
# Single number (XOR trick — every number appears twice except one)
def single_number(nums):
    return reduce(lambda a, b: a ^ b, nums)
# Explanation: a ^ a = 0, a ^ 0 = a, so all pairs cancel out

# Count set bits
bin(n).count('1')
# Or: n.bit_count()  (Python 3.10+)

# Check if power of 2
def is_power_of_2(n):
    return n > 0 and (n & (n-1)) == 0

# Check kth bit is set
def is_bit_set(n, k):
    return bool(n & (1 << k))

# Set kth bit
def set_bit(n, k):
    return n | (1 << k)

# Clear kth bit
def clear_bit(n, k):
    return n & ~(1 << k)
```

---

## 18. Collections Module Cheatsheet

```python
from collections import Counter, defaultdict, deque, OrderedDict, namedtuple

# Counter — frequency counting
c = Counter("abracadabra")
c.most_common(3)          # [('a', 5), ('b', 2), ('r', 2)]
c['z']                    # 0, no KeyError
c.total()                 # sum of all counts (Python 3.10+)
+c                        # remove zero/negative counts
c1 + c2                   # add counts
c1 - c2                   # subtract (keep positive only)
c1 & c2                   # min of each count
c1 | c2                   # max of each count

# defaultdict — no KeyError on missing key
d = defaultdict(int)      # default 0
d = defaultdict(list)     # default []
d = defaultdict(set)      # default set()
d = defaultdict(lambda: float('inf'))  # custom default

# deque — double-ended queue
dq = deque(maxlen=5)      # fixed-size window!
dq.append(1)              # right
dq.appendleft(0)          # left
dq.rotate(1)              # shift right by 1

# OrderedDict — preserves insertion order (dict does this in Python 3.7+)
od = OrderedDict()
od.move_to_end('key')     # move a key to end
od.popitem(last=True)     # remove last item

# namedtuple — readable tuple with field names
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
p.x, p.y       # 3, 4
```

---

## 19. itertools Cheatsheet

```python
import itertools

# Combinations — order doesn't matter, no repeats
list(itertools.combinations([1,2,3], 2))
# [(1,2), (1,3), (2,3)]

# Combinations with replacement
list(itertools.combinations_with_replacement([1,2,3], 2))
# [(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]

# Permutations — order matters
list(itertools.permutations([1,2,3]))
# all 6 permutations

# Permutations of length r
list(itertools.permutations([1,2,3], 2))
# [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]

# Product — cartesian product (nested for loops)
list(itertools.product([1,2], [3,4]))
# [(1,3),(1,4),(2,3),(2,4)]
list(itertools.product([0,1], repeat=3))
# all 3-bit binary numbers

# Chain — flatten iterables
list(itertools.chain([1,2], [3,4], [5]))
# [1, 2, 3, 4, 5]

# Accumulate — running sum/product
list(itertools.accumulate([1,2,3,4]))    # [1, 3, 6, 10]
list(itertools.accumulate([1,2,3,4], lambda a,b: a*b))  # [1,2,6,24]

# Groupby — group consecutive equal elements
for key, group in itertools.groupby("aaabbbcc"):
    print(key, list(group))
# a ['a','a','a']
# b ['b','b','b']
# c ['c','c']

# Groupby with key — sort first!
words = ['apple', 'ant', 'bear', 'bat']
words.sort(key=lambda x: x[0])
for letter, group in itertools.groupby(words, key=lambda x: x[0]):
    print(letter, list(group))

# Islice — lazy slice
list(itertools.islice(range(100), 5, 10))  # [5, 6, 7, 8, 9]

# Count, cycle, repeat
itertools.count(10)           # 10, 11, 12, ... (infinite)
itertools.cycle([1,2,3])      # 1, 2, 3, 1, 2, 3, ... (infinite)
list(itertools.repeat(5, 3))  # [5, 5, 5]
```

---

## 20. Complexity Quick Reference

| Operation | Python code | Time |
|---|---|---|
| List append | `arr.append(x)` | O(1) amortized |
| List pop end | `arr.pop()` | O(1) |
| List pop front | `arr.pop(0)` | O(n) — use deque! |
| List insert | `arr.insert(i, x)` | O(n) |
| List search | `x in arr` | O(n) |
| Dict get/set | `d[k]`, `d[k]=v` | O(1) avg |
| Dict search | `k in d` | O(1) avg |
| Set add | `s.add(x)` | O(1) avg |
| Set search | `x in s` | O(1) avg |
| heappush | `heapq.heappush(h, x)` | O(log n) |
| heappop | `heapq.heappop(h)` | O(log n) |
| Sort list | `arr.sort()` | O(n log n) |
| bisect search | `bisect.bisect_left(arr, x)` | O(log n) |
| Counter build | `Counter(arr)` | O(n) |
| deque append | `dq.append(x)` | O(1) |
| deque popleft | `dq.popleft()` | O(1) |
| String slice | `s[i:j]` | O(j-i) |
| String reverse | `s[::-1]` | O(n) |
| zip | `zip(a, b)` | O(min(len(a), len(b))) |
| enumerate | `enumerate(arr)` | O(n) |

---

*HackerRank accepts all Python built-ins. Use them. Write clean, fast, Pythonic code.*

*Understand the pattern → reach for the right tool → write it confidently.*