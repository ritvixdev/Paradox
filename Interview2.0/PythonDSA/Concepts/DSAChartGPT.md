# Python HackerRank DSA Fast Prep — Algorithm Patterns + Interview Cheat Sheet

> Goal: Prepare fast for HackerRank-style DSA interviews using reusable patterns, normal Python functions, and interview-safe logic without depending on shortcut libraries like `Counter`, `set`, `sorted`, `sum`, `max`, or `min`.

---

## How to Use This File

Do not try to memorize 100 problems. Memorize the **pattern**, the **question signals**, and the **template**.

For each question, follow this process:

```text
1. Read the question carefully.
2. Identify the pattern from keywords.
3. Choose the matching template.
4. Explain your approach before coding.
5. Write simple Python code using loops and dictionaries.
6. Mention time and space complexity.
```

---

# 1. Fast Roadmap

HackerRank interview prep commonly focuses on arrays, dictionaries/hashmaps, sorting, strings, greedy, search, dynamic programming, stacks/queues, graphs, trees, linked lists, and recursion/backtracking.

For very short preparation time, focus on these **8 patterns first**:

| Priority | Pattern | Must Learn? | Solves |
|---|---|---:|---|
| 1 | Frequency Map / Hash Map | Yes | duplicates, anagrams, pair counting, occurrence problems |
| 2 | Two Pointers | Yes | sorted arrays, pair sum, palindrome, remove/move elements |
| 3 | Sliding Window | Yes | longest/shortest substring or subarray |
| 4 | Prefix Sum | Yes | range sum, subarray sum, array manipulation |
| 5 | Stack | Yes | brackets, next greater/smaller, undo-like logic |
| 6 | Binary Search | Yes | sorted search, rotated array, answer-space search |
| 7 | Greedy | Medium | minimum/maximum decisions, jumps, scheduling |
| 8 | Basic DP | Medium | coin change, stairs, max subarray variants |

---

# 2. Pattern Recognition Cheat Sheet

| Question Says | Pattern to Use | Why |
|---|---|---|
| count, frequency, occurrence, duplicate | Frequency Map | Need fast lookup/count |
| anagram, ransom note, matching strings | Frequency Map | Compare character/word counts |
| pair with target sum | Hash Map or Two Pointers | Hash map if unsorted, two pointers if sorted |
| sorted array | Two Pointers / Binary Search | Sorted order lets you eliminate work |
| palindrome | Two Pointers | Compare left and right characters |
| longest substring/subarray | Sliding Window | Maintain a valid continuous window |
| maximum sum of k elements | Fixed Sliding Window | Window size is fixed |
| subarray sum equals k | Prefix Sum + Hash Map | Compare current sum with previous sums |
| many range sum queries | Prefix Sum | Range sum becomes O(1) |
| brackets, parentheses | Stack | Last opened should close first |
| next greater element | Monotonic Stack | Resolve previous smaller elements |
| search in sorted array | Binary Search | Eliminate half each time |
| minimum operations / maximize value | Greedy / DP | Try greedy first, DP if choices overlap |
| count ways / minimum coins | DP | Repeated subproblems |
| graph, connected components, shortest path | BFS / DFS | Traverse relationships |

---

# 3. Interview-Safe Python Rules

## Allowed Basics

These are usually fine:

```python
len(arr)
range(n)
arr.append(x)
dict lookup: if key in freq
dict assignment: freq[key] = value
while loop
for loop
```

## Avoid Depending On These in Interviews

Avoid these if the interviewer asks for manual logic:

```python
from collections import Counter
set(arr)
sorted(arr)
sum(arr)
max(arr)
min(arr)
arr.count(x)
arr.index(x)
```

You can mention: “Python has built-ins, but I’ll implement the logic manually to show the algorithm.”

---

# 4. Pattern 1 — Frequency Map / Hash Map

## When to Use

Use this when the problem asks about:

- duplicates
- frequency
- count
- occurrence
- anagram
- pairs
- matching strings
- ransom note

## Core Idea

Store values in a dictionary:

```text
key   = element / character / word
value = count / index / existence
```

## Template: Build Frequency Map

```python
def build_frequency(arr):
    freq = {}

    for item in arr:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    return freq
```

## Problem Type A: Contains Duplicate

