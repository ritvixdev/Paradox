# LRU Cache — Interview Cheatsheet

## What to say first (memorize this)

> "LRU Cache stores key-value pairs with a fixed capacity. When the cache is full, it removes the **least recently used** item. So we need fast `get` and `put`, ideally O(1)."

---

## The Design

```
HashMap + Doubly Linked List
```

| Structure | Why |
|---|---|
| `HashMap` (dict) | Find any key in **O(1)** |
| `Doubly Linked List` | Move recently used item to front in **O(1)** |

### Visual layout of the list

```
[LEFT dummy] <-> [least recent] <-> ... <-> [most recent] <-> [RIGHT dummy]
```

- **Left dummy** = sentinel for the LRU end
- **Right dummy** = sentinel for the MRU (most recently used) end
- New/accessed items always go **just before RIGHT**
- Eviction always happens at **LEFT.next**

---

## Code Breakdown

### 1. Node — the list building block

```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
```

Each node holds the key+value and knows its neighbors on both sides (that's what makes it *doubly* linked).

---

### 2. `__init__` — setup

```python
def __init__(self, capacity):
    self.capacity = capacity
    self.cache = {}              # HashMap: key → Node

    self.left  = Node(0, 0)     # dummy: LRU side
    self.right = Node(0, 0)     # dummy: MRU side

    self.left.next  = self.right
    self.right.prev = self.left
```

Two dummy nodes mean you **never handle edge cases** for an empty list. The real nodes always live between them.

---

### 3. `remove(node)` — detach a node

```python
def remove(self, node):
    prev_node = node.prev
    next_node = node.next

    prev_node.next = next_node   # skip over node
    next_node.prev = prev_node   # skip over node
```

```
Before: [prev] <-> [node] <-> [next]
After:  [prev] <-> [next]
```

---

### 4. `insert(node)` — add just before RIGHT (= mark as most recent)

```python
def insert(self, node):
    prev_node = self.right.prev  # currently the most recent

    prev_node.next = node
    node.prev      = prev_node

    node.next       = self.right
    self.right.prev = node
```

```
Before: [...] <-> [prev_node] <-> [RIGHT]
After:  [...] <-> [prev_node] <-> [node] <-> [RIGHT]
```

---

### 5. `get(key)` — read a value

```python
def get(self, key):
    if key in self.cache:
        node = self.cache[key]

        self.remove(node)   # pull it out of current position
        self.insert(node)   # put it at MRU end

        return node.value

    return -1
```

**Key insight:** Even a read counts as "recently used", so the node is moved to the front.

---

### 6. `put(key, value)` — write a value

```python
def put(self, key, value):
    if key in self.cache:
        self.remove(self.cache[key])   # remove old node if key exists

    node = Node(key, value)
    self.cache[key] = node
    self.insert(node)                  # add as most recent

    if len(self.cache) > self.capacity:
        lru = self.left.next           # first real node = least recent
        self.remove(lru)
        del self.cache[lru.key]        # clean up HashMap too!
```

> ⚠️ Don't forget `del self.cache[lru.key]` — the node stores the key exactly for this moment.

---

## Full Code (copy-paste ready)

```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.left  = Node(0, 0)   # least recent dummy
        self.right = Node(0, 0)   # most recent dummy

        self.left.next  = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        prev_node = self.right.prev
        prev_node.next = node
        node.prev      = prev_node
        node.next       = self.right
        self.right.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
```

---

## Worked Example (trace through it)

```python
lru = LRUCache(2)

lru.put(1, 10)   # list: [1]
lru.put(2, 20)   # list: [1, 2]

lru.get(1)       # → 10    list: [2, 1]  (1 moved to MRU end)

lru.put(3, 30)   # over capacity → evict LEFT.next = 2
                 # list: [1, 3]

lru.get(2)       # → -1   (2 was evicted)
lru.get(3)       # → 30
```

---

## Complexity

| Operation | Time | Space |
|---|---|---|
| `get` | O(1) | — |
| `put` | O(1) | — |
| Overall | — | O(capacity) |

---

## Closing interview line (say this at the end)

> "I use a dictionary for O(1) lookup and a doubly linked list to maintain usage order. On every `get` or `put`, I move the key to the most recent position. When capacity is exceeded, I remove the node next to the least-recent dummy pointer."