# Python DSA — Complete Interview Prep Guide
> Built for normal coders. No built-in shortcuts. Pure logic, from memory.

---

## How to Actually Use This File

Most people read cheatsheets and feel ready. They aren't. Here is the only method that works:

1. Read the **"Real-world mental model"** — understand it like a story, not a formula
2. Trace the **dry-run example** line by line with a pen
3. Look away and **write the template from scratch**
4. Solve the **practice problems** in order (Easy → Medium → Hard)
5. Check your solution against the **common mistakes** list

---

## Table of Contents

1. [Pattern Recognition — Read This First](#0-pattern-recognition--read-this-first)
2. [Frequency / Hash Map](#1-frequency--hash-map)
3. [Two Pointers](#2-two-pointers)
4. [Sliding Window](#3-sliding-window)
5. [Binary Search](#4-binary-search)
6. [Stack](#5-stack)
7. [Queue + BFS](#6-queue--bfs)
8. [Linked List](#7-linked-list)
9. [Sorting Algorithms](#8-sorting-algorithms)
10. [Recursion & Backtracking](#9-recursion--backtracking)
11. [Tree Traversal](#10-tree-traversal)
12. [Dynamic Programming](#11-dynamic-programming)
13. [Prefix Sum](#12-prefix-sum)
14. [Thinking Framework — How to Approach Any Problem](#13-thinking-framework--how-to-approach-any-problem)
15. [Dry-Run Practice Sheet](#14-dry-run-practice-sheet)
16. [Common Mistakes Journal](#15-common-mistakes-journal)
17. [Practice Problems Bank — Difficulty Rated](#16-practice-problems-bank--difficulty-rated)
18. [7-Day Study Plan](#17-7-day-study-plan)
19. [Interview Simulation Checklist](#18-interview-simulation-checklist)
20. [Quick Reference — Trigger Words](#19-quick-reference--trigger-words)
21. [Built-ins to Avoid](#20-built-ins-to-avoid)
22. [Time & Space Complexity Sheet](#21-time--space-complexity-sheet)

---

## 0. Pattern Recognition — Read This First

Before writing a single line of code in an interview, spend 2 minutes asking yourself these questions:

```
Q1: Is the input sorted?
    YES → Binary Search or Two Pointers
    NO  → Hash Map or Sorting first

Q2: Are we looking for a subarray or substring?
    YES → Sliding Window (fixed size k → Template A, variable → Template B)

Q3: Are we looking for pairs or comparing from both ends?
    YES → Two Pointers

Q4: Do we need to count, find duplicates, or check frequency?
    YES → Hash Map

Q5: Does order of processing matter (LIFO / FIFO)?
    LIFO (last in first out) → Stack
    FIFO (first in first out) → Queue

Q6: Are we exploring all paths, combinations, or choices?
    YES → Recursion + Backtracking

Q7: Is it a tree or graph?
    Depth first → DFS (Recursion or Stack)
    Level by level → BFS (Queue)

Q8: Does the problem say "minimum cost", "maximum ways", "count paths"?
    YES → Dynamic Programming

Q9: Range sum queries on array?
    YES → Prefix Sum
```

---

## 1. Frequency / Hash Map

### Real-world mental model
Imagine you are a teacher taking attendance. You have a notebook. Every time a student's name is called, you put a tally next to their name. At the end, you can answer "how many times did X appear?" in O(1) time. That notebook is your hash map (dict).

### Core idea
Count occurrences using a plain dict. Trades memory (O(n) space) for speed (O(1) lookup).

### Trigger words
`count`, `frequency`, `duplicate`, `most common`, `anagram`, `appears more than once`, `unique`, `pair`

### Template — write this from memory
```python
def frequency_map(arr):
    freq = {}
    for item in arr:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq
```

### Dry-run trace
```
Input: arr = ['a', 'b', 'a', 'c', 'b', 'a']

Step 1: item='a' → freq = {'a': 1}
Step 2: item='b' → freq = {'a': 1, 'b': 1}
Step 3: item='a' → freq = {'a': 2, 'b': 1}
Step 4: item='c' → freq = {'a': 2, 'b': 1, 'c': 1}
Step 5: item='b' → freq = {'a': 2, 'b': 2, 'c': 1}
Step 6: item='a' → freq = {'a': 3, 'b': 2, 'c': 1}
```

### Classic Solutions

**Find duplicate in array**
```python
def has_duplicate(arr):
    seen = {}
    for num in arr:
        if num in seen:
            return True      # found it on second visit
        seen[num] = 1
    return False
```

**First non-repeating character**
```python
def first_unique(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    for ch in s:              # second pass — preserve order
        if freq[ch] == 1:
            return ch
    return -1
```

**Check if two strings are anagrams**
```python
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    freq = {}
    for ch in s1:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    for ch in s2:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1
    return True
```

**Most frequent element**
```python
def most_frequent(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    max_count = 0
    result = arr[0]
    for key in freq:
        if freq[key] > max_count:
            max_count = freq[key]
            result = key
    return result
```

### Common mistakes
- Forgetting to handle empty input — always check `if len(arr) == 0: return`
- Using `set()` instead of dict — set can't store counts
- Second pass forgetting to iterate original string (not the dict) to preserve order

---

## 2. Two Pointers

### Real-world mental model
Imagine squeezing a water balloon from both sides. You have one hand on the left end and one on the right end. You move whichever hand will bring you closer to the target. This avoids checking every pair — which would be like grabbing random parts of the balloon.

### Core idea
Two index variables moving toward each other (or same direction) to eliminate a nested O(n²) loop down to O(n).

### Trigger words
`sorted array`, `pair with sum`, `palindrome`, `reverse`, `compare from both ends`, `remove duplicates`, `three sum`, `container with most water`

### When to use which template

| Situation | Template |
|---|---|
| Sorted array, looking for pair | Opposite ends (left=0, right=end) |
| Remove elements, partition | Same direction (slow/fast) |
| Cycle detection in linked list | Fast/slow (Floyd's) |

### Template A — Opposite ends
```python
def two_pointer_opposite(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:               # MUST be < not <=
        current = arr[left] + arr[right]
        if current == target:
            return [left, right]
        elif current < target:
            left += 1                 # sum too small → move left up
        else:
            right -= 1                # sum too big → move right down
    return []
```

### Template B — Same direction (slow/fast)
```python
def two_pointer_same(arr):
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != 0:            # keep condition
            arr[slow] = arr[fast]
            slow += 1
    return slow                       # slow = new valid length
```

### Dry-run trace — Pair with target sum
```
arr = [1, 3, 5, 7, 9],  target = 10

left=0(1), right=4(9) → sum=10 → FOUND → return [0,4]

---
arr = [1, 3, 5, 7, 9],  target = 8

left=0(1), right=4(9) → sum=10 > 8 → right=3
left=0(1), right=3(7) → sum=8  = 8 → FOUND → return [0,3]

---
arr = [1, 3, 5, 7, 9],  target = 4

left=0(1), right=4(9) → sum=10 > 4 → right=3
left=0(1), right=3(7) → sum=8  > 4 → right=2
left=0(1), right=2(5) → sum=6  > 4 → right=1
left=0(1), right=1(3) → sum=4  = 4 → FOUND → return [0,1]
```

### Classic Solutions

**Pair with target sum (sorted)**
```python
def pair_sum(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return (arr[left], arr[right])
        elif s < target:
            left += 1
        else:
            right -= 1
    return None
```

**Check palindrome**
```python
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

**Reverse array in-place**
```python
def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
```

**Remove duplicates from sorted array**
```python
def remove_duplicates(arr):
    if len(arr) == 0:
        return 0
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1
```

**Three sum = 0**
```python
def three_sum(arr):
    arr = merge_sort(arr)       # sort first — see section 8
    result = []
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i-1]:
            continue            # skip duplicates
        left = i + 1
        right = len(arr) - 1
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

### Common mistakes
- Using `while left < right` is correct — `<=` causes index collision
- Forgetting array must be sorted before two pointers
- On three sum: not skipping duplicate `i` values → duplicate triplets in result

---

## 3. Sliding Window

### Real-world mental model
Imagine looking through a train window. The window frame stays the same size, but the scenery outside keeps changing as the train moves. You never need to look at all the scenery at once — just what's in the frame right now. For dynamic windows, imagine stretching/shrinking a rubber band on a number line.

### Core idea
Instead of recomputing the subarray sum from scratch every step (O(n²)), maintain a running window — add the new right element, remove the old left element. O(n).

### Trigger words
`subarray`, `substring`, `window of size k`, `longest`, `maximum sum contiguous`, `at most k distinct`, `minimum length subarray`

### Template A — Fixed window size k
```python
def fixed_window(arr, k):
    window_sum = 0
    for i in range(k):               # build the first window
        window_sum += arr[i]
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i]         # add incoming right
        window_sum -= arr[i - k]     # remove outgoing left
        if window_sum > max_sum:
            max_sum = window_sum
    return max_sum
```

### Template B — Dynamic window (condition-based)
```python
def dynamic_window(arr, target):
    left = 0
    window_sum = 0
    result = 0
    for right in range(len(arr)):
        window_sum += arr[right]     # always expand right
        while window_sum > target:   # shrink from left if violated
            window_sum -= arr[left]
            left += 1
        length = right - left + 1
        if length > result:
            result = length
    return result
```

### Dry-run trace — Max sum subarray of size 3
```
arr = [2, 1, 5, 1, 3, 2],  k = 3

Build first window [2,1,5]: window_sum = 8, max_sum = 8

i=3: add arr[3]=1 → 9, remove arr[0]=2 → 7. max_sum still 8
i=4: add arr[4]=3 → 10, remove arr[1]=1 → 9. max_sum = 9
i=5: add arr[5]=2 → 11, remove arr[2]=5 → 6. max_sum still 9

Answer: 9  (window [1,3,2] at index 3-5... wait: actually [5,1,3]=9 ✓)
```

### Classic Solutions

**Maximum sum subarray of size k**
```python
def max_sum_subarray(arr, k):
    window_sum = 0
    for i in range(k):
        window_sum += arr[i]
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        if window_sum > max_sum:
            max_sum = window_sum
    return max_sum
```

**Longest substring without repeating characters**
```python
def longest_unique_substring(s):
    seen = {}           # char → last seen index
    left = 0
    max_len = 0
    for right in range(len(s)):
        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1     # jump left past duplicate
        seen[s[right]] = right
        length = right - left + 1
        if length > max_len:
            max_len = length
    return max_len
```

**Smallest subarray with sum >= target**
```python
def smallest_subarray(arr, target):
    left = 0
    window_sum = 0
    min_len = len(arr) + 1
    for right in range(len(arr)):
        window_sum += arr[right]
        while window_sum >= target:
            length = right - left + 1
            if length < min_len:
                min_len = length
            window_sum -= arr[left]
            left += 1
    if min_len == len(arr) + 1:
        return 0
    return min_len
```

### Common mistakes
- Fixed window: forgetting to build the first `k`-window before the main loop
- Dynamic window: putting `if` instead of `while` for the shrink condition — must keep shrinking until condition is met
- Not checking for empty array before accessing `arr[0]`

---

## 4. Binary Search

### Real-world mental model
Think of a dictionary (the paper kind). You never start at page 1 and flip forward. You open to the middle, check if the word is before or after, then repeat on the relevant half. Each step cuts the remaining search in half. 1000 pages → 10 steps max.

### Core idea
On any sorted structure, eliminate half the remaining options each iteration. O(log n) — the most powerful complexity improvement available.

### Trigger words
`sorted array`, `find index`, `search`, `rotated sorted`, `find minimum`, `position`, `first/last occurrence`

### Template
```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:              # <= because single element is valid
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1            # target is in right half
        else:
            right = mid - 1           # target is in left half
    return -1
```

### Dry-run trace
```
arr = [1, 3, 5, 7, 9, 11, 13],  target = 7

left=0, right=6, mid=3 → arr[3]=7 → FOUND at index 3

---
arr = [1, 3, 5, 7, 9, 11, 13],  target = 6

left=0, right=6, mid=3 → arr[3]=7 > 6 → right=2
left=0, right=2, mid=1 → arr[1]=3 < 6 → left=2
left=2, right=2, mid=2 → arr[2]=5 < 6 → left=3
left=3 > right=2 → STOP → return -1
```

### Classic Solutions

**Find first occurrence of target**
```python
def first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1     # don't stop — keep looking left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result
```

**Search in rotated sorted array**
```python
def search_rotated(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:           # left half is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:                               # right half is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

**Find integer square root**
```python
def int_sqrt(n):
    if n < 2:
        return n
    left = 1
    right = n // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            left = mid + 1
        else:
            right = mid - 1
    return right    # floor of square root
```

### Common mistakes
- Using `while left < right` — misses the single element case
- `mid = (left + right) / 2` — use `//` for integer division
- Not handling rotated array: assuming left half always sorted

---

## 5. Stack

### Real-world mental model
A stack of plates. You always add to the top, always take from the top. The last plate you put on is the first one you take off. LIFO. Classic use: browser back button (each page you visit goes on the stack, back = pop).

### Core idea
Use a plain Python list. `append()` = push. `pop()` = pop. `list[-1]` = peek (look without removing).

### Trigger words
`balanced brackets`, `matching parentheses`, `undo`, `valid sequence`, `next greater element`, `evaluate expression`, `DFS iterative`

### Template
```python
stack = []
stack.append(item)          # push
top = stack[-1]             # peek — DON'T pop
item = stack.pop()          # pop
is_empty = len(stack) == 0
```

### Dry-run trace — Balanced brackets
```
Input: s = "({[]})"

ch='(' → open → stack=['(']
ch='{' → open → stack=['(', '{']
ch='[' → open → stack=['(', '{', '[']
ch=']' → close → pairs[']']='[', stack[-1]='[' ✓ → pop → stack=['(', '{']
ch='}' → close → pairs['}']='{ ', stack[-1]='{' ✓ → pop → stack=['(']
ch=')' → close → pairs[')']='(', stack[-1]='(' ✓ → pop → stack=[]

len(stack)==0 → True → BALANCED
```

### Classic Solutions

**Valid parentheses**
```python
def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if len(stack) == 0 or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0
```

**Next greater element**
```python
def next_greater(arr):
    result = [-1] * len(arr)
    stack = []              # stores indices, not values
    for i in range(len(arr)):
        while len(stack) > 0 and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)
    return result
```

**Min stack (stack that returns minimum in O(1))**
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []    # parallel stack tracking minimums

    def push(self, val):
        self.stack.append(val)
        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def get_min(self):
        return self.min_stack[-1]
```

### Common mistakes
- Checking `stack[-1]` on an empty list → IndexError. Always check `len(stack) > 0` first
- Forgetting `return len(stack) == 0` at the end of bracket matching
- Storing values instead of indices in next-greater-element (you need index to update result)

---

## 6. Queue + BFS

### Real-world mental model
A queue at a coffee shop. First person in, first person served. FIFO. BFS uses this to explore a graph level by level — like ripples spreading from a stone dropped in water. All nodes at distance 1 first, then distance 2, etc.

### Core idea
Simulate queue with a list and a `front` index pointer. Never use `.pop(0)` — it shifts the whole list and is O(n).

### Trigger words
`level order`, `BFS`, `shortest path`, `minimum steps`, `nodes at distance k`, `connected components`

### Template (no deque, no pop(0))
```python
queue = []
front = 0
queue.append(item)               # enqueue
item = queue[front]; front += 1  # dequeue
is_empty = front >= len(queue)
```

### Dry-run trace — Level order traversal
```
Tree:       1
           / \
          2   3
         / \
        4   5

queue=[1], front=0

Pop node(1): result=[1], enqueue 2,3 → queue=[1,2,3], front=1
Pop node(2): result=[1,2], enqueue 4,5 → queue=[1,2,3,4,5], front=2
Pop node(3): result=[1,2,3], no children → front=3
Pop node(4): result=[1,2,3,4], no children → front=4
Pop node(5): result=[1,2,3,4,5], no children → front=5

front(5) >= len(5) → DONE
```

### Classic Solutions

**BFS level order traversal**
```python
def level_order(root):
    if root is None:
        return []
    result = []
    queue = [root]
    front = 0
    while front < len(queue):
        node = queue[front]
        front += 1
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
```

**BFS on grid — shortest path**
```python
def bfs_grid(grid, start_r, start_c, end_r, end_c):
    rows = len(grid)
    cols = len(grid[0])
    visited = {}
    queue = [(start_r, start_c, 0)]   # (row, col, distance)
    front = 0
    visited[(start_r, start_c)] = True
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    while front < len(queue):
        r, c, dist = queue[front]
        front += 1
        if r == end_r and c == end_c:
            return dist
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] != '#' and (nr, nc) not in visited:
                    visited[(nr, nc)] = True
                    queue.append((nr, nc, dist + 1))
    return -1
```

### Common mistakes
- Using `queue.pop(0)` — this is O(n), use front index instead
- Forgetting to mark nodes as visited before enqueuing → infinite loop
- Not checking `if root is None` at the start

---

## 7. Linked List

### Real-world mental model
A treasure hunt where each clue tells you where the next clue is. You can only follow the chain from the start — you cannot jump to clue 5 directly. To reverse the chain, you must change where each clue points, while carefully remembering where you came from.

### Core idea
Nodes with a `.next` pointer. No random access by index. Always save `next_node = current.next` before redirecting `.next` or you lose the rest of the chain.

### Trigger words
`linked list`, `reverse`, `detect cycle`, `merge sorted`, `nth from end`, `middle node`, `remove duplicates`

### Node class
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
```

### Dry-run trace — Reverse linked list
```
Original: 1 → 2 → 3 → 4 → None

prev=None, current=1
  next_node = 2
  1.next = None  →  None ← 1
  prev=1, current=2

prev=1, current=2
  next_node = 3
  2.next = 1     →  None ← 1 ← 2
  prev=2, current=3

prev=2, current=3
  next_node = 4
  3.next = 2     →  None ← 1 ← 2 ← 3
  prev=3, current=4

prev=3, current=4
  next_node = None
  4.next = 3     →  None ← 1 ← 2 ← 3 ← 4
  prev=4, current=None

Return prev = 4  (new head)
```

### Classic Solutions

**Reverse a linked list**
```python
def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next    # 1. save next
        current.next = prev         # 2. reverse pointer
        prev = current              # 3. advance prev
        current = next_node         # 4. advance current
    return prev
```

**Detect cycle — Floyd's tortoise and hare**
```python
def has_cycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next            # moves 1 step
        fast = fast.next.next       # moves 2 steps
        if slow == fast:            # they meet inside the cycle
            return True
    return False
```

**Find middle node**
```python
def find_middle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow     # when fast reaches end, slow is at middle
```

**Delete nth node from end**
```python
def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    fast = dummy
    slow = dummy
    for i in range(n + 1):          # advance fast by n+1 steps
        fast = fast.next
    while fast is not None:          # move both until fast hits end
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next       # skip the target node
    return dummy.next
```

### Common mistakes
- Not saving `next_node` before changing `.next` — you lose the rest of the list
- `fast.next.next` without checking `fast.next is not None` first → crash
- Not using a dummy node for delete → edge case when deleting head

---

## 8. Sorting Algorithms

### When to use which sort

| Sort | Time | Space | Use when |
|---|---|---|---|
| Bubble | O(n²) | O(1) | n < 10, dead simple to write |
| Merge | O(n log n) | O(n) | Interview default, stable sort |
| Quick | O(n log n) avg | O(log n) | In-place needed, avg case fine |

### Bubble Sort
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

### Merge Sort — memorize this one
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
```

### Quick Sort
```python
def quick_sort(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

### Common mistakes
- Merge sort: forgetting the two "drain remaining elements" while-loops after the main merge
- Quick sort: passing the wrong `low`/`high` bounds in recursive calls
- Calling `quick_sort(arr)` without `low=0, high=len(arr)-1`

---

## 9. Recursion & Backtracking

### Real-world mental model
**Recursion:** Russian nesting dolls. To open the outermost doll, you open it and find a smaller version of the same problem. You keep opening until you find the tiny solid doll (base case). Then you close them back up.

**Backtracking:** Solving a maze. You walk down a path, if it's a dead end, you step back (backtrack) and try the next path. You explore every possible path systematically.

### Core idea
Every recursive function needs exactly two things: a base case (when to stop) and a recursive call (smaller version of the problem). Backtracking = recursion + undo step.

### Trigger words
`all combinations`, `all permutations`, `generate all`, `subsets`, `N-Queens`, `solve maze`, `word search`

### Template — Recursion
```python
def recursive(n):
    if n == 0:              # BASE CASE — must come first
        return 1
    return n * recursive(n - 1)   # recursive call on smaller input
```

### Template — Backtracking
```python
def backtrack(start, current, result, arr):
    result.append(current[:])       # snapshot current state
    for i in range(start, len(arr)):
        current.append(arr[i])      # CHOOSE
        backtrack(i + 1, current, result, arr)
        current.pop()               # UN-CHOOSE (backtrack)
```

### Classic Solutions

**All subsets**
```python
def subsets(arr):
    result = []
    def backtrack(start, current):
        result.append(current[:])       # include empty set too
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()
    backtrack(0, [])
    return result
```

**All permutations**
```python
def permutations(arr):
    result = []
    def backtrack(current, used):
        if len(current) == len(arr):
            result.append(current[:])
            return
        for i in range(len(arr)):
            if used[i]:
                continue
            used[i] = True
            current.append(arr[i])
            backtrack(current, used)
            current.pop()
            used[i] = False
    backtrack([], [False] * len(arr))
    return result
```

**Combination sum (pick numbers that add to target)**
```python
def combination_sum(candidates, target):
    result = []
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])  # i not i+1 (can reuse)
            current.pop()
    backtrack(0, [], target)
    return result
```

### Common mistakes
- Forgetting `current[:]` (copy) — appending `current` gives a reference, all results end up the same
- Missing the base case → infinite recursion → stack overflow
- Not calling `current.pop()` after recursion → the undo step is the whole point of backtracking

---

## 10. Tree Traversal

### Real-world mental model
A family tree. DFS is like going depth-first through one branch — following a family line all the way to the youngest before coming back. BFS is like exploring by generation: all grandparents first, then all parents, then all children.

### Core idea
Three DFS orders (remember with "root position"): **Pre**order = Root first. **In**order = Root in middle (gives sorted output for BST). **Post**order = Root last.

### Tree node
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

### DFS templates
```python
def inorder(root):      # Left → Root → Right  ← sorted order in BST
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):     # Root → Left → Right  ← copy/serialize tree
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):    # Left → Right → Root  ← delete tree / evaluate
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

### Classic Solutions

**Maximum depth**
```python
def max_depth(root):
    if root is None:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    if left_depth > right_depth:
        return left_depth + 1
    return right_depth + 1
```

**Check if balanced**
```python
def is_balanced(root):
    def height(node):
        if node is None:
            return 0
        left = height(node.left)
        right = height(node.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1
    return height(root) != -1
```

**Lowest common ancestor (BST)**
```python
def lca(root, p, q):
    while root is not None:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
    return None
```

### Common mistakes
- Forgetting the base case `if root is None: return []` — crashes on empty trees
- Confusing inorder/preorder/postorder — just remember where "root" sits in the name
- For balanced check: returning `-1` as a sentinel (not a real height) to signal imbalance — don't confuse with actual depth

---

## 11. Dynamic Programming

### Real-world mental model
You are climbing stairs. You write the answer on each step as you go. When you reach step 10, you don't recalculate steps 1-9 — you just read what you already wrote. DP is about never solving the same subproblem twice.

### Core idea
Two approaches to the same thing:
- **Memoization** (top-down): start from the big problem, recurse, cache results
- **Tabulation** (bottom-up): start from base cases, fill a table forward

### Trigger words
`minimum cost`, `maximum profit`, `count ways`, `longest subsequence`, `can you reach`, `how many paths`, `optimal`

### When each approach fits

| Approach | When to use |
|---|---|
| Memoization | Easier to reason about, write top-down recursion first |
| Tabulation | Avoids recursion limit, slightly faster in practice |

### Template — Memoization
```python
def dp_memo(n, memo=None):
    if memo is None:
        memo = {}              # don't use mutable default arg
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = dp_memo(n-1, memo) + dp_memo(n-2, memo)
    return memo[n]
```

### Template — Tabulation
```python
def dp_table(n):
    table = [0] * (n + 1)
    table[0] = 0               # base case
    table[1] = 1               # base case
    for i in range(2, n + 1):
        table[i] = table[i-1] + table[i-2]
    return table[n]
```

### Classic Solutions

**Climbing stairs**
```python
def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

**0/1 Knapsack**
```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]          # skip item i
            if weights[i-1] <= w:
                take = values[i-1] + dp[i-1][w - weights[i-1]]
                if take > dp[i][w]:
                    dp[i][w] = take         # take item i
    return dp[n][capacity]
```

**Longest common subsequence**
```python
def lcs(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
    return dp[m][n]
```

**Coin change (minimum coins)**
```python
def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)   # fill with impossible value
    dp[0] = 0
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                if dp[a - coin] + 1 < dp[a]:
                    dp[a] = dp[a - coin] + 1
    if dp[amount] > amount:
        return -1
    return dp[amount]
```

### Common mistakes
- Using `memo={}` as default arg — Python shares this across calls. Always use `None` then create inside
- Off-by-one in table size — always `[0] * (n + 1)` to include index n
- Forgetting base cases before the loop
- Knapsack: row `i` uses row `i-1` — don't overwrite in-place unless you understand 1D optimization

---

## 12. Prefix Sum

### Real-world mental model
Running odometer in a car. At any point you can know how far you've traveled between two cities by subtracting the odometer reading at the start of the leg from the reading at the end. You never need to re-drive the route.

### Core idea
Build a cumulative sum array once (O(n)), then answer range sum queries in O(1).

### Trigger words
`range sum`, `sum between index i and j`, `subarray sum equals k`, `running total`, `balance point`

### Template
```python
def build_prefix(arr):
    prefix = [0] * (len(arr) + 1)   # prefix[0] = 0 (empty prefix)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix

def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]   # sum from left to right inclusive
```

### Dry-run trace
```
arr     = [3,  1,  4,  1,  5,  9]
index   =  0   1   2   3   4   5

prefix  = [0,  3,  4,  8,  9,  14, 23]
index   =  0   1   2   3   4   5   6

Sum from index 2 to 4: prefix[5] - prefix[2] = 14 - 4 = 10
Check: arr[2]+arr[3]+arr[4] = 4+1+5 = 10 ✓
```

### Classic Solutions

**Subarray sum equals k**
```python
def subarray_sum_k(arr, k):
    count = 0
    prefix_sum = 0
    seen = {0: 1}               # sum 0 seen once (empty prefix)
    for num in arr:
        prefix_sum += num
        needed = prefix_sum - k
        if needed in seen:
            count += seen[needed]
        if prefix_sum in seen:
            seen[prefix_sum] += 1
        else:
            seen[prefix_sum] = 1
    return count
```

**Maximum subarray sum — Kadane's algorithm**
```python
def max_subarray(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    for i in range(1, len(arr)):
        if current_sum + arr[i] > arr[i]:
            current_sum = current_sum + arr[i]
        else:
            current_sum = arr[i]    # start fresh from arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
```

### Common mistakes
- `prefix` size should be `len(arr) + 1`, not `len(arr)` — you need that leading 0
- Range sum formula: `prefix[right + 1] - prefix[left]`, not `prefix[right] - prefix[left]`
- Subarray sum equals k: always initialize `seen = {0: 1}` — the empty prefix with sum 0

---

## 13. Thinking Framework — How to Approach Any Problem

Use this every time, in this order. Say it out loud in the interview.

```
Step 1 — UNDERSTAND (2 min)
  - Repeat the problem in your own words
  - Ask: What is the input? What is the output?
  - Ask: What are the constraints? (size of n, negative numbers?)
  - Write 1-2 small examples by hand

Step 2 — IDENTIFY THE PATTERN (1 min)
  - Run the "Pattern Recognition" questions from Section 0
  - If unsure, start with brute force and look for the bottleneck

Step 3 — BRUTE FORCE FIRST (2 min)
  - Say: "The naive approach is O(n²) because..."
  - Write or describe it even if you don't code it
  - This shows you understand the problem

Step 4 — OPTIMIZE (2 min)
  - Say: "I can improve this using [pattern] because..."
  - State the new time and space complexity

Step 5 — CODE (10-15 min)
  - Write the template skeleton first
  - Fill in the logic
  - Handle edge cases last (empty array, single element, all same values)

Step 6 — TEST (3 min)
  - Trace through your own example
  - Test the edge case
  - Fix any bugs out loud
```

### Edge cases checklist — always check these
```
[ ] Empty input: arr = [], s = ""
[ ] Single element: arr = [5]
[ ] All same elements: arr = [3, 3, 3]
[ ] Negative numbers (if applicable)
[ ] Target not found (return -1 or None or 0?)
[ ] Very large input (will O(n²) time out?)
```

---

## 14. Dry-Run Practice Sheet

### How to dry-run effectively
Never just read code. Pick an input, trace it by hand, write every variable value at every step.

### Template for dry-running any function
```
Function: _______________
Input: __________________

Variables at start:
  left = ___
  right = ___
  result = ___

Step 1: [variable changes]
Step 2: [variable changes]
...
Final state: ___
Output: ___
Expected: ___
Match? YES / NO
```

### Practice: dry-run this yourself (answers below)
```python
# What does this return for arr=[2,7,11,15], target=9?
def find_pair(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []
```
Answer: `left=0(2), right=3(15) → 17>9 → right=2; left=0(2), right=2(11) → 13>9 → right=1; left=0(2), right=1(7) → 9=9 → return [0,1]`

---

## 15. Common Mistakes Journal

Keep this list in your head. These are the bugs that appear in 90% of failed interview attempts.

### Off-by-one errors
```python
# WRONG — misses last element
for i in range(len(arr) - 1):

# RIGHT — when you need all elements
for i in range(len(arr)):

# WRONG — two pointers stopping too early
while left < right - 1:

# RIGHT
while left < right:
```

### Losing the next pointer in linked list
```python
# WRONG — you lose the chain
current.next = prev
current = current.next    # this is now prev, not the original next!

# RIGHT
next_node = current.next   # SAVE FIRST
current.next = prev
current = next_node
```

### Mutable default argument in DP
```python
# WRONG — memo persists between function calls
def dp(n, memo={}):

# RIGHT
def dp(n, memo=None):
    if memo is None:
        memo = {}
```

### Binary search loop condition
```python
# WRONG — misses single element case
while left < right:

# RIGHT
while left <= right:
```

### Forgetting to copy in backtracking
```python
# WRONG — all results point to same list object
result.append(current)

# RIGHT
result.append(current[:])
```

### Prefix sum size
```python
# WRONG — no room for the leading zero
prefix = [0] * len(arr)

# RIGHT
prefix = [0] * (len(arr) + 1)
```

### Stack empty check before peek
```python
# WRONG — crashes on empty stack
if stack[-1] == target:

# RIGHT
if len(stack) > 0 and stack[-1] == target:
```

---

## 16. Practice Problems Bank — Difficulty Rated

Work through in order. Don't skip ahead.

### Hash Map

| # | Problem | Difficulty | Pattern hint |
|---|---|---|---|
| 1 | Count words in a sentence | Easy | frequency_map |
| 2 | Find all elements appearing more than n/3 times | Easy | freq + threshold |
| 3 | Group anagrams together | Medium | sorted word as key |
| 4 | Longest consecutive sequence | Medium | dict for O(1) lookup |
| 5 | Minimum window substring | Hard | sliding window + freq map |

### Two Pointers

| # | Problem | Difficulty | Pattern hint |
|---|---|---|---|
| 1 | Check if string is palindrome | Easy | opposite ends |
| 2 | Reverse vowels only in string | Easy | opposite ends with skip |
| 3 | Two sum on sorted array | Easy | opposite ends |
| 4 | Container with most water | Medium | opposite ends, max area |
| 5 | Trapping rain water | Hard | left_max and right_max arrays |

### Sliding Window

| # | Problem | Difficulty | Pattern hint |
|---|---|---|---|
| 1 | Max sum subarray of size k | Easy | fixed window |
| 2 | Count occurrences of anagram in string | Medium | fixed window + freq |
| 3 | Longest substring with at most 2 distinct chars | Medium | dynamic window + dict |
| 4 | Minimum size subarray sum | Medium | dynamic window |
| 5 | Minimum window substring | Hard | dynamic window + need dict |

### Binary Search

| # | Problem | Difficulty | Pattern hint |
|---|---|---|---|
| 1 | Search in sorted array | Easy | standard template |
| 2 | First and last position of element | Medium | two binary searches |
| 3 | Find peak element | Medium | compare mid and mid+1 |
| 4 | Search in rotated sorted array | Medium | check which half is sorted |
| 5 | Median of two sorted arrays | Hard | binary search on smaller array |

### Stack

| # | Problem | Difficulty | Pattern hint |
|---|---|---|---|
| 1 | Valid parentheses | Easy | push open, match close |
| 2 | Min stack | Easy | parallel min tracking stack |
| 3 | Daily temperatures (next warmer day) | Medium | monotonic stack |
| 4 | Largest rectangle in histogram | Hard | monotonic stack |

### Dynamic Programming

| # | Problem | Difficulty | Pattern hint |
|---|---|---|---|
| 1 | Fibonacci | Easy | tabulation |
| 2 | Climbing stairs | Easy | same as fibonacci |
| 3 | House robber | Medium | dp[i] = max(dp[i-2]+arr[i], dp[i-1]) |
| 4 | Coin change | Medium | 1D DP, fill up to amount |
| 5 | Longest increasing subsequence | Medium | O(n²) DP |
| 6 | 0/1 Knapsack | Medium | 2D DP |
| 7 | Edit distance | Hard | 2D DP |

### Practice problem solutions to key ones

**Group anagrams**
```python
def group_anagrams(words):
    groups = {}
    for word in words:
        key = tuple(merge_sort(list(word)))   # sorted tuple as key
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]
    result = []
    for key in groups:
        result.append(groups[key])
    return result
```

**House robber**
```python
def rob(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = nums[0] if nums[0] > nums[1] else nums[1]
    for i in range(2, len(nums)):
        option1 = dp[i-1]               # skip current house
        option2 = dp[i-2] + nums[i]     # rob current house
        if option1 > option2:
            dp[i] = option1
        else:
            dp[i] = option2
    return dp[-1]
```

**Trapping rain water**
```python
def trap(height):
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = height[0]
    for i in range(1, n):
        if height[i] > left_max[i-1]:
            left_max[i] = height[i]
        else:
            left_max[i] = left_max[i-1]
    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        if height[i] > right_max[i+1]:
            right_max[i] = height[i]
        else:
            right_max[i] = right_max[i+1]
    water = 0
    for i in range(n):
        smaller = left_max[i] if left_max[i] < right_max[i] else right_max[i]
        water += smaller - height[i]
    return water
```

---

## 17. 7-Day Study Plan

### Day 1 — Foundation (Hash Map + Two Pointers)
- Morning: Read Hash Map section. Write template 3x from scratch. Trace dry-run.
- Afternoon: Solve Easy problems 1-3 from Hash Map bank.
- Evening: Read Two Pointers section. Write both templates 3x. Trace palindrome dry-run.
- Night: Solve Two Pointer Easy problems 1-3.

### Day 2 — Sliding Window + Binary Search
- Morning: Read Sliding Window. Write both templates from scratch. Trace fixed window dry-run.
- Afternoon: Solve Sliding Window Easy + Medium 1-3.
- Evening: Read Binary Search. Write template from scratch. Trace dry-run on both examples.
- Night: Solve Binary Search Easy + Medium 1-2.

### Day 3 — Stack + Queue + Sorting
- Morning: Read Stack. Write is_balanced from scratch. Trace brackets dry-run.
- Afternoon: Solve Stack problems 1-3. Write merge_sort 3x from memory.
- Evening: Read Queue. Write BFS level order from scratch.
- Night: Pick any 2 problems from any section and solve under 20-minute timer.

### Day 4 — Linked List + Recursion
- Morning: Read Linked List. Write reverse_list from scratch. Trace on paper with 4-node list.
- Afternoon: Solve Linked List problems 1-3.
- Evening: Read Recursion & Backtracking. Write subsets from scratch.
- Night: Solve all permutations and combination sum.

### Day 5 — Dynamic Programming
- Morning: Read DP section. Write fib (tabulation) and climb_stairs from scratch.
- Afternoon: Solve DP Easy + Medium 1-4 (fibonacci, climbing stairs, house robber, coin change).
- Evening: Knapsack — trace the 2D table by hand for a 3-item example.
- Night: LCS — trace the 2D table for two short strings.

### Day 6 — Tree + Prefix Sum + Mixed Review
- Morning: Read Tree Traversal. Write all three DFS orders from scratch.
- Afternoon: Write BFS level order. Solve tree problems.
- Evening: Read Prefix Sum. Write build_prefix and range_sum from scratch.
- Night: Mixed review — pick 1 problem from each of the 4 Tier 1 patterns.

### Day 7 — Mock Interview Day
- Set a 45-minute timer.
- Pick 2 problems you haven't solved before (one Easy, one Medium).
- Follow the full Thinking Framework from Section 13.
- No notes, no looking at solutions first.
- After: review your mistakes against the Common Mistakes Journal.

---

## 18. Interview Simulation Checklist

Run through this before every mock session and real interview.

### Before you start coding
```
[ ] Read the problem twice
[ ] State your understanding out loud
[ ] Write 1 small example (input + expected output)
[ ] Ask: sorted? duplicates allowed? negative numbers? what to return if not found?
[ ] Name the pattern out loud ("I think this is a sliding window problem because...")
[ ] State brute force complexity ("Naive approach is O(n²)...")
[ ] State your approach complexity ("I'll improve to O(n) using...")
```

### While coding
```
[ ] Write function signature first
[ ] Write comment for each key section
[ ] Name variables clearly (left/right, slow/fast, window_sum)
[ ] Handle empty input check at the top
[ ] No built-ins: no sorted(), Counter(), deque(), max(), min(), sum()
```

### After writing code
```
[ ] Trace your code on the example you wrote earlier
[ ] Check the edge case (empty, single element)
[ ] State the final time complexity
[ ] State the final space complexity
[ ] Ask "does this look correct to you?" — shows collaboration
```

### Phrases that make you sound senior
- "Before I code, let me think through the approach..."
- "The brute force would be O(n²) because of the nested loop. I can improve this by..."
- "The tricky edge case here is when the array is empty, so I handle that first."
- "This is essentially a sliding window because we want a contiguous subarray..."
- "I'm using a dict here instead of a set because I need to store counts, not just presence."

---

## 19. Quick Reference — Trigger Words

| If the problem says... | Use this pattern |
|---|---|
| "count", "frequency", "anagram", "duplicate" | Hash Map |
| "sorted array", "pair with sum", "palindrome" | Two Pointers |
| "subarray", "substring", "window of size k", "longest without" | Sliding Window |
| "sorted" + "find" / "search" | Binary Search |
| "balanced brackets", "next greater", "undo" | Stack |
| "level order", "BFS", "shortest path in grid" | Queue + BFS |
| "reverse list", "detect cycle", "nth from end" | Linked List |
| "all combinations", "all permutations", "generate all subsets" | Backtracking |
| "binary tree", "height", "traversal", "BST" | Tree DFS/BFS |
| "minimum cost", "maximum ways", "count paths", "optimal" | Dynamic Programming |
| "range sum", "sum between index i and j" | Prefix Sum |
| "need sorted but no built-ins" | Merge Sort |

---

## 20. Built-ins to Avoid

| Instead of this | Write this |
|---|---|
| `sorted(arr)` / `arr.sort()` | `merge_sort(arr)` |
| `Counter(arr)` | Manual `freq = {}` dict |
| `collections.deque` | List with `front` index |
| `bisect.bisect_left(arr, x)` | `binary_search(arr, x)` |
| `sum(arr)` | `total = 0; for x in arr: total += x` |
| `max(arr)` / `min(arr)` | Loop and compare manually |
| `reversed(arr)` | Two-pointer reverse |
| `set()` for lookup | `dict` with value `1` |
| `arr.index(x)` | Linear scan loop |
| `''.join(arr)` | Loop and concatenate |

---

## 21. Time & Space Complexity Sheet

| Pattern | Time | Space | Why |
|---|---|---|---|
| Hash Map build | O(n) | O(n) | One pass, stores all keys |
| Hash Map lookup | O(1) avg | — | Direct hash access |
| Two Pointers | O(n) | O(1) | Single pass, no extra storage |
| Sliding Window | O(n) | O(1) or O(k) | Single pass |
| Binary Search | O(log n) | O(1) | Halves each step |
| Stack operations | O(1) each | O(n) total | List append/pop |
| Queue (BFS) | O(n) | O(n) | Visit each node once |
| Linked List traversal | O(n) | O(1) | Follow pointers |
| Bubble Sort | O(n²) | O(1) | Nested loops |
| Merge Sort | O(n log n) | O(n) | Divide, merge copies |
| Quick Sort | O(n log n) avg | O(log n) | In-place, recursion stack |
| Tree DFS | O(n) | O(h) | h = height of tree |
| Tree BFS | O(n) | O(n) | Queue stores a whole level |
| DP 1D | O(n) | O(n) | Fill array |
| DP 2D | O(m × n) | O(m × n) | Fill matrix |
| Backtracking | O(2ⁿ) worst | O(n) | Explore all subsets |
| Prefix Sum build | O(n) | O(n) | One pass |
| Prefix Sum query | O(1) | — | Simple subtraction |

---

*You do not need to memorize everything. You need to understand the 4 Tier-1 patterns deeply. The rest is pattern recognition and practice.*

*Good luck.*