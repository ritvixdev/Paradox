"""
 ========= Merge Sort > Insertion Sort ============== For interviwes

╔══════════════════════════════════════════════════════════════════════╗
║          SORTING ALGORITHMS — FULL INTERVIEW PREP GUIDE              ║
║                        Author: Suvam Das                             ║
╠══════════════════════════════════════════════════════════════════════╣
║  ✅ 6 core sorting algorithms with full working code                 ║
║  ✅ Step-by-step trace for each algorithm                            ║
║  ✅ Actual output shown as inline comments                           ║
║  ✅ "How to explain to interviewer" for each algorithm               ║
║  ✅ When to use / avoid each algorithm                               ║
║  ✅ No built-in sorted() used in implementations                     ║
║  ✅ No main block                                                    ║
╚══════════════════════════════════════════════════════════════════════╝

GOLDEN RULE FOR INTERVIEWS:
  "I'll implement this from scratch without using Python's built-in
   sorted() or list.sort(), so you can see my understanding of the
   underlying algorithm."

QUICK COMPLEXITY CHEAT SHEET:
  ┌─────────────────┬──────────┬──────────┬──────────┬────────┬──────────┐
  │ Algorithm       │ Best     │ Average  │ Worst    │ Space  │ Stable?  │
  ├─────────────────┼──────────┼──────────┼──────────┼────────┼──────────┤
  │ Bubble Sort     │ O(n)     │ O(n²)    │ O(n²)    │ O(1)   │ Yes      │
  │ Selection Sort  │ O(n²)    │ O(n²)    │ O(n²)    │ O(1)   │ No       │
  │ Insertion Sort  │ O(n)     │ O(n²)    │ O(n²)    │ O(1)   │ Yes      │
  │ Merge Sort      │ O(n lgn) │ O(n lgn) │ O(n lgn) │ O(n)   │ Yes      │
  │ Quick Sort      │ O(n lgn) │ O(n lgn) │ O(n²)    │ O(lgn) │ No       │
  │ Counting Sort   │ O(n+k)   │ O(n+k)   │ O(n+k)   │ O(k)   │ Yes      │
  └─────────────────┴──────────┴──────────┴──────────┴────────┴──────────┘
  (k = max value in array for Counting Sort)

WHAT "STABLE" MEANS (important for interviews!):
  A sort is STABLE if equal elements keep their original relative order.
  Example: [(A,2), (B,2), (C,1)] sorted by number
    Stable result:   [(C,1), (A,2), (B,2)]  ← A still before B
    Unstable result: [(C,1), (B,2), (A,2)]  ← order of A,B may flip
"""


# ==========================================================
# Helper: Manual list copy (interviewer approved — no .copy())
# ==========================================================
def manual_copy(arr):
    out = []
    for x in arr:
        out.append(x)
    return out


# ==========================================================
# 1) BUBBLE SORT
# ==========================================================
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS IT?
  Repeatedly compare adjacent elements and SWAP if they're
  in the wrong order. Largest element "bubbles up" to the
  end after each full pass.

HOW TO EXPLAIN TO INTERVIEWER:
  "I use two nested loops. The outer loop runs n times.
   The inner loop compares each pair of adjacent elements
   and swaps them if left > right. After each outer pass,
   the largest unsorted element is now in its correct final
   position, so the inner loop shrinks by one each time.
   I also add a 'swapped' flag — if no swaps happened in
   a full pass, the array is already sorted and I break
   early. This gives O(n) best case for already-sorted arrays."

WHEN TO USE:
  ✅ Teaching / understanding sorting concepts
  ✅ Very small arrays (n < 10)
  ✅ When you need a STABLE sort and simplicity matters

WHEN TO AVOID:
  ❌ Large arrays — O(n²) is too slow
  ❌ Performance-critical code

