**Q1. What is Python?**
> Python is a high-level, interpreted, dynamically typed, general-purpose programming language known for its simple, readable syntax.

💡**Concept:** Python is popular because its syntax is close to plain English, which reduces boilerplate and makes code review easier. In interviews, also mention its huge ecosystem (PyPI) and that it’s used everywhere—from scripting and automation to backend APIs and data/AI.

- Free and open-source
- Used for web dev, data science, AI, automation, scripting
- Runs on Windows, Mac, Linux (cross-platform)

---

**Q2. Is Python compiled or interpreted?**
> Both. Python first compiles source code to **bytecode**, then the **Python Virtual Machine (PVM)** interprets that bytecode.

💡**Concept:** In CPython, your source is compiled to bytecode first, and then the VM executes that bytecode. This is why Python feels “interpreted” during development, but still has a compilation step that enables caching as `.pyc` for faster startup next time.

```
.py file → compiler → bytecode (.pyc) → PVM → output
```

---

**Q3. What is a dynamically typed language?**
> You don't declare variable types. Python figures out the type at **runtime** based on the value.

💡**Concept:** Dynamic typing means the variable name doesn’t “lock” a type—only the value has a type at runtime. It speeds up prototyping, but you must be careful with unexpected types in production (type hints help here).

```python
x = 10        # int
x = "hello"   # now str — no error!
```

---

**Q4. Is Python case sensitive?**
> **Yes.** `name`, `Name`, and `NAME` are three different variables.

💡**Concept:** Case sensitivity matters because `userName`, `username`, and `USERNAME` are different identifiers. In real projects this affects imports and variable naming, so consistent naming conventions (PEP 8) reduce mistakes.

```python
name = "Alice"
Name = "Bob"   # different variable!
```

---

**Q5. Is indentation required in Python?**
> **Yes — mandatory.** Python uses spaces/tabs instead of `{}` to define code blocks.

💡**Concept:** Indentation is part of Python’s syntax, so it replaces braces `{}` used in many other languages. This enforces a clean structure, but mixed tabs/spaces can cause confusing errors—most teams standardize on 4 spaces.

```python
if True:
    print("indented = inside block")   # correct
# print("no indent")  ← IndentationError!
```

---

**Q6. What are the key features of Python?**
> Interpreted, dynamically typed, object-oriented, cross-platform, open-source, first-class functions.

💡**Concept:** These features explain why Python is often chosen for fast delivery: readable syntax, batteries-included standard library, and strong community packages. Also mention that Python supports multiple paradigms (procedural, OOP, functional).

- **Readable** syntax (reads like English)
- **Extensive libraries** (numpy, pandas, flask, django)
- **First-class functions** — functions can be passed, returned, stored

---

**Q7. What are the built-in data types in Python?**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```
Numbers  → int, float, complex       e.g. 10, 3.14, 2+3j
Sequence → str, list, tuple          e.g. "hi", [1,2], (1,2)
Set      → set, frozenset            e.g. {1,2,3}
Mapping  → dict                      e.g. {"a": 1}
Boolean  → bool                      True, False
```

---

**Q8. What is the difference between mutable and immutable?**
> **Mutable** = can be changed after creation. **Immutable** = cannot be changed.

💡**Concept:** Mutability is important because it affects how objects behave when passed to functions or assigned to new variables. Many “bugs” in interviews come from mutating a list/dict in-place and accidentally affecting other references.

```
MUTABLE:   list, dict, set
IMMUTABLE: int, float, str, tuple, bool, frozenset
```
```python
lst = [1, 2, 3]
lst[0] = 99     # works — list is mutable

s = "hello"
# s[0] = "H"   # TypeError — string is immutable
```

---

**Q9. What is the difference between `is` and `==`?**
> `==` checks **values are equal**. `is` checks **same object in memory**.

💡**Concept:** `==` is about equality of value, while `is` is about identity (same object). A common interview pitfall is using `is` for string/number comparisons—use `==` unless you really mean object identity (like checking `x is None`).

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True  — same values
print(a is b)   # False — different objects

c = a
print(a is c)   # True  — same object!
```

---

**Q10. What is type conversion in Python?**
> Changing one data type into another. Can be implicit (auto) or explicit (manual).

💡**Concept:** Type conversion is common when reading input (strings) and converting to numbers, or serializing values for APIs. Interviewers like when you mention that invalid conversions raise exceptions (e.g., `int('abc')` → `ValueError`).

```python
int("42")        # → 42
float("3.14")    # → 3.14
str(100)         # → "100"
list("hello")    # → ['h','e','l','l','o']
bool(0)          # → False
bool("hi")       # → True
ord('A')         # → 65  (char to ASCII)
```

---

**Q11. What is slicing in Python?**
> Accessing a part of a sequence using `[start : end : step]`. Start is inclusive, end is exclusive.

💡**Concept:** Slicing is a powerful, readable way to take subranges of strings/lists without loops. Knowing that the end index is exclusive helps avoid off-by-one errors, and step slicing is often used for reversing or skipping elements.

```python
s = "Hello World"
s[0:5]    # "Hello"
s[::-1]   # "dlroW olleH"  ← reversed!
s[::2]    # "HloWrd"       ← every 2nd char

lst = [1, 2, 3, 4, 5]
lst[1:4]  # [2, 3, 4]
lst[-1]   # 5  ← last element
```

---

**Q12. What is the difference between indexing and slicing?**
> **Indexing** = single item (`s[2]`). **Slicing** = a range of items (`s[1:4]`).

💡**Concept:** Indexing returns a single element, while slicing returns a new sequence (a copy of the range). In interviews, mention that slicing makes a new object (for lists/strings) which has memory cost for large data.

```python
s = "Python"
s[0]     # 'P'        — indexing (one char)
s[0:3]   # 'Pyt'      — slicing (range)
s[-1]    # 'n'        — negative index (last)
```

---

**Q13. What are negative indexes and why use them?**
> Negative indexes count from the **end** of a sequence. `-1` = last element.

💡**Concept:** Negative indexing is a convenience feature that makes code cleaner, especially for “last element” or “last N elements” patterns. It also avoids manual `len(x)-1` arithmetic which is error-prone.

```python
lst = [10, 20, 30, 40, 50]
lst[-1]   # 50  — last
lst[-2]   # 40  — second to last
# Cleaner than: lst[len(lst)-1]
```

---

**Q14. What is `len()` and what does it do?**
> Returns the **number of items** in a sequence or collection.

💡**Concept:** `len()` calls an object’s `__len__` under the hood, so it works for built-in and custom containers. For most built-in containers it’s O(1), which is why it’s safe to use inside loops.

```python
len("hello")          # 5
len([1, 2, 3])        # 3
len({"a": 1, "b": 2}) # 2
len((10, 20, 30))     # 3
```

---

**Q15. What does `bool()` do?**
> Returns `True` or `False`. Falsy values: `0`, `""`, `[]`, `{}`, `()`, `None`, `False`.

💡**Concept:** Truthy/falsy rules matter in conditionals and short-circuit expressions (`and/or`). Interviewers often test whether you know empty containers and `0` behave as `False`, while non-empty containers behave as `True`.

```python
bool(1)       # True
bool(0)       # False
bool("hi")    # True
bool("")      # False
bool([])      # False
bool([1])     # True
```

---

**Q16. What is `pass` in Python?**
> A **do-nothing placeholder**. Used where code is syntactically required but nothing should execute.

💡**Concept:** `pass` is mainly a placeholder while designing code structure (stubs) or defining empty classes. It’s different from `continue`/`break` because it does nothing and does not change control flow.

```python
def my_function():
    pass   # TODO later — without pass → IndentationError!

class EmptyClass:
    pass
```

---

**Q17. What is `break`, `continue`, and `pass`?**

💡**Concept:** These three control keywords change loop behavior in different ways: exit (`break`), skip iteration (`continue`), or do nothing (`pass`). A clear mental model helps in debugging loops and interview dry-runs.

```
break    → EXIT the loop completely
continue → SKIP current iteration, go to next
pass     → DO NOTHING (placeholder)
```
```python
for i in range(5):
    if i == 3: break      # stops at 3: prints 0,1,2
    print(i)

for i in range(5):
    if i == 3: continue   # skips 3: prints 0,1,2,4
    print(i)
