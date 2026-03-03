"""
Reverse Array / List Patterns (Interview Pack) - Python
Author: Suvam Das

Updated Version:
✅ Multiple ways to reverse a list
✅ Output shown immediately after each method
✅ Expected output written as inline comments
✅ No main block

Note:
In production, Python's built-in slicing or list.reverse() is preferred,
but here we also implement manual interview-style approaches.
"""


# ==========================================================
# 1) Reverse Using Slicing (Pythonic Way) ⭐⭐⭐⭐⭐
# Time: O(n)
# Space: O(n)
# ==========================================================
def reverse_using_slicing(arr):
    return arr[::-1]


print("1) Reverse Using Slicing:", reverse_using_slicing([1, 2, 3, 4, 5]))
# Expected: [5, 4, 3, 2, 1]


# ==========================================================
# 2) Reverse In-Place Using Two Pointers ⭐⭐⭐⭐⭐
# Time: O(n)
# Space: O(1)
# ==========================================================
def reverse_inplace(arr):
    a = []
    for x in arr:   # manual copy (avoid list.copy())
        a.append(x)

    left = 0
    right = len(a) - 1

    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1

    return a


print("2) Reverse In-Place (Two Pointers):", reverse_inplace([10, 20, 30, 40]))
# Expected: [40, 30, 20, 10]


# ==========================================================
# 3) Reverse Using Loop (Build New List) ⭐⭐⭐
# Time: O(n)
# Space: O(n)
# ==========================================================
def reverse_using_loop(arr):
    result = []
    for i in range(len(arr) - 1, -1, -1):
        result.append(arr[i])
    return result


print("3) Reverse Using Loop:", reverse_using_loop([5, 6, 7, 8]))
# Expected: [8, 7, 6, 5]


# ==========================================================
# 4) Reverse Using Stack Concept ⭐⭐
# Time: O(n)
# Space: O(n)
# ==========================================================
def reverse_using_stack(arr):
    stack = []
    for x in arr:
        stack.append(x)

    result = []
    while stack:
        result.append(stack.pop())

    return result


print("4) Reverse Using Stack:", reverse_using_stack([1, 3, 5, 7]))
# Expected: [7, 5, 3, 1]


# ==========================================================
# 5) Reverse Using Recursion ⭐⭐⭐⭐
# Time: O(n)
# Space: O(n) (recursion stack)
# ==========================================================
def reverse_using_recursion(arr):
    if len(arr) == 0:
        return []

    return reverse_using_recursion(arr[1:]) + [arr[0]]


print("5) Reverse Using Recursion:", reverse_using_recursion([2, 4, 6, 8]))
# Expected: [8, 6, 4, 2]


# ==========================================================
# 6) Reverse String (Bonus Variant)
# ==========================================================
def reverse_string(s):
    result = ""
    for i in range(len(s) - 1, -1, -1):
        result += s[i]
    return result


print("6) Reverse String:", reverse_string("python"))
# Expected: "nohtyp"


# ==========================================================
# Interview Notes (as comments)
# ==========================================================
# - Best for interviews: Two Pointer approach (in-place, O(1) space)
# - Pythonic way: arr[::-1]
# - Recursion shows understanding of stack
# - Stack method demonstrates LIFO concept
# - Avoid unnecessary extra memory in real-world large arrays
