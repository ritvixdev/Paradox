# 🐍 Python Interview — Ultimate Guide

> **Who is this for?**
> Anyone preparing for a Python interview — from beginner to experienced developer.
> Every concept is explained simply, grouped logically, with code examples, ASCII diagrams and memory tricks.
> Read this once and walk into **any** Python interview with complete confidence.

---

## 📋 Table of Contents

| # | Section | Level |
|---|---------|-------|
| 1 | [Python Fundamentals](#1-python-fundamentals) | ⭐ Fresher |
| 2 | [Data Types & Variables](#2-data-types--variables) | ⭐ Fresher |
| 3 | [Strings & String Methods](#3-strings--string-methods) | ⭐ Fresher |
| 4 | [Lists, Tuples & Sets](#4-lists-tuples--sets) | ⭐ Fresher |
| 5 | [Dictionaries](#5-dictionaries) | ⭐ Fresher |
| 6 | [Control Flow](#6-control-flow) | ⭐ Fresher |
| 7 | [Functions](#7-functions) | ⭐⭐ Intermediate |
| 8 | [OOP — Classes, Inheritance, Abstraction](#8-oop) | ⭐⭐ Intermediate |
| 9 | [Memory Management, Copy & GIL](#9-memory-management-copy--gil) | ⭐⭐ Intermediate |
| 10 | [Error Handling & Exceptions](#10-error-handling--exceptions) | ⭐⭐ Intermediate |
| 11 | [Advanced Python — Generators, Decorators, Closures](#11-advanced-python) | ⭐⭐⭐ Advanced |
| 12 | [Collections Module](#12-collections-module) | ⭐⭐ Intermediate |
| 13 | [Data Structures — Queues, Heaps, Linked Lists](#13-data-structures) | ⭐⭐ Intermediate |
| 14 | [Modules, Packages & PIP](#14-modules-packages--pip) | ⭐ Fresher |
| 15 | [File Handling](#15-file-handling) | ⭐⭐ Intermediate |
| 16 | [Multithreading & Multiprocessing](#16-multithreading--multiprocessing) | ⭐⭐⭐ Advanced |
| 17 | [NumPy & Pandas](#17-numpy--pandas) | ⭐⭐ Intermediate |
| 18 | [Flask & Django](#18-flask--django) | ⭐⭐ Intermediate |
| 19 | [Python Internals — How Python Works Inside](#19-python-internals) | ⭐⭐⭐ Advanced |
| 20 | [Tricky Output Questions](#20-tricky-output-questions) | 🔥 Interview |
| 21 | [Coding Challenges](#21-coding-challenges) | 🔥 Interview |
| 22 | [Quick Cheatsheet & Memory Tips](#22-quick-cheatsheet--memory-tips) | 📌 Reference |

---
## 1. Python Fundamentals

### What is Python?

**Python** is a **high-level, interpreted, dynamically typed, general-purpose programming language**. It emphasises code readability and simplicity.

```
High-level     → closer to human language, away from machine code
Interpreted    → code runs line by line, no separate compile step
Dynamically typed → no need to declare variable types
General-purpose  → used for web, data science, automation, AI, scripting
```

### Is Python Compiled or Interpreted?

Python is **both** — partly compiled, partly interpreted.

```
Your .py file
     │
     ▼ (1) Compiler
  Bytecode (.pyc file)  ← stored in __pycache__
     │
     ▼ (2) Python Virtual Machine (PVM)
  Execution on your OS
```

> **One-line answer:** "Python compiles source code to bytecode, then the PVM interprets that bytecode."

### Key Features of Python

| Feature | What it means |
|---|---|
| **Free & Open-source** | Download and use for free |
| **Interpreted** | No manual compilation needed |
| **Dynamically typed** | `x = 5` then `x = "hello"` — no type declaration |
| **Object-Oriented** | Supports classes, objects, inheritance |
| **First-class functions** | Functions can be passed, returned, stored in variables |
| **Cross-platform** | Runs on Windows, Mac, Linux |
| **Extensive libraries** | `numpy`, `pandas`, `flask`, `django`, `requests`, etc. |
| **Readable syntax** | Code reads almost like English |

### What are Python Namespaces?

A **namespace** is a mapping from names to objects — like a labelled container that tracks all variable/function names.

```
Built-in namespace   → Python's default names (print, len, range...)
Global namespace     → names defined at the top level of your script
Enclosing namespace  → outer function's names (for nested functions)
Local namespace      → names defined inside a function

Lookup order: Local → Enclosing → Global → Built-in (LEGB Rule)
```

```python
x = "global"          # global namespace

def outer():
    x = "enclosing"   # enclosing namespace
    def inner():
        x = "local"   # local namespace
        print(x)      # prints "local" → LEGB: finds local first
    inner()

outer()
```

### Is Python Case Sensitive?

**Yes.** `name`, `Name`, and `NAME` are three different variables.

```python
name = "Alice"
Name = "Bob"
print(name)  # Alice
print(Name)  # Bob
```

### Is Indentation Required in Python?

**Yes — indentation is mandatory.** Python uses indentation (spaces/tabs) instead of `{}` to define code blocks.

```python
# CORRECT
if True:
    print("Hello")    # indented → inside the if block

# ERROR — missing indentation
if True:
print("Hello")        # IndentationError!
```

> **Standard:** Use **4 spaces** per level (PEP 8 recommendation).

### What is PEP 8?

**PEP 8** (Python Enhancement Proposal 8) is the **official style guide** for writing Python code — covering naming conventions, spacing, line length, comments, and more.

```python
# PEP 8 rules (key ones):
# Variable names: snake_case
my_variable = 10

# Constants: UPPER_CASE
MAX_SIZE = 100

# Class names: PascalCase
class MyClass:
    pass

# Max line length: 79 characters
# 2 blank lines between top-level functions/classes
# 1 blank line between methods inside a class
```

### What is Python Path?

**Python Path** is an environment variable that tells the Python interpreter **where to look for modules** when you use `import`. It's a list of directories searched in order.

---

## 2. Data Types & Variables

### Built-in Data Types

```
Python Data Types
│
├── Numeric
│   ├── int       →  x = 10
│   ├── float     →  x = 3.14
│   └── complex   →  x = 2 + 3j
│
├── Sequence
│   ├── str       →  x = "hello"
│   ├── list      →  x = [1, 2, 3]
│   └── tuple     →  x = (1, 2, 3)
│
├── Set
│   ├── set       →  x = {1, 2, 3}
│   └── frozenset →  x = frozenset({1, 2, 3})
│
├── Mapping
│   └── dict      →  x = {"key": "value"}
│
└── Boolean       →  x = True / False
```

### Mutable vs Immutable Types

```
MUTABLE (can be changed after creation)     IMMUTABLE (cannot be changed)
──────────────────────────────────────       ──────────────────────────────
list         [1, 2, 3]                       int          5
dict         {"a": 1}                        float        3.14
set          {1, 2, 3}                       str          "hello"
bytearray                                    tuple        (1, 2, 3)
                                             bool         True
                                             frozenset
```

```python
# Mutable example:
my_list = [1, 2, 3]
my_list[0] = 99        # works fine → [99, 2, 3]

# Immutable example:
my_str = "hello"
my_str[0] = "H"        # TypeError! strings are immutable

# Immutable creates NEW object:
x = "hello"
x = x + " world"       # x now points to a NEW string object
```

> **Memory trick:** "**Lists and Dicts are FLEXIBLE (mutable). Strings and Tuples are FROZEN (immutable).**"

### is vs ==

```
==   →  checks if VALUES are equal
is   →  checks if both point to the SAME object in memory
```

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True  → same values
print(a is b)   # False → different objects in memory

c = a           # c points to the SAME object as a
print(a is c)   # True  → same object!

# Small integer caching (Python caches -5 to 256):
x = 5
y = 5
print(x is y)   # True → Python reuses the same int object for small numbers
```

### Type Conversion (Type Casting)

Changing one data type into another.

```python
# Implicit conversion (Python does it automatically)
result = 5 + 2.0      # int + float → Python converts to float → 7.0

# Explicit conversion (you do it manually)
int("42")        # → 42
float("3.14")    # → 3.14
str(100)         # → "100"
list("hello")    # → ['h', 'e', 'l', 'l', 'o']
tuple([1,2,3])   # → (1, 2, 3)
set([1,1,2,3])   # → {1, 2, 3}   (removes duplicates)
bool(0)          # → False
bool("")         # → False
bool("hi")       # → True
bool([])         # → False
bool([1])        # → True
ord('A')         # → 65  (character to ASCII integer)
hex(255)         # → '0xff'
oct(8)           # → '0o10'
```

> **Falsy values in Python:** `0`, `0.0`, `""`, `[]`, `{}`, `()`, `None`, `False`

### What does `len()` do?

`len()` returns the **number of items** in a sequence or collection.

```python
len("hello")          # 5
len([1, 2, 3])        # 3
len((10, 20))         # 2
len({"a": 1, "b": 2}) # 2
len({1, 2, 3, 3})     # 3 (set removes duplicates)
```

---

## 3. Strings

### String Basics

```python
# Creating strings
s1 = 'single quotes'
s2 = "double quotes"
s3 = """triple quotes
        for multiline"""

# String is immutable — can't change individual characters
name = "hello"
# name[0] = "H"  ← TypeError!
name = "H" + name[1:]  # create a new string instead
```

### Slicing

**Slicing** accesses a part of a sequence using `[start : end : step]`.

```
string:   H  e  l  l  o     W  o  r  l  d
index:    0  1  2  3  4  5  6  7  8  9  10
neg idx: -11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
```

```python
s = "Hello World"

s[0]       # 'H'         → index 0
s[-1]      # 'd'         → last character
s[0:5]     # 'Hello'     → from 0 to 4 (end is exclusive)
s[6:]      # 'World'     → from index 6 to end
s[:5]      # 'Hello'     → from start to index 4
s[::2]     # 'HloWrd'    → every 2nd character
s[::-1]    # 'dlroW olleH' → reversed string!
```

> **Memory trick for `[::-1]`:** "Negative step = go backwards = reverse."

### Common String Methods

```python
s = "  Hello World  "

s.upper()           # "  HELLO WORLD  "
s.lower()           # "  hello world  "
s.strip()           # "Hello World"    (removes whitespace from both ends)
s.lstrip()          # "Hello World  "  (left strip only)
s.rstrip()          # "  Hello World"  (right strip only)
s.replace("World", "Python")  # "  Hello Python  "
s.split(" ")        # splits into list by space
s.capitalize()      # capitalises first letter only
s.title()           # Capitalises First Letter Of Each Word
s.startswith("He")  # True / False
s.endswith("ld")    # True / False
s.find("World")     # returns index, or -1 if not found
s.count("l")        # counts occurrences
s.isdigit()         # True if all chars are digits
s.isalpha()         # True if all chars are letters
" ".join(["Hello", "World"])  # "Hello World"

# f-string formatting (modern, recommended)
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
```

### Indexing vs Slicing

| | Indexing | Slicing |
|---|---|---|
| Syntax | `s[2]` | `s[1:4]` |
| Returns | Single item | Subsequence |
| Out of range | `IndexError` | Returns empty (no error) |

---

## 4. Lists, Tuples & Sets

### Lists

**List** = ordered, mutable, allows duplicates.

```python
# Creating
fruits = ["apple", "banana", "cherry"]

# Accessing
fruits[0]        # "apple"
fruits[-1]       # "cherry"

# Modifying
fruits[1] = "mango"           # replace
fruits.append("orange")       # add to end
fruits.insert(1, "grape")     # insert at index
fruits.extend(["kiwi","pear"])# add multiple items
fruits.remove("apple")        # remove by value
fruits.pop()                  # remove last item
fruits.pop(1)                 # remove by index
del fruits[0]                 # delete by index

# Other operations
fruits.sort()                 # sort in place
sorted(fruits)                # returns new sorted list
fruits.reverse()              # reverse in place
fruits.index("banana")        # find index of item
fruits.count("apple")         # count occurrences
fruits.copy()                 # shallow copy
fruits.clear()                # empty the list
len(fruits)                   # length

# List multiplication
[0] * 5          # [0, 0, 0, 0, 0]
[1, 2] * 3       # [1, 2, 1, 2, 1, 2]
```

### List Comprehension

A concise way to create lists.

```python
# Syntax: [expression for item in iterable if condition]

# Without comprehension:
squares = []
for x in range(5):
    squares.append(x ** 2)

# With comprehension (one line!):
squares = [x ** 2 for x in range(5)]
# → [0, 1, 4, 9, 16]

# With condition:
evens = [x for x in range(10) if x % 2 == 0]
# → [0, 2, 4, 6, 8]

# Nested:
matrix = [[i * j for j in range(3)] for i in range(3)]
# → [[0,0,0], [0,1,2], [0,2,4]]
```

### 2D Arrays (Lists of Lists)

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

grid[0]       # [1, 2, 3]     → first row
grid[1][2]    # 6             → row 1, column 2
grid[2][-1]   # 9             → last element of last row

# Iterating:
for row in grid:
    for item in row:
        print(item, end=" ")
```

### Tuples

**Tuple** = ordered, **immutable**, allows duplicates.

```python
# Creating
coords = (10, 20)
single = (42,)       # single element tuple NEEDS trailing comma
empty  = ()

# Accessing (same as list)
coords[0]     # 10
coords[-1]    # 20

# Tuple unpacking
x, y = coords
print(x, y)   # 10 20

# Extended unpacking
a, *b, c = (1, 2, 3, 4, 5)
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

# Tuples can be used as dictionary keys (lists cannot!)
d = {(0, 0): "origin", (1, 0): "right"}
```

### List vs Tuple — Interview Favourite

```
+------------------+--------------------------+---------------------------+
|                  | List                     | Tuple                     |
+------------------+--------------------------+---------------------------+
| Syntax           | [1, 2, 3]               | (1, 2, 3)                |
| Mutable?         | YES — can change         | NO — cannot change        |
| Speed            | Slower                   | Faster (fixed size)       |
| Memory           | More                     | Less                      |
| Use as dict key? | NO (mutable)             | YES (immutable, hashable) |
| Use for          | Collection of items      | Fixed records, coordinates|
|                  | that may change          | function return values    |
+------------------+--------------------------+---------------------------+
```

### Sets

**Set** = **unordered**, mutable, **no duplicates**.

```python
# Creating
s = {1, 2, 3, 3, 2}    # → {1, 2, 3}  (duplicates removed)
s = set([1, 2, 2, 3])  # from list → {1, 2, 3}
s = set()              # EMPTY set (not {} — that creates a dict!)

# Operations
s.add(4)               # add one element
s.update([5, 6])       # add multiple
s.remove(3)            # remove (raises KeyError if not found)
s.discard(3)           # remove (no error if not found)
s.pop()                # remove random element

# Set math — very useful!
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b    # union       → {1,2,3,4,5,6}   (all elements)
a & b    # intersection → {3,4}          (common elements)
a - b    # difference  → {1,2}           (in a, not in b)
a ^ b    # symmetric diff → {1,2,5,6}   (in either but not both)

3 in a   # True  → O(1) lookup! Much faster than list
```

> **Why is a set unordered?** Sets use a **hash table** internally. Items are stored based on their hash value, not insertion order. You can't index a set (`s[0]` → TypeError).

> **Is a set mutable?** The **set itself** is mutable (you can add/remove elements). But items **inside** a set must be **immutable/hashable** (no lists inside sets!). Use `frozenset` for an immutable set.

### sort() vs sorted()

```python
# list.sort() — sorts IN PLACE, returns None
nums = [3, 1, 4, 1, 5]
nums.sort()                   # nums is now [1, 1, 3, 4, 5]
result = nums.sort()          # result is None!

# sorted() — returns NEW sorted list, original unchanged
nums = [3, 1, 4, 1, 5]
new = sorted(nums)            # new = [1, 1, 3, 4, 5], nums unchanged

# Both support reverse and key:
sorted(nums, reverse=True)             # [5, 4, 3, 1, 1]
sorted(words, key=str.lower)           # case-insensitive sort
sorted(data, key=lambda x: x['age'])  # sort by dict value

# Which sorting algorithm? TIMSORT (hybrid merge sort + insertion sort)
# Time: O(n log n) average and worst case
```

---

## 5. Dictionaries

### Dictionary Basics

**Dictionary** = unordered (insertion-ordered since Python 3.7), mutable, key-value pairs. Keys must be **unique and immutable** (hashable).

```python
# Creating
person = {"name": "Alice", "age": 25, "city": "New York"}
person = dict(name="Alice", age=25)

# Accessing
person["name"]          # "Alice"
person.get("age")       # 25
person.get("salary", 0) # 0 (default if key missing — no KeyError!)

# Modifying
person["age"] = 26                  # update existing
person["email"] = "a@b.com"         # add new key
del person["city"]                  # delete key
person.pop("email")                 # delete + return value
person.update({"age": 27, "job": "Dev"})  # update multiple

# Iterating
for key in person:            # iterate keys
for val in person.values():   # iterate values
for k, v in person.items():   # iterate key-value pairs

# Useful methods
person.keys()         # dict_keys(['name', 'age'])
person.values()       # dict_values(['Alice', 25])
person.items()        # dict_items([('name','Alice'), ('age',25)])
person.clear()        # empty the dict
"name" in person      # True — O(1) key lookup!

# Dict comprehension
squares = {x: x**2 for x in range(5)}
# → {0:0, 1:1, 2:4, 3:9, 4:16}
```

### Why is Dictionary Lookup Faster than List?

```
List lookup:   O(N) — checks each item one by one
Dict lookup:   O(1) average — uses a hash table

How hash table works:
  key = "name"
  hash("name") → 1234567  (some integer)
  1234567 % table_size → slot number
  Jump directly to that memory slot!

This is why keys must be hashable (immutable).
A mutable key could change its hash → can't find it anymore.
```

### Merging Dictionaries

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

# Python 3.9+ (best)
merged = d1 | d2        # → {"a":1, "b":3, "c":4}  (d2 overrides d1)

# Python 3.5+ (older)
merged = {**d1, **d2}   # same result

# update() — modifies in place
d1.update(d2)
```

---

## 6. Control Flow

### if / elif / else

```python
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# One-liner (ternary):
status = "pass" if score >= 50 else "fail"
```

### for Loop

```python
# Basic loop
for i in range(5):         # 0, 1, 2, 3, 4
    print(i)

# Loop with index
for i, val in enumerate(["a", "b", "c"]):
    print(i, val)          # 0 a, 1 b, 2 c

# Loop over dict
for key, value in my_dict.items():
    print(key, value)

# range(start, stop, step)
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# Reversed
for i in range(10, 0, -1): # 10, 9, 8 ... 1
    print(i)
```

### while Loop

```python
count = 0
while count < 5:
    print(count)
    count += 1

# for vs while:
# for   → when you KNOW the number of iterations (iterate over sequence)
# while → when you DON'T know, loop until a condition becomes false
```

### break, continue, pass

```
break    → EXIT the loop immediately
continue → SKIP current iteration, go to next
pass     → DO NOTHING (placeholder — code is syntactically required but empty)
```

```python
# break — stop when you find what you need
for i in range(10):
    if i == 5:
        break             # exits loop, i never reaches 6,7,8,9
    print(i)              # prints 0,1,2,3,4

# continue — skip even numbers
for i in range(10):
    if i % 2 == 0:
        continue          # skip even, don't print
    print(i)              # prints 1,3,5,7,9

# pass — empty function/class as placeholder
def my_function():
    pass                  # TODO: implement later
    # without pass → IndentationError (can't have empty body)

class MyClass:
    pass                  # empty class for now
```

### Negative Indexing

```python
lst = [10, 20, 30, 40, 50]
#      0    1   2   3   4   (positive)
#     -5   -4  -3  -2  -1  (negative)

lst[-1]     # 50  → last element
lst[-2]     # 40  → second to last
lst[-1::-1] # [50, 40, 30, 20, 10] → reversed
```

---

## 7. Functions

### Function Basics

```python
# Define
def greet(name, greeting="Hello"):   # "Hello" is a default argument
    """This is a docstring — explains what the function does."""
    return f"{greeting}, {name}!"

# Call
greet("Alice")               # "Hello, Alice!"
greet("Bob", "Hi")            # "Hi, Bob!"
greet(greeting="Hey", name="Carol")  # keyword arguments (order doesn't matter)
```

### *args and **kwargs

```
*args   → collects extra POSITIONAL arguments into a TUPLE
**kwargs → collects extra KEYWORD arguments into a DICT
```

```python
def show_args(*args):
    print(args)               # tuple

def show_kwargs(**kwargs):
    print(kwargs)             # dict

def combined(name, *args, **kwargs):
    print(name)               # positional
    print(args)               # extra positionals → tuple
    print(kwargs)             # keyword args → dict

combined("Alice", 1, 2, 3, city="NY", age=25)
# Alice
# (1, 2, 3)
# {'city': 'NY', 'age': 25}
```

### Lambda Functions

**Lambda** = small, anonymous, one-line function.

```python
# Regular function:
def add(x, y):
    return x + y

# Lambda equivalent:
add = lambda x, y: x + y
add(3, 4)   # 7

# Common uses:
nums = [3, 1, 4, 1, 5]
nums.sort(key=lambda x: -x)           # sort descending
sorted_data = sorted(data, key=lambda d: d["age"])  # sort dicts by key

# map, filter, reduce with lambda:
squares = list(map(lambda x: x**2, [1, 2, 3]))   # [1, 4, 9]
evens   = list(filter(lambda x: x%2==0, range(10)))  # [0,2,4,6,8]
```

### How Arguments Are Passed in Python

Python uses **pass by object reference** (also called "pass by assignment").

```
If the object is MUTABLE   → changes inside function affect the original
If the object is IMMUTABLE → original is unchanged (new object is created)
```

```python
# Mutable — list is modified:
def add_item(lst):
    lst.append(99)

my_list = [1, 2, 3]
add_item(my_list)
print(my_list)    # [1, 2, 3, 99] ← CHANGED!

# Immutable — integer is NOT modified:
def add_ten(n):
    n = n + 10    # creates a NEW int object locally

x = 5
add_ten(x)
print(x)          # 5 ← UNCHANGED!
```

### Nested Functions & Closures

```python
def outer(message):
    def inner():
        print(message)    # inner can access outer's variables → CLOSURE
    return inner          # return the function itself!

say_hello = outer("Hello!")
say_hello()               # "Hello!"

# The inner function "closes over" the outer variable — that's a closure.
```

### Can We Pass Functions as Arguments?

**Yes** — functions are **first-class objects** in Python.

```python
def apply(func, value):
    return func(value)

apply(str.upper, "hello")   # "HELLO"
apply(len, [1, 2, 3])       # 3
apply(lambda x: x*2, 5)     # 10
```

### Docstrings

A **docstring** is a string literal that documents what a function/class/module does.

```python
def calculate_area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    import math
    return math.pi * radius ** 2

# Access it:
print(calculate_area.__doc__)
help(calculate_area)
```

---

## 8. OOP

### Classes and Objects

```
Class  → blueprint / template
Object → an instance of a class (the actual thing)

Class  : Car (has colour, speed, model)
Objects: my_car = Car("red", 120, "Tesla")
```

```python
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis lupus familiaris"

    # Constructor — called when creating an object
    def __init__(self, name, age):
        # Instance attributes (unique per object)
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

    # String representation
    def __str__(self):
        return f"Dog({self.name}, {self.age})"

# Create objects
dog1 = Dog("Rex", 3)
dog2 = Dog("Bella", 5)

dog1.bark()       # "Rex says Woof!"
print(dog1)       # "Dog(Rex, 3)"
dog1.name         # "Rex"
Dog.species       # "Canis lupus familiaris"
```

### What is `self`?

`self` represents the **current instance** of the class. It's the first parameter of every instance method and is how the method knows which object to work with.

```python
class Counter:
    def __init__(self):
        self.count = 0      # self.count belongs to THIS object

    def increment(self):
        self.count += 1     # self refers to the specific Counter object

c1 = Counter()
c2 = Counter()
c1.increment()
print(c1.count)  # 1
print(c2.count)  # 0  ← separate object, separate state
```

### Instance, Class & Static Methods

```python
class MyClass:
    class_var = "I am shared"

    def __init__(self, x):
        self.x = x

    # INSTANCE METHOD: belongs to an object, accesses instance data
    def instance_method(self):
        return self.x

    # CLASS METHOD: belongs to the class, accesses class-level data
    @classmethod
    def class_method(cls):
        return cls.class_var

    # STATIC METHOD: no access to self or cls — just a utility function
    @staticmethod
    def static_method(a, b):
        return a + b

obj = MyClass(10)
obj.instance_method()     # 10
MyClass.class_method()    # "I am shared"
MyClass.static_method(3, 4)  # 7
```

### Inheritance

**Inheritance** allows a child class to **reuse code** from a parent class.

```python
# Parent class (Base class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

    def eat(self):
        return f"{self.name} is eating"

# Child class (Derived class)
class Dog(Animal):
    def speak(self):          # Method overriding
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Rex")
dog.speak()     # "Rex says Woof!"   ← overridden
dog.eat()       # "Rex is eating"    ← inherited from Animal
```

### Types of Inheritance

```
SINGLE:        Dog inherits from Animal
               Animal → Dog

MULTI-LEVEL:   Puppy inherits from Dog which inherits from Animal
               Animal → Dog → Puppy

HIERARCHICAL:  Dog and Cat both inherit from Animal
               Animal → Dog
               Animal → Cat

MULTIPLE:      FlyingCar inherits from BOTH Car and Airplane
               Car  ─┐
                      ├→ FlyingCar
               Plane ─┘
```

```python
# Multiple inheritance
class Car:
    def drive(self): return "driving"

class Airplane:
    def fly(self): return "flying"

class FlyingCar(Car, Airplane):
    pass

fc = FlyingCar()
fc.drive()   # "driving"
fc.fly()     # "flying"
```

### MRO — Method Resolution Order

When multiple inheritance is involved, Python uses the **C3 linearisation algorithm** to determine which method to call.

```python
class A:
    def method(self): return "A"

class B(A):
    def method(self): return "B"

class C(A):
    def method(self): return "C"

class D(B, C):
    pass

print(D().method())  # "B"  → follows MRO

# Check MRO:
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

> **MRO rule:** Left to right, depth first, respecting the order.

### Access Modifiers (Global, Protected, Private)

Python doesn't have true access modifiers like Java, but uses **naming conventions**:

```python
class BankAccount:
    def __init__(self):
        self.name = "Alice"      # PUBLIC — accessible anywhere
        self._balance = 1000     # PROTECTED — convention: don't use outside class
        self.__pin = 1234        # PRIVATE — name-mangled, harder to access

acc = BankAccount()
acc.name                         # "Alice"      ✓ works
acc._balance                     # 1000         ✓ works (but shouldn't!)
acc.__pin                        # AttributeError!
acc._BankAccount__pin            # 1234 — name mangling reveals it, but don't do this
```

```
PUBLIC    → name          → accessible everywhere
PROTECTED → _name         → accessible in class + subclasses (by convention)
PRIVATE   → __name        → accessible only inside the class (name-mangled)
```

### Method Overriding vs Overloading

```
OVERRIDING: child class redefines a method from the parent class
OVERLOADING: same function name, different parameters — Python doesn't support natively
```

```python
# Overriding — Python fully supports
class Animal:
    def sound(self): return "generic sound"

class Dog(Animal):
    def sound(self): return "Woof"    # overrides parent

# Overloading simulation using *args or default params:
def add(a, b=0, c=0):
    return a + b + c

add(1)       # 1
add(1, 2)    # 3
add(1, 2, 3) # 6
```

### __new__ vs __init__

```
__new__   → CREATES the object (allocates memory), runs first
__init__  → INITIALISES the object (sets attributes), runs after __new__
```

```python
class MyClass:
    def __new__(cls):
        print("__new__ called — creating object")
        return super().__new__(cls)

    def __init__(self):
        print("__init__ called — initialising object")

obj = MyClass()
# __new__ called — creating object
# __init__ called — initialising object
```

### Abstraction & Encapsulation

```
ABSTRACTION:   Hiding complexity — showing only what's necessary
               "I use drive(), I don't need to know the engine internals"

ENCAPSULATION: Wrapping data + methods together in one unit (class)
               + restricting direct access using private/protected attributes
               "Data and methods live together, data is protected"
```

```python
from abc import ABC, abstractmethod

class Shape(ABC):               # Abstract class — can't be instantiated
    @abstractmethod
    def area(self):             # Abstract method — MUST be implemented by subclass
        pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r ** 2

c = Circle(5)
c.area()    # 78.5
# Shape()  → TypeError! Can't instantiate abstract class
```

---

## 9. Memory Management & GIL

### How Python Manages Memory

```
1. PRIVATE HEAP SPACE
   All Python objects live in a private heap.
   The programmer cannot access this heap directly.
   The Python Memory Manager controls it.

2. REFERENCE COUNTING
   Every object has a count of how many variables point to it.
   When count drops to 0 → object is immediately deallocated.

3. GARBAGE COLLECTOR
   Handles REFERENCE CYCLES (objects pointing to each other).
   Reference counting alone can't handle: A → B → A
   gc module periodically cleans these up.

4. MEMORY POOLS (pymalloc)
   Python uses pools of pre-allocated memory for small objects
   to avoid constant malloc/free system calls → faster!
```

```python
import sys

x = [1, 2, 3]
print(sys.getrefcount(x))  # shows reference count (usually 2: x + the call itself)

import gc
gc.collect()               # manually trigger garbage collection
```

### Shallow Copy vs Deep Copy

```
SHALLOW COPY: new object, but NESTED objects are still SHARED (referenced)
DEEP COPY:    new object AND all nested objects are FULLY COPIED (independent)
```

```python
import copy

original = [[1, 2], [3, 4]]

# Shallow copy:
shallow = copy.copy(original)
shallow[0][0] = 99          # CHANGES original[0][0] too!
print(original)             # [[99, 2], [3, 4]] ← affected!

original = [[1, 2], [3, 4]] # reset

# Deep copy:
deep = copy.deepcopy(original)
deep[0][0] = 99             # does NOT affect original
print(original)             # [[1, 2], [3, 4]] ← unchanged!
```

```
Visualised:
original  →  [ ref→[1,2], ref→[3,4] ]
                     ↑          ↑
shallow   →  [ ref→[1,2], ref→[3,4] ]   ← same nested lists!

original  →  [ ref→[1,2], ref→[3,4] ]
deep      →  [ ref→[1,2], ref→[3,4] ]   ← brand new copies of nested lists
```

### What is the GIL?

**GIL (Global Interpreter Lock)** is a mutex in CPython that allows **only one thread to execute Python bytecode at a time**.

```
Why does GIL exist?
  Python's memory management (reference counting) is NOT thread-safe.
  Without GIL → two threads could simultaneously change the same object's
  reference count → memory corruption!
  GIL prevents this by letting only one thread run at a time.

What does GIL mean for you?
  CPU-bound tasks (number crunching):
    Threading doesn't help — GIL prevents true parallelism.
    Use multiprocessing instead (each process has its own GIL).

  I/O-bound tasks (reading files, network requests):
    GIL is released during I/O waiting.
    Threading DOES help here!
```

### Why Doesn't Python Deallocate All Memory on Exit?

- Garbage collection has **overhead** — not everything is cleaned up immediately
- **Circular references** may not be resolved instantly
- **External resources** (OS handles, C extensions) may hold memory
- From the OS perspective, all memory **is** reclaimed when the process exits

---

## 10. Error Handling & Exceptions

### try / except / else / finally

```python
try:
    result = 10 / 0         # code that might fail
except ZeroDivisionError:
    print("Can't divide by zero!")
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
else:
    print("No error! Result:", result)   # runs ONLY if no exception
finally:
    print("Always runs — cleanup here")  # runs no matter what

# try → attempt
# except → handle the error
# else → success path (no exception)
# finally → ALWAYS runs (close files, release connections)
```

### Common Built-in Exceptions

```python
ZeroDivisionError    # 5 / 0
TypeError            # "hello" + 5
ValueError           # int("abc")
IndexError           # [1,2,3][10]
KeyError             # {"a":1}["b"]
AttributeError       # None.upper()
FileNotFoundError    # open("ghost.txt")
ImportError          # import non_existent_module
NameError            # print(undefined_var)
RecursionError       # infinite recursion
StopIteration        # next() on exhausted iterator
OverflowError        # value too large for float
```

### Raising Custom Exceptions

```python
class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"Tried to withdraw {amount}, but balance is only {balance}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    return balance - amount

try:
    withdraw(100, 200)
except InsufficientFundsError as e:
    print(e)   # "Tried to withdraw 200, but balance is only 100"
```

### Compile-time vs Runtime Errors in Python

```
COMPILE-TIME ERRORS (SyntaxError, IndentationError):
  Caught when Python parses the file before execution.
  Example: print("hello"   ← missing closing paren

RUNTIME ERRORS (Exceptions):
  Occur during execution — code was syntactically valid but failed.
  Example: 1/0, accessing undefined variable, index out of range

Python has NO traditional compile-time type errors (unlike Java/C++)
because it's dynamically typed — types are checked at runtime.
```

---

## 11. Advanced Python

### Decorators

A **decorator** is a function that **wraps another function** to add behaviour without modifying the original code.

```python
# A decorator is just a function that takes a function and returns a new function
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function")
        result = func(*args, **kwargs)
        print("After the function")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
# Before the function
# Hello, Alice!
# After the function

# @my_decorator is just syntactic sugar for:
# say_hello = my_decorator(say_hello)
```

**Real-world decorator examples:**

```python
import time
import functools

# Timer decorator
def timer(func):
    @functools.wraps(func)        # preserves func's metadata
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

slow_function()   # "slow_function took 1.0012s"
```

### Generators

A **generator** is a function that **yields values one at a time** instead of returning all at once. It's **memory efficient** for large datasets.

```python
# Regular function (loads everything into memory):
def get_squares(n):
    return [x**2 for x in range(n)]     # list of n items in memory at once

# Generator (produces one item at a time):
def gen_squares(n):
    for x in range(n):
        yield x**2                      # yields one value, pauses, resumes later

# Usage:
for val in gen_squares(1000000):       # only ONE value in memory at a time!
    print(val)

# Generator expression (like list comprehension but with ()):
gen = (x**2 for x in range(10))       # creates a generator
next(gen)   # 0
next(gen)   # 1
list(gen)   # consumes remaining: [4, 9, 16, ...81]
# Generator is exhausted after one use!
```

### zip() Function

`zip()` combines multiple iterables element by element into tuples.

```python
names  = ["Alice", "Bob", "Carol"]
ages   = [25, 30, 22]
cities = ["NY", "LA", "Chicago"]

zipped = list(zip(names, ages))
# [("Alice", 25), ("Bob", 30), ("Carol", 22)]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} from {city}")

# Unzip:
names_back, ages_back = zip(*zipped)
```

### xrange vs range (Python 2 vs 3)

```
Python 2:
  range(n)  → returns a full list in memory (memory-hungry for large n)
  xrange(n) → returns a lazy iterator (memory efficient)

Python 3:
  range(n)  → is already lazy like Python 2's xrange!
  xrange    → doesn't exist in Python 3

Rule: In Python 3, just use range() — it's already efficient.
```

### range() and common patterns

```python
range(5)          # 0, 1, 2, 3, 4
range(2, 8)       # 2, 3, 4, 5, 6, 7
range(0, 10, 2)   # 0, 2, 4, 6, 8
range(10, 0, -1)  # 10, 9, 8 ... 1

# Convert to list:
list(range(5))    # [0, 1, 2, 3, 4]
```

### Monkey Patching

**Monkey patching** = replacing/modifying a class or function at **runtime**.

```python
class Dog:
    def bark(self):
        return "Woof"

def new_bark(self):
    return "WOOF WOOF WOOF"

Dog.bark = new_bark         # replace the method at runtime
d = Dog()
d.bark()                    # "WOOF WOOF WOOF"
```

### Pickling & Unpickling

```python
import pickle

data = {"name": "Alice", "scores": [95, 87, 92]}

# Pickling (serialise to bytes → save to file):
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# Unpickling (deserialise → restore Python object):
with open("data.pkl", "rb") as f:
    loaded = pickle.load(f)

print(loaded)  # {'name': 'Alice', 'scores': [95, 87, 92]}
```

### Operators

```
Arithmetic:   +  -  *  /  //  %  **
  /   → true division   (7/2 = 3.5)
  //  → floor division  (7//2 = 3, -7//2 = -4)
  %   → modulus/remainder (7%3 = 1)
  **  → power            (2**8 = 256)

Comparison:   ==  !=  >  <  >=  <=
Logical:      and  or  not
Identity:     is  is not
Membership:   in  not in
Bitwise:      &  |  ^  ~  <<  >>
```

```python
# Floor division:
7 // 2     # 3
-7 // 2    # -4   (floors toward negative infinity!)

# Modulus:
7 % 3      # 1
-7 % 3     # 2    (in Python, result has same sign as divisor)

# Add without + (using bitwise XOR + carry):
def add(a, b):
    while b:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a
```

---

## 12. Collections Module

> The `collections` module has **specialised container datatypes** that are faster and cleaner than using regular dicts/lists. A must-know for interviews.

### Counter — Count Frequencies in One Line

```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
c = Counter(words)
print(c)                      # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
c.most_common(2)              # [('apple', 3), ('banana', 2)]

# One-liner word frequency:
Counter("hello world".split())  # Counter({'hello': 1, 'world': 1})

# Works on strings too:
Counter("abracadabra")  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
```

### defaultdict — No KeyError for Missing Keys

```python
from collections import defaultdict

d = defaultdict(list)          # default = empty list
d["fruits"].append("apple")    # no KeyError even though key didn't exist!
d["fruits"].append("banana")
print(d)  # defaultdict(<class 'list'>, {'fruits': ['apple', 'banana']})

d2 = defaultdict(int)          # default = 0
d2["count"] += 1               # works without initialising first
```

### deque — Fast Double-Ended Queue

```python
from collections import deque

q = deque([1, 2, 3])
q.append(4)           # add to RIGHT  → O(1)
q.appendleft(0)       # add to LEFT   → O(1)
q.pop()               # remove RIGHT  → O(1)
q.popleft()           # remove LEFT   → O(1)
```

```
LIST vs DEQUE — Performance comparison:
+---------------------------+--------+--------+
| Operation                 | List   | deque  |
+---------------------------+--------+--------+
| append to end             | O(1)   | O(1)   |
| append to front           | O(N)   | O(1) ← |
| pop from end              | O(1)   | O(1)   |
| pop from front            | O(N)   | O(1) ← |
| random access by index    | O(1) ← | O(N)   |
+---------------------------+--------+--------+

Use LIST when you need random access by index.
Use DEQUE when you need fast inserts/pops at both ends.
```

### Why Can't Sets Contain Other Sets But CAN Contain frozensets?

```python
# Sets are MUTABLE → UNHASHABLE → cannot be put inside another set
s = {[1, 2], 3}         # TypeError! list is unhashable
s = {{1, 2}, 3}         # TypeError! set is unhashable

# frozenset is IMMUTABLE → HASHABLE → CAN go inside a set
s = {frozenset([1, 2]), frozenset([3, 4])}   # works!
d = {frozenset([1, 2]): "value"}             # can also be a dict key!
```

---

## 13. Data Structures

> Python doesn't have built-in linked list or heap types like Java/C++, but you implement them using lists and the `heapq` module. These come up in coding interviews.

### Queues

A **queue** is FIFO (First In, First Out) — like a line at a shop. First person in, first person out.

```python
# Method 1: collections.deque (recommended — O(1) both ends)
from collections import deque

queue = deque()
queue.append("Alice")   # enqueue (add to back)
queue.append("Bob")
queue.append("Carol")
queue.popleft()         # dequeue (remove from front) → "Alice"
print(queue)            # deque(['Bob', 'Carol'])

# Method 2: queue.Queue (thread-safe)
from queue import Queue

q = Queue()
q.put("item1")    # enqueue
q.get()           # dequeue

# Check:
q.empty()         # True/False
q.qsize()         # number of items
```

```
QUEUE (FIFO):
  Front [Alice, Bob, Carol] Back
  Dequeue ←                 ← Enqueue
  (remove from front)        (add to back)
```

### Hash Sets

A **hash set** in Python = `set`. O(1) average lookup, insertion, deletion.

```python
seen = set()

# Add
seen.add(1)
seen.add(2)
seen.add(2)       # duplicate — ignored!
print(seen)       # {1, 2}

# Check membership — O(1)!
1 in seen         # True
5 in seen         # False

# Remove
seen.discard(1)   # safe — no error if missing
seen.remove(2)    # raises KeyError if missing

# Common interview use: detect duplicates
def has_duplicates(lst):
    return len(lst) != len(set(lst))
```

### Hash Maps (Dictionaries)

In Python, a **hash map** = `dict`. Key-value store with O(1) average lookup.

```python
freq = {}

# Count character frequency (classic hash map problem):
for char in "hello":
    freq[char] = freq.get(char, 0) + 1
print(freq)   # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Or use Counter (cleaner):
from collections import Counter
Counter("hello")   # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

# Two Sum problem (classic):
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i
    return []

two_sum([2, 7, 11, 15], 9)   # [0, 1]
```

### Heaps (Priority Queue)

A **heap** gives you the smallest (min-heap) or largest (max-heap) element in O(1), and insert/remove in O(log n).

```python
import heapq

# MIN-HEAP (default in Python):
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)

heapq.heappop(heap)    # 1 → always removes the SMALLEST
print(heap)            # [3, 5]

heap[0]                # peek at minimum without removing

# Build heap from a list:
nums = [5, 3, 1, 4, 2]
heapq.heapify(nums)    # converts list to valid heap IN PLACE
heapq.heappop(nums)    # 1

# MAX-HEAP (negate values):
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -3)
-heapq.heappop(max_heap)   # 5 → largest value (negate back)

# N largest / N smallest:
heapq.nlargest(3, [1,5,2,8,3])    # [8, 5, 3]
heapq.nsmallest(3, [1,5,2,8,3])   # [1, 2, 3]
```

```
HEAP (min-heap tree view):
       1
      / \
     3   5
    / \
   4   2

Always: parent ≤ children
heappop always removes root (smallest)
```

### Linked List

Python has no built-in linked list. You implement it with a Node class.

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None   # pointer to next node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" → ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(1); ll.append(2); ll.append(3)
ll.print_list()   # 1 → 2 → 3 → None
```

```
Linked List:
[1] → [2] → [3] → None
head

Access by index: O(N)   ← must traverse from head
Insert at head:  O(1)   ← just update pointer
Insert at tail:  O(N)   ← traverse to end first
```

### Time Complexity of Inserting into a Linked List

```
Insert at HEAD (beginning):   O(1)  → update head pointer
Insert at TAIL (end):         O(N)  → must traverse to end
Insert at MIDDLE (by index):  O(N)  → traverse to position, then O(1) link
```

### How to Find the Middle Element of a Linked List in ONE Pass

```python
def find_middle(head):
    """
    Two-pointer (slow/fast) technique:
    slow moves 1 step, fast moves 2 steps.
    When fast reaches end, slow is at middle.
    """
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next        # 1 step
        fast = fast.next.next   # 2 steps
    return slow                 # slow is at middle!

# Visual for [1,2,3,4,5]:
# Step 1: slow=1, fast=1
# Step 2: slow=2, fast=3
# Step 3: slow=3, fast=5  ← fast.next is None → stop
# Middle = 3 ✓
```

---

## 14. Modules, Packages & PIP

### Module vs Package

```
MODULE:  A single .py file containing functions, classes, variables.
         Example: math.py, random.py, os.py

PACKAGE: A DIRECTORY containing multiple modules + an __init__.py file.
         __init__.py marks the directory as a package.

         mypackage/
         ├── __init__.py    ← makes it a package
         ├── utils.py       ← a module
         └── models.py      ← another module
```

```python
import math                         # entire module
from math import pi, sqrt           # specific items
from math import *                  # everything (NOT recommended!)
import numpy as np                  # alias

math.sqrt(16)     # 4.0
sqrt(16)          # 4.0 (direct import)
np.array([1,2,3]) # using alias
```

### Commonly Used Built-in Modules

| Module | What it does |
|---|---|
| `os` | File paths, environment variables, directories |
| `sys` | System info, command-line args, Python path |
| `math` | Math: `sqrt`, `floor`, `ceil`, `pi`, `log` |
| `random` | Random numbers, shuffle, sample |
| `datetime` | Date and time operations |
| `json` | JSON encode/decode |
| `re` | Regular expressions (pattern matching) |
| `collections` | Counter, defaultdict, deque, OrderedDict |
| `itertools` | chain, product, combinations, permutations |
| `functools` | reduce, wraps, lru_cache |
| `copy` | Shallow and deep copy |
| `time` | Time measurement, sleep |
| `threading` | Thread-based parallelism |
| `subprocess` | Run shell commands from Python |
| `pickle` | Serialise/deserialise Python objects |
| `csv` | Read/write CSV files |

### What is PIP?

**PIP** = Python's **package manager** — installs libraries from PyPI (Python Package Index).

```bash
pip install numpy                  # install latest version
pip install numpy==1.24.0         # install specific version
pip uninstall numpy                # uninstall
pip list                           # show all installed packages
pip show numpy                     # details about a package
pip freeze > requirements.txt      # save all packages + versions to file
pip install -r requirements.txt    # install from requirements file
pip install --upgrade numpy        # upgrade to latest
```

---

## 15. File Handling

### Reading & Writing Files

```python
# Open modes:
# 'r'  → read only (default)
# 'w'  → write (creates/overwrites)
# 'a'  → append (adds to end)
# 'rb' → read binary
# 'wb' → write binary
# 'r+' → read and write

# Reading:
with open("file.txt", "r") as f:
    content = f.read()         # entire file as string
    lines = f.readlines()      # list of lines
    for line in f:             # iterate line by line (memory efficient)
        print(line.strip())

# Writing:
with open("file.txt", "w") as f:
    f.write("Hello, World!\n")
    f.writelines(["Line 1\n", "Line 2\n"])

# Always use 'with' — it automatically closes the file even if an error occurs
```

### Deleting a File

```python
import os

# Delete a file
os.remove("myfile.txt")

# Check if exists first (safe approach):
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
    print("Deleted")
else:
    print("File not found")

# Delete an empty directory:
os.rmdir("mydir")

# Delete directory and all contents:
import shutil
shutil.rmtree("mydir")
```

---

## 16. Multithreading & Multiprocessing

### Multithreading

```python
import threading

def print_numbers():
    for i in range(5):
        print(i)

def print_letters():
    for c in "ABCDE":
        print(c)

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for both to finish
t1.join()
t2.join()
```

### Threading vs Multiprocessing

```
THREADING:
  Threads share the same memory.
  Limited by GIL → only one thread runs Python code at a time.
  Good for: I/O-bound tasks (reading files, network calls, DB queries).

MULTIPROCESSING:
  Each process has its OWN Python interpreter + memory.
  No GIL limitation → true parallelism on multiple CPU cores.
  Good for: CPU-bound tasks (number crunching, image processing, ML).
```

```python
from multiprocessing import Pool

def square(n):
    return n ** 2

with Pool(4) as p:            # 4 worker processes
    results = p.map(square, range(10))
print(results)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Python List vs NumPy Array — Speed

```
Python list:   Interpreted, dynamic types, each element is a Python object.
NumPy array:   Implemented in C, fixed type, contiguous memory block.

NumPy is 10x-100x faster for numerical operations because:
  1. Operations run in compiled C (not interpreted Python)
  2. Vectorised operations (no explicit Python loops)
  3. Contiguous memory → CPU cache-friendly
```

---

## 17. NumPy & Pandas Basics

### NumPy Basics

```python
import numpy as np

# Creating arrays
a = np.array([1, 2, 3, 4, 5])
b = np.zeros((3, 3))           # 3x3 of zeros
c = np.ones((2, 4))            # 2x4 of ones
d = np.arange(0, 10, 2)       # [0, 2, 4, 6, 8]
e = np.linspace(0, 1, 5)      # [0, .25, .5, .75, 1]
f = np.random.rand(3, 3)      # random 3x3

# Operations (vectorised — no loops needed!)
a * 2          # [2, 4, 6, 8, 10]
a + 10         # [11, 12, 13, 14, 15]
np.sqrt(a)     # [1, 1.41, 1.73, 2, 2.24]

# Statistics
np.mean(a)     # 3.0
np.median(a)   # 3.0
np.std(a)      # 1.41
np.sum(a)      # 15
np.min(a)      # 1
np.max(a)      # 5

# Sort by column N-1 (last column):
arr = np.array([[3, 1], [1, 4], [2, 2]])
sorted_arr = arr[arr[:, -1].argsort()]   # sort by last column
```

### Pandas Basics

```python
import pandas as pd

# Series — 1D labelled array
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
s["a"]    # 10
s.mean()  # 20

# DataFrame — 2D table
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Carol"],
    "age":  [25, 30, 22],
    "city": ["NY", "LA", "Chicago"]
})

# Accessing data
df["name"]             # column → Series
df[["name", "age"]]    # multiple columns → DataFrame
df.loc[0]              # row by label
df.iloc[0]             # row by integer index
df[df["age"] > 24]     # filter rows

# Common operations
df.head(3)             # first 3 rows
df.tail(3)             # last 3 rows
df.shape               # (rows, cols)
df.columns             # column names
df.dtypes              # data types
df.describe()          # statistics
df.isnull().sum()      # count NaN values

# Add a new column
df["salary"] = [70000, 85000, 60000]
df["annual"] = df["salary"] * 12     # calculated column

# groupby
df.groupby("city")["salary"].mean()  # average salary per city

# DataFrame vs Series:
# Series  = 1D labelled array (one column)
# DataFrame = 2D table with rows AND columns
```

---

## 18. Flask & Django Basics

### Flask

**Flask** is a **micro web framework** for Python — lightweight, minimal, flexible.

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")                        # decorator defines URL route
def home():
    return "Hello, World!"

@app.route("/user/<name>")
def greet(name):
    return f"Hello, {name}!"

@app.route("/api/data", methods=["GET", "POST"])
def data():
    if request.method == "POST":
        body = request.json
        return jsonify({"received": body})
    return jsonify({"data": "some data"})

if __name__ == "__main__":
    app.run(debug=True)
```

**Flask benefits:** Simple, lightweight, flexible, unopinionated, easy to learn, good for microservices and small APIs.

### Django

**Django** is a **full-stack web framework** with batteries included.

**Django MVT Architecture:**
```
Model (M) → defines data structure + interacts with database via ORM
View (V)  → handles business logic, processes requests, returns responses
Template (T) → HTML files with Django template tags for dynamic rendering

Request flow:
  User → URL dispatcher → View → Model (if needed) → Template → Response
```

### Django vs Flask

| | Flask | Django |
|---|---|---|
| Type | Micro-framework | Full-stack framework |
| Out-of-the-box | Minimal | Admin panel, ORM, Auth |
| Flexibility | Very flexible (you decide) | Opinionated (Django's way) |
| Learning curve | Easier to start | More to learn upfront |
| Best for | Microservices, small APIs | Large, complex apps |

### Django Inheritance Styles

```
ABSTRACT BASE CLASS:   Not a real table, just a template for other models.
MULTI-TABLE:           Each model gets its own database table, linked by Django.
PROXY MODEL:           Same DB table as parent, but different Python behaviour.
```

---

## 19. Python Internals — How Python Works Inside

> These questions come up in senior/advanced interviews. Understanding them shows you truly know Python.

### What Happens When You Run a .py File?

```
Your script: hello.py
        │
        ▼  Step 1: LEXER (Tokeniser)
   Stream of tokens: keywords, identifiers, operators, literals
        │
        ▼  Step 2: PARSER
   Abstract Syntax Tree (AST) — tree structure representing code
        │
        ▼  Step 3: COMPILER
   Bytecode (.pyc stored in __pycache__/)
        │
        ▼  Step 4: PVM (Python Virtual Machine)
   Executes bytecode instruction by instruction → your output!

Summary: .py → tokens → AST → bytecode (.pyc) → PVM → execution
```

### Why Can't Python Threads Run in True Parallel on Multi-Core CPUs?

```
Because of the GIL (Global Interpreter Lock) in CPython.

Even on a 16-core machine:
  Thread 1 tries to run  →  must acquire GIL first
  Thread 2 tries to run  →  GIL is taken, must WAIT
  Thread 1 finishes or does I/O → releases GIL
  Thread 2 now acquires GIL → runs

Only ONE thread executes Python bytecode at any moment.

Solution for true parallelism: Use multiprocessing (each
process has its OWN GIL and its OWN interpreter).
```

### How Does Python's Memory Allocation Work Behind the Scenes?

```
Every Python object is a PyObject structure containing:
  - ob_refcnt:  reference count (how many variables point to this)
  - ob_type:    pointer to the object's type

Small integer interning:
  Python pre-creates int objects for -5 to 256.
  x = 5 and y = 5 → x is y == True (same cached object!)
  x = 257 and y = 257 → x is y == False (new objects!)

String interning:
  Short strings (identifiers) are often interned too.
  s1 = "hello" and s2 = "hello" → may share the same object.

Memory pools (pymalloc):
  Python uses pre-allocated pools for objects < 512 bytes.
  Avoids slow OS-level malloc/free calls → much faster!
```

```python
import sys

x = [1, 2, 3]
sys.getrefcount(x)          # reference count (usually count + 1 for the call)
sys.getsizeof(x)            # memory size in bytes

# Interning demo:
a = 256; b = 256
print(a is b)   # True  (interned)
a = 257; b = 257
print(a is b)   # False (not interned — usually)
```

### What is the id() Function vs Memory Address?

```python
x = 42
id(x)           # unique integer identifier for object x

# In CPython: id(x) IS the memory address of x
# In PyPy or other implementations: may NOT be the real memory address

a = [1, 2, 3]
b = a           # b points to same object
id(a) == id(b)  # True → same object

# id() is only guaranteed unique for objects alive at the SAME time
# (after an object is deleted, its memory can be reused by a new object)
```

### How Does Python Implement for Loops Internally?

```python
# What you write:
for item in [1, 2, 3]:
    print(item)

# What Python actually does:
iterator = iter([1, 2, 3])   # Step 1: call iter() to get iterator
while True:
    try:
        item = next(iterator) # Step 2: call next() repeatedly
        print(item)
    except StopIteration:     # Step 3: stop when exhausted
        break
```

> **Key insight:** Python `for` loops use the **iterator protocol** — any object with `__iter__()` and `__next__()` methods can be iterated.

### How Does Python Store and Look Up Variables Internally?

```
Local variables  → stored in a fast "locals array" (very fast access)
Global variables → stored in a dict (frame's f_globals)
Built-in names   → stored in a dict (f_builtins)

Name lookup follows LEGB:
  L → Local array first
  E → Enclosing function's locals
  G → Global dict
  B → Built-in dict
  If not found anywhere → NameError!
```

### Why Are Function Default Arguments Evaluated Only Once?

```python
# This is THE most famous Python gotcha:
def append_to(val, lst=[]):   # list created ONCE at function definition time
    lst.append(val)
    return lst

append_to(1)   # [1]
append_to(2)   # [1, 2]  ← same list! not a fresh []
append_to(3)   # [1, 2, 3]  ← still the same list!

# Why? Default values are stored in func.__defaults__ at DEFINITION TIME.
print(append_to.__defaults__)   # ([1, 2, 3],) ← the live list!

# THE FIX — use None as sentinel:
def append_to_safe(val, lst=None):
    if lst is None:
        lst = []        # create fresh list on EVERY call
    lst.append(val)
    return lst
```

### Does Python Support Tail Recursion?

**No.** Python does **not** optimise tail recursive calls.

```python
# This WILL hit Python's recursion limit (default: 1000):
def count_down(n):
    if n == 0: return 0
    return count_down(n - 1)   # tail call — but Python doesn't optimise it!

# Check/set recursion limit:
import sys
sys.getrecursionlimit()        # 1000 (default)
sys.setrecursionlimit(5000)    # increase if needed

# Better: use iteration instead of deep recursion:
def count_down_iter(n):
    while n > 0:
        n -= 1
    return 0
```

### What are Python's Special (Dunder) Methods?

Also called **dunder methods** (double underscore).

```python
class MyList:
    def __init__(self, data):       # object creation
        self.data = data

    def __str__(self):              # print(obj) → human-readable string
        return f"MyList({self.data})"

    def __repr__(self):             # repr(obj) → developer string
        return f"MyList({self.data!r})"

    def __len__(self):              # len(obj)
        return len(self.data)

    def __getitem__(self, idx):     # obj[idx]
        return self.data[idx]

    def __contains__(self, item):   # item in obj
        return item in self.data

    def __add__(self, other):       # obj1 + obj2
        return MyList(self.data + other.data)

    def __eq__(self, other):        # obj1 == obj2
        return self.data == other.data

ml = MyList([1, 2, 3])
print(ml)       # MyList([1, 2, 3])
len(ml)         # 3
ml[0]           # 1
1 in ml         # True
```

---
## 20. Tricky Output Questions

> These are real interview questions. Read the code, predict output, then check.

---

### T1 · Mutable Default Argument (Classic Trap!)

```python
def add_item(x, data=[]):
    data.append(x)
    return data

print(add_item(1))
print(add_item(2))
print(add_item(3))
```

**Output:**
```
[1]
[1, 2]
[1, 2, 3]
```

> **Why?** Default arguments are created **once when the function is defined**, not on each call. The same list is reused every time.

**Fix:**
```python
def add_item(x, data=None):
    if data is None:
        data = []          # create a new list on each call
    data.append(x)
    return data
```

---

### T2 · Generator Exhaustion

```python
gen = (i for i in range(3))
list1 = list(gen)
list2 = list(gen)
print(list1, list2)
```

**Output:** `[0, 1, 2] []`

> **Why?** Generators can only be iterated **once**. After `list1` consumes it, the generator is exhausted — `list2` gets nothing.

---

### T3 · finally Always Wins

```python
def func():
    try:
        return 1
    finally:
        return 2

print(func())
```

**Output:** `2`

> **Why?** The `finally` block **always runs** and its `return` overrides the `try` block's return.

---

### T4 · Boolean Arithmetic

```python
print(True + True, True * 5, False + 1)
```

**Output:** `2 5 1`

> **Why?** `True == 1` and `False == 0` in Python arithmetic.

---

### T5 · List Comprehension Scope

```python
x = 10
[x for x in range(3)]
print(x)
```

**Output:** `10`

> **Why?** In Python 3, the loop variable inside a list comprehension does **NOT leak** into the outer scope. `x` remains `10`.

---

### T6 · Simultaneous Swap

```python
a, b = 1, 2
b, a = a, b
print(a, b)
```

**Output:** `2 1`

> **Why?** Python evaluates the right side `(a, b)` completely first → creates tuple `(1, 2)` → then unpacks to `b=1, a=2`. Clean atomic swap — no temp variable needed!

---

### T7 · Star Unpacking

```python
a, *b, c = [1, 2, 3, 4, 5]
print(a, b, c)
```

**Output:** `1 [2, 3, 4] 5`

> **Why?** `*b` captures all "middle" elements into a list.

---

### T8 · Dictionary Key Snapshot

```python
a = 1
d = {a: "value"}
a = 2
print(d)
```

**Output:** `{1: 'value'}`

> **Why?** When the dict is created, the key takes the **value of `a` at that moment** (which is `1`). Changing `a` later doesn't affect the existing key.

---

### T9 · Mutable List as Dict Value

```python
my_list = [1, 2]
my_dict = {tuple(my_list): my_list}
my_list.append(3)
print(my_dict)
```

**Output:** `{(1, 2): [1, 2, 3]}`

> **Why?** The key is a **snapshot** (immutable tuple). But the value is still a **reference** to the original list — so when `3` is appended, the value updates.

---

### T10 · Short-Circuit Evaluation

```python
print([] and [1] or [2])
```

**Output:** `[2]`

> **Why?**
```
[] and [1]  → [] is falsy → short-circuits to []
[] or [2]   → [] is falsy → evaluates right side → [2]
```

---

### T11 · UnboundLocalError

```python
x = 10
def outer():
    x = 20
    def inner():
        print(x)   # x is treated as local (because it's in outer, not inner)
    inner()
outer()
```

**Output:** `20` (prints outer's `x` via closure)

```python
# This WOULD cause UnboundLocalError:
x = 10
def func():
    print(x)      # tries to use local x
    x = 20        # x is local because of this line → but not defined yet!
func()            # UnboundLocalError!

# Fix with nonlocal or global:
def func():
    global x
    print(x)
    x = 20
```

---

### T12 · Slice Reversal

```python
print("hello world"[::-1])
```

**Output:** `dlrow olleh`

---

### T13 · List Multiplication

```python
print([1, 2] * 3)
```

**Output:** `[1, 2, 1, 2, 1, 2]`

---

### T14 · Floor Division of Negative

```python
print((-7) // 2)
```

**Output:** `-4`

> **Why?** Floor division **floors toward negative infinity**, not toward zero. `-7/2 = -3.5` → floor is `-4`.

---

## 21. Coding Challenges

### C1 · Fibonacci Series

```python
def fibonacci(n):
    """Generate first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)   # 0 1 1 2 3 5 8 13 21 34

# Recursive version:
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Generator version (memory efficient):
def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

### C2 · Check Palindrome

```python
def is_palindrome(s):
    """A palindrome reads the same forwards and backwards."""
    s = s.lower().replace(" ", "")   # normalise
    return s == s[::-1]

is_palindrome("racecar")    # True
is_palindrome("hello")      # False
is_palindrome("A man a plan a canal Panama")  # True
```

### C3 · Check Prime Number

```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):   # only check up to √n
        if n % i == 0:
            return False
    return True

is_prime(17)    # True
is_prime(20)    # False
```

### C4 · Factorial

```python
# Iterative (preferred):
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Recursive:
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

factorial(5)   # 120
```

### C5 · Reverse a String

```python
s = "Hello, World!"

# Method 1: slicing (most Pythonic)
reversed_s = s[::-1]        # "!dlroW ,olleH"

# Method 2: built-in
reversed_s = "".join(reversed(s))

# Method 3: loop
reversed_s = ""
for char in s:
    reversed_s = char + reversed_s
```

### C6 · Find Second Largest in a List

```python
def second_largest(lst):
    unique = list(set(lst))   # remove duplicates
    unique.sort()
    return unique[-2]         # second to last = second largest

second_largest([10, 20, 4000, 6000])  # 4000
```

### C7 · Check Armstrong Number

```python
def is_armstrong(n):
    """Armstrong: sum of each digit raised to power of total digits."""
    digits = str(n)
    power = len(digits)
    return sum(int(d) ** power for d in digits) == n

is_armstrong(153)   # True  (1³ + 5³ + 3³ = 1+125+27 = 153)
is_armstrong(370)   # True
is_armstrong(10)    # False
```

### C8 · Bubble Sort

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]   # swap
    return arr

bubble_sort([64, 34, 25, 12, 22])   # [12, 22, 25, 34, 64]
```

### C9 · Swap Two Variables

```python
# Python way (clean, no temp variable):
a, b = 5, 10
a, b = b, a
print(a, b)    # 10 5

# Swap elements in a list:
lst = [1, 2, 3, 4]
lst[0], lst[-1] = lst[-1], lst[0]   # swap first and last
print(lst)   # [4, 2, 3, 1]
```

### C10 · Leap Year Check

```python
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

is_leap_year(2024)   # True
is_leap_year(1900)   # False
is_leap_year(2000)   # True
```

### C11 · Strong Number

```python
import math

def is_strong(n):
    """Strong number: sum of factorial of digits == the number."""
    return sum(math.factorial(int(d)) for d in str(n)) == n

is_strong(145)    # True  (1! + 4! + 5! = 1+24+120 = 145)
is_strong(12)     # False
```

### C12 · Find Duplicates in a List

```python
def find_duplicates(lst):
    seen = set()
    duplicates = []
    for item in lst:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates

# One-liner using Counter:
from collections import Counter
def find_duplicates(lst):
    return [item for item, count in Counter(lst).items() if count > 1]
```

### C13 · Remove Duplicates (Keeping Order)

```python
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Using dict.fromkeys (keeps order, Python 3.7+):
unique = list(dict.fromkeys(lst))   # [3, 1, 4, 5, 9, 2, 6]

# Using set (fast but loses order):
unique = list(set(lst))             # order not guaranteed
```

---

## 22. Quick Cheatsheet & Memory Tips

### One-Line Definitions

| Term | One-Line Definition |
|---|---|
| **Python** | High-level, interpreted, dynamically typed, general-purpose language. |
| **Interpreted** | Code runs line-by-line through the Python Virtual Machine. |
| **Dynamically typed** | Variable types assigned at runtime, not declared by programmer. |
| **GIL** | Lock in CPython allowing only one thread to run Python code at a time. |
| **List** | Ordered, mutable, allows duplicates. `[1, 2, 3]` |
| **Tuple** | Ordered, immutable, allows duplicates. `(1, 2, 3)` |
| **Set** | Unordered, mutable, NO duplicates. `{1, 2, 3}` |
| **frozenset** | Immutable version of set — hashable, usable as dict key. |
| **Dict** | Key-value pairs, O(1) lookup via hash table. `{"a": 1}` |
| **Mutable** | Can be changed after creation (list, dict, set). |
| **Immutable** | Cannot be changed after creation (int, str, tuple). |
| **is** | Checks identity — same object in memory. |
| **==** | Checks equality — same value. |
| **`*args`** | Collects extra positional args into a tuple. |
| **`**kwargs`** | Collects extra keyword args into a dict. |
| **Lambda** | Anonymous one-line function. `lambda x: x*2` |
| **Decorator** | Function wrapping another function to add behaviour. |
| **Generator** | Function using `yield` to produce values lazily, one at a time. |
| **Shallow copy** | New container, but nested objects are shared references. |
| **Deep copy** | Fully independent copy — all nested objects also copied. |
| **Namespace** | Container mapping names to objects. LEGB lookup order. |
| **Self** | First parameter of instance methods — refers to current object. |
| **`__init__`** | Constructor — initialises a new object's attributes. |
| **`__new__`** | Creates the object in memory (before `__init__`). |
| **Inheritance** | Child class reuses parent class code. |
| **MRO** | Order Python searches for methods in inheritance. C3 algorithm. |
| **Encapsulation** | Bundling data + methods; restricting direct access. |
| **Abstraction** | Hiding complexity; showing only what's necessary (ABC). |
| **Overriding** | Child class redefines parent's method. |
| **Overloading** | Not natively supported; simulated via default/`*args` params. |
| **PEP 8** | Official Python style guide. |
| **PIP** | Python package manager. |
| **Module** | Single `.py` file. |
| **Package** | Directory of modules + `__init__.py`. |
| **Docstring** | Triple-quoted string documenting a function/class/module. |
| **Pickling** | Serialising Python objects to bytes (for storage/transfer). |
| **Timsort** | Sorting algorithm used by `sort()` and `sorted()`. O(n log n). |
| **Flask** | Lightweight micro web framework. |
| **Django** | Full-stack web framework following MVT architecture. |

---

### Memory Tricks

**1. Mutable vs Immutable:**
```
"Lists and Dicts are LIQUID (can change shape)"
"Strings and Tuples are SOLID (locked in place)"
```

**2. break vs continue vs pass:**
```
break    → STOP the loop entirely      (like an emergency exit)
continue → SKIP this iteration, keep going (like skipping a page)
pass     → DO NOTHING (placeholder)   (like an empty page)
```

**3. LEGB Rule (Name lookup order):**
```
L → Local      (inside current function)
E → Enclosing  (outer function, for nested functions)
G → Global     (module level)
B → Built-in   (Python's built-ins: print, len, range...)

Memory: "Let Every Good Boy win"
```

**4. Inheritance types:**
```
Single     = one parent      (A → B)
Multi-level = chain of parents (A → B → C)
Hierarchical = one parent many children (A → B, A → C)
Multiple   = many parents    (A + B → C)
```

**5. shallow vs deep copy:**
```
Shallow = same house, different rooms (but shared bathroom = nested objects)
Deep    = completely different house  (nothing shared)
```

**6. sort() vs sorted():**
```
sort()   = SORTS the list itself — CHANGES original, returns NONE
sorted() = SORTS and RETURNS new list — original UNCHANGED
```

**7. GIL in simple terms:**
```
GIL = a talking stick in a meeting.
Only the person holding the stick can talk (execute code).
Even if you have 10 people (threads), only 1 talks at a time.
```

---

### Study Priority Guide

| Level | Must-Know Topics |
|---|---|
| **Fresher** | Data types, mutable/immutable, list/tuple/dict/set, loops, functions, OOP basics (class, self, `__init__`), exception handling, list comprehension |
| **Mid-level** | Inheritance + MRO, *args/**kwargs, decorators, generators, lambda, shallow/deep copy, GIL, memory management, comprehensions, file handling |
| **Senior** | Metaclasses, descriptors, context managers, `__dunder__` methods, asyncio, multiprocessing, profiling, design patterns in Python |

---

> **Final Interview Tip:**
> The most common Python interview questions are:
> - "Mutable vs immutable" → know all types cold
> - "Shallow vs deep copy" → be ready to draw it
> - "`*args` vs `**kwargs`" → write an example
> - "What is the GIL?" → one paragraph answer
> - "Decorators" → write a simple one from scratch
> - "List vs Tuple" → 5 differences
> - "How does Python manage memory?" → reference counting + GC
> - "What is `self`?" → instance reference, not a keyword
>
> Code every concept. Don't just read — type it, run it, break it, fix it.
> That's how Python sticks. 🚀