```

---

**Q18. What is the difference between `for` loop and `while` loop?**
> `for` — iterate over a sequence / known number of times. `while` — loop until condition is False.

💡**Concept:** `for` is ideal when iterating over items or a known range, while `while` is ideal for condition-driven loops (e.g., until input is valid). Interviewers may ask about infinite loops—`while True` must have a break condition.

```python
for i in range(5):     # use when you know how many times
    print(i)

count = 0
while count < 5:       # use when condition-driven
    print(count)
    count += 1
```

---

**Q19. What is PEP 8?**
> **Python Enhancement Proposal 8** — the official style guide for writing clean, readable Python code.

💡**Concept:** PEP 8 is about readability and consistency across teams. In interviews, mention common rules: 4-space indent, snake_case, meaningful names, and avoiding overly long lines.

```python
my_variable = 10      # snake_case for variables
MAX_SIZE = 100        # UPPER_CASE for constants
class MyClass:        # PascalCase for classes
    pass
# 4 spaces per indent, max 79 chars per line
```

---

**Q20. What are comments in Python?**
> `#` makes everything after it on that line a comment. Triple quotes for multi-line.

💡**Concept:** Comments explain intent and tricky logic, which helps maintainability. Mention that triple-quoted strings are primarily docstrings (documentation), not “real comments,” though they can be used that way.

```python
# This is a single-line comment
x = 5  # inline comment

"""
This is a
multi-line comment (docstring)
"""
```

---

**Q21. What is an expression in Python?**
> Any combination of values, variables, and operators that **evaluates to a single value**.

💡**Concept:** Expressions produce a value; statements do work (like `if`, `for`, `def`). This matters because some places expect expressions (e.g., inside a list comprehension).

```python
3 + 5          # expression → 8
x * 2          # expression → value depends on x
len([1,2,3])   # expression → 3
x > 5          # expression → True or False
```

---

**Q22. What does `==` do in Python?**
> Checks if two values are **equal**. Returns `True` or `False`.

💡**Concept:** `==` compares values after applying the type’s equality logic (`__eq__`). In interviews, it’s good to mention that different types can still be equal in some cases (like `1 == True`), so be mindful.

```python
5 == 5      # True
5 == "5"    # False — different types
[1,2] == [1,2]  # True — same values
```

---

## 📌 SECTION 2 — Strings

---

**Q23. How do you capitalise the first letter of a string?**

💡**Concept:** Capitalizing is a formatting task: sometimes you want only the first character uppercase, sometimes each word. Interviewers may also test edge cases like empty strings and single-character strings.

```python
"hello world".capitalize()  # "Hello world"  (first letter only)
"hello world".title()       # "Hello World"  (first of each word)
s = "hello"
s[0].upper() + s[1:]        # "Hello"
```

**No built-ins version (no `.capitalize()`, `.title()`, `.upper()`):**
```python
def capitalize_first_ascii(s):
    if s == "":
        return s

    first = s[0]
    code = ord(first)
    # 'a'..'z' -> 'A'..'Z'
    if 97 <= code <= 122:
        first = chr(code - 32)
    return first + s[1:]

print(capitalize_first_ascii("hello world"))  # Hello world
```

---

**Q24. What is the purpose of `.lower()` and `.upper()`?**
> `.lower()` converts all chars to lowercase. `.upper()` converts all to uppercase.

💡**Concept:** Case conversion is commonly used for normalization before comparisons (e.g., case-insensitive search). Mention Unicode: `.lower()`/`.upper()` handle more than ASCII in real Python.

```python
"HELLO".lower()   # "hello"
"hello".upper()   # "HELLO"
```

**No built-ins version (no `.lower()` / `.upper()`):**
```python
def to_lower_ascii(s):
    out = ""
    for ch in s:
        code = ord(ch)
        if 65 <= code <= 90:      # 'A'..'Z'
            out += chr(code + 32)
        else:
            out += ch
    return out

def to_upper_ascii(s):
    out = ""
    for ch in s:
        code = ord(ch)
        if 97 <= code <= 122:     # 'a'..'z'
            out += chr(code - 32)
        else:
            out += ch
    return out

print(to_lower_ascii("HELLO"))  # hello
print(to_upper_ascii("hello"))  # HELLO
```

---

**Q25. What is the difference between `split()` and `join()`?**
> `split()` — breaks a string into a list. `join()` — combines a list into a string.

💡**Concept:** `split()` is parsing (string → list), and `join()` is formatting (list → string). In interviews, emphasize that `join()` is more efficient than repeated string concatenation in a loop.

```python
"Hello World Python".split()    # ['Hello', 'World', 'Python']
"a,b,c".split(",")              # ['a', 'b', 'c']

" ".join(["Hello", "World"])    # "Hello World"
",".join(["a", "b", "c"])       # "a,b,c"
```

**No built-ins version (no `.split()` / `.join()`):**
```python
def split_by_space(s):
    parts = []
    current = ""
    for ch in s:
        if ch == " ":
            if current != "":
                parts.append(current)
                current = ""
        else:
            current += ch
    if current != "":
        parts.append(current)
    return parts

def join_with_sep(parts, sep):
    out = ""
    i = 0
    while i < len(parts):
        out += parts[i]
        if i != len(parts) - 1:
            out += sep
        i += 1
    return out

print(split_by_space("Hello World Python"))      # ['Hello','World','Python']
print(join_with_sep(["Hello","World"], " "))   # Hello World
```

---

**Q26. How do you reverse a string?**

💡**Concept:** Reversing strings is a classic warm-up to test indexing and loops. A good interview answer mentions both a Pythonic way (slicing) and a loop-based way (two-pointer/manual build) when built-ins are restricted.

```python
s = "hello"
s[::-1]              # "olleh"  ← most Pythonic (slicing)
"".join(reversed(s)) # "olleh"
```

**No built-ins version (no slicing, no `reversed()`, no `join()`):**
```python
def reverse_string(s):
    out = ""
    i = 0
    while i < len(s):
        out = s[i] + out
        i += 1
    return out

print(reverse_string("hello"))  # olleh
```

---

**Q27. What is `ord()` and what does it return?**
> Returns the **ASCII integer value** of a character.

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
ord('A')   # 65
ord('a')   # 97
ord('0')   # 48
chr(65)    # 'A'  ← reverse of ord
```

---

## 📌 SECTION 3 — Lists, Tuples & Sets

---

**Q28. What is the difference between a list and a tuple?**

💡**Concept:** Lists are flexible for data that changes, while tuples are fixed and can be used as dictionary keys (if contents are hashable). In interviews, mention tuples often represent records/coordinates and are slightly more memory-efficient.

```
LIST                        TUPLE
[1, 2, 3]                   (1, 2, 3)
Mutable (can change)        Immutable (cannot change)
Slower                      Faster
More memory                 Less memory
Can't be dict key           Can be dict key (hashable)
Use: changing collection    Use: fixed data, coordinates
```

---

**Q29. What is list comprehension?**
> A concise one-line way to create lists.

💡**Concept:** List comprehensions are syntactic sugar over loops and are often faster and more readable for simple transformations. Interviewers like when you can convert between loop form and comprehension form.

```python
# Without:
squares = []
for x in range(5): squares.append(x**2)

# With comprehension:
squares = [x**2 for x in range(5)]      # [0,1,4,9,16]
evens   = [x for x in range(10) if x%2==0]  # [0,2,4,6,8]
```

---

**Q30. What are different ways to delete an element from a list?**

💡**Concept:** Deletion methods differ by whether you remove by value or by index, and whether you need the removed element back. Picking the right one avoids bugs (e.g., removing the wrong duplicate with `remove`).

```python
lst = [10, 20, 30, 40]

lst.remove(20)   # remove by VALUE (first occurrence)
lst.pop()        # remove LAST item, returns it
lst.pop(1)       # remove by INDEX, returns it
del lst[0]       # delete by index (no return)
lst.clear()      # empty the entire list
```

---

**Q31. How do you remove duplicates from a list?**

💡**Concept:** Duplicate removal is often tested with hashing (fast) vs nested loops (no extra space). In interviews, clarify whether order must be preserved, because that changes the solution.

```python
lst = [1, 2, 2, 3, 1, 4]

# Remove duplicates, KEEP order (recommended):
list(dict.fromkeys(lst))   # [1, 2, 3, 4]

# Remove duplicates, order NOT guaranteed:
list(set(lst))             # fast but unordered
```

**No built-ins version (no `set()`, no `dict.fromkeys()`):**
```python
def remove_duplicates_keep_order(arr):
    result = []
    for x in arr:
        seen = False
        for y in result:
            if y == x:
                seen = True
                break
        if not seen:
            result.append(x)
    return result