TRACE EXAMPLE: [5, 1, 4, 2, 8]
  Pass 1: [5,1]→swap→[1,5,4,2,8], [5,4]→swap→[1,4,5,2,8],
           [5,2]→swap→[1,4,2,5,8], [5,8]→ok → [1,4,2,5,8]  ← 8 is done
  Pass 2: [1,4]→ok, [4,2]→swap→[1,2,4,5,8], [4,5]→ok     → [1,2,4,5,8] ← 5 done
  Pass 3: [1,2]→ok, [2,4]→ok → no swaps → BREAK early ✓
  Final:  [1, 2, 4, 5, 8]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def bubble_sort(arr):
    a = manual_copy(arr)
    n = len(a)

    for i in range(n):
        swapped = False                          # optimization: early exit flag
        for j in range(0, n - i - 1):           # last i elements already sorted
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:                          # no swaps = already sorted
            break

    return a

print("=" * 60)
print("1) BUBBLE SORT")
print("=" * 60)
print("Input :", [5, 1, 4, 2, 8])
print("Output:", bubble_sort([5, 1, 4, 2, 8]))              # Output: [1, 2, 4, 5, 8]
print("Input :", [1, 2, 3, 4, 5], "(already sorted)")
print("Output:", bubble_sort([1, 2, 3, 4, 5]))              # Output: [1, 2, 3, 4, 5]  ← O(n) best case
print("Input :", [5, 4, 3, 2, 1], "(reverse sorted)")
print("Output:", bubble_sort([5, 4, 3, 2, 1]))              # Output: [1, 2, 3, 4, 5]  ← O(n²) worst case


# ==========================================================
# 2) SELECTION SORT
# ==========================================================
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS IT?
  Find the MINIMUM element in the unsorted portion, then
  place it at the start of the unsorted portion. Repeat
  for each position from left to right.

HOW TO EXPLAIN TO INTERVIEWER:
  "I divide the array into two parts: sorted (left) and
   unsorted (right). In each pass, I scan the entire
   unsorted section to find the minimum, then swap it into
   its correct sorted position. Unlike Bubble Sort, I only
   do ONE swap per pass — so Selection Sort has fewer swaps
   total (O(n) swaps vs O(n²) swaps for Bubble). However
   it's NOT stable because that single swap can jump an
   equal element past another."

WHEN TO USE:
  ✅ When WRITE operations are expensive (memory/flash storage)
     — it does minimum number of swaps: exactly O(n) swaps
  ✅ Small arrays

WHEN TO AVOID:
  ❌ When stability is required
  ❌ Large arrays (always O(n²), even if sorted)
  ❌ No early-exit optimization possible

KEY DIFFERENCE FROM BUBBLE:
  Bubble: many swaps per pass, can exit early
  Selection: exactly 1 swap per pass, never exits early
  → Selection is better when swaps are costly

TRACE EXAMPLE: [64, 25, 12, 22, 11]
  i=0: find min in [64,25,12,22,11] → min=11 at idx=4 → swap with idx=0 → [11, 25, 12, 22, 64]
  i=1: find min in [25,12,22,64]    → min=12 at idx=2 → swap with idx=1 → [11, 12, 25, 22, 64]
  i=2: find min in [25,22,64]       → min=22 at idx=3 → swap with idx=2 → [11, 12, 22, 25, 64]
  i=3: find min in [25,64]          → min=25 at idx=3 → no swap needed  → [11, 12, 22, 25, 64]
  Final: [11, 12, 22, 25, 64]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def selection_sort(arr):
    a = manual_copy(arr)
    n = len(a)

    for i in range(n):
        min_idx = i                              # assume current position is minimum
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j                      # found a new minimum
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i] # ONE swap per outer iteration

    return a

print("\n" + "=" * 60)
print("2) SELECTION SORT")
print("=" * 60)
print("Input :", [64, 25, 12, 22, 11])
print("Output:", selection_sort([64, 25, 12, 22, 11]))       # Output: [11, 12, 22, 25, 64]
print("Input :", [3, 1, 4, 1, 5, 9, 2, 6])
print("Output:", selection_sort([3, 1, 4, 1, 5, 9, 2, 6]))  # Output: [1, 1, 2, 3, 4, 5, 6, 9]
print("Input :", [1])
print("Output:", selection_sort([1]))                         # Output: [1]  ← single element edge case


# ==========================================================
# 3) INSERTION SORT
# ==========================================================
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS IT?
  Think of sorting playing cards in your hand. Pick up one
  card at a time and INSERT it into the correct position
  among the already-sorted cards on the left.