```python
def contains_duplicate(nums):
    seen = {}

    for num in nums:
        if num in seen:
            return True
        else:
            seen[num] = True

    return False
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

## Problem Type B: Valid Anagram

```python
def is_anagram(s, t):
    if len(s) != len(t):
        return False

    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    for ch in t:
        if ch not in freq:
            return False

        freq[ch] -= 1

        if freq[ch] < 0:
            return False

    return True
```

## Problem Type C: Two Sum Using Hash Map

```python
def two_sum(nums, target):
    seen = {}  # value -> index

    for i in range(len(nums)):
        need = target - nums[i]

        if need in seen:
            return [seen[need], i]

        seen[nums[i]] = i

    return []
```

## Problem Type D: Matching Strings / Sparse Arrays

```python
def matching_strings(strings, queries):
    freq = {}

    for word in strings:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    result = []

    for q in queries:
        if q in freq:
            result.append(freq[q])
        else:
            result.append(0)

    return result
```

## Interview Explanation

> I use a hash map because I need fast lookup. Instead of checking the array again and again, I store each value and its frequency/index. This reduces nested loop O(n²) logic to O(n) average time.

---

# 5. Pattern 2 — Two Pointers

## When to Use

Use this when:

- array is sorted
- string needs left/right comparison
- pair sum in sorted array
- remove duplicates from sorted array
- move zeroes
- reverse array/string

## Template

```python
def two_pointer_template(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # compare arr[left] and arr[right]
        left += 1
        right -= 1
```

## Problem Type A: Palindrome

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

## Problem Type B: Two Sum in Sorted Array

```python
def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []
```

## Problem Type C: Move Zeroes

```python
def move_zeroes(nums):
    insert_pos = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos] = nums[i]
            insert_pos += 1

    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1

    return nums
```

## Interview Explanation

> I use two pointers because I can move from both ends or maintain a write position. This avoids extra nested loops and keeps the solution linear.

---

# 6. Pattern 3 — Sliding Window

## When to Use

Use this when the question asks for:

- longest substring
- shortest substring
- max/min subarray
- continuous range
- fixed window size k
- no repeating characters

## Two Types

| Type | Example |
|---|---|
| Fixed-size window | maximum sum of k consecutive numbers |
| Variable-size window | longest substring without repeating characters |

## Fixed Window Template

```python
def fixed_window(nums, k):
    window_sum = 0

    for i in range(k):
        window_sum += nums[i]

    best = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right - k]

        if window_sum > best:
            best = window_sum

    return best
```

## Variable Window Template

```python
def variable_window(arr):
    left = 0
    best = 0

    for right in range(len(arr)):
        # add arr[right]

        while window_is_invalid:
            # remove arr[left]
            left += 1

        current_length = right - left + 1

        if current_length > best:
            best = current_length

    return best
```

## Problem Type A: Maximum Sum of K Consecutive Elements

```python
def max_sum_k(nums, k):
    window_sum = 0

    for i in range(k):
        window_sum += nums[i]

    best = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right - k]

        if window_sum > best:
            best = window_sum

    return best
```

## Problem Type B: Longest Substring Without Repeating Characters

```python
def longest_unique_substring(s):
    freq = {}
    left = 0
    best = 0

    for right in range(len(s)):
        ch = s[right]

        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

        while freq[ch] > 1:
            left_ch = s[left]
            freq[left_ch] -= 1
            left += 1

        current_length = right - left + 1

        if current_length > best:
            best = current_length

    return best
```

## Interview Explanation

> Sliding window works because the answer is based on a continuous range. I expand the right pointer, and when the window becomes invalid, I shrink from the left.

---

# 7. Pattern 4 — Prefix Sum

## When to Use

Use this when:

- range sum is asked repeatedly
- subarray sum is needed
- array manipulation/range update appears
- question says “between index L and R”

## Template

```python
def build_prefix_sum(nums):
    prefix = [0] * (len(nums) + 1)

    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]

    return prefix
```

Range sum from `left` to `right`:

```python
range_sum = prefix[right + 1] - prefix[left]
```

## Problem Type A: Range Sum Query

```python
def range_sum_query(nums, queries):
    prefix = [0] * (len(nums) + 1)

    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]

    result = []

    for q in queries:
        left = q[0]
        right = q[1]
        total = prefix[right + 1] - prefix[left]
        result.append(total)

    return result
```

## Problem Type B: Subarray Sum Equals K

```python
def subarray_sum_equals_k(nums, k):
    freq = {}
    freq[0] = 1

    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        need = current_sum - k

        if need in freq:
            count += freq[need]

        if current_sum in freq:
            freq[current_sum] += 1
        else:
            freq[current_sum] = 1

    return count
