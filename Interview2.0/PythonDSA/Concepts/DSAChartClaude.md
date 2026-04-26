# Python DSA Cheatsheet — HackerRank Interview Prep
> No built-in functions. No shortcuts. Just pure logic you can write from memory.

---

## How to Use This File
1. Read the **core idea** (one sentence)
2. Memorize the **template** — write it from scratch 3 times
3. Recognize the **trigger words** in a problem
4. Practice the **classic problems** listed under each pattern

---

## Table of Contents
1. [Frequency / Hash Map](#1-frequency--hash-map)
2. [Two Pointers](#2-two-pointers)
3. [Sliding Window](#3-sliding-window)
4. [Binary Search](#4-binary-search)
5. [Stack](#5-stack)
6. [Queue](#6-queue)
7. [Linked List](#7-linked-list)
8. [Sorting Algorithms](#8-sorting-algorithms)
9. [Recursion & Backtracking](#9-recursion--backtracking)
10. [Tree Traversal](#10-tree-traversal)
11. [Dynamic Programming](#11-dynamic-programming)
12. [Prefix Sum](#12-prefix-sum)
13. [Quick Reference — Trigger Words](#quick-reference--trigger-words)

---

## 1. Frequency / Hash Map

**Core idea:** Count occurrences using a plain dict. You already know this — go deeper.

**Trigger words:** "count", "frequency", "duplicate", "most common", "anagram", "appears more than once"

### Template
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

### Classic Problems

**1. Find duplicate in array**
```python
def has_duplicate(arr):
    seen = {}
    for num in arr:
        if num in seen:
            return True
        seen[num] = 1
    return False
```

**2. First non-repeating character**
```python
def first_unique(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return -1
```

**3. Check if two strings are anagrams**
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

**4. Most frequent element**
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

---

## 2. Two Pointers

**Core idea:** Use two index variables (left, right) moving toward each other or in the same direction to avoid a nested loop.

**Trigger words:** "sorted array", "pair with sum", "palindrome", "reverse", "compare from both ends", "remove duplicates"

**Time complexity:** O(n) instead of O(n²)

### Template A — Opposite ends (sorted array)
```python
def two_pointer_opposite(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            return [left, right]      # found
        elif current < target:
            left += 1                 # need bigger sum
        else:
            right -= 1                # need smaller sum
    return []
```

### Template B — Same direction (fast/slow)
```python
def two_pointer_same(arr):
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != 0:           # condition to keep
            arr[slow] = arr[fast]
            slow += 1
    return slow                      # new length
```

### Classic Problems

**1. Pair with target sum (sorted array)**
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

**2. Check palindrome**
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

**3. Reverse an array in-place**
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

**4. Remove duplicates from sorted array**
```python
def remove_duplicates(arr):
    if len(arr) == 0:
        return 0
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1   # new length
```

**5. Three sum = 0 (unsorted)**
```python
def three_sum(arr):
    # first sort manually
    arr = merge_sort(arr)   # see sorting section
    result = []
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
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

---

## 3. Sliding Window

**Core idea:** Maintain a window (subarray/substring) that slides right. Expand right pointer, shrink left pointer based on a condition.

**Trigger words:** "subarray", "substring", "window of size k", "longest", "maximum sum contiguous", "at most k distinct"

**Time complexity:** O(n)

### Template A — Fixed window size k
```python
def fixed_window(arr, k):
    window_sum = 0
    for i in range(k):          # build first window
        window_sum += arr[i]
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i]        # add new right element
        window_sum -= arr[i - k]    # remove old left element
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
        window_sum += arr[right]            # expand window
        while window_sum > target:          # shrink condition
            window_sum -= arr[left]
            left += 1
        length = right - left + 1
        if length > result:
            result = length
    return result
```

### Classic Problems

**1. Maximum sum subarray of size k**
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

**2. Longest substring without repeating characters**
```python
def longest_unique_substring(s):
    seen = {}
    left = 0
    max_len = 0
    for right in range(len(s)):
        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1
        seen[s[right]] = right
        length = right - left + 1
        if length > max_len:
            max_len = length
    return max_len
```

**3. Smallest subarray with sum >= target**
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

---

## 4. Binary Search

**Core idea:** On a sorted array, eliminate half the search space each step. O(log n) instead of O(n).

**Trigger words:** "sorted", "find index", "search", "rotated array", "find minimum", "position of element"

### Template — Standard binary search
```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1   # not found
```

### Classic Problems

**1. Find first occurrence**
```python
def first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1    # keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result
```

**2. Search in rotated sorted array**
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

**3. Find square root (integer)**
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
    return right   # floor value
```

---

## 5. Stack

**Core idea:** Last In First Out (LIFO). Use a plain list. `append()` = push, `pop()` = pop.

**Trigger words:** "balanced", "matching brackets", "undo", "valid parentheses", "next greater element", "evaluate expression"

### Template
```python
def use_stack():
    stack = []
    stack.append(item)      # push
    top = stack[-1]         # peek
    item = stack.pop()      # pop
    is_empty = len(stack) == 0
```

### Classic Problems

**1. Valid parentheses / balanced brackets**
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

**2. Next greater element**
```python
def next_greater(arr):
    result = [-1] * len(arr)
    stack = []   # stores indices
    for i in range(len(arr)):
        while len(stack) > 0 and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)
    return result
```

**3. Evaluate reverse polish notation**
```python
def eval_rpn(tokens):
    stack = []
    for token in tokens:
        if token in ('+', '-', '*', '/'):
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            else: stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[0]
```

---

## 6. Queue

**Core idea:** First In First Out (FIFO). Simulate with a list using an index pointer (avoid `.pop(0)` — it's O(n)).

**Trigger words:** "level order", "BFS", "order of processing", "first come first served"

### Template (index-based, no deque)
```python
def use_queue():
    queue = []
    front = 0
    queue.append(item)             # enqueue
    item = queue[front]            # peek front
    front += 1                     # dequeue
    is_empty = front >= len(queue)
```

### Classic Problems

**1. BFS level order traversal (tree)**
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

---

## 7. Linked List

**Core idea:** Nodes pointing to next node. No index access. Always track `current`, `prev`, `next` manually.

**Trigger words:** "linked list", "reverse", "detect cycle", "merge", "nth from end", "middle of list"

### Node definition
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
```

### Classic Problems

**1. Reverse a linked list**
```python
def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next   # save next
        current.next = prev        # reverse pointer
        prev = current             # move prev forward
        current = next_node        # move current forward
    return prev   # new head
```

**2. Detect cycle (Floyd's algorithm)**
```python
def has_cycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

**3. Find middle of linked list**
```python
def find_middle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow   # slow is at middle
```

**4. Delete nth node from end**
```python
def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    fast = dummy
    slow = dummy
    for i in range(n + 1):
        fast = fast.next
    while fast is not None:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next
```

---

## 8. Sorting Algorithms

**Core idea:** Never use `.sort()` or `sorted()` in interviews. Know merge sort (stable, O(n log n)) and quick sort.

### Bubble Sort — O(n²) — only for tiny arrays
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

### Merge Sort — O(n log n) — USE THIS
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

### Quick Sort — O(n log n) avg
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

---

## 9. Recursion & Backtracking

**Core idea:** Solve a smaller version of the same problem. Every recursive function needs a base case and a recursive call.

**Trigger words:** "all combinations", "all permutations", "generate", "subsets", "N-Queens", "solve maze"

### Template — Recursion
```python
def recursive(n):
    if n == 0:          # base case — ALWAYS first
        return 1
    return n * recursive(n - 1)   # recursive call
```

### Template — Backtracking
```python
def backtrack(start, current, result, arr):
    result.append(current[:])       # save a copy of current state
    for i in range(start, len(arr)):
        current.append(arr[i])      # choose
        backtrack(i + 1, current, result, arr)
        current.pop()               # un-choose (backtrack)
```

### Classic Problems

**1. Fibonacci (no recursion limit risk)**
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

**2. All subsets of array**
```python
def subsets(arr):
    result = []
    def backtrack(start, current):
        result.append(current[:])
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()
    backtrack(0, [])
    return result
```

**3. All permutations**
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

---

## 10. Tree Traversal

**Core idea:** Visit every node. Three orders for DFS (in/pre/post). BFS uses a queue.

**Trigger words:** "binary tree", "BST", "level by level", "height", "diameter", "lowest common ancestor"

### Tree node definition
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

### DFS Templates
```python
def inorder(root):      # Left → Root → Right  (gives sorted order in BST)
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):     # Root → Left → Right
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):    # Left → Right → Root
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

### Classic Problems

**1. Maximum depth of tree**
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

**2. Check if tree is balanced**
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

---

## 11. Dynamic Programming

**Core idea:** Break into overlapping subproblems. Store results to avoid recomputation. Two approaches: top-down (memoization) or bottom-up (tabulation).

**Trigger words:** "minimum cost", "maximum profit", "count ways", "longest subsequence", "can you reach", "how many paths"

### Template — Memoization (top-down)
```python
def dp_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:          # base case
        return n
    memo[n] = dp_memo(n-1, memo) + dp_memo(n-2, memo)
    return memo[n]
```

### Template — Tabulation (bottom-up)
```python
def dp_table(n):
    table = [0] * (n + 1)
    table[0] = 0        # base case
    table[1] = 1        # base case
    for i in range(2, n + 1):
        table[i] = table[i-1] + table[i-2]
    return table[n]
```

### Classic Problems

**1. Fibonacci (DP)**
```python
def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

**2. Climbing stairs (reach step n using 1 or 2 steps)**
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

**3. 0/1 Knapsack**
```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]   # don't take item i
            if weights[i-1] <= w:
                take = values[i-1] + dp[i-1][w - weights[i-1]]
                if take > dp[i][w]:
                    dp[i][w] = take
    return dp[n][capacity]
```

**4. Longest common subsequence**
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

---

## 12. Prefix Sum

**Core idea:** Build a cumulative sum array so any range sum is O(1) instead of O(n).

**Trigger words:** "range sum", "sum between index i and j", "subarray sum equals k", "running total"

### Template
```python
def build_prefix(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix

def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]
```

### Classic Problems

**1. Subarray sum equals k**
```python
def subarray_sum_k(arr, k):
    count = 0
    prefix_sum = 0
    seen = {0: 1}   # sum: frequency
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

**2. Maximum subarray sum (Kadane's algorithm)**
```python
def max_subarray(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    for i in range(1, len(arr)):
        if current_sum + arr[i] > arr[i]:
            current_sum = current_sum + arr[i]
        else:
            current_sum = arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
```

---

## Quick Reference — Trigger Words

| Trigger phrase in problem | Pattern to use |
|---|---|
| "count occurrences", "frequency", "anagram" | Hash Map |
| "pair with sum", "palindrome", "reverse in place" | Two Pointers |
| "sorted array" + "find" | Binary Search |
| "subarray", "substring", "window of size k" | Sliding Window |
| "balanced brackets", "next greater element" | Stack |
| "level by level", "BFS", "shortest path" | Queue + BFS |
| "linked list", "cycle", "reverse nodes" | Linked List |
| "all combinations", "all subsets", "generate" | Backtracking |
| "tree", "height", "traversal" | Tree DFS/BFS |
| "minimum cost", "count ways", "maximum profit" | Dynamic Programming |
| "range sum", "sum between i and j" | Prefix Sum |
| "sort without built-ins" | Merge Sort |

---

## Interview Do's and Don'ts

### Do this
- Write a dict manually: `freq = {}` then `if x in freq: freq[x] += 1 else: freq[x] = 1`
- Sort manually using merge sort
- Simulate a queue with a list + `front` index
- Explain your approach out loud before coding
- Start with a brute force, then optimize

### Never use (the interviewer may reject)
| Built-in | Replace with |
|---|---|
| `sorted()` / `.sort()` | Merge sort function |
| `Counter()` | Manual dict frequency map |
| `collections.deque` | List with front index |
| `bisect.bisect_left` | Manual binary search |
| `sum(arr)` | Manual loop sum |
| `max()` / `min()` | Manual loop comparison |
| `reversed()` | Two pointer reverse |
| `set()` for lookup | Dict with value 1 |

---

## Time Complexity Cheat Sheet

| Pattern | Time | Space |
|---|---|---|
| Hash Map | O(n) | O(n) |
| Two Pointers | O(n) | O(1) |
| Sliding Window | O(n) | O(1) or O(k) |
| Binary Search | O(log n) | O(1) |
| Stack/Queue ops | O(1) each | O(n) |
| Merge Sort | O(n log n) | O(n) |
| Tree DFS | O(n) | O(h) |
| Tree BFS | O(n) | O(n) |
| DP (1D) | O(n) | O(n) |
| DP (2D) | O(m×n) | O(m×n) |
| Backtracking | O(2^n) | O(n) |
| Prefix Sum build | O(n) | O(n) |
| Prefix Sum query | O(1) | — |

---

*Good luck — you've got this.*