# 🐍 Python Interview Tricks — Complete Guide
> Every gotcha, every output trap, every concept interviewers use to test depth.
> Three levels so you can stop, absorb, and come back without reading fatigue.

---

## How to Use This Guide

| Level | Who it's for | Topics |
|---|---|---|
| 🟢 **Basic** | Beginners or quick refresher | Mutability, is vs ==, truthiness, strings, type traps |
| 🟡 **Intermediate** | 1–2 years experience | Closures, scope, mutable defaults, list traps, OOP |
| 🔴 **Advanced** | Senior roles | Decorators, generators, metaclasses, GIL, memory, dunder methods |

**Tip:** Each level ends with a quick-fire recap. Get them all right → move on. Miss one → re-read that section.

---

## Table of Contents

**🟢 Level 1 — Basic (Questions 1–10)**
1. [Mutable vs Immutable — The Core Rule](#1-mutable-vs-immutable--the-core-rule)
2. [is vs == — Identity vs Equality](#2-is-vs----identity-vs-equality)
3. [Integer Caching — The Small Int Pool](#3-integer-caching--the-small-int-pool)
4. [Truthy and Falsy in Python](#4-truthy-and-falsy-in-python)
5. [String Immutability Trap](#5-string-immutability-trap)
6. [List Multiplication Trap](#6-list-multiplication-trap)
7. [Floating Point — Same as JS](#7-floating-point--same-as-js)
8. [None is Not Zero](#8-none-is-not-zero)
9. [Integer Division vs True Division](#9-integer-division-vs-true-division)
10. [Type Function Surprises](#10-type-function-surprises)

**🟡 Level 2 — Intermediate (Questions 11–22)**
11. [Mutable Default Argument — The Most Famous Python Bug](#11-mutable-default-argument--the-most-famous-python-bug)
12. [List is Passed by Reference](#12-list-is-passed-by-reference)
13. [Shallow Copy vs Deep Copy](#13-shallow-copy-vs-deep-copy)
14. [LEGB Scope Rule](#14-legb-scope-rule)
15. [global and nonlocal Keywords](#15-global-and-nonlocal-keywords)
16. [Closure — The Late Binding Trap](#16-closure--the-late-binding-trap)
17. [List Slicing Surprises](#17-list-slicing-surprises)
18. [Dictionary Ordering and Key Rules](#18-dictionary-ordering-and-key-rules)
19. [Unpacking and Star Expressions](#19-unpacking-and-star-expressions)
20. [Class vs Instance Variables — The Trap](#20-class-vs-instance-variables--the-trap)
21. [Inheritance MRO — Which Method Wins?](#21-inheritance-mro--which-method-wins)
22. [List Comprehension vs Generator Expression](#22-list-comprehension-vs-generator-expression)

**🔴 Level 3 — Advanced (Questions 23–35)**
23. [Generators — Lazy Evaluation and Exhaustion](#23-generators--lazy-evaluation-and-exhaustion)
24. [Decorators — What They Really Do](#24-decorators--what-they-really-do)
25. [functools.wraps — Why It Matters](#25-functoolswraps--why-it-matters)
26. [Dunder Methods — The Magic Behind Operators](#26-dunder-methods--the-magic-behind-operators)
27. [context managers — with Statement Internals](#27-context-managers--with-statement-internals)
28. [*args and **kwargs — Every Combination](#28-args-and-kwargs--every-combination)
29. [Lambda in a Loop — The Capture Trap](#29-lambda-in-a-loop--the-capture-trap)
30. [Tuple is Immutable — Except When It's Not](#30-tuple-is-immutable--except-when-its-not)
31. [Exception Handling Traps](#31-exception-handling-traps)
32. [GIL — Global Interpreter Lock](#32-gil--global-interpreter-lock)
33. [Memory and Reference Counting](#33-memory-and-reference-counting)
34. [Walrus Operator — := Trap](#34-walrus-operator---trap)
35. [if __name__ == "__main__" — What and Why](#35-if-__name__--__main__--what-and-why)

**📋 Master Summary**
36. [Every Rule in One Place](#36-master-summary--every-rule-in-one-place)

---

---

# 🟢 LEVEL 1 — BASIC
### What to expect: Fundamental output questions. These come up in every Python interview at every level.
### Goal: If any answer surprises you, that's your study target. All 10 should feel obvious before moving to Level 2.

---

## 1. Mutable vs Immutable — The Core Rule

### ❓ Output?
```python
# Which can be changed after creation?
a = [1, 2, 3]
a[0] = 99
print(a)

b = (1, 2, 3)
b[0] = 99
print(b)
```

### 😱 Answer
```
[99, 2, 3]          # list — mutable, changed in place
TypeError: 'tuple' object does not support item assignment
```

### 🧠 Concept — The Foundation of Python

| Mutable (can change) | Immutable (cannot change) |
|---|---|
| `list` | `int`, `float`, `bool` |
| `dict` | `str` |
| `set` | `tuple` |
| custom objects (usually) | `frozenset` |
| | `bytes` |

**Why it matters:**
- Mutable objects can be edited in place — mutations affect all references
- Immutable objects create new objects on every "change" — the original is untouched
- Only immutable objects can be dictionary keys or set elements (they must be hashable)

---

## 2. is vs == — Identity vs Equality

### ❓ Output?
```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
print(a is b)
print(a is c)
```

### 😱 Answer
```
True    # same contents
False   # different objects in memory
True    # c points to the exact same object as a
```

### 🧠 Concept
- `==` checks **value** (contents are equal)
- `is` checks **identity** (same object in memory — same memory address)

```python
print(id(a))   # memory address of a
print(id(b))   # different memory address
print(id(c))   # same as a
```

> **Rule: Use `==` for value comparison. Use `is` only for `None`, `True`, `False` checks.**

```python
# Correct
if x is None:     # ✅
if x == None:     # ❌ works but wrong style

# Never do this
if x is [1, 2]:   # ❌ almost always False — different objects
```

---

## 3. Integer Caching — The Small Int Pool

### ❓ Output?
```python
a = 256
b = 256
print(a is b)

c = 257
d = 257
print(c is d)

x = -5
y = -5
print(x is y)

p = -6
q = -6
print(p is q)
```

### 😱 Answer
```
True    # 256 is cached
False   # 257 is NOT cached — different objects
True    # -5 is cached (range is -5 to 256)
False   # -6 is NOT cached
```

### 🧠 Concept
Python pre-creates and caches small integers from **-5 to 256** at startup. Integers in this range are **singletons** — `a = 256` and `b = 256` point to the exact same object.

Outside this range, each assignment creates a new object — `is` returns `False`.

> **This is CPython-specific behaviour. Never rely on `is` for integer comparison. Always use `==`.**

---

## 4. Truthy and Falsy in Python

### ❓ Output?
```python
print(bool([]))
print(bool({}))
print(bool(""))
print(bool(0))
print(bool(None))
print(bool([0]))
print(bool("0"))
print(bool(" "))
```

### 😱 Answer
```
False   # empty list
False   # empty dict
False   # empty string
False   # zero
False   # None
True    # list with one element (even if that element is 0)
True    # non-empty string
True    # string with a space — not empty!
```

### 🧠 Python Falsy Values
```
False    None    0    0.0    0j    ""    []    {}    ()    set()    b""
```
Everything else is truthy — including `[0]`, `"0"`, `" "`.

**Common trap:**
```python
data = []
if data:          # False — empty list is falsy
    process(data)

value = 0
if value:         # False — 0 is falsy, even if 0 is a valid value!
    use(value)    # BUG: never reached when value is 0

# Fix: be explicit
if value is not None:   # only skips None
```

---

## 5. String Immutability Trap

### ❓ Output?
```python
s = "hello"
s[0] = "H"
print(s)
```

### 😱 Answer
```
TypeError: 'str' object does not support item assignment
```

### ❓ Then how does this work?
```python
s = "hello"
s = s.upper()
print(s)

s = "hello"
s += " world"
print(s)
```

### 😱 Answer
```
"HELLO"
"hello world"
```

### 🧠 Concept
Strings are **immutable** — you cannot change a character in place. Every string "modification" creates a **new string object**. The original is untouched.

```python
s = "hello"
print(id(s))       # address of original
s += " world"
print(id(s))       # different address — new string object!
```

**String interning — another trap:**
```python
a = "hello"
b = "hello"
print(a is b)      # True — Python interns short strings

a = "hello world"
b = "hello world"
print(a is b)      # might be False — longer strings may not be interned
```

> **Never use `is` to compare strings. Always use `==`.**

---

## 6. List Multiplication Trap

### ❓ Output?
```python
# Create a 3x3 grid
grid = [[0] * 3] * 3
grid[0][0] = 99
print(grid)
```

### 😱 Answer
```
[[99, 0, 0], [99, 0, 0], [99, 0, 0]]
```

### 🧠 Concept — The Shared Reference Trap
`[[0] * 3] * 3` creates one inner list and replicates the **reference** to it three times. All three rows point to the **same list object** in memory.

Changing `grid[0][0]` changes all three rows because they're all the same list.

**Fix — use a list comprehension:**
```python
grid = [[0] * 3 for _ in range(3)]
grid[0][0] = 99
print(grid)
# [[99, 0, 0], [0, 0, 0], [0, 0, 0]]  ✅
```

The comprehension creates a **new** inner list for each row.

---

## 7. Floating Point — Same as JS

### ❓ Output?
```python
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
```

### 😱 Answer
```
0.30000000000000004
False
```

### 🧠 Concept
IEEE 754 floating point — `0.1` cannot be stored exactly in binary. Same issue exists in every language.

**Fix:**
```python
import math
math.isclose(0.1 + 0.2, 0.3)   # True — use tolerance

round(0.1 + 0.2, 10) == 0.3    # True
```

> **Never use `==` to compare floats. Use `math.isclose()` or `round()`.**

---

## 8. None is Not Zero

### ❓ Output?
```python
print(None == 0)
print(None == False)
print(None == "")
print(None == [])
print(bool(None))
print(None is None)
```

### 😱 Answer
```
False
False
False
False
False   # None is falsy but not equal to anything else
True    # None is a singleton
```

### 🧠 Concept
`None` is Python's `null`. It is **falsy** but not equal to `0`, `False`, `""`, or `[]`. Unlike JavaScript, Python's `None` does not equal these values even with `==`.

`None` is a **singleton** — there is only ever one `None` object in memory. Always check with `is None`, never `== None`.

```python
if x is None:       # ✅ correct
if x is not None:   # ✅ correct
if not x:           # ❌ also catches 0, [], "" — too broad
```

---

## 9. Integer Division vs True Division

### ❓ Output?
```python
print(7 / 2)
print(7 // 2)
print(-7 // 2)
print(7 % 2)
print(-7 % 2)
print(divmod(7, 2))
```

### 😱 Answer
```
3.5    # true division — always returns float
3      # floor division — rounds DOWN (toward negative infinity)
-4     # floor division — NOT truncation! Rounds toward -infinity
1      # modulo
1      # modulo is always same sign as the divisor in Python
(3, 1) # divmod returns (quotient, remainder)
```

### 🧠 Concept
- `/` always returns a `float` in Python 3
- `//` is **floor division** — rounds toward negative infinity, NOT toward zero
- `-7 // 2` = `-4` NOT `-3` (floor of -3.5 is -4)
- `%` in Python follows the sign of the **divisor** (second number), unlike C or JavaScript

```python
# The difference
-7 // 2    # -4  (floor: -3.5 → -4)
int(-7/2)  # -3  (truncation: -3.5 → -3)
```

---

## 10. Type Function Surprises

### ❓ Output?
```python
print(type(1))
print(type(1.0))
print(type(True))
print(type(None))
print(type([]))
print(type(()))
print(type({}))
print(isinstance(True, int))
print(isinstance(False, int))
print(True + True)
print(True * 5)
```

### 😱 Answer
```
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
<class 'list'>
<class 'tuple'>
<class 'dict'>
True     # bool is a SUBCLASS of int!
True
2        # True = 1, True + True = 2
5        # True = 1, 1 * 5 = 5
```

### 🧠 Concept
`bool` is a **subclass** of `int` in Python. `True` = `1`, `False` = `0`. They can be used in arithmetic.

```python
sum([True, True, False, True])  # 2 — counts True values!
[1, 2, 3][True]                 # 2 — True is index 1
```

> **`isinstance(True, int)` returns `True`! Use `type(x) is bool` for strict type check.**

---

### 🟢 Level 1 Recap — Before You Move On

Quick-fire:
```python
print(bool([]))          # ?
print(0.1 + 0.2 == 0.3) # ?
print(256 is 256)        # ?
print(257 is 257)        # ?
print(True + True)       # ?
grid = [[0]*2]*2; grid[0][0]=9; print(grid)  # ?
```

**Answers:** `False` / `False` / `True` / `False` / `2` / `[[9, 0], [9, 0]]`

All correct → move to Level 2.

---

---

# 🟡 LEVEL 2 — INTERMEDIATE
### What to expect: These are where most Python developers get tripped up. Scope, closures, mutable traps, and OOP behaviour.
### Goal: Understand WHY each answer is what it is. Don't just memorise the output.

---

## 11. Mutable Default Argument — The Most Famous Python Bug

### ❓ Output?
```python
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))
print(add_item(2))
print(add_item(3))
```

### 😱 Answer
```
[1]
[1, 2]
[1, 2, 3]
```

### 🧠 Concept — The #1 Python Gotcha
Default arguments are evaluated **once when the function is defined**, not each time it's called.

The `lst=[]` creates ONE list object at definition time. Every call that uses the default shares that same list. It accumulates across calls — never resets.

**Fix — use `None` as default:**
```python
def add_item(item, lst=None):
    if lst is None:
        lst = []          # new list created on each call
    lst.append(item)
    return lst

print(add_item(1))   # [1]
print(add_item(2))   # [2]
print(add_item(3))   # [3]  ✅
```

> **Rule: Never use mutable objects (list, dict, set) as default arguments. Always use `None`.**

Same problem with dicts:
```python
def add_to_dict(key, val, d={}):  # ❌ same trap
    d[key] = val
    return d
```

---

## 12. List is Passed by Reference

### ❓ Output?
```python
def modify(lst):
    lst.append(4)
    lst = [10, 20, 30]   # reassignment

original = [1, 2, 3]
modify(original)
print(original)
```

### 😱 Answer
```
[1, 2, 3, 4]
```

### 🧠 Concept — Mutable Object Reference
Python passes object **references**. Mutating through the reference affects the original. But **reassigning** the parameter creates a new local reference — it doesn't affect the original.

- `lst.append(4)` → mutates through reference → original changes ✅
- `lst = [10, 20, 30]` → reassigns local variable `lst` → original unchanged

Think of it as: you're given the address of a house. You can redecorate inside (mutation). But writing a new address on your paper (reassignment) doesn't move the original house.

---

## 13. Shallow Copy vs Deep Copy

### ❓ Output?
```python
import copy

original = [[1, 2], [3, 4]]

shallow = original.copy()
shallow[0][0] = 99
print(original)

deep = copy.deepcopy(original)
deep[0][0] = 77
print(original)
```

### 😱 Answer
```
[[99, 2], [3, 4]]   # shallow copy — inner lists still shared!
[[99, 2], [3, 4]]   # deep copy — completely independent
```

### 🧠 Concept

| Method | What it copies |
|---|---|
| `=` assignment | Same reference — not a copy at all |
| `list.copy()` | Shallow — new outer list, same inner objects |
| `list[:]` | Shallow |
| `copy.copy()` | Shallow |
| `copy.deepcopy()` | Deep — completely independent at all levels |

**Shallow copy** creates a new container but fills it with references to the same inner objects.
**Deep copy** recursively creates new objects for everything.

---

## 14. LEGB Scope Rule

### ❓ Output?
```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        print(x)    # which x?

    inner()

outer()
print(x)
```

### 😱 Answer
```
"enclosing"
"global"
```

### 🧠 Concept — LEGB Rule
Python looks up variables in this exact order:

```
L — Local        (inside current function)
E — Enclosing    (in outer/enclosing functions, for nested functions)
G — Global       (module level)
B — Built-in     (Python built-ins: len, print, etc.)
```

`inner()` has no local `x` → looks at enclosing `outer()` → finds `"enclosing"` → stops there. Never reaches global.

```python
x = 10

def test():
    print(x)       # reads global x ✅
    x = 20         # creates local x — BUT...
    print(x)

test()  # UnboundLocalError!
```

Once Python sees `x = 20` inside the function, it treats ALL references to `x` in that function as local — including the `print(x)` before the assignment. Accessing a local variable before assignment = `UnboundLocalError`.

---

## 15. global and nonlocal Keywords

### ❓ Output?
```python
count = 0

def increment():
    count += 1    # does this work?

increment()
print(count)
```

### 😱 Answer
```
UnboundLocalError: local variable 'count' referenced before assignment
```

### ❓ Fix with global:
```python
count = 0

def increment():
    global count
    count += 1

increment()
increment()
print(count)
```

### 😱 Answer
```
2
```

### ❓ nonlocal for nested functions:
```python
def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1
    inner()
    inner()
    print(x)

outer()
```

### 😱 Answer
```
2
```

### 🧠 Concept
- `global` → declares that a variable name refers to the global scope
- `nonlocal` → declares that a variable refers to the enclosing function's scope (not global)

Without these keywords, assignment creates a **new local variable** — it never modifies the outer one.

---

## 16. Closure — The Late Binding Trap

### ❓ Output?
```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)

print(funcs[0]())
print(funcs[1]())
print(funcs[2]())
```

### 😱 Answer
```
2
2
2
```

### 🧠 Concept
Python closures bind to the **variable itself**, not the value it had when the lambda was created. By the time the lambdas are called, the loop has ended and `i = 2`. All three lambdas reference the same `i`.

Same problem as JavaScript's `var` in loops.

**Fix 1 — default argument captures value immediately:**
```python
funcs = [lambda i=i: i for i in range(3)]
print(funcs[0]())  # 0
print(funcs[1]())  # 1
print(funcs[2]())  # 2  ✅
```

**Fix 2 — use a factory function:**
```python
def make_func(i):
    return lambda: i

funcs = [make_func(i) for i in range(3)]
```

---

## 17. List Slicing Surprises

### ❓ Output?
```python
lst = [1, 2, 3, 4, 5]

print(lst[1:3])
print(lst[-2:])
print(lst[::-1])
print(lst[::2])
print(lst[10:20])
print(lst[3:1])

copy = lst[:]
copy[0] = 99
print(lst[0])
```

### 😱 Answer
```
[2, 3]        # index 1 up to (not including) 3
[4, 5]        # last 2 elements
[5, 4, 3, 2, 1]  # reverse
[1, 3, 5]     # every 2nd element
[]            # out of range → empty list, no error
[]            # start > end → empty list, no error
1             # slice creates a shallow copy — original unchanged
```

### 🧠 Key Slicing Rules
```
lst[start:stop:step]
- stop is EXCLUSIVE (not included)
- Negative index counts from the end: -1 = last, -2 = second-to-last
- Out-of-range slice → empty list (no IndexError)
- step=-1 → reverse
- lst[:] → shallow copy of entire list
```

---

## 18. Dictionary Ordering and Key Rules

### ❓ Output?
```python
# Can you use these as dict keys?
d = {}
d[[1, 2]] = "list key"    # ?
d[(1, 2)] = "tuple key"   # ?
d[{1, 2}] = "set key"     # ?
d[{1: 'a'}] = "dict key"  # ?
```

### 😱 Answer
```
TypeError: unhashable type: 'list'
# (1, 2): "tuple key"  ✅
TypeError: unhashable type: 'set'
TypeError: unhashable type: 'dict'
```

### 🧠 Concept
Dictionary keys must be **hashable** — meaning they have a fixed hash value that never changes. Only immutable objects are hashable.

- `list` → unhashable (mutable)
- `tuple` → hashable IF all its elements are hashable
- `set` → unhashable (mutable)
- `frozenset` → hashable (immutable set)

```python
d[(1, [2])] = "val"    # TypeError — tuple containing a list is unhashable
d[(1, (2,))] = "val"   # ✅ — tuple of tuples is fine
```

**Dictionary order:** As of Python 3.7+, dicts maintain **insertion order**. This is guaranteed by the language spec.

---

## 19. Unpacking and Star Expressions

### ❓ Output?
```python
a, b, c = [1, 2, 3]
print(a, b, c)

a, *b, c = [1, 2, 3, 4, 5]
print(a, b, c)

a, b = b, a      # swap
print(a, b)

first, *rest = range(5)
print(first, rest)
```

### 😱 Answer
```
1 2 3
1 [2, 3, 4] 5          # *b collects the middle as a list
5 1                     # swap — right side evaluated first as tuple
0 [1, 2, 3, 4]
```

### 🧠 Key Points
- `*name` in unpacking collects multiple values into a list
- Can appear anywhere in the unpacking (left, middle, right) — but only once
- Swap trick `a, b = b, a` works because the right side is evaluated as a tuple first, then unpacked

---

## 20. Class vs Instance Variables — The Trap

### ❓ Output?
```python
class Dog:
    tricks = []    # class variable — shared!

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d1 = Dog("Rex")
d2 = Dog("Buddy")

d1.add_trick("sit")
d2.add_trick("roll")

print(d1.tricks)
print(d2.tricks)
```

### 😱 Answer
```
['sit', 'roll']
['sit', 'roll']
```

### 🧠 Concept — Shared Mutable Class Variable
`tricks = []` is a **class variable** — shared by ALL instances. `d1.tricks.append("sit")` mutates the class-level list. Both `d1.tricks` and `d2.tricks` point to the same list.

**Fix — create instance variable in `__init__`:**
```python
def __init__(self, name):
    self.name = name
    self.tricks = []   # new list per instance ✅
```

### ❓ Tricky variation:
```python
class Counter:
    count = 0

c1 = Counter()
c2 = Counter()

c1.count += 1    # this SHADOWS the class variable!
print(c1.count)
print(c2.count)
print(Counter.count)
```

### 😱 Answer
```
1
0
0
```

`c1.count += 1` (which is `c1.count = c1.count + 1`) creates a **new instance variable** `count` on `c1` that shadows the class variable. `c2.count` and `Counter.count` are unaffected.

---

## 21. Inheritance MRO — Which Method Wins?

### ❓ Output?
```python
class A:
    def hello(self):
        return "A"

class B(A):
    def hello(self):
        return "B"

class C(A):
    def hello(self):
        return "C"

class D(B, C):
    pass

d = D()
print(d.hello())
print(D.__mro__)
```

### 😱 Answer
```
"B"
(<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

### 🧠 Concept — MRO (Method Resolution Order)
Python uses the **C3 linearization** algorithm to determine which method to call in multiple inheritance.

```
D → B → C → A → object
```

When you call `d.hello()`, Python walks left to right and picks the first class that has the method. `B` comes before `C`, so `B.hello()` wins.

Use `ClassName.__mro__` or `ClassName.mro()` to see the order.

> **If you use `super()` inside B, it calls C's method next — not A. `super()` follows MRO, not direct parent.**

---

## 22. List Comprehension vs Generator Expression

### ❓ Output?
```python
# List comprehension
lc = [x * 2 for x in range(5)]
print(type(lc))
print(lc)

# Generator expression
ge = (x * 2 for x in range(5))
print(type(ge))
print(list(ge))
print(list(ge))   # what happens here?
```

### 😱 Answer
```
<class 'list'>
[0, 2, 4, 6, 8]
<class 'generator'>
[0, 2, 4, 6, 8]
[]                 # generator is exhausted!
```

### 🧠 Concept

| | List comprehension `[...]` | Generator expression `(...)` |
|---|---|---|
| Returns | A list (all values in memory) | A generator object (lazy) |
| Memory | O(n) — all at once | O(1) — one value at a time |
| Reusable | ✅ Yes | ❌ No — exhausted after one pass |
| Use when | Need all values, multiple iterations | Large data, only need one pass |

**Generators are lazy** — they produce values one at a time as you ask for them. Once exhausted, they're empty forever.

---

### 🟡 Level 2 Recap — Before You Move On

```python
def f(lst=[]):
    lst.append(1)
    return lst

print(f())   # ?
print(f())   # ?

funcs = [lambda: i for i in range(3)]
print(funcs[0]())   # ?

class A:
    x = []
a1 = A()
a2 = A()
a1.x.append(1)
print(a2.x)   # ?

ge = (i for i in range(3))
list(ge)
print(list(ge))  # ?
```

**Answers:** `[1]` / `[1, 1]` / `2` / `[1]` / `[]`

---

---

# 🔴 LEVEL 3 — ADVANCED
### What to expect: Python internals, patterns, and the edge cases that reveal deep understanding. Senior and specialist questions.
### Goal: Even knowing what these concepts ARE impresses interviewers. Understanding them fully sets you apart.

---

## 23. Generators — Lazy Evaluation and Exhaustion

### ❓ Output?
```python
def gen():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")

g = gen()
print("created")
print(next(g))
print(next(g))
print(next(g))   # what happens?
```

### 😱 Answer
```
created           # generator not started yet — lazy!
start
1
middle
2
end
StopIteration     # no more values
```

### 🧠 Concept
A generator function returns a **generator object** immediately — no code runs yet.

`next()` resumes execution from where it last paused (at `yield`). Code runs until the next `yield`, then pauses again.

```python
# Generator function (uses yield)
def count_up():
    yield 1
    yield 2
    yield 3

# Generator expression (lazy list comprehension)
squares = (x**2 for x in range(1000000))  # no memory used yet
```

**Key facts:**
- `yield` pauses execution and sends a value out
- `return` inside a generator raises `StopIteration`
- Generators are exhausted after one full pass
- `yield from iterable` delegates to another iterable

---

## 24. Decorators — What They Really Do

### ❓ Output?
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"hello {name}")

say_hello("Suvam")
print(say_hello.__name__)
```

### 😱 Answer
```
before
hello Suvam
after
wrapper    # ← original name is lost!
```

### 🧠 Concept
`@my_decorator` is **syntactic sugar** for:
```python
say_hello = my_decorator(say_hello)
```

The original function is replaced by `wrapper`. This is why `__name__` shows `"wrapper"` — the original function identity is lost.

**Fix: `functools.wraps`** (see next question).

**Decorators with arguments** require an extra layer:
```python
def repeat(n):           # outer function takes decorator args
    def decorator(func): # actual decorator
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("hi")

greet()  # prints "hi" three times
```

---

## 25. functools.wraps — Why It Matters

### ❓ Output?
```python
import functools

def my_decorator(func):
    @functools.wraps(func)     # preserves original metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def important_function():
    """This docstring matters."""
    pass

print(important_function.__name__)
print(important_function.__doc__)
```

### 😱 Answer
```
"important_function"    # ✅ name preserved
"This docstring matters."  # ✅ docstring preserved
```

### 🧠 Concept
Without `@functools.wraps`, the decorator replaces the function — losing `__name__`, `__doc__`, `__module__`, and other metadata. This breaks debugging, documentation tools, and introspection.

`@functools.wraps(func)` copies all metadata from the original function to the wrapper.

> **Rule: Always use `@functools.wraps` when writing decorators.**

---

## 26. Dunder Methods — The Magic Behind Operators

### ❓ Output?
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __len__(self):
        return 2

    def __bool__(self):
        return self.x != 0 or self.y != 0

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)
print(len(v1))
print(bool(Vector(0, 0)))
```

### 😱 Answer
```
Vector(4, 6)
2
False
```

### 🧠 Key Dunder Methods

| Dunder | Triggered by |
|---|---|
| `__init__` | `MyClass()` |
| `__repr__` | `repr(obj)`, default display |
| `__str__` | `str(obj)`, `print(obj)` |
| `__len__` | `len(obj)` |
| `__bool__` | `bool(obj)`, `if obj:` |
| `__add__` | `obj + other` |
| `__eq__` | `obj == other` |
| `__lt__` | `obj < other` |
| `__getitem__` | `obj[key]` |
| `__contains__` | `x in obj` |
| `__iter__` | `for x in obj` |
| `__enter__` / `__exit__` | `with obj:` |

> **If you define `__eq__`, you should also define `__hash__`. If `__eq__` is defined without `__hash__`, the class becomes unhashable (cannot be used as dict key or in sets).**

---

## 27. Context Managers — with Statement Internals

### ❓ Output?
```python
class ManagedResource:
    def __enter__(self):
        print("entering")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exiting")
        if exc_type is ValueError:
            print("handled ValueError")
            return True    # suppress the exception
        return False       # re-raise other exceptions

with ManagedResource() as r:
    print("inside")
    raise ValueError("oops")

print("after with block")
```

### 😱 Answer
```
entering
inside
exiting
handled ValueError
after with block   # ← code continues because exception was suppressed!
```

### 🧠 Concept
`with` calls `__enter__` at start and `__exit__` at end (even if an exception occurs).

`__exit__` receives the exception info. If it returns `True`, the exception is **suppressed** — execution continues after the `with` block. If it returns `False` or `None`, the exception propagates.

**`contextlib.contextmanager`** — easier way using a generator:
```python
from contextlib import contextmanager

@contextmanager
def managed():
    print("entering")
    yield "resource"
    print("exiting")   # runs after yield, acts as __exit__

with managed() as r:
    print(r)   # "resource"
```

---

## 28. *args and **kwargs — Every Combination

### ❓ Output?
```python
def func(a, b, *args, c, d=10, **kwargs):
    print(a, b, args, c, d, kwargs)

func(1, 2, 3, 4, c=5, e=6)
func(1, 2, c=3)
```

### 😱 Answer
```
1 2 (3, 4) 5 10 {'e': 6}
1 2 () 3 10 {}
```

### 🧠 Parameter Order
```python
def func(
    positional,         # regular positional
    *args,              # extra positional → tuple
    keyword_only,       # after * → MUST be passed as keyword
    keyword_default=10, # keyword with default
    **kwargs            # extra keyword → dict
):
```

**Important:** Parameters after `*args` are **keyword-only** — they cannot be passed positionally.

```python
func(1, 2, 3, c=5)   # c is keyword-only, must use c=5
func(1, 2, 3, 5)     # TypeError — 5 doesn't go to c
```

---

## 29. Lambda in a Loop — The Capture Trap

### ❓ Output?
```python
multipliers = [lambda x: x * i for i in range(1, 4)]

print(multipliers[0](10))
print(multipliers[1](10))
print(multipliers[2](10))
```

### 😱 Answer
```
30
30
30
```

### 🧠 Concept — Late Binding
Same as the closure loop trap in Level 2. By the time the lambdas are called, `i = 3` (loop finished). All three closures reference the same `i`.

**Fix — capture value with default argument:**
```python
multipliers = [lambda x, i=i: x * i for i in range(1, 4)]
print(multipliers[0](10))  # 10
print(multipliers[1](10))  # 20
print(multipliers[2](10))  # 30  ✅
```

Default arguments are evaluated at definition time — each lambda captures its own `i`.

---

## 30. Tuple is Immutable — Except When It's Not

### ❓ Output?
```python
t = (1, [2, 3], 4)
t[1].append(99)
print(t)
```

### 😱 Answer
```
(1, [2, 3, 99], 4)
```

### 🧠 Concept
A tuple is immutable — you cannot reassign its elements. But if an element is a mutable object (like a list), you can **mutate the object through the reference**.

The tuple still holds the same list reference — it just points to a list that now has different contents.

```python
t[1] = [2, 3]    # ❌ TypeError — can't reassign tuple element
t[1].append(99)  # ✅ mutating the list object the tuple holds a reference to
```

> **Tuples are immutable at the reference level, not at the object level.**

---

## 31. Exception Handling Traps

### ❓ Output?
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("caught")
    raise ValueError("new error")
finally:
    print("finally always runs")
```

### 😱 Answer
```
caught
finally always runs
ValueError: new error   (raised after finally)
```

### ❓ What does the else do?
```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("error")
else:
    print("no error:", result)   # runs only if NO exception
finally:
    print("always")
```

### 😱 Answer
```
no error: 5.0
always
```

### 🧠 Concept
- `except` — runs only if exception matches
- `else` — runs only if **no exception** occurred in `try`
- `finally` — **always runs** — even if there's a `return`, `break`, or unhandled exception

```python
def test():
    try:
        return 1
    finally:
        return 2   # overrides the return 1!

print(test())   # 2 — finally overrides everything
```

**Catch multiple exceptions:**
```python
except (TypeError, ValueError):    # tuple of exception types
except Exception as e:             # catch all (except SystemExit, KeyboardInterrupt)
except:                            # bare except — catches EVERYTHING including ctrl+C — avoid
```

---

## 32. GIL — Global Interpreter Lock

### 🧠 Concept (No output question — pure concept)

The **GIL** is a mutex that allows only **one thread** to execute Python bytecode at a time.

**What this means:**
- Multi-threaded CPU-bound code (number crunching) does NOT run in parallel — GIL blocks it
- Multi-threaded I/O-bound code (file reads, network calls) DOES benefit — thread releases GIL during I/O
- `multiprocessing` uses **separate processes** (each has its own GIL) — true parallelism for CPU tasks

**Interview answer:**
> "Python's GIL means threads can't run Python code in parallel. For CPU-bound tasks, I'd use `multiprocessing`. For I/O-bound tasks, `threading` or `asyncio` work fine because the GIL is released during I/O operations."

| Task type | Best tool |
|---|---|
| CPU-bound (heavy computation) | `multiprocessing` |
| I/O-bound (network, files) | `threading` or `asyncio` |
| Async/concurrent I/O | `asyncio` |

---

## 33. Memory and Reference Counting

### ❓ Output?
```python
import sys

a = [1, 2, 3]
b = a
c = a

print(sys.getrefcount(a))   # reference count includes the getrefcount call itself

del b
print(sys.getrefcount(a))

del c
print(sys.getrefcount(a))
```

### 😱 Answer
```
4    # a, b, c, + the getrefcount argument (temporary reference)
3    # after del b: a, c, + getrefcount
2    # after del c: a, + getrefcount
```

### 🧠 Concept
Python uses **reference counting** as its primary memory management strategy. Each object has a count of how many references point to it. When the count reaches zero, the object is immediately deallocated.

`del x` doesn't delete the object — it removes the reference. Object is deleted when **all** references are gone.

**Circular references** break reference counting:
```python
a = []
b = [a]
a.append(b)  # a references b, b references a
del a
del b        # reference count never reaches 0 — memory leak!
```
Python's **cyclic garbage collector** (`gc` module) handles these cases separately.

---

## 34. Walrus Operator — := Trap

### ❓ Output?
```python
data = [1, 2, 3, 4, 5]

# Without walrus
filtered = [y for x in data if (y := x * 2) > 4]
print(filtered)
print(y)    # y is accessible outside!

# Common use — avoid calling function twice
import re
text = "hello world 123"
if (match := re.search(r'\d+', text)):
    print(match.group())
```

### 😱 Answer
```
[6, 8, 10]
10           # y leaks out of comprehension scope!
123
```

### 🧠 Concept
The walrus operator `:=` assigns a value **and** returns it in the same expression.

Normal comprehension variables don't leak scope:
```python
[x for x in range(3)]
print(x)   # NameError in Python 3 — x is local to comprehension
```

But walrus operator variables **do** leak:
```python
[y := x for x in range(3)]
print(y)   # 2 — last value assigned
```

---

## 35. if __name__ == "__main__" — What and Why

### 🧠 Concept
When Python runs a file, it sets `__name__` to `"__main__"` if it's the script being run directly. If the file is imported as a module, `__name__` is set to the module's name instead.

```python
# mymodule.py
def useful_function():
    return 42

print("This always runs!")      # bad — runs on import too

if __name__ == "__main__":
    print("Only runs directly") # ✅ only runs when executed directly
    result = useful_function()
```

**Without the guard:** Every import of `mymodule` also runs the print statement and any other top-level code — tests, debug output, side effects.

**With the guard:** Imports are clean. Tests can import `useful_function` without side effects.

---

### 🔴 Level 3 Recap

```python
# 1. What happens here?
def f(lst=[]):
    lst.append(1)
    return lst

print(f())
print(f())

# 2. What is the output?
multipliers = [lambda x: x * i for i in range(1, 4)]
print(multipliers[0](5))

# 3. What does this print?
t = ([1, 2],)
t[0].append(3)
print(t)

# 4. finally override?
def g():
    try:
        return "try"
    finally:
        return "finally"
print(g())
```

**Answers:** `[1]` / `[1, 1]` / `15` / `([1, 2, 3],)` / `"finally"`

---

---

# 📋 MASTER SUMMARY
### Everything in one place. Use this the night before an interview.

---

## 36. Master Summary — Every Rule in One Place

---

### 🔑 Mutable vs Immutable
```
MUTABLE:   list, dict, set, bytearray, custom objects
IMMUTABLE: int, float, bool, str, tuple, frozenset, bytes

Only immutable (hashable) objects can be dict keys or set elements.
bool is a subclass of int: True=1, False=0 — can be used in arithmetic.
```

---

### 🔑 is vs == — Always Know Which to Use
```
==   → value equality (contents)
is   → identity (same object in memory)

Use is only for: None, True, False
Never use is for: strings, integers (above 256), lists, dicts
```

---

### 🔑 Truthy / Falsy
```
FALSY:  False, None, 0, 0.0, 0j, "", [], {}, (), set(), b""
TRUTHY: everything else — including [0], "0", " ", -1
```

---

### 🔑 Integer Cache
```
Python caches integers -5 to 256 as singletons.
Outside this range: new objects → is returns False.
NEVER use `is` for integer comparison — always ==.
```

---

### 🔑 Mutable Default Argument — THE Most Common Bug
```python
# ❌ WRONG
def f(lst=[]):
    lst.append(1)

# ✅ CORRECT
def f(lst=None):
    if lst is None:
        lst = []
```
Default args evaluated ONCE at definition time, not per call.

---

### 🔑 LEGB Scope Rule
```
L — Local       (current function)
E — Enclosing   (outer functions, for closures)
G — Global      (module level)
B — Built-in    (len, print, etc.)

Assignment inside a function = creates a LOCAL variable.
To modify outer: use `global` (for module-level) or `nonlocal` (for enclosing).
```

---

### 🔑 Closure Late Binding
```python
# ❌ All lambdas see final value of i
funcs = [lambda: i for i in range(3)]

# ✅ Default arg captures value immediately
funcs = [lambda i=i: i for i in range(3)]
```

---

### 🔑 Copy Rules
```
=                  → same reference (not a copy)
list.copy()        → shallow (inner objects shared)
list[:]            → shallow
copy.copy()        → shallow
copy.deepcopy()    → deep (completely independent)

[[0]*3]*3          → shallow! All rows are same list. Use [[0]*3 for _ in range(3)]
```

---

### 🔑 List Slicing
```
lst[start:stop:step]
stop is EXCLUSIVE
negative index → count from end
out of range → empty list (no error)
lst[:] → shallow copy
lst[::-1] → reverse
```

---

### 🔑 Class vs Instance Variables
```python
class A:
    shared = []           # class variable — shared by all instances

    def __init__(self):
        self.own = []     # instance variable — per instance

# Mutating class variable affects all instances
# Reassigning instance.classvar → creates new instance variable (shadows)
```

---

### 🔑 MRO
```
Python uses C3 linearization for multiple inheritance.
D(B, C) → D → B → C → A → object
super() follows MRO, not direct parent.
View with: ClassName.__mro__
```

---

### 🔑 Generators
```
Lazy — code doesn't run until next() is called
Exhaustible — once done, cannot be restarted
yield → pauses and sends value out
yield from → delegates to another iterable
Generator expression: (x for x in lst)  — vs list: [x for x in lst]
```

---

### 🔑 Decorators
```python
@decorator
def func():
    pass
# is exactly:
func = decorator(func)

Always use @functools.wraps(func) inside a decorator to preserve __name__, __doc__.
```

---

### 🔑 Dunder Methods
```
__init__     → constructor
__repr__     → repr(obj), default display in shell
__str__      → print(obj), str(obj)
__eq__       → ==  (defining this removes __hash__ — unhashable unless you define __hash__ too)
__hash__     → hash(obj), needed for dict keys and sets
__len__      → len(obj)
__bool__     → bool(obj), if obj
__add__      → obj + other
__getitem__  → obj[key]
__contains__ → x in obj
__iter__     → for x in obj
__enter__/__exit__ → with obj
```

---

### 🔑 Exception Handling
```
try/except/else/finally:
- else   → runs only if NO exception occurred
- finally → ALWAYS runs (even after return, break, raise)
- finally return overrides try return

Catch multiple: except (TypeError, ValueError)
Avoid bare except — catches SystemExit and KeyboardInterrupt
```

---

### 🔑 GIL
```
One thread executes Python bytecode at a time.
CPU-bound → use multiprocessing (separate processes, each with own GIL)
I/O-bound → threading or asyncio (GIL released during I/O)
```

---

### 🔑 Walrus Operator :=
```python
if (n := len(data)) > 10:   # assign and use in same expression
    print(n)

# Walrus variables LEAK out of comprehensions (unlike normal comp variables)
[y := x for x in range(3)]
print(y)   # 2 — accessible outside!
```

---

### 🔑 Tuple Immutability — The Nuance
```
Tuple cannot be reassigned: t[0] = x → TypeError
But mutable objects inside CAN be mutated: t[0].append(x) → ✅
Tuple with mutable elements is NOT hashable.
```

---

### 🔑 Division in Python 3
```python
7 / 2    # 3.5  — always float
7 // 2   # 3    — floor division (rounds toward -infinity)
-7 // 2  # -4   — NOT -3 (floor of -3.5 is -4)
7 % 2    # 1
-7 % 2   # 1    — sign follows divisor in Python
```

---

### 🔑 5 Sentences Every Python Interviewer Wants to Hear

1. **"Never use a mutable object as a default argument — always use `None` and create inside"**
2. **"Use `is` only for `None`, `True`, `False` — use `==` for everything else"**
3. **"Shallow copy shares nested references — use `copy.deepcopy()` for true independence"**
4. **"The GIL means threads don't give CPU parallelism — use `multiprocessing` for CPU-bound work"**
5. **"Generators are lazy and exhaustible — perfect for large data, but can only iterate once"**

---

*Python Interview Tricks — three levels, one guide, every gotcha covered.*