```

## Problem Type C: HackerRank Array Manipulation

This is a classic difference-array/prefix-sum problem.

```python
def array_manipulation(n, queries):
    diff = [0] * (n + 2)

    for query in queries:
        start = query[0]
        end = query[1]
        value = query[2]

        diff[start] += value
        diff[end + 1] -= value

    max_value = 0
    current = 0

    for i in range(1, n + 1):
        current += diff[i]

        if current > max_value:
            max_value = current

    return max_value
```

## Interview Explanation

> Prefix sum helps avoid recalculating sums repeatedly. For range updates, I use a difference array and then take prefix sum once at the end.

---

# 8. Pattern 5 — Stack

## When to Use

Use this when:

- brackets / parentheses
- undo operation
- nested structure
- last-in-first-out logic
- next greater / next smaller element

## Template

```python
def stack_template(arr):
    stack = []

    for item in arr:
        if should_push:
            stack.append(item)
        else:
            top = stack.pop()

    return stack
```

## Problem Type A: Balanced Brackets

```python
def is_balanced(s):
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        else:
            if len(stack) == 0:
                return False

            top = stack.pop()

            if pairs[ch] != top:
                return False

    return len(stack) == 0
```

## Problem Type B: Next Greater Element

```python
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []  # stores indexes

    for i in range(len(nums)):
        while len(stack) > 0 and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i]

        stack.append(i)

    return result
```

## Interview Explanation

> Stack is useful when the latest unresolved item should be solved first. For brackets, the latest opening bracket must match the next closing bracket.

---

# 9. Pattern 6 — Binary Search

## When to Use

Use this when:

- array is sorted
- search space is sorted
- find first/last occurrence
- minimum possible answer
- maximum possible answer

## Template

```python
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

## Problem Type A: Search in Rotated Sorted Array

```python
def search_rotated(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

## Problem Type B: First Occurrence

```python
def first_occurrence(nums, target):
    left = 0
    right = len(nums) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            answer = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return answer
```

## Interview Explanation

> Binary search is useful when the data or answer space is ordered. Each comparison removes half of the remaining search space.

---

# 10. Pattern 7 — Sorting Manually

## When to Use

Sorting helps in:

- pair problems
- greedy problems
- minimum absolute difference
- grouping similar values

If interviewer says no built-in sorting, implement a simple sort.

## Bubble Sort

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
```

## Selection Sort

```python
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
```

## Interview Note

For real large inputs, Python’s built-in sort is better. But if the interviewer wants algorithm demonstration, use manual sort for explanation.

---

# 11. Pattern 8 — Greedy

## When to Use

Use greedy when:

- local best choice gives global best result
- minimum operations
- maximum profit/value
- interval selection
- jump game
- luck balance

## Greedy Checklist

Before using greedy, ask:

```text
1. Can I choose the best option now?
2. Will this choice hurt future choices?
3. Is there a simple proof or intuition?
```

If not, use DP instead.

## Problem Type A: Minimum Coins Greedy

Works for standard coin systems like `[1, 2, 5, 10]`, but not all coin systems.

```python
def min_coins_greedy(amount, coins):
    # Manual descending sort
    for i in range(len(coins)):
        for j in range(i + 1, len(coins)):
            if coins[j] > coins[i]:
                coins[i], coins[j] = coins[j], coins[i]

    count = 0

    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1

    if amount == 0:
        return count

    return -1
```

## Problem Type B: Minimum Jumps Style

```python
def min_jumps(nums):
    if len(nums) <= 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        reach = i + nums[i]

        if reach > farthest:
            farthest = reach

        if i == current_end:
            jumps += 1
            current_end = farthest

            if current_end >= len(nums) - 1:
                return jumps

    return jumps
```

## Interview Explanation

> I use greedy when the best local decision still keeps the future valid. If greedy cannot be proven, I switch to dynamic programming.

---

# 12. Pattern 9 — Dynamic Programming

## When to Use

Use DP when:

- there are repeated subproblems
- question asks for count ways
- minimum/maximum result
- choose/take/not take decisions
- recursion would repeat the same work

## DP Thinking Formula

```text
1. Define state: dp[i] means what?
2. Define base case.
3. Define transition.
4. Build answer from small to large.
```

## Problem Type A: Climbing Stairs

```python
def climb_stairs(n):
    if n <= 2:
        return n

    first = 1
    second = 2

    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third

    return second
```

