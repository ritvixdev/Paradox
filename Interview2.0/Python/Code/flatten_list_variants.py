"""
Flatten Nested List Variants (Interview Ready)
Author: Suvam Das

This file contains multiple ways to flatten a nested Python list.
- No heavy built-ins like itertools.chain or numpy.
- Includes recursion, generator (yield from), and iterative stack approach.

Note:
- These versions treat only `list` as "nested container".
- If you want to also flatten tuples, change `isinstance(item, list)` to
  `isinstance(item, (list, tuple))`.
"""


# ==========================================================
# 1) Recursive Flatten (manual append; no extend shortcut)
# ==========================================================
def flatten_recursive(arr):
    """Flatten using recursion (classic interview solution)."""
    result = []

    for item in arr:
        if isinstance(item, list):
            sub = flatten_recursive(item)
            # manually append items (no extend)
            for value in sub:
                result.append(value)
        else:
            result.append(item)

    return result


# ==========================================================
# 2) Recursive Flatten (cleaner; uses +=)
# ==========================================================
def flatten_recursive_clean(arr):
    """Flatten using recursion (cleaner syntax)."""
    result = []

    for item in arr:
        if isinstance(item, list):
            result += flatten_recursive_clean(item)
        else:
            result.append(item)

    return result


# ==========================================================
# 3) Generator Flatten (yield from) - memory efficient
# ==========================================================
def flatten_generator(arr):
    """Flatten using a generator (advanced interview bonus)."""
    for item in arr:
        if isinstance(item, list):
            yield from flatten_generator(item)
        else:
            yield item


# ==========================================================
# 4) Iterative Flatten (stack; avoids recursion depth issues)
# ==========================================================
def flatten_iterative(arr):
    """Flatten using an explicit stack (no recursion)."""
    stack = [arr]
    result = []

    while stack:
        current = stack.pop()

        if isinstance(current, list):
            # push in reverse so original order is preserved
            for item in reversed(current):
                stack.append(item)
        else:
            result.append(current)

    return result


# ==========================================================
# Main demo / quick tests
# ==========================================================
if __name__ == "__main__":
    arr = [1, 2, [3, 4, [5, 6, [7, 8, [9, 10]]]]]

    print("Original:", arr)
    print("Recursive:", flatten_recursive(arr))
    print("Recursive Clean:", flatten_recursive_clean(arr))
    print("Generator:", list(flatten_generator(arr)))
    print("Iterative:", flatten_iterative(arr))
