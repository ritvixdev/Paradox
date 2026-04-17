"""

====== Birnary search for interviwes ==============

╔══════════════════════════════════════════════════════════════════════╗
║          SEARCHING ALGORITHMS — FULL INTERVIEW PREP GUIDE            ║
║                        Author: Suvam Das                             ║
╠══════════════════════════════════════════════════════════════════════╣
║  ✅ 8 core searching algorithms / patterns with full working code    ║
║  ✅ Step-by-step trace for each algorithm                            ║
║  ✅ Actual output shown as inline comments                           ║
║  ✅ "How to explain to interviewer" for each algorithm               ║
║  ✅ When to use / avoid each algorithm                               ║
║  ✅ No built-in index(), find(), bisect used in implementations      ║
║  ✅ No main block                                                    ║
╚══════════════════════════════════════════════════════════════════════╝

GOLDEN RULE FOR INTERVIEWS:
  "I'll implement the search from scratch so you can see my
   understanding of the underlying logic — no built-in index() or
   bisect() here."

QUICK COMPLEXITY CHEAT SHEET:
  ┌──────────────────────────┬──────────┬──────────┬────────┬────────────────────────┐
  │ Algorithm                │ Best     │ Worst    │ Space  │ Requirement            │
  ├──────────────────────────┼──────────┼──────────┼────────┼────────────────────────┤
  │ Linear Search            │ O(1)     │ O(n)     │ O(1)   │ None (any array)       │
  │ Binary Search            │ O(1)     │ O(log n) │ O(1)   │ Sorted array           │
  │ Binary Search (recursive)│ O(1)     │ O(log n) │ O(lgn) │ Sorted array           │
  │ Find First/Last Occurrence│ O(1)    │ O(log n) │ O(1)   │ Sorted array           │
  │ Search in Rotated Array  │ O(1)     │ O(log n) │ O(1)   │ Rotated sorted array   │
  │ Search in 2D Matrix      │ O(1)     │ O(n+m)   │ O(1)   │ Sorted matrix          │
  │ Jump Search              │ O(1)     │ O(√n)    │ O(1)   │ Sorted array           │
  │ Exponential Search       │ O(1)     │ O(log n) │ O(lgn) │ Sorted, unbounded size │
  └──────────────────────────┴──────────┴──────────┴────────┴────────────────────────┘

WHAT "SORTED" MEANS HERE:
  Sorted = elements in ascending order (unless stated otherwise).
  Binary Search and its variants REQUIRE sorted input.
  Linear Search works on ANY array — sorted or not.
"""


# ==========================================================
# 1) LINEAR SEARCH
# ==========================================================
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS IT?
  The simplest search — scan every element from left to right
  until you find the target or exhaust the array.

HOW TO EXPLAIN TO INTERVIEWER:
  "Linear Search checks each element one by one from the start.
   No pre-conditions needed — works on any array, sorted or not,
   with duplicates or without. The trade-off is O(n) time in the
   worst case. I'd use this when the array is small, unsorted,
   or when I'm searching for a non-comparable type (e.g. custom
   objects with no defined order)."

WHEN TO USE:
  ✅ Array is unsorted
  ✅ Array is small (n < 20)
  ✅ Searching a linked list (no random access for binary search)
  ✅ You need ALL occurrences, not just one

WHEN TO AVOID:
  ❌ Large sorted arrays — Binary Search is O(log n) vs O(n)