## Problem Type B: Coin Change

```python
def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if current_amount - coin >= 0:
                candidate = dp[current_amount - coin] + 1

                if candidate < dp[current_amount]:
                    dp[current_amount] = candidate

    if dp[amount] == amount + 1:
        return -1

    return dp[amount]
```

## Problem Type C: Max Array Sum With No Adjacent Elements

```python
def max_subset_sum_no_adjacent(nums):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    prev_two = nums[0]

    if nums[0] > nums[1]:
        prev_one = nums[0]
    else:
        prev_one = nums[1]

    for i in range(2, len(nums)):
        take = nums[i] + prev_two
        skip = prev_one

        if take > skip:
            current = take
        else:
            current = skip

        prev_two = prev_one
        prev_one = current

    return prev_one
```

## Interview Explanation

> I use DP because the same subproblems repeat. I store smaller answers and use them to build the final answer efficiently.

---

# 13. Pattern 10 — Recursion and Backtracking

## When to Use

Use this when:

- generate combinations
- generate permutations
- choose/not choose
- subsets
- path exploration

## Template

```python
def backtrack(index, path):
    if index == end_condition:
        result.append(path[:])
        return

    # choose
    path.append(value)
    backtrack(index + 1, path)

    # unchoose
    path.pop()
    backtrack(index + 1, path)
```

## Problem Type: Generate Subsets

```python
def subsets(nums):
    result = []
    path = []

    def backtrack(index):
        if index == len(nums):
            result.append(path[:])
            return

        path.append(nums[index])
        backtrack(index + 1)

        path.pop()
        backtrack(index + 1)

    backtrack(0)
    return result
```

## Interview Explanation

> Backtracking tries choices one by one. After exploring one path, I undo the choice and try another path.

---

# 14. Pattern 11 — BFS / DFS Basics

## When to Use

Use graph traversal when:

- connected components
- shortest path in unweighted graph
- islands/grid traversal
- relationships between nodes

## DFS Template

```python
def dfs(graph, node, visited):
    visited[node] = True

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

## BFS Template Without deque

```python
def bfs(graph, start):
    queue = []
    queue.append(start)

    visited = {}
    visited[start] = True

    front = 0

    while front < len(queue):
        node = queue[front]
        front += 1

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited[neighbor] = True
                queue.append(neighbor)

    return visited
```

## Interview Explanation

> DFS goes deep first, useful for exploring connected components. BFS explores level by level and is useful for shortest path in an unweighted graph.

---

# 15. Common HackerRank Problem Mapping

| HackerRank Problem | Pattern |
|---|---|
| Sock Merchant | Frequency Map |
| Counting Valleys | State tracking |
| Jumping on Clouds | Greedy |
| Repeated String | Math + Frequency Count |
| 2D Array DS | Matrix traversal |
| Left Rotation | Array manipulation |
| New Year Chaos | Greedy / Bubble-count idea |
| Minimum Swaps 2 | Index map / Cycle sort idea |
| Array Manipulation | Difference Array + Prefix Sum |
| Ransom Note | Frequency Map |
| Two Strings | Frequency / Common character |
| Sherlock and Anagrams | Frequency Map + Substrings |
| Count Triplets | Hash Map counting |
| Frequency Queries | Hash Map + Reverse Frequency Map |
| Mark and Toys | Sorting + Greedy |
| Bubble Sort | Sorting |
| Maximum Toys | Sorting + Greedy |
| Balanced Brackets | Stack |
| Queue Using Two Stacks | Stack / Queue simulation |
| Pairs | Hash Map or Sorting + Two Pointers |
| Ice Cream Parlor | Two Sum Hash Map |
| Max Array Sum | Dynamic Programming |
| Candies | Greedy two-pass |
| Coin Change | Dynamic Programming |

---

# 16. 5-Day Emergency Preparation Plan

## Day 1 — Frequency Map + Arrays

Practice:

1. Contains Duplicate
2. Two Sum
3. Sock Merchant
4. Sparse Arrays
5. Ransom Note
6. Two Strings

Memorize:

```python
freq = {}
for item in arr:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1
```

---

## Day 2 — Two Pointers + Sliding Window

Practice:

1. Palindrome
2. Two Sum Sorted
3. Move Zeroes
4. Max Sum of K Elements
5. Longest Unique Substring

Memorize:

```python
left = 0
for right in range(len(arr)):
    # expand
    while invalid:
        left += 1
