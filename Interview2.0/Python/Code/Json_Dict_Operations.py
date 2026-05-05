# =============================================================================
# DICTIONARY & JSON — INTERVIEW PRACTICE
# =============================================================================
# Every problem an interviewer can ask about dicts/JSON.
# Each solution has: manual way (no builtins) + Pythonic way.
# Run this file to verify all outputs.
# =============================================================================


# =============================================================================
# PROBLEM 1 — Access a specific key
# =============================================================================
# Q: Given a profile dict, return the value of the "age" key.

profile = {
    "name": "Ash",
    "age": "100",
    "id": "123"
}

# Manual — loop through keys
def get_key_manual(d, key):
    for k in d:
        if k == key:
            return d[k]
    return None

# Pythonic — .get() never raises KeyError
def get_key_pythonic(d, key):
    return d.get(key, "Key not found")

print("--- Problem 1: Access a key ---")
print(get_key_manual(profile, "age"))
print(get_key_pythonic(profile, "age"))
print(get_key_pythonic(profile, "missing"))


# =============================================================================
# PROBLEM 2 — Swap keys and values
# =============================================================================
# Q: Given {"A": "1", "B": "2"} return {"1": "A", "2": "B"}

freq = {"A": "1", "B": "2"}

# Manual — loop and build new dict
def swap_manual(d):
    result = {}
    for key in d:
        result[d[key]] = key
    return result

# Pythonic — dict comprehension
def swap_pythonic(d):
    return {v: k for k, v in d.items()}

print("\n--- Problem 2: Swap keys and values ---")
print(swap_manual(freq))
print(swap_pythonic(freq))


# =============================================================================
# PROBLEM 3 — Count frequency of each value
# =============================================================================
# Q: Count how many times each item appears.
# Input:  ["apple", "banana", "apple", "cherry", "banana", "apple"]
# Output: {"apple": 3, "banana": 2, "cherry": 1}

items = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# Manual — loop, check if key exists, increment
def count_manual(lst):
    result = {}
    for item in lst:
        if item in result:
            result[item] = result[item] + 1
        else:
            result[item] = 1
    return result

# Pythonic — .get() with default
def count_pythonic(lst):
    result = {}
    for item in lst:
        result[item] = result.get(item, 0) + 1
    return result

print("\n--- Problem 3: Count frequency ---")
print(count_manual(items))
print(count_pythonic(items))


# =============================================================================
# PROBLEM 4 — Merge two dictionaries
# =============================================================================
# Q: Merge dict1 and dict2. If same key exists, dict2 value wins.

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 99, "c": 3}

# Manual — loop through both
def merge_manual(d1, d2):
    result = {}
    for key in d1:
        result[key] = d1[key]
    for key in d2:
        result[key] = d2[key]  # overwrites if key exists in d1
    return result

# Pythonic — ** unpacking
def merge_pythonic(d1, d2):
    return {**d1, **d2}

print("\n--- Problem 4: Merge two dicts ---")
print(merge_manual(dict1, dict2))
print(merge_pythonic(dict1, dict2))


# =============================================================================
# PROBLEM 5 — Find key with maximum value
# =============================================================================
# Q: Given {"a": 3, "b": 7, "c": 1}, return the key with the highest value.

scores = {"a": 3, "b": 7, "c": 1}

# Manual — loop and track best
def max_key_manual(d):
    best_key = None
    best_val = None
    for key in d:
        if best_val is None or d[key] > best_val:
            best_val = d[key]
            best_key = key
    return best_key

# Pythonic — max() with key argument
def max_key_pythonic(d):
    return max(d, key=d.get)

print("\n--- Problem 5: Key with max value ---")
print(max_key_manual(scores))
print(max_key_pythonic(scores))


# =============================================================================
# PROBLEM 6 — Filter a dict by value condition
# =============================================================================
# Q: Return only entries where age > 25.

people = {"Alice": 30, "Bob": 20, "Charlie": 35, "Dave": 22}

# Manual — loop and check condition
def filter_manual(d, threshold):
    result = {}
    for key in d:
        if d[key] > threshold:
            result[key] = d[key]
    return result

# Pythonic — dict comprehension with condition
def filter_pythonic(d, threshold):
    return {k: v for k, v in d.items() if v > threshold}

print("\n--- Problem 6: Filter dict by value ---")
print(filter_manual(people, 25))
print(filter_pythonic(people, 25))


# =============================================================================
# PROBLEM 7 — Remove a key safely
# =============================================================================
# Q: Remove "age" from profile without raising an error if it doesn't exist.

data = {"name": "Ash", "age": "100", "id": "123"}