TRACE EXAMPLE: arr=[10, 4, 7, 2, 9], target=7
  i=0: arr[0]=10 ≠ 7
  i=1: arr[1]=4  ≠ 7
  i=2: arr[2]=7  = 7 → return 2 ✓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def linear_search(arr, target):
    """Return index of target, or -1 if not found."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i                              # found — return immediately
    return -1                                    # not found

def linear_search_all(arr, target):
    """Return list of ALL indices where target appears."""
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices                               # may be empty []

print("=" * 62)
print("1) LINEAR SEARCH")
print("=" * 62)
print("Input : [10, 4, 7, 2, 9],  target=7")
print("Output:", linear_search([10, 4, 7, 2, 9], 7))           # Output: 2

print("Input : [10, 4, 7, 2, 9],  target=99")
print("Output:", linear_search([10, 4, 7, 2, 9], 99))          # Output: -1

print("Input : [3, 1, 4, 1, 5, 1], target=1  (find ALL)")
print("Output:", linear_search_all([3, 1, 4, 1, 5, 1], 1))     # Output: [1, 3, 5]
#
# TRACE: i=0→3≠1, i=1→1=1✓ add, i=2→4≠1, i=3→1=1✓ add, i=4→5≠1, i=5→1=1✓ add


# ==========================================================
# 2) BINARY SEARCH (Iterative) ⭐⭐⭐ Most Important
# ==========================================================
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS IT?
  Works ONLY on sorted arrays. Use three pointers: low, mid,
  high. Compare target with mid element. If target < mid, search
  left half. If target > mid, search right half. Repeat.
  Each step HALVES the search space → O(log n).

HOW TO EXPLAIN TO INTERVIEWER:
  "Binary Search works like finding a word in a dictionary.
   I open to the middle — if my word comes before the middle word,
   I only look at the left half; otherwise the right half. I keep
   two pointers, low and high, and calculate mid = (low+high)//2.
   I compare arr[mid] to target:
     • Equal   → found, return mid
     • target < arr[mid] → target must be in left  → high = mid - 1
     • target > arr[mid] → target must be in right → low  = mid + 1
   I stop when low > high (target not present).
   This is O(log n) — for 1 billion elements, it takes at most 30 steps!"

WHEN TO USE:
  ✅ Array is sorted — this is the go-to O(log n) search
  ✅ Searching in answer-space (binary search on the answer)
  ✅ Finding boundaries (first/last occurrence)

WHEN TO AVOID:
  ❌ Unsorted array (must sort first — O(n log n) overhead)
  ❌ Linked list (no O(1) random access to compute mid)

COMMON BUG TO AVOID:
  mid = (low + high) // 2       ← can OVERFLOW in languages like Java/C++
  Safe version: mid = low + (high - low) // 2   ← use this in interviews!

TRACE EXAMPLE: arr=[2, 5, 8, 12, 16, 23, 38], target=23
  low=0, high=6
  Step 1: mid=3, arr[3]=12, 23>12 → low=4
  Step 2: mid=5, arr[5]=23, 23=23 → return 5 ✓  (only 2 steps for 7 elements!)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def binary_search(arr, target):
    """Iterative binary search. Returns index or -1."""
    low  = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2            # safe mid (avoids int overflow)

        if arr[mid] == target:
            return mid                           # found!
        elif arr[mid] < target:
            low = mid + 1                        # target is in RIGHT half
        else:
            high = mid - 1                       # target is in LEFT half

    return -1                                    # not found

print("\n" + "=" * 62)
print("2) BINARY SEARCH (Iterative)  ← Most Common in Interviews")
print("=" * 62)
print("Input : [2, 5, 8, 12, 16, 23, 38],  target=23")
print("Output:", binary_search([2, 5, 8, 12, 16, 23, 38], 23))  # Output: 5

print("Input : [2, 5, 8, 12, 16, 23, 38],  target=2  (first element)")
print("Output:", binary_search([2, 5, 8, 12, 16, 23, 38], 2))   # Output: 0

print("Input : [2, 5, 8, 12, 16, 23, 38],  target=38  (last element)")
print("Output:", binary_search([2, 5, 8, 12, 16, 23, 38], 38))  # Output: 6

print("Input : [2, 5, 8, 12, 16, 23, 38],  target=10  (not present)")
print("Output:", binary_search([2, 5, 8, 12, 16, 23, 38], 10))  # Output: -1

print("Input : [42],  target=42  (single element)")
print("Output:", binary_search([42], 42))                         # Output: 0


# ==========================================================
# 3) BINARY SEARCH (Recursive)
# ==========================================================
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS IT?
  Same logic as iterative Binary Search, written recursively.
  Each call works on a smaller subarray.

HOW TO EXPLAIN TO INTERVIEWER:
  "This is the same binary search logic but expressed recursively.
   The base case is low > high (return -1) or arr[mid] == target
   (return mid). Each recursive call reduces the problem to half
   the array. The call stack depth is O(log n) — same as the
   number of iterations in the iterative version. I prefer
   iterative in interviews since it avoids stack overflow risk on
   huge arrays, but recursive is cleaner to read."

SPACE NOTE:
  Recursive → O(log n) stack space (each call frame stays on stack)
  Iterative → O(1) space (just variables, no call stack)
  → Prefer ITERATIVE when memory matters.

TRACE EXAMPLE: arr=[1, 3, 5, 7, 9, 11], target=7, low=0, high=5
  Call 1: mid=2, arr[2]=5, 7>5  → recurse(low=3, high=5)
  Call 2: mid=4, arr[4]=9, 7<9  → recurse(low=3, high=3)
  Call 3: mid=3, arr[3]=7, 7=7  → return 3 ✓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def binary_search_recursive(arr, target, low=None, high=None):
    """Recursive binary search. Returns index or -1."""
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1

    if low > high:                               # base case: search space exhausted
        return -1

    mid = low + (high - low) // 2

    if arr[mid] == target:
        return mid                               # base case: found
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)  # right half
    else:
        return binary_search_recursive(arr, target, low, mid - 1)   # left half

print("\n" + "=" * 62)
print("3) BINARY SEARCH (Recursive)")
print("=" * 62)
print("Input : [1, 3, 5, 7, 9, 11],  target=7")
print("Output:", binary_search_recursive([1, 3, 5, 7, 9, 11], 7))   # Output: 3

print("Input : [1, 3, 5, 7, 9, 11],  target=1  (first)")
print("Output:", binary_search_recursive([1, 3, 5, 7, 9, 11], 1))   # Output: 0

print("Input : [1, 3, 5, 7, 9, 11],  target=4  (not present)")
print("Output:", binary_search_recursive([1, 3, 5, 7, 9, 11], 4))   # Output: -1


# ==========================================================
# 4) FIND FIRST AND LAST OCCURRENCE ⭐⭐ Very Common
# ==========================================================
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS IT?
  In a sorted array with DUPLICATES, find the FIRST index
  and LAST index where the target appears.
  Uses a modified Binary Search — don't stop at first match,
  keep narrowing to find the boundary.

HOW TO EXPLAIN TO INTERVIEWER:
  "This is a classic Binary Search modification. For FIRST
   occurrence: when I find arr[mid]==target, I record mid as
   a candidate but keep searching LEFT (high = mid - 1) in
   case there's an earlier occurrence. For LAST occurrence:
   when I find arr[mid]==target, I record mid but keep searching
   RIGHT (low = mid + 1). Each direction requires one full pass
   of binary search → O(log n) total."

WHEN TO USE:
  ✅ Sorted array with duplicates
  ✅ Count occurrences: last - first + 1
  ✅ Leetcode "Find First and Last Position" (problem #34)

TRACE EXAMPLE: arr=[1, 2, 2, 2, 3, 4], target=2
  FIRST occurrence:
    low=0, high=5
    mid=2, arr[2]=2 → found! record first=2, search LEFT → high=1
    mid=0, arr[0]=1, 1<2 → low=1
    mid=1, arr[1]=2 → found! record first=1, search LEFT → high=0
    low>high → stop. first = 1 ✓

  LAST occurrence:
    low=0, high=5
    mid=2, arr[2]=2 → found! record last=2, search RIGHT → low=3
    mid=4, arr[4]=3, 3>2 → high=3
    mid=3, arr[3]=2 → found! record last=3, search RIGHT → low=4
    low>high → stop. last = 3 ✓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def find_first_occurrence(arr, target):
    """Return index of FIRST occurrence of target, or -1."""
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            result = mid                         # candidate found
            high = mid - 1                       # keep searching LEFT for earlier
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

def find_last_occurrence(arr, target):
    """Return index of LAST occurrence of target, or -1."""
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            result = mid                         # candidate found
            low = mid + 1                        # keep searching RIGHT for later
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

def count_occurrences(arr, target):
    """Count how many times target appears using first/last occurrence."""
    first = find_first_occurrence(arr, target)
    if first == -1:
        return 0
    last = find_last_occurrence(arr, target)
    return last - first + 1

print("\n" + "=" * 62)
print("4) FIND FIRST & LAST OCCURRENCE  ← Very Common Interview Q")
print("=" * 62)
arr4 = [1, 2, 2, 2, 3, 4]
print("Input : [1, 2, 2, 2, 3, 4],  target=2")
print("First occurrence:", find_first_occurrence(arr4, 2))     # Output: 1
print("Last  occurrence:", find_last_occurrence(arr4, 2))      # Output: 3
print("Count of 2s     :", count_occurrences(arr4, 2))         # Output: 3

print("\nInput : [5, 5, 5, 5, 5],  target=5  (all same)")
print("First:", find_first_occurrence([5,5,5,5,5], 5))         # Output: 0
print("Last :", find_last_occurrence([5,5,5,5,5], 5))          # Output: 4
print("Count:", count_occurrences([5,5,5,5,5], 5))             # Output: 5

print("\nInput : [1, 2, 3, 4],  target=7  (not present)")
print("First:", find_first_occurrence([1,2,3,4], 7))           # Output: -1
print("Count:", count_occurrences([1,2,3,4], 7))               # Output: 0


# ==========================================================
# 5) BINARY SEARCH IN ROTATED SORTED ARRAY ⭐⭐⭐ Classic
# ==========================================================
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS IT?
  A sorted array has been "rotated" at some pivot point.
  Example: [1,2,3,4,5,6,7] rotated at index 3 → [4,5,6,7,1,2,3]
  Find the target in O(log n) without finding the pivot first.

HOW TO EXPLAIN TO INTERVIEWER:
  "Even in a rotated array, at least ONE half around mid is
   always properly sorted. I determine which half is sorted by
   comparing arr[low] and arr[mid]:
     • If arr[low] <= arr[mid]: left half [low..mid] is sorted
         → Check if target falls inside [arr[low]..arr[mid]]
         → If yes: search left (high = mid-1)
         → If no:  search right (low = mid+1)
     • Else: right half [mid..high] is sorted
         → Check if target falls inside [arr[mid]..arr[high]]
         → If yes: search right (low = mid+1)
         → If no:  search left (high = mid-1)
   This gives O(log n) — same as regular Binary Search."

WHEN TO USE:
  ✅ Classic interview problem (Leetcode #33)
  ✅ Any rotated/circularly shifted sorted array

TRACE EXAMPLE: arr=[4, 5, 6, 7, 0, 1, 2], target=0
  low=0, high=6
  Step 1: mid=3, arr[3]=7
    arr[0]=4 <= arr[3]=7 → LEFT half [4,5,6,7] is sorted
    target=0 not in [4..7] → search RIGHT → low=4
  Step 2: mid=5, arr[5]=1
    arr[4]=0 <= arr[5]=1 → LEFT half [0,1] is sorted
    target=0 in [0..1] → search LEFT → high=4
  Step 3: mid=4, arr[4]=0 = 0 → return 4 ✓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def search_rotated_array(arr, target):
    """Binary search in a rotated sorted array. Returns index or -1."""
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid

        # Check which half is properly sorted
        if arr[low] <= arr[mid]:                 # LEFT half is sorted
            if arr[low] <= target < arr[mid]:    # target inside sorted left
                high = mid - 1
            else:
                low = mid + 1                    # target must be in right
        else:                                    # RIGHT half is sorted
            if arr[mid] < target <= arr[high]:   # target inside sorted right
                low = mid + 1
            else:
                high = mid - 1                   # target must be in left

    return -1

print("\n" + "=" * 62)
print("5) SEARCH IN ROTATED SORTED ARRAY  ← Classic Interview Q")
print("=" * 62)
print("Input : [4, 5, 6, 7, 0, 1, 2],  target=0")
print("Output:", search_rotated_array([4, 5, 6, 7, 0, 1, 2], 0))   # Output: 4

print("Input : [4, 5, 6, 7, 0, 1, 2],  target=4  (first element)")
print("Output:", search_rotated_array([4, 5, 6, 7, 0, 1, 2], 4))   # Output: 0

print("Input : [4, 5, 6, 7, 0, 1, 2],  target=3  (not present)")
print("Output:", search_rotated_array([4, 5, 6, 7, 0, 1, 2], 3))   # Output: -1

print("Input : [6, 7, 1, 2, 3, 4, 5],  target=3")
print("Output:", search_rotated_array([6, 7, 1, 2, 3, 4, 5], 3))   # Output: 4

print("Input : [1],  target=1")
print("Output:", search_rotated_array([1], 1))                       # Output: 0


# ==========================================================
# 6) SEARCH IN A 2D SORTED MATRIX ⭐⭐ Common
# ==========================================================
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS IT?
  Matrix where each row is sorted left→right, and the first
  element of each row is greater than last element of previous row.
  Example:
    [[ 1,  3,  5,  7],
     [10, 11, 16, 20],
     [23, 30, 34, 60]]

HOW TO EXPLAIN TO INTERVIEWER:
  "There are two approaches:
   APPROACH 1 — Staircase Search O(n+m): Start at TOP-RIGHT corner.
     If target < current: move LEFT (eliminates a column)
     If target > current: move DOWN (eliminates a row)
     If equal: found! This works because top-right is the largest
     in its row and smallest in its column.

   APPROACH 2 — Binary Search O(log(n*m)): Treat the whole
     matrix as a flat sorted array of n*m elements. Map index i
     to row = i // cols, col = i % cols. Run standard binary search.
   I prefer Approach 1 for its clarity in an interview."

WHEN TO USE:
  ✅ Sorted 2D matrix search (Leetcode #74, #240)
  ✅ Any grid where rows and columns are individually sorted

TRACE EXAMPLE (Staircase): target=16
  Matrix:
    [[ 1,  3,  5,  7],
     [10, 11, 16, 20],
     [23, 30, 34, 60]]
  Start at top-right: (row=0, col=3) → value=7
    7 < 16 → move DOWN → (row=1, col=3) → value=20
    20 > 16 → move LEFT → (row=1, col=2) → value=16
    16 = 16 → return (1, 2) ✓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def search_2d_matrix(matrix, target):
    """Staircase search from top-right corner. O(n+m)."""
    if not matrix or not matrix[0]:
        return (-1, -1)

    rows = len(matrix)
    cols = len(matrix[0])
    row = 0
    col = cols - 1                               # start at top-right

    while row < rows and col >= 0:
        val = matrix[row][col]
        if val == target:
            return (row, col)                    # found — return (row, col)
        elif val < target:
            row += 1                             # too small → go down
        else:
            col -= 1                             # too big  → go left

    return (-1, -1)                              # not found

def search_2d_matrix_binary(matrix, target):
    """Binary search treating matrix as flat array. O(log(n*m))."""
    if not matrix or not matrix[0]:
        return (-1, -1)

    rows = len(matrix)
    cols = len(matrix[0])
    low  = 0
    high = rows * cols - 1

    while low <= high:
        mid = low + (high - low) // 2
        r = mid // cols                          # convert flat index → row
        c = mid % cols                           # convert flat index → col
        val = matrix[r][c]

        if val == target:
            return (r, c)
        elif val < target:
            low = mid + 1
        else:
            high = mid - 1

    return (-1, -1)

matrix6 = [
    [ 1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

print("\n" + "=" * 62)
print("6) SEARCH IN 2D SORTED MATRIX")
print("=" * 62)
print("Matrix:")
for row in matrix6:
    print("  ", row)
print("target=16")
print("Staircase → (row, col):", search_2d_matrix(matrix6, 16))         # Output: (1, 2)
print("Binary    → (row, col):", search_2d_matrix_binary(matrix6, 16))  # Output: (1, 2)

print("\ntarget=1  (top-left corner)")
print("Output:", search_2d_matrix(matrix6, 1))                          # Output: (0, 0)

print("target=60  (bottom-right corner)")
print("Output:", search_2d_matrix(matrix6, 60))                         # Output: (2, 3)

print("target=13  (not present)")
print("Output:", search_2d_matrix(matrix6, 13))                         # Output: (-1, -1)


# ==========================================================
# 7) JUMP SEARCH ⭐
# ==========================================================
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS IT?
  Jump ahead in fixed steps of √n. When you overshoot (find
  a value > target), do a LINEAR SEARCH backward in the
  previous block. Best for sorted arrays where binary search
  jump cost (random access) is expensive.

HOW TO EXPLAIN TO INTERVIEWER:
  "Jump Search is a middle-ground between Linear O(n) and
   Binary O(log n). I choose a block size of √n. I jump
   forward in steps of √n until I find arr[step] > target or
   reach the end. Then I do a linear scan backwards from that
   point to find the exact position. Total time is O(√n) — worse
   than Binary Search but works well when backward stepping is
   cheap (e.g. on magnetic disk where seeks are costly forward
   vs backward). Optimal step size is √n."

WHEN TO USE:
  ✅ Sorted array on a system where backward traversal is cheap
  ✅ When Binary Search isn't possible but Linear is too slow

WHEN TO AVOID:
  ❌ Random access is fast → use Binary Search O(log n) instead

TRACE EXAMPLE: arr=[0,1,2,3,4,5,6,7,8,9], target=7, step=√10≈3
  Jump: arr[3]=3 < 7 → jump
  Jump: arr[6]=6 < 7 → jump
  Jump: arr[9]=9 > 7 → overshoot! step back
  Linear scan from index 6: arr[6]=6, arr[7]=7 = 7 → return 7 ✓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def jump_search(arr, target):
    """Jump Search on sorted array. Returns index or -1."""
    n = len(arr)
    if n == 0:
        return -1

    # Compute √n manually (avoid math.sqrt)
    step = 1
    while step * step < n:
        step += 1                                # step ≈ √n

    prev = 0

    # Jump forward in blocks of 'step'
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(step ** 0.5) if False else step   # keep step constant = √n
        # Simpler: just add original block size
        if prev >= n:
            return -1

    # Linear scan backward in the current block
    block_end = min(step, n)
    for i in range(prev, block_end):
        if arr[i] == target:
            return i
    return -1

def jump_search_clean(arr, target):
    """Cleaner Jump Search implementation."""
    n = len(arr)
    if n == 0:
        return -1

    # Find √n without math module
    step = 1
    while (step + 1) * (step + 1) <= n:
        step += 1                                # step = floor(√n)

    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(n ** 0.5) + 1               # advance by √n
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

print("\n" + "=" * 62)
print("7) JUMP SEARCH")
print("=" * 62)
arr7 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Input : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],  target=7")
print("Output:", jump_search_clean(arr7, 7))                    # Output: 7

print("Input : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],  target=0  (first)")
print("Output:", jump_search_clean(arr7, 0))                    # Output: 0

print("Input : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],  target=9  (last)")
print("Output:", jump_search_clean(arr7, 9))                    # Output: 9

print("Input : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],  target=11  (not present)")
print("Output:", jump_search_clean(arr7, 11))                   # Output: -1


# ==========================================================
# 8) EXPONENTIAL SEARCH ⭐⭐
# ==========================================================
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS IT?
  Find the RANGE where target might exist by doubling the
  index (1, 2, 4, 8, 16...) until you overshoot, then run
  Binary Search in that range.

HOW TO EXPLAIN TO INTERVIEWER:
  "Exponential Search is ideal when the array is very large
   or UNBOUNDED (infinite/stream where you don't know the size).
   I start at index 1 and keep doubling: 1, 2, 4, 8, 16...
   until arr[i] >= target. Now I know the target must be in
   [i//2 .. i]. I run binary search in that range.
   Total cost: O(log i) to find the range + O(log i) binary search
   = O(log i) where i is the target's actual position.
   This is better than O(log n) when the target is near the start!"

WHEN TO USE:
  ✅ Unbounded / infinite sorted arrays
  ✅ Target is likely near the beginning (O(log i) not O(log n))
  ✅ Sorted arrays where size is unknown

WHEN TO AVOID:
  ❌ Small arrays — overhead not worth it vs plain Binary Search

TRACE EXAMPLE: arr=[1,2,3,4,5,6,7,8,9,10,11,12], target=11
  Check index 1: arr[1]=2  < 11 → double → i=2
  Check index 2: arr[2]=3  < 11 → double → i=4
  Check index 4: arr[4]=5  < 11 → double → i=8
  Check index 8: arr[8]=9  < 11 → double → i=16 (capped at n-1=11)
  Binary Search in range [8..11]: finds 11 at index 10 ✓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def _binary_search_range(arr, target, low, high):
    """Binary search within a specific range [low..high]."""
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def exponential_search(arr, target):
    """Exponential Search on sorted array. Returns index or -1."""
    n = len(arr)
    if n == 0:
        return -1

    if arr[0] == target:                         # check first element
        return 0

    # Find range by doubling index
    i = 1
    while i < n and arr[i] <= target:
        i *= 2                                   # double the index

    # Binary search in [i//2 .. min(i, n-1)]
    return _binary_search_range(arr, target, i // 2, min(i, n - 1))

print("\n" + "=" * 62)
print("8) EXPONENTIAL SEARCH")
print("=" * 62)
arr8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("Input : [1..12],  target=11")
print("Output:", exponential_search(arr8, 11))                  # Output: 10

print("Input : [1..12],  target=1  (first — O(1) best case)")
print("Output:", exponential_search(arr8, 1))                   # Output: 0

print("Input : [1..12],  target=12  (last)")
print("Output:", exponential_search(arr8, 12))                  # Output: 11

print("Input : [1..12],  target=15  (not present)")
print("Output:", exponential_search(arr8, 15))                  # Output: -1


# ==========================================================
# COMMON INTERVIEW QUESTIONS — ANSWERED
# ==========================================================
print("\n" + "=" * 62)
print("COMMON INTERVIEW Q&A")
print("=" * 62)
print("""
Q1: "What is Binary Search and when can you use it?"
A:  "Binary Search is an O(log n) algorithm that finds a target
     in a SORTED array by repeatedly halving the search space.
     Each step, I compare the target to the middle element and
     discard the half that can't contain the target.
     Requirement: the array MUST be sorted. If unsorted, I'd sort
     it first (O(n log n)), but then total cost = O(n log n), so
     binary search only pays off if I'm doing many searches."

