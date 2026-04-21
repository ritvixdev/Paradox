"""
Flatten Nested List Variants (Interview Ready)
Author: Suvam Das

Updated Version:
✅ No main block
✅ Output shown immediately after each approach
✅ Expected output written as inline comments
"""
# ==========================================================
# 2) Recursive Flatten (cleaner version using +=)
# ==========================================================
def flatten_recursive_clean(arr):
    result = []

    for item in arr:
        if isinstance(item, list):
            result += flatten_recursive_clean(item)
        else:
            result.append(item)

    return result


arr2 = [10, [20, [30, 40]], 50]
print("2) Recursive Clean:", flatten_recursive_clean(arr2))
# Expected: [10, 20, 30, 40, 50]














# ==========================================================
# 1) Recursive Flatten (manual append; no extend shortcut)
# ==========================================================
def flatten_recursive(arr):
    result = []

    for item in arr:
        if isinstance(item, list):
            sub = flatten_recursive(item)
            for value in sub:
                result.append(value)
        else:
            result.append(item)

    return result


arr1 = [1, 2, [3, 4, [5, 6, [7, 8]]]]
print("1) Recursive:", flatten_recursive(arr1))
# Expected: [1, 2, 3, 4, 5, 6, 7, 8]





# ==========================================================
# 3) Generator Flatten (yield from)
# ==========================================================
def flatten_generator(arr):
    for item in arr:
        if isinstance(item, list):
            yield from flatten_generator(item)
        else:
            yield item


arr3 = [1, [2, [3, [4]]]]
print("3) Generator:", list(flatten_generator(arr3)))
# Expected: [1, 2, 3, 4]


# ==========================================================
# 4) Iterative Flatten (stack-based, no recursion)
# ==========================================================
def flatten_iterative(arr):
    stack = [arr]
    result = []

    while stack:
        current = stack.pop()

        if isinstance(current, list):
            for item in reversed(current):
                stack.append(item)
        else:
            result.append(current)

    return result


arr4 = [5, [6, 7], [[8, 9]], 10]
print("4) Iterative:", flatten_iterative(arr4))
# Expected: [5, 6, 7, 8, 9, 10]


# ==========================================================
# 5) Advanced Case: Mixed Depth
# ==========================================================
arr5 = [1, [2, [3, 4], 5], 6, [[7], 8]]
print("5) Recursive (Mixed Depth):", flatten_recursive(arr5))
# Expected: [1, 2, 3, 4, 5, 6, 7, 8]

print("5) Iterative (Mixed Depth):", flatten_iterative(arr5))
# Expected: [1, 2, 3, 4, 5, 6, 7, 8]