# Manual — check before delete
def remove_key_manual(d, key):
    result = {}
    for k in d:
        if k != key:
            result[k] = d[k]
    return result

# Pythonic — .pop() with default avoids KeyError
def remove_key_pythonic(d, key):
    d = d.copy()
    d.pop(key, None)
    return d

print("\n--- Problem 7: Remove a key safely ---")
print(remove_key_manual(data, "age"))
print(remove_key_pythonic(data, "age"))
print(remove_key_pythonic(data, "missing"))  # no error


# =============================================================================
# PROBLEM 8 — Check if key exists
# =============================================================================
# Q: Check if "email" exists in profile without raising an error.

profile2 = {"name": "Ash", "age": "100"}

# Manual — loop to find
def key_exists_manual(d, key):
    for k in d:
        if k == key:
            return True
    return False

# Pythonic — `in` keyword
def key_exists_pythonic(d, key):
    return key in d

print("\n--- Problem 8: Check if key exists ---")
print(key_exists_manual(profile2, "age"))
print(key_exists_manual(profile2, "email"))
print(key_exists_pythonic(profile2, "age"))
print(key_exists_pythonic(profile2, "email"))


# =============================================================================
# PROBLEM 9 — Sort dict by value
# =============================================================================
# Q: Sort {"banana": 3, "apple": 5, "cherry": 1} by value ascending.

fruit_count = {"banana": 3, "apple": 5, "cherry": 1}

# Manual — extract pairs, bubble sort, rebuild dict
def sort_by_value_manual(d):
    pairs = []
    for key in d:
        pairs.append((key, d[key]))
    # bubble sort by value
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            if pairs[i][1] > pairs[j][1]:
                pairs[i], pairs[j] = pairs[j], pairs[i]
    result = {}
    for key, val in pairs:
        result[key] = val
    return result

# Pythonic — sorted() with lambda
def sort_by_value_pythonic(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

print("\n--- Problem 9: Sort dict by value ---")
print(sort_by_value_manual(fruit_count))
print(sort_by_value_pythonic(fruit_count))


# =============================================================================
# PROBLEM 10 — Group list of dicts by a key
# =============================================================================
# Q: Group these employees by department.
# Input:  [{"name": "Alice", "dept": "Eng"}, {"name": "Bob", "dept": "HR"}, ...]
# Output: {"Eng": ["Alice", "Charlie"], "HR": ["Bob"]}

employees = [
    {"name": "Alice",   "dept": "Eng"},
    {"name": "Bob",     "dept": "HR"},
    {"name": "Charlie", "dept": "Eng"},
    {"name": "Dave",    "dept": "HR"},
    {"name": "Eve",     "dept": "Design"}
]

# Manual — loop, check if group exists, append
def group_by_manual(lst, key):
    result = {}
    for item in lst:
        group = item[key]
        if group not in result:
            result[group] = []
        result[group].append(item["name"])
    return result

# Pythonic — setdefault or dict comprehension + groupby
def group_by_pythonic(lst, key):
    result = {}
    for item in lst:
        result.setdefault(item[key], []).append(item["name"])
    return result

print("\n--- Problem 10: Group list of dicts by key ---")
print(group_by_manual(employees, "dept"))
print(group_by_pythonic(employees, "dept"))


# =============================================================================
# PROBLEM 11 — Flatten a nested dict (deep access)
# =============================================================================
# Q: Given a nested dict, return a flat dict with dot-notation keys.
# Input:  {"user": {"name": "Ash", "address": {"city": "London"}}}
# Output: {"user.name": "Ash", "user.address.city": "London"}

nested = {
    "user": {
        "name": "Ash",
        "address": {
            "city": "London",
            "zip": "E1 1AA"
        }
    },
    "id": "123"
}

# Manual / recursive — traverse and build keys
def flatten_manual(d, parent_key="", result=None):
    if result is None:
        result = {}
    for key in d:
        full_key = parent_key + "." + key if parent_key else key
        if type(d[key]) == dict:
            flatten_manual(d[key], full_key, result)
        else:
            result[full_key] = d[key]
    return result

# Pythonic — same logic but using .items()
def flatten_pythonic(d, parent_key=""):
    result = {}
    for key, value in d.items():
        full_key = f"{parent_key}.{key}" if parent_key else key
        if isinstance(value, dict):
            result.update(flatten_pythonic(value, full_key))
        else:
            result[full_key] = value
    return result

print("\n--- Problem 11: Flatten nested dict ---")
print(flatten_manual(nested))
print(flatten_pythonic(nested))


# =============================================================================
# PROBLEM 12 — Find common keys between two dicts
# =============================================================================
# Q: Return keys that exist in both dicts.

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "c": 30, "d": 40}