Q2: "What's the difference between iterative and recursive Binary Search?"
A:  "Same O(log n) time complexity. Iterative uses O(1) space
     (just pointers). Recursive uses O(log n) stack space (one
     frame per call level). For very large arrays, recursive can
     cause a stack overflow — I prefer iterative in production.
     But recursive is cleaner and easier to explain in interviews."

Q3: "How do you handle duplicates in Binary Search?"
A:  "Standard Binary Search returns any match — you don't know
     if it's the first or last. For duplicates, I use the modified
     'Find First Occurrence' or 'Find Last Occurrence' variant:
     when I find a match, I don't stop — I continue searching
     left (for first) or right (for last) and keep the best
     candidate found. O(log n) still."

Q4: "What's the bug in mid = (low + high) / 2?"
A:  "In languages like Java and C++, low + high can overflow a
     32-bit integer if both are large. The safe formula is:
     mid = low + (high - low) // 2
     This gives the same result without overflow. In Python,
     integers don't overflow, but I use the safe form anyway
     to show the interviewer I'm aware of it."

Q5: "When would you use Linear Search over Binary Search?"
A:  "Four situations:
     1. Unsorted array — can't use Binary Search without sorting.
     2. Very small array (n < ~10) — overhead of Binary Search not worth it.
     3. Linked list — no O(1) random access to compute mid.
     4. Need ALL occurrences — linear scan naturally collects all."