print(remove_duplicates_keep_order([1, 2, 2, 3, 1, 4]))  # [1, 2, 3, 4]
```

---

**Q32. How do you sort a list? What's the difference between `sort()` and `sorted()`?**

💡**Concept:** Sorting questions test whether you know in-place vs copy behavior, and stability/key functions. Also be ready to explain time complexity and what happens with mixed types (often errors in Python 3).

```
sort()   → sorts IN PLACE, returns None, modifies original
sorted() → returns NEW sorted list, original unchanged
```

**No built-ins version (no `.sort()`, no `sorted()`):**
```python
# Selection sort (O(n^2))
def selection_sort(arr):
    n = len(arr)
    i = 0
    while i < n:
        min_idx = i
        j = i + 1
        while j < n:
            if arr[j] < arr[min_idx]:
                min_idx = j
            j += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        i += 1
    return arr

print(selection_sort([3, 1, 4, 1, 5]))  # [1, 1, 3, 4, 5]
```
```python
nums = [3, 1, 4, 1, 5]
nums.sort()                     # nums is now [1,1,3,4,5]
new = sorted([3,1,4,1,5])      # new=[1,1,3,4,5], original unchanged

sorted(nums, reverse=True)      # descending
sorted(words, key=str.lower)    # case-insensitive
```
> **Both use TIMSORT — O(n log n)**

---

**Q33. What are sets? Why are they unordered?**
> A set is an **unordered collection of unique elements**. Items stored by hash value, not order.

💡**Concept:** Sets are optimized for membership checks and uniqueness. They are unordered because they’re based on hashing, so you can’t rely on index positions like a list.

```python
s = {1, 2, 2, 3}   # → {1, 2, 3}  (duplicates removed)
s = set()           # empty set (NOT {} — that's a dict!)

s.add(4)
s.discard(1)        # safe remove (no error if missing)
3 in s              # True — O(1) lookup!
```
> **Unordered** because uses hash table. Cannot index (`s[0]` → TypeError).

---

**Q34. What is `frozenset`? Why can sets contain frozensets but not other sets?**
> `frozenset` is an **immutable set** — hashable, so can be used as dict key or inside a set.

💡**Concept:** Because sets are mutable, they are unhashable and cannot be placed inside another set. `frozenset` is immutable, so it becomes hashable and usable as a key or element.

```python
# set is mutable → unhashable → can't go inside a set
# {1, 2}, {3, 4}}  ← TypeError!

# frozenset is immutable → hashable → can go inside a set
s = {frozenset([1,2]), frozenset([3,4])}   # works!
```

---

**Q35. What is the difference between `append()` and `extend()`?**

💡**Concept:** `append()` adds one item (even if it’s a list), while `extend()` iterates over the iterable and adds its items. Interviewers often check whether you understand the difference in the resulting list shape.

```python
lst = [1, 2, 3]

lst.append([4, 5])   # [1, 2, 3, [4, 5]]  ← adds LIST as ONE item
lst = [1, 2, 3]
lst.extend([4, 5])   # [1, 2, 3, 4, 5]    ← adds ELEMENTS one by one
```

---

**Q36. How do you swap the first and last element in a list?**

💡**Concept:** Swapping using tuple unpacking is idiomatic Python and avoids temporary variables. It also works with any assignable targets, not just list indices.

```python
lst = [10, 20, 30, 40, 50]
lst[0], lst[-1] = lst[-1], lst[0]
print(lst)   # [50, 20, 30, 40, 10]
```

---

**Q37. How do you find the second largest element?**

💡**Concept:** Second-largest tests edge cases like duplicates and short arrays. A robust answer uses a single pass to track largest and second-largest without sorting (better time complexity).

```python
lst = [10, 20, 4000, 6000]
sorted(set(lst))[-2]   # 4000  ← second largest
```

**No built-ins version (no `sorted()`, no `set()`):**
```python
def second_largest(arr):
    if len(arr) < 2:
        return None
    first = None
    second = None
    for x in arr:
        if first is None or x > first:
            second = first
            first = x
        elif x != first and (second is None or x > second):
            second = x
    return second

print(second_largest([10, 20, 4000, 6000]))  # 4000
```

---

**Q38. How do you shuffle a list?**

💡**Concept:** Shuffling tests whether you understand randomness and in-place operations. A good “no built-in” answer uses Fisher–Yates, which produces an unbiased shuffle when implemented correctly.

```python
import random
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)   # shuffles IN PLACE
print(lst)            # e.g. [3, 1, 5, 2, 4]
```

**No built-ins version (no `random.shuffle()`):**
```python
import random

# Fisher–Yates shuffle (unbiased)
def fisher_yates(arr):
    i = len(arr) - 1
    while i > 0:
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
        i -= 1
    return arr

print(fisher_yates([1, 2, 3, 4, 5]))  # e.g. [3, 1, 5, 2, 4]
```

---

**Q39. What is the output of `[1, 2] * 2`?**
> List multiplication repeats the elements.

💡**Concept:** These questions test whether you can reason about Python execution order, scope, and object behavior without running the code. A strong interview answer explains the *why* (not just the value) and names the underlying rule (like default args, generator exhaustion, or `finally`).

```python
[1, 2] * 2    # [1, 2, 1, 2]
[0] * 5       # [0, 0, 0, 0, 0]
```

---

## 📌 SECTION 4 — Dictionaries

---

**Q40. What is a dictionary in Python?**
> An **unordered key-value store** with O(1) average lookup. Keys must be unique and immutable.

💡**Concept:** Dictionaries are a core Python tool because they provide fast key-based lookups. Interviewers love dicts for frequency counting, caching, and mapping relationships.

```python
d = {"name": "Alice", "age": 25}
d["name"]             # "Alice"
d.get("salary", 0)    # 0  ← safe, no KeyError
d["city"] = "NY"      # add new key
del d["age"]          # delete key
```

---

**Q41. How do you get all keys from a dictionary?**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
d = {"a": 1, "b": 2, "c": 3}
list(d.keys())     # ['a', 'b', 'c']
list(d.values())   # [1, 2, 3]
list(d.items())    # [('a',1), ('b',2), ('c',3)]
```

---

**Q42. Why is dict lookup faster than list lookup?**
> Dict uses a **hash table** → O(1). List searches linearly → O(N).

💡**Concept:** Hash tables let dict jump directly to a bucket using a hash of the key, avoiding scanning all items. Lists require linear scanning unless you maintain an index structure yourself.

```
List: check item 1... 2... 3... until found  → O(N)
Dict: hash("key") → jump directly to slot   → O(1)
```

---

**Q43. Can you use a list or dict as a dictionary key?**
> **No** — keys must be hashable (immutable). Lists and dicts are mutable → unhashable.

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
d = {}
# d[[1,2]] = "val"   # TypeError! list unhashable
d[(1, 2)] = "val"    # OK! tuple is hashable ✓
```

---

**Q44. How do you merge two dictionaries?**

💡**Concept:** Merging dicts can overwrite keys—mention how conflicts are resolved (later value wins). In interviews, show both modern syntax (`|`) and older compatible patterns (`{**d1, **d2}` / `.update`).

```python
d1 = {"a": 1}
d2 = {"b": 2}

# Python 3.9+:
merged = d1 | d2          # {"a":1, "b":2}

# Older Python:
merged = {**d1, **d2}     # same result
d1.update(d2)             # modifies d1 in place
```

---

**Q45. How do you increment all values in a dictionary?**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
d = {"a": 1, "b": 2, "c": 3}
d = {k: v + 1 for k, v in d.items()}
print(d)   # {"a": 2, "b": 3, "c": 4}
```

---

## 📌 SECTION 5 — Functions

---

**Q46. What are `*args` and `**kwargs`?**

💡**Concept:** These are essential for writing flexible APIs and wrappers. In interviews, explain that `*args` and `**kwargs` also help forward arguments in decorators.

```
*args   → collects extra POSITIONAL arguments → TUPLE
**kwargs → collects extra KEYWORD arguments  → DICT
```
```python
def show(*args, **kwargs):
    print(args)    # (1, 2, 3)
    print(kwargs)  # {'name': 'Alice', 'age': 25}

show(1, 2, 3, name="Alice", age=25)
```

---

**Q47. What is a lambda function?**
> A small, **anonymous one-line function**. Used when you need a quick function without defining it formally.

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
add = lambda x, y: x + y
add(3, 4)   # 7