# Manual — loop d1, check if key in d2
def common_keys_manual(d1, d2):
    result = []
    for key in d1:
        if key in d2:
            result.append(key)
    return result

# Pythonic — set intersection on keys
def common_keys_pythonic(d1, d2):
    return list(d1.keys() & d2.keys())

print("\n--- Problem 12: Common keys ---")
print(common_keys_manual(d1, d2))
print(common_keys_pythonic(d1, d2))


# =============================================================================
# PROBLEM 13 — Deep get (safe nested access)
# =============================================================================
# Q: Access nested["user"]["address"]["city"] safely without KeyError.
#    Return None if any key in the path is missing.

data2 = {
    "user": {
        "name": "Ash",
        "address": {
            "city": "London"
        }
    }
}

# Manual — loop through keys one by one
def deep_get_manual(d, keys):
    current = d
    for key in keys:
        found = False
        if type(current) == dict:
            for k in current:
                if k == key:
                    current = current[k]
                    found = True
                    break
        if not found:
            return None
    return current

# Pythonic — loop with .get()
def deep_get_pythonic(d, keys):
    current = d
    for key in keys:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current

print("\n--- Problem 13: Deep/nested key access ---")
print(deep_get_manual(data2, ["user", "address", "city"]))
print(deep_get_pythonic(data2, ["user", "address", "city"]))
print(deep_get_pythonic(data2, ["user", "phone"]))  # None — key missing


# =============================================================================
# PROBLEM 14 — Parse and extract from a list of JSON-like dicts
# =============================================================================
# Q: From this API response, return a list of names where status is "active".

api_response = {
    "users": [
        {"id": 1, "name": "Alice",   "status": "active"},
        {"id": 2, "name": "Bob",     "status": "inactive"},
        {"id": 3, "name": "Charlie", "status": "active"},
        {"id": 4, "name": "Dave",    "status": "inactive"},
    ]
}

# Manual — loop through list, check condition
def active_users_manual(response):
    result = []
    for user in response["users"]:
        if user["status"] == "active":
            result.append(user["name"])
    return result

# Pythonic — list comprehension
def active_users_pythonic(response):
    return [u["name"] for u in response["users"] if u["status"] == "active"]

print("\n--- Problem 14: Filter list of dicts by condition ---")
print(active_users_manual(api_response))
print(active_users_pythonic(api_response))


# =============================================================================
# PROBLEM 15 — Transform list of dicts (reshape JSON)
# =============================================================================
# Q: Convert list of user dicts into a dict keyed by id.
# Input:  [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
# Output: {1: {"name": "Alice"}, 2: {"name": "Bob"}}

users = [
    {"id": 1, "name": "Alice",   "age": 30},
    {"id": 2, "name": "Bob",     "age": 25},
    {"id": 3, "name": "Charlie", "age": 35}
]

# Manual — loop and build
def index_by_id_manual(lst):
    result = {}
    for item in lst:
        key = item["id"]
        result[key] = {}
        for field in item:
            if field != "id":
                result[key][field] = item[field]
    return result

# Pythonic — dict comprehension
def index_by_id_pythonic(lst):
    return {u["id"]: {k: v for k, v in u.items() if k != "id"} for u in lst}

print("\n--- Problem 15: Index list of dicts by a key ---")
print(index_by_id_manual(users))
print(index_by_id_pythonic(users))


# =============================================================================
# PROBLEM 16 — Two dicts differ — find what changed
# =============================================================================
# Q: Given old and new versions of a dict, return what was added,
#    removed, and changed.

old = {"name": "Ash", "age": "25",  "city": "London"}
new = {"name": "Ash", "age": "26",  "email": "ash@x.com"}

# Manual — loop both dicts
def diff_manual(old, new):
    added   = {}
    removed = {}
    changed = {}
    for key in old:
        if key not in new:
            removed[key] = old[key]
        elif old[key] != new[key]:
            changed[key] = {"old": old[key], "new": new[key]}
    for key in new:
        if key not in old:
            added[key] = new[key]
    return {"added": added, "removed": removed, "changed": changed}

# Pythonic — using set operations on keys
def diff_pythonic(old, new):
    old_keys = set(old.keys())
    new_keys = set(new.keys())
    return {
        "added":   {k: new[k] for k in new_keys - old_keys},
        "removed": {k: old[k] for k in old_keys - new_keys},
        "changed": {k: {"old": old[k], "new": new[k]}
                    for k in old_keys & new_keys if old[k] != new[k]}
    }

print("\n--- Problem 16: Diff two dicts ---")
print(diff_manual(old, new))
print(diff_pythonic(old, new))


print("\n=== All problems complete ===")