Q6: "Binary Search on the answer — what does that mean?"
A:  "Beyond searching arrays, Binary Search applies to answer spaces.
     Example: 'Find the minimum speed to finish work in D days.'
     The answer is in a range [1..max_value]. I binary search on
     that range and check: can I do it at speed mid? If yes, try
     lower; if no, try higher. This is a very common advanced
     interview pattern — same O(log n) idea, different application."
""")


# ==========================================================
# FINAL CHEAT SHEET
# ==========================================================
print("=" * 62)
print("FINAL DECISION CHEAT SHEET")
print("=" * 62)
print("""
  Scenario                                    → Best Choice
  ──────────────────────────────────────────────────────────────
  Array is unsorted                           → Linear Search
  Array is sorted, find any match             → Binary Search (iterative)
  Sorted, need first/last of duplicates       → Modified Binary Search
  Array was sorted then rotated               → Rotated Binary Search
  2D matrix (rows & cols sorted)              → Staircase Search
  Array is very large or unbounded size       → Exponential Search
  Sorted, disk/block storage, costly jumps    → Jump Search
  Need ALL occurrences                        → Linear Search (collect all)
  Recursive solution requested                → Recursive Binary Search
  "Binary search on the answer" problem       → Binary Search on range

  ALWAYS ASK INTERVIEWER:
    ✔ Is the array sorted?
    ✔ Can there be duplicates?
    ✔ Do I need the first match, last match, or any match?
    ✔ Is the array size known / bounded?
""")
