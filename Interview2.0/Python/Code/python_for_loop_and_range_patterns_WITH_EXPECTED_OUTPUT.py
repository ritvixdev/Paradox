"""
Python For Loop & range() Patterns (Interview Pack)
Author: Suvam Das

Updated Version:
✅ Covers different ways to use for loop
✅ Covers range() variations
✅ Output shown immediately after each example
✅ Expected output written as inline comments
✅ No main block
"""


# ==========================================================
# 1) Basic for loop over list ⭐⭐⭐⭐⭐
# ==========================================================
nums = [1, 2, 3, 4]

for num in nums:
    print("1) Element:", num)
# Expected:
# 1) Element: 1
# 1) Element: 2
# 1) Element: 3
# 1) Element: 4


# ==========================================================
# 2) Using range(stop) ⭐⭐⭐⭐⭐
# ==========================================================
for i in range(5):
    print("2) range(5):", i)
# Expected:
# 2) range(5): 0
# 2) range(5): 1
# 2) range(5): 2
# 2) range(5): 3
# 2) range(5): 4


# ==========================================================
# 3) Using range(start, stop) ⭐⭐⭐⭐
# ==========================================================
for i in range(2, 6):
    print("3) range(2,6):", i)
# Expected:
# 3) range(2,6): 2
# 3) range(2,6): 3
# 3) range(2,6): 4
# 3) range(2,6): 5


# ==========================================================
# 4) Using range(start, stop, step) ⭐⭐⭐⭐
# ==========================================================
for i in range(1, 10, 2):
    print("4) range(1,10,2):", i)
# Expected:
# 4) range(1,10,2): 1
# 4) range(1,10,2): 3
# 4) range(1,10,2): 5
# 4) range(1,10,2): 7
# 4) range(1,10,2): 9


# ==========================================================
# 5) Reverse loop using range ⭐⭐⭐⭐
# ==========================================================
for i in range(5, 0, -1):
    print("5) Reverse:", i)
# Expected:
# 5) Reverse: 5
# 5) Reverse: 4
# 5) Reverse: 3
# 5) Reverse: 2
# 5) Reverse: 1


# ==========================================================
# 6) Loop with index (manual index access) ⭐⭐⭐
# ==========================================================
arr = ["a", "b", "c"]

for i in range(len(arr)):
    print("6) Index:", i, "Value:", arr[i])
# Expected:
# 6) Index: 0 Value: a
# 6) Index: 1 Value: b
# 6) Index: 2 Value: c


# ==========================================================
# 7) Loop with enumerate (Pythonic index + value) ⭐⭐⭐⭐⭐
# ==========================================================
for index, value in enumerate(arr):
    print("7) Enumerate:", index, value)
# Expected:
# 7) Enumerate: 0 a
# 7) Enumerate: 1 b
# 7) Enumerate: 2 c


# ==========================================================
# 8) Nested for loop ⭐⭐⭐⭐
# ==========================================================
for i in range(1, 3):
    for j in range(1, 3):
        print("8) Nested:", i, j)
# Expected:
# 8) Nested: 1 1
# 8) Nested: 1 2
# 8) Nested: 2 1
# 8) Nested: 2 2


# ==========================================================
# 9) for loop with break ⭐⭐⭐
# ==========================================================
for i in range(10):
    if i == 3:
        break
    print("9) Break:", i)
# Expected:
# 9) Break: 0
# 9) Break: 1
# 9) Break: 2


# ==========================================================
# 10) for loop with continue ⭐⭐⭐
# ==========================================================
for i in range(5):
    if i == 2:
        continue
    print("10) Continue:", i)
# Expected:
# 10) Continue: 0
# 10) Continue: 1
# 10) Continue: 3
# 10) Continue: 4


# ==========================================================
# 11) for-else loop ⭐⭐⭐⭐
# ==========================================================
for i in range(3):
    print("11) For-Else:", i)
else:
    print("11) Loop Completed")
# Expected:
# 11) For-Else: 0
# 11) For-Else: 1
# 11) For-Else: 2
# 11) Loop Completed


# ==========================================================
# 12) Loop through dictionary ⭐⭐⭐⭐
# ==========================================================
data = {"a": 1, "b": 2}

for key in data:
    print("12) Dict Key:", key, "Value:", data[key])
# Expected:
# 12) Dict Key: a Value: 1
# 12) Dict Key: b Value: 2


# ==========================================================
# Interview Notes (as comments)
# ==========================================================
# - range(stop) -> starts from 0
# - range(start, stop) -> stop exclusive
# - range(start, stop, step) -> custom increment/decrement
# - enumerate() -> clean way to get index + value
# - break -> exits loop
# - continue -> skips current iteration
# - for-else -> else executes if loop does not break
