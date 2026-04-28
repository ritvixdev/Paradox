# Sliding Window Maximum (Maximum of all subarrays of size K)

# Given an array arr[] of integers and an integer k, your task is to find the maximum value for each contiguous subarray of size k. The output should be an array of maximum values corresponding to each contiguous subarray.
# Examples : 
# Input: arr[] = [1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3
# Output: [3, 3, 4, 5, 5, 5, 6] 
# Explanation: 
# 1st contiguous subarray = [1 2 3] max = 3
# 2nd contiguous subarray = [2 3 1] max = 3
# 3rd contiguous subarray = [3 1 4] max = 4
# 4th contiguous subarray = [1 4 5] max = 5
# 5th contiguous subarray = [4 5 2] max = 5
# 6th contiguous subarray = [5 2 3] max = 5
# 7th contiguous subarray = [2 3 6] max = 6
# Input: arr[] = [5, 1, 3, 4, 2, 6], k = 1
# Output: [5, 1, 3, 4, 2, 6]
# Explanation: When k = 1, each element in the array is its own subarray, so the output is simply the same array.
# Input: arr[] = [1, 3, 2, 1, 7, 3], k = 3
# Output: [3, 3, 7, 7]




# =============================================================================
# SLIDING WINDOW MAXIMUM (Maximum of all subarrays of size K)
# =============================================================================
#
# PROBLEM:
#   Given an array arr[] of integers and an integer k, find the maximum value
#   for each contiguous subarray of size k.
#
# EXAMPLES:
#   Input : arr[] = [1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3
#   Output: [3, 3, 4, 5, 5, 5, 6]
#
#   Input : arr[] = [5, 1, 3, 4, 2, 6], k = 1
#   Output: [5, 1, 3, 4, 2, 6]
#
#   Input : arr[] = [1, 3, 2, 1, 7, 3], k = 3
#   Output: [3, 3, 7, 7]
#
# =============================================================================


# -----------------------------------------------------------------------------
# PATTERN: Sliding Window — Trigger words
# -----------------------------------------------------------------------------
# subarray, substring, window of size k, longest, maximum/minimum contiguous,
# at most k distinct, minimum length subarray
#
# MENTAL MODEL (Bouncer at a club):
#   A bouncer throws out anyone less impressive than the new arrival.
#   The deque always keeps candidates for "who's currently the max,"
#   in decreasing order of value. The front is ALWAYS the current window max.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# APPROACH — Monotonic Deque | Time: O(n) | Space: O(k)  ← USE THIS
# -----------------------------------------------------------------------------
#
# KEY INSIGHT: Store indices in a deque, kept in decreasing order of value.
#              Each element is pushed/popped at most once → amortized O(1).
#
# 3 RULES (same every time):
#   1. Evict indices that have slid OUT of the window  (pop from FRONT)
#   2. Evict indices whose values are WEAKER than current (pop from BACK)
#   3. Front of deque = max of current window
#
# WHERE THIS PATTERN REAPPEARS:
#   - Sliding window minimum      → flip <= to >= in step 2
#   - Longest subarray (abs diff ≤ limit) → two deques (one max, one min)
#   - Jump Game VI                → same deque applied to DP transitions
#   - Constrained subsequence sum → deque on DP array

from collections import deque
 
def sliding_window_max(arr, k):
    dq     = deque()  # stores indices (not values)
    result = []
 
    for i in range(len(arr)):
 
        # STEP 1: Evict out-of-window index from the front
        while dq and dq[0] <= i - k:
            dq.popleft()
 
        # STEP 2: Evict weaker candidates from the back
        # (if arr[i] is larger, older smaller values can NEVER be the max)
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
 
        dq.append(i)
 
        # STEP 3: Record answer once the first full window is formed
        if i >= k - 1:
            result.append(arr[dq[0]])
 
    return result
 
 
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3
print(sliding_window_max(arr, k))  # Output: [3, 3, 4, 5, 5, 5, 6]

# DRY RUN — arr = [1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3
#
#  i | arr[i] | Deque (indices) | Window    | Max
# ---|--------|-----------------|-----------|----
#  0 |   1    | [0]             | —         | —
#  1 |   2    | [1]             | —         | —
#  2 |   3    | [2]             | [1, 2, 3] |  3
#  3 |   1    | [2, 3]          | [2, 3, 1] |  3
#  4 |   4    | [4]             | [3, 1, 4] |  4
#  5 |   5    | [5]             | [1, 4, 5] |  5
#  6 |   2    | [5, 6]          | [4, 5, 2] |  5
#  7 |   3    | [5, 7]          | [5, 2, 3] |  5
#  8 |   6    | [8]             | [2, 3, 6] |  6
#
# Output: [3, 3, 4, 5, 5, 5, 6] ✓