HOW TO EXPLAIN TO INTERVIEWER:
  "I start from index 1. For each element (called 'key'),
   I compare it with elements to its LEFT and shift those
   larger elements one position RIGHT to make room. Then I
   drop the key into the correct gap. The left portion is
   always sorted after each step. This is O(n) best case
   (already sorted — no shifts needed) and the BEST practical
   choice for small or nearly-sorted arrays. It's also the
   algorithm used inside Timsort (Python's built-in) for
   small subarrays."

WHEN TO USE:
  ✅ Nearly sorted arrays — best practical performance O(n)
  ✅ Small arrays (n < 20) — very low constant overhead
  ✅ Online sorting (sorting data as it arrives, one at a time)
  ✅ Used as subroutine inside Timsort and Introsort

WHEN TO AVOID:
  ❌ Large unsorted arrays

KEY DIFFERENCE FROM SELECTION/BUBBLE:
  Insertion shifts elements (not full swaps) to make room.
  It's adaptive — fewer operations on nearly-sorted data.

TRACE EXAMPLE: [12, 11, 13, 5, 6]
  i=1: key=11, compare with 12 → shift 12 right → [12,12,13,5,6] → insert 11 → [11,12,13,5,6]
  i=2: key=13, compare with 12 → 12<13 → no shift needed         → [11,12,13,5,6]
  i=3: key=5,  shift 13,12,11 right → [11,11,12,13,6] ... → insert 5 → [5,11,12,13,6]
         Wait let's redo: shifts → 13→right, 12→right, 11→right → insert 5 at front → [5,11,12,13,6]
  i=4: key=6,  11>6 shift, then 5<6 stop → insert 6 → [5,6,11,12,13]
  Final: [5, 6, 11, 12, 13]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def insertion_sort(arr):
    a = manual_copy(arr)

    for i in range(1, len(a)):
        key = a[i]                               # element to be inserted
        j = i - 1

        while j >= 0 and a[j] > key:            # shift larger elements right
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key                           # drop key into correct position

    return a

print("\n" + "=" * 60)
print("3) INSERTION SORT")
print("=" * 60)
print("Input :", [12, 11, 13, 5, 6])
print("Output:", insertion_sort([12, 11, 13, 5, 6]))          # Output: [5, 6, 11, 12, 13]
print("Input :", [1, 2, 3, 4, 5], "(already sorted — O(n) best case)")
print("Output:", insertion_sort([1, 2, 3, 4, 5]))             # Output: [1, 2, 3, 4, 5]
print("Input :", [5, 4, 3, 2, 1], "(reverse — O(n²) worst case)")
print("Output:", insertion_sort([5, 4, 3, 2, 1]))             # Output: [1, 2, 3, 4, 5]


# ==========================================================
# 4) MERGE SORT
# ==========================================================
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS IT?
  Divide and Conquer. Split the array in half recursively
  until you have single elements (always sorted), then MERGE
  pairs back together in sorted order.

HOW TO EXPLAIN TO INTERVIEWER:
  "Merge Sort uses divide and conquer. I recursively split
   the array in half until each piece has 1 element. Then
   I merge adjacent pieces together by comparing the front
   of each piece and picking the smaller one — like merging
   two sorted decks of cards. Each merge is O(n) and there
   are O(log n) levels of recursion, giving O(n log n) total.
   It's STABLE and GUARANTEED O(n log n) in all cases —
   unlike Quick Sort which can hit O(n²). The tradeoff is
   O(n) extra space for the temporary merged arrays."

WHEN TO USE:
  ✅ Need GUARANTEED O(n log n) — no worst-case risk
  ✅ Need STABLE sort for large datasets
  ✅ External sorting (data too big for RAM — merge chunks)
  ✅ Sorting linked lists (no random access needed)

WHEN TO AVOID:
  ❌ Memory is very limited — needs O(n) extra space
  ❌ Small arrays — overhead of recursion not worth it

DIVIDE & CONQUER PATTERN (important for interviews!):
  Base case:  len(arr) <= 1  → already sorted, return it
  Divide:     split at mid
  Conquer:    recursively sort left and right halves
  Combine:    merge the two sorted halves

TRACE EXAMPLE: [38, 27, 43, 3]
  Split:    [38,27] and [43,3]
  Split:    [38],[27] and [43],[3]
  Merge [38],[27]: compare 38 vs 27 → take 27, then 38 → [27,38]
  Merge [43],[3]:  compare 43 vs 3  → take 3, then 43  → [3,43]
  Merge [27,38],[3,43]:
    27 vs 3  → take 3
    27 vs 43 → take 27
    38 vs 43 → take 38
    leftover → take 43
    → [3, 27, 38, 43]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def _merge(left, right):
    """Merge two sorted arrays into one sorted array."""
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:                  # <= keeps it STABLE
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):                         # leftover from left half
        merged.append(left[i])
        i += 1

    while j < len(right):                        # leftover from right half
        merged.append(right[j])
        j += 1

    return merged