# Common uses:
nums.sort(key=lambda x: -x)              # sort descending
list(map(lambda x: x**2, [1,2,3]))      # [1,4,9]
list(filter(lambda x: x>2, [1,2,3,4]))  # [3,4]
```

---

**Q48. Can we pass a function as an argument?**
> **Yes.** Functions are **first-class objects** in Python — can be passed, returned, stored.

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
def apply(func, value):
    return func(value)

apply(str.upper, "hello")   # "HELLO"
apply(len, [1, 2, 3])       # 3
```

---

**Q49. How are arguments passed in Python — by value or reference?**
> Python uses **pass by object reference**. Mutable objects can be changed; immutable create new objects.

💡**Concept:** The important idea is: mutation affects the original object because both references point to the same object. Rebinding (like `n = n + 1`) does not affect the caller for immutables because it creates a new object locally.

```python
def change(lst):
    lst.append(99)     # modifies original!

my_list = [1, 2, 3]
change(my_list)
print(my_list)   # [1, 2, 3, 99]  ← changed!

def change_num(n):
    n = n + 10   # creates new int locally

x = 5
change_num(x)
print(x)   # 5  ← unchanged (int is immutable)
```

---

**Q50. What are docstrings?**
> A string literal at the **start of a function/class/module** that documents what it does.

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
def greet(name):
    """Returns a greeting message for the given name."""
    return f"Hello, {name}!"

print(greet.__doc__)   # "Returns a greeting message for the given name."
```

---

**Q51. What is recursion?**
> A function that **calls itself** to solve a smaller version of the same problem.

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
def factorial(n):
    if n <= 1: return 1          # base case — stops recursion
    return n * factorial(n - 1)  # recursive call

factorial(5)   # 120  (5×4×3×2×1)
```

---

**Q52. What is the scope of a variable? What is the LEGB rule?**
> **Scope** = where a variable is accessible. Python looks up names using **LEGB order**.

💡**Concept:** LEGB is a common source of confusion when variables exist at multiple scopes. In interviews, mention `global` and `nonlocal` for writing to outer scopes.

```
L → Local      (inside current function)
E → Enclosing  (outer function for closures)
G → Global     (module level)
B → Built-in   (print, len, range...)
```
```python
x = "global"
def outer():
    x = "enclosing"
    def inner():
        print(x)   # "enclosing" — LEGB finds Enclosing first
    inner()
```

---

## 📌 SECTION 6 — OOP (Object-Oriented Programming)

---

**Q53. How are classes created in Python?**
> Using the `class` keyword. `__init__` is the constructor, `self` refers to the instance.

💡**Concept:** Classes bundle state (attributes) and behavior (methods), making code modular and reusable. Mention that `__init__` initializes per-object state, and `self` is how methods access the current instance.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name    # instance attribute
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

dog = Dog("Rex", 3)
dog.bark()   # "Rex says Woof!"
```

---

**Q54. What is `self` in Python?**
> `self` refers to the **current instance** of the class. It tells the method which object to work with.

💡**Concept:** `self` is how Python passes the instance into instance methods. It’s not a keyword, but the convention makes code readable and consistent across projects.

```python
class Counter:
    def __init__(self): self.count = 0
    def increment(self): self.count += 1

c1 = Counter(); c2 = Counter()
c1.increment()
print(c1.count)  # 1
print(c2.count)  # 0  ← separate objects, separate state
```
> `self` is **not a keyword** — just a strong convention.

---

**Q55. What are instance, class, and static methods?**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
class MyClass:
    class_var = "shared"

    def instance_method(self):     # needs self — accesses instance data
        return self.x

    @classmethod
    def class_method(cls):         # needs cls — accesses class data
        return cls.class_var

    @staticmethod
    def static_method(a, b):       # no self/cls — pure utility
        return a + b
```

---

**Q56. What is `__init__` vs `__new__`?**

💡**Concept:** `__new__` is responsible for creating the instance (especially relevant for immutables/singletons), while `__init__` configures it after creation. Many interviews ask this to test deeper object model understanding.

```
__new__   → CREATES the object in memory (runs FIRST)
__init__  → INITIALISES the object's attributes (runs AFTER)
```
```python
class A:
    def __new__(cls):
        print("Creating")
        return super().__new__(cls)
    def __init__(self):
        print("Initialising")

a = A()
# Creating
# Initialising
```

---

**Q57. What is inheritance? What types does Python support?**
> Allows a child class to **reuse code** from a parent class.

💡**Concept:** Inheritance enables reuse and polymorphism—child classes can extend or override behavior. In interviews, mention the “is-a” relationship and avoid misuse where composition fits better.

```python
class Animal:
    def eat(self): return "eating"

class Dog(Animal):          # inherits from Animal
    def bark(self): return "Woof!"

d = Dog()
d.eat()    # "eating"  ← inherited from Animal
d.bark()   # "Woof!"   ← own method
```
```
Types:
Single      → Dog inherits from Animal
Multi-level → Puppy → Dog → Animal
Hierarchical → Dog and Cat both inherit from Animal
Multiple    → FlyingCar inherits from Car AND Airplane
```

---

**Q58. What is MRO (Method Resolution Order)?**
> The order Python searches for methods in multiple inheritance. Uses **C3 linearisation**.

💡**Concept:** MRO matters in multiple inheritance because it defines which parent implementation is chosen. Knowing `__mro__`/`mro()` helps debug ambiguous method selection.

```python
class A:
    def hello(self): return "A"

class B(A):
    def hello(self): return "B"

class C(B):
    pass

print(C().hello())   # "B"  ← follows MRO
print(C.__mro__)     # (C, B, A, object)
```

---

**Q59. What are public, protected, and private attributes?**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```
name    → PUBLIC:    accessible anywhere
_name   → PROTECTED: convention — only class/subclasses
__name  → PRIVATE:   name-mangled, hard to access outside
```
```python
class BankAccount:
    def __init__(self):
        self.owner = "Alice"   # public
        self._balance = 1000   # protected (by convention)
        self.__pin = 1234      # private (name-mangled)

acc = BankAccount()
acc.owner           # "Alice"  ✓
acc._balance        # 1000     ✓ (but shouldn't!)
# acc.__pin         # AttributeError!
```

---

**Q60. Does Python support multiple inheritance?**
> **Yes.** A class can inherit from multiple parents.

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
class Car:
    def drive(self): return "driving"

class Airplane:
    def fly(self): return "flying"

class FlyingCar(Car, Airplane):
    pass

