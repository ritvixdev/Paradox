# Python Copying — Interview Prep
### Assignment vs Shallow Copy vs Deep Copy

---

## 🧠 Key Concept First
Variables don't store values — they store **references** to objects in memory.

```python
a = [1, 2, 3]
# a ──► [1, 2, 3]   (a points to the object, not holds it)
```

---

## ❌ Assignment — NOT a Copy

```python
a = [1, 2, 3]
b = a          # b points to the SAME object

b[0] = 100
print(a)       # [100, 2, 3]  ← a changed too!
```

```
a ──► [1, 2, 3]
b ──┘              # both arrows point to same object
```

---

## 🔹 Shallow Copy — New outer, shared inner

```python
a = [1, 2, 3]
b = a.copy()   # also: list(a)  or  a[:]
```

```
a ──► [1, 2, 3]
b ──► [1, 2, 3]   # different outer object ✅
```

**Works fine** for flat lists (immutable elements like int, str):
```python
b[0] = 100
print(a)       # [1, 2, 3]  ← unchanged ✅
```

**Fails** for nested mutable objects:
```python
a = [[1, 2], [3, 4]]
b = a.copy()

b[0][0] = 100
print(a)       # [[100, 2], [3, 4]]  ← a changed! ❌
```

```
a ──► [ ──► [1, 2]        # inner lists are SHARED
        ──► [3, 4] ]
b ──► [ ──► same [1, 2]   # outer is new, inner still shared
        ──► same [3, 4] ]
```

---

## 🔥 Deep Copy — Fully independent

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0][0] = 100
print(a)       # [[1, 2], [3, 4]]  ← unchanged ✅
```

```
a ──► [ ──► [1, 2]
        ──► [3, 4] ]
b ──► [ ──► new [1, 2]    # everything is new and independent
        ──► new [3, 4] ]
```

---

## 🎯 Summary Table

| Type | Outer Object | Inner Objects | Use When |
|------|-------------|---------------|----------|
| Assignment | ❌ same | ❌ same | You want an alias |
| Shallow Copy | ✅ new | ❌ same | Flat data, immutable elements |
| Deep Copy | ✅ new | ✅ new | Nested mutable objects |

---

## 🧪 Full Demo

```python
import copy

# Assignment
a = [[1, 2], [3, 4]]
b = a
b[0][0] = 100
print(a)   # [[100, 2], [3, 4]]  ← changed ❌

# Shallow Copy
a = [[1, 2], [3, 4]]
b = a.copy()
b[0][0] = 100
print(a)   # [[100, 2], [3, 4]]  ← inner still shared ❌

# Deep Copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0][0] = 100
print(a)   # [[1, 2], [3, 4]]   ← fully independent ✅
```

---

## 🏆 Interview Answers

**Q: What's the difference between shallow and deep copy?**
> "Shallow copy creates a new outer object but inner objects are still shared references. Deep copy recursively copies everything — no references are shared at any level."

**Q: When does shallow copy fail?**
> "When the object contains nested mutable objects. Changing an inner object through the copy will affect the original because both point to the same inner objects."

**Q: Should you always use deep copy to be safe?**
> "No — deep copy is slower and uses more memory because it recurses through the entire structure. Use shallow copy for flat data, deep copy only when you have nested mutable objects and need full independence."