def merge_sort(arr):
    a = manual_copy(arr)

    if len(a) <= 1:                              # base case: 0 or 1 element
        return a

    mid = len(a) // 2
    left  = merge_sort(a[:mid])                  # conquer left half
    right = merge_sort(a[mid:])                  # conquer right half

    return _merge(left, right)                   # combine

print("\n" + "=" * 60)
print("4) MERGE SORT")
print("=" * 60)
print("Input :", [38, 27, 43, 3, 9, 82, 10])
print("Output:", merge_sort([38, 27, 43, 3, 9, 82, 10]))      # Output: [3, 9, 10, 27, 38, 43, 82]
print("Input :", [5, 4, 3, 2, 1], "(worst case for others, same O(n logn) here)")
print("Output:", merge_sort([5, 4, 3, 2, 1]))                  # Output: [1, 2, 3, 4, 5]
print("Input :", [1])
print("Output:", merge_sort([1]))                               # Output: [1]
print("Input :", [])
print("Output:", merge_sort([]))                                # Output: []


# ==========================================================
# 5) QUICK SORT
# ==========================================================
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS IT?
  Divide and Conquer. Pick a PIVOT element, PARTITION the
  array so all elements less than pivot go LEFT and all
  greater go RIGHT. Pivot is now in its final sorted position.
  Recursively sort left and right partitions.

HOW TO EXPLAIN TO INTERVIEWER:
  "Quick Sort picks a pivot (I use the last element here).
   I partition the array in-place: I keep a pointer 'i'
   starting before the array. I scan 'j' from left to right.
   Whenever a[j] <= pivot, I advance i and swap a[i] with a[j].
   After scanning, I put the pivot at position i+1 — this is
   its correct final position. Everything left of it is <=
   pivot, everything right is > pivot.
   Then I recurse on both sides. Average case is O(n log n)
   but worst case is O(n²) if the pivot is always the min/max
   (e.g. already sorted array). In practice it's faster than
   Merge Sort due to better cache performance and in-place sorting."

WHEN TO USE:
  ✅ Best AVERAGE performance in practice — low constants
  ✅ In-place — O(log n) stack space only
  ✅ Cache-friendly (works on contiguous memory)

WHEN TO AVOID:
  ❌ When you NEED guaranteed O(n log n) — worst case is O(n²)
  ❌ When stability is required
  ❌ Already sorted arrays with last-element pivot (use random pivot)

HOW TO AVOID WORST CASE (interview bonus point!):
  → Use random pivot: swap arr[random] with arr[high] before partitioning
  → Use median-of-three pivot

PARTITION TRACE: [10, 7, 8, 9, 1, 5]  pivot=5 (last element)
  i = -1  (pointer for "less than pivot" boundary)
  j=0: a[0]=10, 10>5 → skip
  j=1: a[1]=7,  7>5  → skip
  j=2: a[2]=8,  8>5  → skip
  j=3: a[3]=9,  9>5  → skip
  j=4: a[4]=1,  1≤5  → i=0, swap a[0]↔a[4] → [1, 7, 8, 9, 10, 5]
  End: place pivot at i+1=1 → swap a[1]↔a[5] → [1, 5, 8, 9, 10, 7]
  Pivot 5 is now at index 1 (correct final position ✓)
  Recurse on [1] and [8, 9, 10, 7]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def _partition(a, low, high):
    pivot = a[high]                              # choose last element as pivot
    i = low - 1                                  # boundary of "less than pivot" section

    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]             # move small element to left section

    a[i + 1], a[high] = a[high], a[i + 1]       # place pivot in its correct position
    return i + 1                                 # return pivot's final index