```

---

## Day 3 — Prefix Sum + Stack

Practice:

1. Range Sum Query
2. Subarray Sum Equals K
3. Array Manipulation
4. Balanced Brackets
5. Next Greater Element

Memorize:

```python
prefix[i + 1] = prefix[i] + nums[i]
```

---

## Day 4 — Binary Search + Sorting + Greedy

Practice:

1. Binary Search
2. First Occurrence
3. Search Rotated Array
4. Mark and Toys
5. Minimum Absolute Difference
6. Jumping on Clouds

Memorize:

```python
while left <= right:
    mid = (left + right) // 2
```

---

## Day 5 — DP Basics + Mock Practice

Practice:

1. Climbing Stairs
2. Coin Change
3. Max Array Sum
4. Candies
5. One timed HackerRank mock

Memorize:

```python
dp[0] = base_case
for i in range(1, n + 1):
    dp[i] = best choice using previous states
```

---

# 17. Universal Interview Answer Template

Use this for every DSA answer:

```text
This problem looks like a <pattern name> problem because <reason>.

I will use <data structure> to store <what>.
Then I will iterate through the input and update <state/result>.
This avoids <bad approach>.

Time complexity is O(...)
Space complexity is O(...)
```

Example:

```text
This problem looks like a frequency map problem because we need to count occurrences.
I will use a dictionary where key is the item and value is its count.
Then I will loop through the array once and update the count.
This avoids comparing every item with every other item.
Time complexity is O(n), and space complexity is O(n).
```

---

# 18. Complexity Cheat Sheet

| Code Pattern | Time Complexity |
|---|---:|
| One loop | O(n) |
| Two separate loops | O(n) |
| Nested loop over same array | O(n²) |
| Binary search | O(log n) |
| Sorting | O(n log n) usually, manual bubble sort O(n²) |
| Dictionary lookup average | O(1) |
| Sliding window | O(n) |
| Prefix sum build | O(n) |
| Stack push/pop all elements once | O(n) |
| BFS/DFS | O(V + E) |

---

# 19. Final Master Cheat Sheet

## Frequency Map

```python
freq = {}
for x in arr:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
```

## Two Pointers

```python
left = 0
right = len(arr) - 1
while left < right:
    left += 1
    right -= 1
```

## Sliding Window

```python
left = 0
for right in range(len(arr)):
    while invalid:
        left += 1
```

## Prefix Sum

```python
prefix = [0] * (len(arr) + 1)
for i in range(len(arr)):
    prefix[i + 1] = prefix[i] + arr[i]
```

## Stack

```python
stack = []
for x in arr:
    stack.append(x)
    # or stack.pop()
```

## Binary Search

```python
left = 0
right = len(arr) - 1
while left <= right:
    mid = (left + right) // 2
```

## DP

```python
dp = [0] * (n + 1)
dp[0] = base
for i in range(1, n + 1):
    dp[i] = answer_using_previous_states
```

---

# 20. Final Priority List

If you have only a few hours, learn in this order:

```text
1. Frequency Map
2. Two Pointers
3. Sliding Window
4. Prefix Sum
5. Stack
6. Binary Search
7. Greedy
8. Basic DP
```

The biggest return comes from Frequency Map + Sliding Window + Prefix Sum + Stack because these cover a large number of HackerRank-style questions.

---

# 21. Mini Practice Checklist

Tick these after practice:

- [ ] I can solve Contains Duplicate using dictionary.
- [ ] I can solve Two Sum using dictionary.
- [ ] I can solve Valid Anagram using frequency map.
- [ ] I can solve Matching Strings using frequency map.
- [ ] I can solve Palindrome using two pointers.
- [ ] I can solve Move Zeroes using write pointer.
- [ ] I can solve Max Sum of K using sliding window.
- [ ] I can solve Longest Unique Substring using sliding window.
- [ ] I can solve Range Sum using prefix sum.
- [ ] I can solve Array Manipulation using difference array.
- [ ] I can solve Balanced Brackets using stack.
- [ ] I can solve Binary Search.
- [ ] I can solve Search in Rotated Array.
- [ ] I can explain Greedy vs DP.
- [ ] I can solve Coin Change basic DP.

---

# 22. Last-Minute Interview Advice

Before writing code, always say:

```text
I will first explain the pattern, then write the code, then discuss complexity.
```

While coding, use clear names:

```python
left, right, current_sum, max_value, freq, seen, stack, result
```

Avoid silent coding. Interviewers like hearing your reasoning.