fc = FlyingCar()
fc.drive()   # "driving"  ← from Car
fc.fly()     # "flying"   ← from Airplane
```

---

**Q61. What is method overriding vs method overloading?**

💡**Concept:** Python supports overriding naturally because methods are resolved at runtime. “Overloading” is usually simulated with default arguments or `*args/**kwargs` because Python doesn’t select methods by signature like Java/C++.

```
OVERRIDING:  Child redefines parent's method → Python fully supports
OVERLOADING: Same name, different params → Python does NOT support natively
```
```python
# Overriding:
class Animal:
    def speak(self): return "generic"

class Dog(Animal):
    def speak(self): return "Woof!"  # overrides parent

# Overloading (simulated):
def add(a, b=0, c=0):
    return a + b + c
add(1)       # 1
add(1, 2)    # 3
add(1, 2, 3) # 6
```

---

**Q62. What is abstraction and encapsulation?**

💡**Concept:** Encapsulation is about protecting internal state and providing safe methods, while abstraction is about hiding complexity behind a simple interface. Interviewers often expect a simple real-world example (bank account, car engine).

```
ENCAPSULATION: Bundle data + methods together; restrict direct access.
               "I call deposit(), I don't touch the balance directly"

ABSTRACTION:   Hide complexity; show only what's necessary.
               "I press drive(), I don't need to know the engine"
```
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):   # must be implemented by subclass
        pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r ** 2

# Shape()  → TypeError! Can't instantiate abstract class
```

---

**Q63. What are Python's special (dunder) methods?**
> Methods with double underscores that define how objects behave with built-in operations.

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
class Box:
    def __init__(self, size): self.size = size
    def __str__(self):   return f"Box({self.size})"   # print(box)
    def __len__(self):   return self.size               # len(box)
    def __add__(self, o): return Box(self.size + o.size) # box1 + box2
    def __eq__(self, o):  return self.size == o.size    # box1 == box2

b = Box(5)
print(b)    # Box(5)
len(b)      # 5
```

---

**Q64. What is monkey patching?**
> Changing a class or function **at runtime** — replacing a method without modifying the original source.

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
class Dog:
    def bark(self): return "Woof"

def louder_bark(self): return "WOOF WOOF!"
Dog.bark = louder_bark     # replaced at runtime!

Dog().bark()   # "WOOF WOOF!"
```

---

## 📌 SECTION 7 — Memory Management

---

**Q65. How does Python manage memory?**
> Python uses a **private heap** for all objects. Memory managed via **reference counting + garbage collection**.

💡**Concept:** Understanding memory management helps explain performance and bugs around object lifetime. Mention reference counting for immediate cleanup and the GC for cycles that reference counting can’t collect alone.

```
1. Private heap space — all objects live here
2. Reference counting — when count drops to 0, object freed immediately
3. Garbage collector  — handles circular references (A → B → A)
4. Memory pools       — pre-allocated pools for small objects (faster!)
```

---

**Q66. What is reference counting?**
> Every object has a count of how many variables point to it. When count = 0, memory is freed.

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
import sys
x = [1, 2, 3]
sys.getrefcount(x)   # shows reference count

y = x          # count → 2
del x          # count → 1
del y          # count → 0 → memory freed!
```

---

**Q67. Why doesn't Python free all memory on exit?**
> Circular references, C extension objects, and GC overhead may delay cleanup. The OS reclaims all memory when the process fully exits.

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.


---

**Q68. What is shallow copy vs deep copy?**

💡**Concept:** This is a common gotcha with nested lists/dicts: a shallow copy duplicates only the outer container. Deep copy is safer for nested structures, but more expensive in time and memory.

```
SHALLOW: New container, but nested objects are SHARED
DEEP:    New container AND all nested objects are fully COPIED
```
```python
import copy
original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
shallow[0][0] = 99
print(original)   # [[99, 2], [3, 4]]  ← AFFECTED!

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 99
print(original)   # [[1, 2], [3, 4]]   ← UNCHANGED!
```
> **Memory trick:** Shallow = same house (shared bathroom). Deep = separate house (nothing shared).

---

**Q69. What is the GIL (Global Interpreter Lock)?**
> A mutex in CPython that allows **only one thread to execute Python bytecode at a time**.

💡**Concept:** The GIL primarily affects CPU-bound multithreading in CPython; it does not mean Python can’t do concurrency. Interviewers like when you can recommend: threads for I/O, multiprocessing for CPU, asyncio for high-concurrency I/O.

```
Why? Python's reference counting isn't thread-safe without GIL.
Impact on CPU-bound tasks:  Threading does NOT help (use multiprocessing!)
Impact on I/O-bound tasks:  GIL released during I/O → threading DOES help!
```

---

**Q70. What is the process of compilation and linking in Python?**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```
Pure Python code:
  .py → bytecode (.pyc via compiler) → executed by PVM

C extensions (e.g. NumPy):
  .c → machine code (via GCC/MSVC compiler)
  → linked into shared library (.so / .dll)
  → loaded by Python at import time
```

---

## 📌 SECTION 8 — Error Handling

---

**Q71. How is exception handling done in Python?**
> Using `try / except / else / finally` blocks.

💡**Concept:** Python exceptions let you handle failures gracefully while keeping normal logic clean. In interviews, always mention `finally` for cleanup (closing files, releasing locks) and using specific exception types.

```python
try:
    result = 10 / 0            # risky code
except ZeroDivisionError:
    print("Can't divide by zero!")
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
else:
    print("Success!")          # runs ONLY if no exception
finally:
    print("Always runs!")      # ALWAYS runs (cleanup)
```

---

**Q72. Do runtime errors exist in Python?**
> **Yes.** Python has two types of errors:

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```
Compile-time: SyntaxError, IndentationError — caught before execution
Runtime:      ZeroDivisionError, NameError, TypeError — occur during execution
```
```python
# Runtime error example:
result = 10 / 0      # ZeroDivisionError
int("abc")           # ValueError
lst = [1,2]
lst[10]              # IndexError
```

---

**Q73. What are common built-in exceptions?**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```
ZeroDivisionError  → 5/0
TypeError          → "hello" + 5
ValueError         → int("abc")
IndexError         → [1,2,3][10]
KeyError           → {"a":1}["b"]
AttributeError     → None.upper()
FileNotFoundError  → open("ghost.txt")
NameError          → print(undefined_var)
RecursionError     → infinite recursion
```

---

**Q74. Explain the `try`, `except`, `else`, `finally` blocks.**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```
try     → code that might fail
except  → what to do if it fails
else    → runs ONLY if no exception occurred
finally → ALWAYS runs (good for cleanup: close files, etc.)
```

---

## 📌 SECTION 9 — Advanced Python

---

**Q75. What are decorators?**
> A function that **wraps another function** to add behaviour without changing the original code.

💡**Concept:** Decorators are common in real code (logging, auth checks, caching) and show you understand functions as objects. Explaining that a decorator returns a new callable (wrapper) is the key idea.

```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b): return a + b

add(2, 3)
# Calling add
# 5
```

---

**Q76. What are generators?**
> Functions using `yield` to produce values **one at a time** — memory efficient for large data.

💡**Concept:** Generators are about laziness and memory efficiency: values are produced when needed, not stored. In interviews, mention they’re great for streaming large data or pipelines.

```python
# List — loads ALL values in memory at once:
squares_list = [x**2 for x in range(1000000)]  # uses lots of RAM

# Generator — produces ONE value at a time:
def gen_squares(n):
    for x in range(n):
        yield x**2

for val in gen_squares(1000000):   # only 1 value in memory!
    print(val)

# Generator expression:
gen = (x**2 for x in range(10))   # use () not []
next(gen)   # 0
next(gen)   # 1
# Warning: generator exhausted after one use!
```

---

**Q77. What is the difference between generators and lists?**

💡**Concept:** Generators and Lists look similar, but they solve different problems and have different trade-offs. In interviews, the easiest way to explain is: define each one, then show a tiny example where choosing the wrong one would cause a bug or inefficiency.

```
List:       All values stored in memory at once.     [x**2 for x in range(n)]
Generator:  Values produced lazily, one at a time.   (x**2 for x in range(n))

Use generators when: dataset is huge, you only need one value at a time
```

---

**Q78. What is a closure?**
> An inner function that **remembers variables from its outer function** even after the outer function has returned.

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
def outer(message):
    def inner():
        print(message)   # "closes over" message
    return inner

say_hi = outer("Hello!")
say_hi()   # "Hello!" — still remembers 'message'!
```

---

**Q79. What is pickling and unpickling?**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```
Pickling:   Convert Python object → bytes (to save/send)
Unpickling: Convert bytes → Python object (to restore)
```
```python
import pickle

data = {"name": "Alice", "scores": [95, 87]}

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)          # pickling

with open("data.pkl", "rb") as f:
    loaded = pickle.load(f)       # unpickling
print(loaded)   # {'name': 'Alice', 'scores': [95, 87]}
```

---

**Q80. What is the zip() function?**
> Combines multiple iterables **element by element** into tuples.

💡**Concept:** `zip()` is often used to iterate in parallel across multiple lists and produce pairs/tuples. Interviewers may test that `zip()` stops at the shortest iterable unless using `itertools.zip_longest`.

```python
names = ["Alice", "Bob", "Carol"]
ages  = [25, 30, 22]

list(zip(names, ages))
# [('Alice', 25), ('Bob', 30), ('Carol', 22)]

for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

**No built-ins version (no `zip()`):**
```python
def manual_zip(a, b):
    out = []
    n = len(a) if len(a) < len(b) else len(b)
    i = 0
    while i < n:
        out.append((a[i], b[i]))
        i += 1
    return out

names = ["Alice", "Bob", "Carol"]
ages  = [25, 30, 22]
print(manual_zip(names, ages))
# [('Alice', 25), ('Bob', 30), ('Carol', 22)]
```

---

**Q81. What is the difference between `range()` and `xrange()`?**

💡**Concept:** Range() and Xrange() look similar, but they solve different problems and have different trade-offs. In interviews, the easiest way to explain is: define each one, then show a tiny example where choosing the wrong one would cause a bug or inefficiency.

```
Python 2:  range() → creates full list in memory (slow for large n)
           xrange() → lazy iterator (memory efficient)

Python 3:  range() IS already lazy — xrange() doesn't exist in Python 3
```
```python
list(range(5))   # [0, 1, 2, 3, 4]
range(5)[2]      # 2  ← supports indexing
```

---

**Q82. What are modules and packages?**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```
Module:  A single .py file           e.g. math.py
Package: A directory with modules    e.g. mypackage/ + __init__.py
```
```python
import math                # import module
from math import pi, sqrt  # import specific items
import numpy as np         # import with alias

math.sqrt(16)   # 4.0
sqrt(16)        # 4.0
```

---

**Q83. What is PIP?**
> Python's **package manager** for installing third-party libraries from PyPI.

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```bash
pip install numpy          # install
pip uninstall numpy        # remove
pip list                   # show installed
pip freeze > req.txt       # save to file
pip install -r req.txt     # install from file
```

---

## 📌 SECTION 10 — Collections Module

---

**Q84. What is `collections.Counter`?**
> Counts the frequency of elements in an iterable.

💡**Concept:** Counter is a convenience wrapper around frequency dictionaries. In interviews, you should still be able to implement a frequency map manually using a dict when libraries are restricted.

```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "apple"]
c = Counter(words)
print(c)              # Counter({'apple': 3, 'banana': 1, 'cherry': 1})
c.most_common(2)      # [('apple', 3), ('banana', 1)]

# One-liner word count:
Counter("hello".split())
```

**No built-ins version (no `collections.Counter`):**
```python
def frequency_map(items):
    freq = {}
    for x in items:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    return freq

words = ["apple", "banana", "apple", "cherry", "apple"]
print(frequency_map(words))  # {'apple': 3, 'banana': 1, 'cherry': 1}
```

---

**Q85. What is `collections.deque`? How is it different from a list?**
> A double-ended queue with **O(1) append/pop from both ends**.

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
from collections import deque
q = deque([1, 2, 3])
q.append(4)      # add right  O(1)
q.appendleft(0)  # add left   O(1)
q.pop()          # remove right O(1)
q.popleft()      # remove left  O(1)
```
```
List:  fast random access O(1), slow front insert/remove O(N)
Deque: slow random access O(N), fast both-ends insert/remove O(1)
```

---

**Q86. What is `collections.defaultdict`?**
> Like a regular dict but returns a **default value for missing keys** instead of raising `KeyError`.

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
from collections import defaultdict
d = defaultdict(list)
d["fruits"].append("apple")   # no KeyError even though key is new!
print(d)   # defaultdict(<class 'list'>, {'fruits': ['apple']})
```

---

## 📌 SECTION 11 — File Handling

---

**Q87. What file modes does Python support?**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```
'r'  → read only (default)
'w'  → write (overwrites existing)
'a'  → append (adds to end)
'r+' → read and write
'rb' → read binary
'wb' → write binary
```
```python
with open("file.txt", "r") as f:
    content = f.read()        # always use 'with' — auto-closes file

with open("out.txt", "w") as f:
    f.write("Hello!\n")
```

---

**Q88. How do you delete a file using Python?**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
import os

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
    print("Deleted!")
else:
    print("File not found")
```

---

**Q89. Count capital letters in a file (works even if file is too big for memory)?**

💡**Concept:** This tests file streaming and memory usage: you should read line-by-line for large files. Interviewers often want to see that you avoid loading the entire file into RAM.

```python
# One-liner using generator (memory efficient — reads line by line):
count = sum(1 for line in open("file.txt") for c in line if c.isupper())
```

**No built-ins version (no `sum()`, no `.isupper()`):**
```python
def count_capitals_in_file(path):
    count = 0
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            for ch in line:
                code = ord(ch)
                if 65 <= code <= 90:  # 'A'..'Z'
                    count += 1
    return count
```

---

## 📌 SECTION 12 — Multithreading & NumPy

---

**Q90. How is multithreading achieved in Python?**
> Using the `threading` module. Threads share the same memory within a process.

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
import threading

def task(name):
    print(f"Running {name}")

t1 = threading.Thread(target=task, args=("A",))
t2 = threading.Thread(target=task, args=("B",))
t1.start(); t2.start()
t1.join();  t2.join()
```
> Due to the **GIL**, threading is best for **I/O-bound** tasks, not CPU-bound.

---

**Q91. Is Python list or NumPy array faster? Why?**
> **NumPy is 10-100x faster** for numerical operations.

💡**Concept:** NumPy is faster because its operations are vectorized and implemented in optimized C, using contiguous memory layouts. Python lists hold references to Python objects, which adds overhead for numeric heavy work.

```
Python list: interpreted, each item is a Python object, dynamic types
NumPy array: implemented in C, fixed type, contiguous memory, vectorised ops

Vectorised example (no explicit loop):
import numpy as np
a = np.array([1,2,3,4,5])
a * 2       # [2,4,6,8,10] — computed in C, no Python loop!
```

---

## 📌 SECTION 13 — Pandas & NumPy Q&A

---

**Q92. What is Pandas?**
> An open-source Python library for **data manipulation and analysis**. Provides DataFrame and Series.

💡**Concept:** Pandas is built for tabular data manipulation—filtering, grouping, joining, and time series. In interviews, mention DataFrame is like an Excel table with powerful programmatic operations.

```python
import pandas as pd
df = pd.DataFrame({"name": ["Alice","Bob"], "age": [25,30]})
print(df)
```

---

**Q93. What is the difference between DataFrame and Series?**

💡**Concept:** Series is a single labeled column, while DataFrame is a table of multiple columns. Many DataFrame operations return a Series when you select a single column.

```
Series    = 1D labelled array (single column)
DataFrame = 2D table with rows AND columns (collection of Series)
```
```python
s  = pd.Series([10, 20, 30])          # Series
df = pd.DataFrame({"a": [1,2], "b": [3,4]})  # DataFrame
```

---

**Q94. How do you create a DataFrame from a dictionary?**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
import pandas as pd
data = {"name": ["Alice", "Bob", "Carol"], "age": [25, 30, 22]}
df = pd.DataFrame(data)
print(df)
```

---

**Q95. How do you add a new column to a DataFrame?**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
df["salary"] = [70000, 85000, 60000]     # add with list
df["annual"] = df["salary"] * 12         # calculated column
```

---

**Q96. How do you get measures of central tendency for a NumPy array?**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
import numpy as np
arr = np.array([1, 2, 2, 3, 4, 5])

np.mean(arr)      # mean:   2.833...
np.median(arr)    # median: 2.5
# mode (needs scipy):
from scipy import stats
stats.mode(arr)   # ModeResult(mode=2, count=2)
```

---

**Q97. How do you get items NOT common to two Pandas Series?**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
a = pd.Series([1, 2, 3, 4, 5])
b = pd.Series([3, 4, 5, 6, 7])

not_common = pd.concat([a[~a.isin(b)], b[~b.isin(a)]])
print(not_common.values)   # [1, 2, 6, 7]
```

---

**Q98. How do you sort a NumPy array by the last column?**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
import numpy as np
arr = np.array([[3,1], [1,4], [2,2]])
sorted_arr = arr[arr[:, -1].argsort()]   # sort by last column
```

---

## 📌 SECTION 14 — Flask & Django

---

**Q99. What is Flask? What are its benefits?**
> A **lightweight micro web framework** for Python — minimal setup, highly flexible.

💡**Concept:** Flask is minimal and gives you control over choices (ORM, auth, structure). Interviewers like when you contrast it with Django’s batteries-included approach.

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

app.run(debug=True)
```
```
Benefits:
- Simple and easy to learn
- Lightweight (no unnecessary features)
- Flexible (choose your own libraries)
- Great for APIs and small apps
```

---

**Q100. Is Django better than Flask?**

💡**Concept:** This is a trade-off question: Django is faster for large structured apps, Flask is great for smaller services and APIs. A good answer matches framework to requirements rather than claiming one is always better.

```
FLASK:  Micro-framework, minimal, you decide everything, great for small apps/APIs
DJANGO: Full-stack, batteries included (admin, ORM, auth), great for large apps

Neither is "better" — pick based on project size and needs.
```

---

**Q101. What is Django's architecture?**
> Django follows **MVT — Model, View, Template**.

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```
Model    → defines data structure, talks to DB via ORM
View     → handles business logic, processes requests
Template → HTML files with Django tags for dynamic content

Request → URL Dispatcher → View → Model (if needed) → Template → Response
```

---

**Q102. What are sessions in Django?**
> Sessions let the server **remember user data across multiple requests** (HTTP is stateless).

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

- Used for: login state, shopping cart, user preferences
- Data stored server-side; user gets a session ID cookie

---

**Q103. What are Django's inheritance styles?**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```
Abstract Base Class → template, no DB table created
Multi-table         → each model gets its own DB table
Proxy Model         → same DB table, different Python behavior
```

---

## 📌 SECTION 15 — Python Internals

---

**Q104. What actually happens when you run a .py file?**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```
.py file → Lexer (tokens) → Parser (AST) → Compiler (bytecode .pyc)
       → PVM (Python Virtual Machine) → Output
```

---

**Q105. Why can't Python threads run truly in parallel on multi-core CPUs?**
> Because of the **GIL** — only one thread executes Python bytecode at any time, even on multi-core.
> Fix: Use `multiprocessing` for CPU-bound parallel work.

💡**Concept:** The core limitation is the GIL for CPU-bound work in CPython threads. The standard interview answer is: use multiprocessing for CPU-bound parallelism, threads/async for I/O concurrency.


---

**Q106. How does Python implement for loops internally?**
> Uses the **iterator protocol**: calls `iter()` then `next()` until `StopIteration`.

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
# What Python does internally:
it = iter([1, 2, 3])
while True:
    try:    item = next(it); print(item)
    except StopIteration: break
```

---

**Q107. Why are function default arguments evaluated only once?**
> Defaults stored in `func.__defaults__` at **definition time**, not per call.

💡**Concept:** This is a famous Python gotcha: default arguments are evaluated once and reused. The safe pattern is using `None` and creating a new list/dict inside the function.

```python
def append(val, lst=[]):    # WRONG — same list reused!
    lst.append(val)
    return lst

def append(val, lst=None):  # CORRECT — fresh list each time
    if lst is None: lst = []
    lst.append(val)
    return lst
```

---

**Q108. What is the id() function?**
> Returns a unique integer identifier for an object. In CPython = memory address.

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
x = 42
id(x)          # e.g. 140234567
y = x
id(x) == id(y) # True — same object
```

---

**Q109. Does Python support tail recursion optimisation?**
> **No.** Python does not optimise tail calls. Deep recursion hits the limit (default: 1000).

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
import sys
sys.getrecursionlimit()       # 1000
sys.setrecursionlimit(5000)   # increase if needed
# Better: replace deep recursion with a loop
```

---

## 📌 SECTION 16 — Tricky Output Questions

---

**Q110. What is the output?**

💡**Concept:** Because the default list is created once, both calls share the same list object. This is why the second call sees the result of the first call—an interview classic.

```python
def func(x, data=[]):
    data.append(x)
    return data

print(func(1))   # ?
print(func(2))   # ?
```
> **Output:** `[1]` then `[1, 2]`
> **Why:** Default `[]` created **once** at definition time, reused on every call!

---

**Q111. What does this print?**

💡**Concept:** Generators are iterators that get exhausted after one full pass. Once consumed, they don’t “reset,” so converting it to a list twice yields an empty list the second time.

```python
gen = (i for i in range(3))
list1 = list(gen)
list2 = list(gen)
print(list1, list2)
```
> **Output:** `[0, 1, 2] []`
> **Why:** Generators can only be consumed **once**. After `list1` uses it, it's exhausted.

---

**Q112. What does this print?**

💡**Concept:** `finally` executes even if `return` happens in `try`, and a `return` inside `finally` overrides earlier returns. This is why many style guides recommend avoiding `return` in `finally` unless intentional.

```python
def func():
    try:    return 1
    finally: return 2
print(func())
```
> **Output:** `2`
> **Why:** `finally` ALWAYS runs and its `return` overrides the `try` return.

---

**Q113. What does this print?**

💡**Concept:** These questions test whether you can reason about Python execution order, scope, and object behavior without running the code. A strong interview answer explains the *why* (not just the value) and names the underlying rule (like default args, generator exhaustion, or `finally`).

```python
print(True + True, True * 5, False + 1)
```
> **Output:** `2 5 1`
> **Why:** `True == 1`, `False == 0` in arithmetic.

---

**Q114. What does this print?**

💡**Concept:** In Python 3, the loop variable inside a list comprehension is scoped to the comprehension and doesn’t leak. In Python 2 it leaked, so this is also a version-awareness question.

```python
x = 5
[x for x in range(3)]
print(x)
```
> **Output:** `5`
> **Why:** List comprehension variable does **not** leak to outer scope in Python 3.

---

**Q115. What does this print?**

💡**Concept:** These questions test whether you can reason about Python execution order, scope, and object behavior without running the code. A strong interview answer explains the *why* (not just the value) and names the underlying rule (like default args, generator exhaustion, or `finally`).

```python
a, b = 1, 2
b, a = a, b
print(a, b)
```
> **Output:** `2 1`
> **Why:** Right side fully evaluated first → tuple `(1,2)` → unpacked. Clean swap!

---

**Q116. What does this print?**

💡**Concept:** These questions test whether you can reason about Python execution order, scope, and object behavior without running the code. A strong interview answer explains the *why* (not just the value) and names the underlying rule (like default args, generator exhaustion, or `finally`).

```python
a = 1
d = {a: "value"}
a = 2
print(d)
```
> **Output:** `{1: 'value'}`
> **Why:** Key takes the value of `a` at **creation time** (which was `1`). Reassigning `a` later doesn't change the key.

---

**Q117. What does this print?**

💡**Concept:** These questions test whether you can reason about Python execution order, scope, and object behavior without running the code. A strong interview answer explains the *why* (not just the value) and names the underlying rule (like default args, generator exhaustion, or `finally`).

```python
a, *b, c = [1, 2, 3, 4, 5]
print(a, b, c)
```
> **Output:** `1 [2, 3, 4] 5`
> **Why:** `*b` collects all **middle elements** into a list.

---

**Q118. What does this print?**

💡**Concept:** These questions test whether you can reason about Python execution order, scope, and object behavior without running the code. A strong interview answer explains the *why* (not just the value) and names the underlying rule (like default args, generator exhaustion, or `finally`).

```python
print([] and [1] or [2])
```
> **Output:** `[2]`
> **Why:** `[] and [1]` → `[]` (falsy, short-circuits). Then `[] or [2]` → `[2]` ([] is falsy).

---

**Q119. What is `(-7) // 2`?**
> **Output:** `-4`
> **Why:** Floor division floors toward **negative infinity**. `-7/2 = -3.5` → floor = `-4` (not `-3`!).

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.


---

**Q120. What is `"hello world"[::-1]`?**
> **Output:** `"dlrow olleh"`
> **Why:** `[::-1]` reverses the string using step `-1`.

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.


---

## 📌 SECTION 17 — Coding Questions

---

**Q121. Write Fibonacci series.**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(8)   # 0 1 1 2 3 5 8 13
```

---

**Q122. Check if a string is a palindrome.**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

is_palindrome("racecar")   # True
is_palindrome("hello")     # False
```

**No built-ins version (no `.lower()`, no `.replace()`, no slicing):**
```python
def is_palindrome_no_builtins(s):
    cleaned = []
    for ch in s:
        code = ord(ch)
        is_digit = 48 <= code <= 57
        is_upper = 65 <= code <= 90
        is_lower = 97 <= code <= 122

        if is_digit or is_upper or is_lower:
            if is_upper:
                cleaned.append(chr(code + 32))  # to lowercase
            else:
                cleaned.append(ch)

    i, j = 0, len(cleaned) - 1
    while i < j:
        if cleaned[i] != cleaned[j]:
            return False
        i += 1
        j -= 1
    return True

print(is_palindrome_no_builtins("A man, a plan, a canal: Panama"))  # True
```

---

**Q123. Check if a number is prime.**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

is_prime(17)   # True
is_prime(20)   # False
```

**No built-ins version (avoid sqrt/int; use `i*i <= n`):**
```python
def is_prime_no_sqrt(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print(is_prime_no_sqrt(17))  # True
print(is_prime_no_sqrt(20))  # False
```

---

**Q124. Write bubble sort.**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

bubble_sort([64, 34, 25, 12])   # [12, 25, 34, 64]
```

---

**Q125. Generate squares of every element in a list.**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
nums = [1, 2, 3, 4, 5]
squares = [x**2 for x in nums]   # [1, 4, 9, 16, 25]
```

**No built-ins version (no list comprehension):**
```python
nums = [1, 2, 3, 4, 5]
squares = []
for x in nums:
    squares.append(x * x)
print(squares)  # [1, 4, 9, 16, 25]
```

---

**Q126. Check if a number is an Armstrong number.**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
def is_armstrong(n):
    digits = str(n)
    return sum(int(d)**len(digits) for d in digits) == n

is_armstrong(153)   # True  (1³+5³+3³ = 153)
is_armstrong(10)    # False
```

**No built-ins version (no `str()`, no `sum()`):**
```python
def is_armstrong_no_builtins(n):
    if n < 0:
        return False

    # count digits
    temp = n
    digits = 0
    if temp == 0:
        digits = 1
    else:
        while temp > 0:
            digits += 1
            temp //= 10

    # compute armstrong sum
    temp = n
    total = 0
    while temp > 0:
        d = temp % 10
        # power manually: d ** digits
        p = 1
        i = 0
        while i < digits:
            p *= d
            i += 1
        total += p
        temp //= 10

    return total == n

print(is_armstrong_no_builtins(153))  # True
```

---

**Q127. Check leap year.**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
def is_leap(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

is_leap(2024)   # True
is_leap(1900)   # False
```

---

**Q128. Factorial of a number.**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
def factorial(n):
    result = 1
    for i in range(2, n+1): result *= i
    return result

factorial(5)   # 120
```

---

**Q129. Swap two variables.**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
a, b = 5, 10
a, b = b, a       # Python way — no temp variable needed!
print(a, b)       # 10 5
```

---

**Q130. Find the second largest element.**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
lst = [10, 20, 4000, 6000]
sorted(set(lst))[-2]   # 4000
```

**No built-ins version (no `sorted()`, no `set()`):**
```python
def second_largest(arr):
    if len(arr) < 2:
        return None

    first = None
    second = None

    for x in arr:
        if first is None or x > first:
            second = first
            first = x
        elif x != first and (second is None or x > second):
            second = x

    return second

print(second_largest([10, 20, 4000, 6000]))  # 4000
```

---

**Q131. Check if a number is a strong number.**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
import math
def is_strong(n):
    return sum(math.factorial(int(d)) for d in str(n)) == n

is_strong(145)   # True  (1!+4!+5! = 1+24+120 = 145)
```

**No built-ins version (no `math.factorial()`, no `str()`, no `sum()`):**
```python
def factorial(k):
    res = 1
    i = 2
    while i <= k:
        res *= i
        i += 1
    return res

def is_strong_no_builtins(n):
    if n < 0:
        return False

    temp = n
    total = 0

    if temp == 0:
        total = 1  # 0! = 1

    while temp > 0:
        d = temp % 10
        total += factorial(d)
        temp //= 10

    return total == n

print(is_strong_no_builtins(145))  # True
```

---

**Q132. Print number pattern.**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
# Pattern: 0 0 0 0 / 1 1 1 / 2 2 / 3
rows = 4
for i in range(rows):
    print(" ".join([str(i)] * (rows - i)))
# 0 0 0 0
# 1 1 1
# 2 2
# 3
```

**No built-ins version (no `.join()`, no `str()` list-multiply trick):**
```python
rows = 4
for i in range(rows):
    line = ""
    k = 0
    while k < (rows - i):
        # manual int->string for 0-9 (pattern uses small numbers)
        line += chr(ord('0') + i)
        if k != (rows - i) - 1:
            line += " "
        k += 1
    print(line)
```

---

**Q133. Reverse a string (two methods).**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
s = "hello"
s[::-1]              # "olleh" — slicing
"".join(reversed(s)) # "olleh" — built-in
```

**No built-ins version (no slicing, no `reversed()`, no `join()`):**
```python
def reverse_string(s):
    out = ""
    i = 0
    while i < len(s):
        out = s[i] + out
        i += 1
    return out

print(reverse_string("hello"))  # olleh
```

---

**Q134. Add two integers without the `+` operator.**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
def add(a, b):
    while b:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

add(5, 3)   # 8
```

---

**Q135. Convert date from YYYY-MM-DD to DD-MM-YYYY.**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
from datetime import datetime

def convert_date(s):
    d = datetime.strptime(s, "%Y-%m-%d")
    return d.strftime("%d-%m-%Y")

convert_date("2024-03-15")   # "15-03-2024"
```

**No built-ins version (no `datetime`):**
```python
def convert_date_no_datetime(s):
    # expected: YYYY-MM-DD
    parts = []
    cur = ""
    for ch in s:
        if ch == "-":
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    parts.append(cur)

    if len(parts) != 3:
        return None

    yyyy, mm, dd = parts
    return dd + "-" + mm + "-" + yyyy

print(convert_date_no_datetime("2024-03-15"))  # 15-03-2024
```

---

**Q136. Save an image from a URL.**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
import requests

url = "https://example.com/photo.jpg"
r = requests.get(url)
with open("photo.jpg", "wb") as f:
    f.write(r.content)
```

**Standard library version (no `requests`):**
```python
from urllib.request import urlopen

url = "https://example.com/photo.jpg"
with urlopen(url) as r:
    data = r.read()

with open("photo.jpg", "wb") as f:
    f.write(data)
```

---

**Q137. Send an email using Python.**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Hello!")
msg["Subject"] = "Test"
msg["From"] = "you@gmail.com"
msg["To"]   = "them@gmail.com"

with smtplib.SMTP("smtp.gmail.com", 587) as s:
    s.starttls()
    s.login("you@gmail.com", "password")
    s.send_message(msg)
```

---

**Q138. Find middle element of a linked list in one pass.**

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.

```python
# Two-pointer (slow + fast) technique:
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next        # 1 step
        fast = fast.next.next   # 2 steps
    return slow   # when fast reaches end, slow is at middle!
```

---

**Q139. How do you find the middle of a linked list? (Interview Explanation)**
> Use **slow/fast pointers**: slow moves 1 step, fast moves 2 steps. When fast reaches the end, slow is at the middle. No need to know the length.

💡**Concept:** Add 1–2 lines about why this matters in real projects and what interviewers typically look for. A small example or edge case explanation usually makes the concept stick.


---

## 📌 QUICK MEMORY TRICKS

```
is vs ==          →  is = same PERSON, == = same VALUE
Mutable           →  Lists & Dicts are LIQUID (can change)
Immutable         →  Strings & Tuples are SOLID (locked)
LEGB rule         →  "Let Every Good Boy win"
sort() vs sorted()→  sort() changes original, sorted() returns NEW list
Shallow copy      →  same house, shared bathroom (shared nested objects)
Deep copy         →  separate house (nothing shared)
GIL               →  talking stick — only 1 thread talks at a time
*args             →  extra positionals → TUPLE
**kwargs          →  extra keywords   → DICT
break             →  EXIT door
continue          →  SKIP a page
pass              →  EMPTY page placeholder
Generator         →  LAZY — produces one value at a time (yield)
Decorator         →  WRAPPER — adds behaviour without changing original
```

---

## 📌 INTERVIEW CHEATSHEET — 30-Second Answers

| Question | Answer in one line |
|---|---|
| Compiled or interpreted? | Both — compiles to bytecode, PVM interprets |
| Mutable types? | list, dict, set |
| Immutable types? | int, str, tuple, float, bool |
| sort() vs sorted()? | sort() = in-place/None. sorted() = new list |
| is vs ==? | is = same object. == = same value |
| *args vs **kwargs? | *args = tuple. **kwargs = dict |
| Shallow vs deep copy? | shallow = shared nested. deep = fully independent |
| GIL? | One thread runs at a time in CPython |
| Module vs package? | Module = .py file. Package = directory + __init__.py |
| List vs tuple? | List = mutable. Tuple = immutable, faster, hashable |
| for loop internally? | iter() → next() → StopIteration |
| Why set is unordered? | Items stored by hash value, not insertion order |
| Lambda? | Anonymous one-line function |
| Generator? | Uses yield, produces one value at a time, memory efficient |
| Decorator? | Wraps a function to add behaviour without changing it |
| self? | Reference to current class instance, not a keyword |
| __init__ vs __new__? | __new__ creates. __init__ initialises |
| Abstraction? | Hide complexity, show only what's needed |
| Encapsulation? | Bundle data+methods, restrict direct access |
| Default arg evaluated? | Once at definition time — not per call (gotcha!) |

---

> **Final tip:** Read this file once carefully. Then do a quick scan before your interview.
> The goal isn't to memorise word-for-word — it's to understand the concept so you can explain it naturally.
> **Good luck! 🐍🚀**