def _quick_sort_inplace(a, low, high):
    if low < high:
        pivot_idx = _partition(a, low, high)
        _quick_sort_inplace(a, low, pivot_idx - 1)   # sort left of pivot
        _quick_sort_inplace(a, pivot_idx + 1, high)  # sort right of pivot

def quick_sort(arr):
    a = manual_copy(arr)
    _quick_sort_inplace(a, 0, len(a) - 1)
    return a

print("\n" + "=" * 60)
print("5) QUICK SORT")
print("=" * 60)
print("Input :", [10, 7, 8, 9, 1, 5])
print("Output:", quick_sort([10, 7, 8, 9, 1, 5]))             # Output: [1, 5, 7, 8, 9, 10]
print("Input :", [3, 6, 8, 10, 1, 2, 1])
print("Output:", quick_sort([3, 6, 8, 10, 1, 2, 1]))          # Output: [1, 1, 2, 3, 6, 8, 10]
print("Input :", [1, 2, 3, 4, 5], "(sorted input = O(n²) worst case with last-element pivot)")
print("Output:", quick_sort([1, 2, 3, 4, 5]))                  # Output: [1, 2, 3, 4, 5]


# ==========================================================
# 6) COUNTING SORT
# ==========================================================
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS IT?
  NOT a comparison sort. Instead, COUNT how many times each
  value appears, then reconstruct the sorted array from those
  counts. Beats O(n log n) lower bound because it doesn't
  compare elements.

HOW TO EXPLAIN TO INTERVIEWER:
  "Counting Sort works when the input is non-negative integers
   in a known range [0..k]. I create a count array of size k+1.
   I scan the input once to count occurrences of each value.
   Then I walk through the count array from 0 to k — for each
   value, I output it exactly count[value] times. This is O(n+k)
   time and O(k) space. It completely bypasses the O(n log n)
   comparison-sort lower bound because it doesn't compare
   elements — it uses values as array indices.
   The tradeoff: only works for non-negative integers in a
   reasonably small range. If k >> n, it wastes memory."

WHEN TO USE:
  ✅ Input is non-negative integers with known small range
  ✅ Sorting ages, scores, grades (0-100), character ASCII codes
  ✅ When you need O(n) time and the range k is small

WHEN TO AVOID:
  ❌ Floating point numbers or negative numbers (need modification)
  ❌ Range k is huge (e.g. sort 10 numbers up to 1 billion → 1GB array!)
  ❌ When extra O(k) memory is not acceptable

INTERVIEW FOLLOW-UP — "Can you sort negative numbers?"
  Yes! Find the minimum value, shift all values by -min so
  they start from 0, sort, then shift back.

TRACE EXAMPLE: [4, 2, 2, 8, 3, 3, 1]
  max_val = 8
  count array (index 0-8): [0, 0, 0, 0, 0, 0, 0, 0, 0]
  After counting:           [0, 1, 2, 2, 1, 0, 0, 0, 1]
                              ↑  ↑  ↑  ↑  ↑           ↑
                              0  1  2  3  4           8
  Reconstruct:
    index 0: count=0 → skip
    index 1: count=1 → output [1]
    index 2: count=2 → output [1, 2, 2]
    index 3: count=2 → output [1, 2, 2, 3, 3]
    index 4: count=1 → output [1, 2, 2, 3, 3, 4]
    index 5-7: count=0 → skip
    index 8: count=1 → output [1, 2, 2, 3, 3, 4, 8]
  Final: [1, 2, 2, 3, 3, 4, 8] ✓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def counting_sort(nums):
    if len(nums) == 0:
        return []

    # Find max manually (no built-in max())
    max_val = nums[0]
    for x in nums:
        if x > max_val:
            max_val = x

    count = [0] * (max_val + 1)                 # count array indexed by value

    for x in nums:
        count[x] += 1                            # count occurrences

    out = []
    for value in range(len(count)):
        while count[value] > 0:
            out.append(value)                    # output each value count[value] times
            count[value] -= 1

    return out

def counting_sort_with_negatives(nums):
    """Extended version that handles negative numbers too."""
    if len(nums) == 0:
        return []

    min_val = nums[0]
    max_val = nums[0]
    for x in nums:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x

    offset = -min_val                            # shift so minimum maps to index 0
    count = [0] * (max_val - min_val + 1)

    for x in nums:
        count[x + offset] += 1

    out = []
    for i in range(len(count)):
        while count[i] > 0:
            out.append(i - offset)               # shift back
            count[i] -= 1
    return out

print("\n" + "=" * 60)
print("6) COUNTING SORT")
print("=" * 60)
print("Input :", [4, 2, 2, 8, 3, 3, 1])
print("Output:", counting_sort([4, 2, 2, 8, 3, 3, 1]))        # Output: [1, 2, 2, 3, 3, 4, 8]
print("Input :", [0, 0, 1, 1, 2])
print("Output:", counting_sort([0, 0, 1, 1, 2]))              # Output: [0, 0, 1, 1, 2]
print("\nBonus — with negatives:")
print("Input :", [-3, -1, 2, 0, -2, 1])
print("Output:", counting_sort_with_negatives([-3, -1, 2, 0, -2, 1]))  # Output: [-3, -2, -1, 0, 1, 2]


# ==========================================================
# COMMON INTERVIEW QUESTIONS — ANSWERED
# ==========================================================
print("\n" + "=" * 60)
print("COMMON INTERVIEW Q&A")
print("=" * 60)

print("""
Q1: "What is the best sorting algorithm?"
A:  "It depends on the situation:
     - Nearly sorted data?       → Insertion Sort  (O(n) best case)
     - Need guaranteed O(n logn)?→ Merge Sort
     - General purpose, fast?   → Quick Sort (best cache perf)
     - Integers, small range?   → Counting Sort    (O(n))
     There's no single best — I'd choose based on the constraints."

Q2: "What does stable sort mean? Does it matter?"
A:  "Stable means equal elements preserve their original order.
     It matters when you sort objects by one key that already
     have a secondary ordering. Example: sort employees by dept
     (keeping salary order within each dept). Bubble, Insertion,
     Merge are stable. Selection, Quick are not."

Q3: "Quick Sort is O(n²) worst case — why use it at all?"
A:  "Average case is O(n logn) with very small constants.
     It sorts IN-PLACE (O(logn) stack space) vs Merge Sort's O(n)
     extra space. Better cache locality since it works on contiguous
     memory. In practice, randomized Quick Sort's worst case is
     astronomically unlikely. That's why C++ std::sort and Python's
     Timsort use Quick Sort variants internally."

Q4: "How does Python's built-in sort work?"
A:  "Python uses Timsort — a hybrid of Merge Sort and Insertion Sort.
     It looks for naturally sorted 'runs', sorts small runs with
     Insertion Sort, then merges them. O(n logn) worst case,
     O(n) best case, stable, and very fast in practice."

Q5: "Can you sort in O(n)? I thought O(n logn) was the minimum."
A:  "O(n logn) is the lower bound only for COMPARISON sorts.
     Counting Sort, Radix Sort, and Bucket Sort bypass this by not
     comparing elements — they use values as indices or buckets.
     The tradeoff is they only work on specific input types
     (integers, floats in a range, etc.)."
""")


# ==========================================================
# FINAL CHEAT SHEET
# ==========================================================
print("=" * 60)
print("FINAL DECISION CHEAT SHEET")
print("=" * 60)
print("""
  Scenario                              → Best Choice
  ─────────────────────────────────────────────────────────
  Array is nearly sorted                → Insertion Sort
  Need guaranteed O(n logn) always      → Merge Sort
  General purpose, best avg speed       → Quick Sort
  Sorting non-neg integers, small range → Counting Sort
  Need stable sort, large data          → Merge Sort
  Minimize number of writes/swaps       → Selection Sort
  Teaching / interview simplest         → Bubble Sort
  Data arrives one piece at a time      → Insertion Sort
  Sorting linked list                   → Merge Sort
  Memory is very tight                  → Quick Sort (in-place)
""")
