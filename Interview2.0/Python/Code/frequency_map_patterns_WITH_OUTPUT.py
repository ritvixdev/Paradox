"""
Frequency Map Patterns (Interview Pack) - Python
Author: Suvam Das

✅ Each problem prints its example output immediately below the program
✅ Actual output shown as inline comments next to each print statement
✅ Examples are clear and interview-ready

CORE THEOREM:
  - Build a frequency map (dict) in O(n)
  - Then query/decide in O(k), k = unique items
  - Total: O(n) time, O(k) space — optimal for most frequency problems

KEY PATTERNS TO REMEMBER:
  1. Single-pass freq map          → count everything, then query
  2. Decrement pattern             → increment for A, decrement for B (anagram check)
  3. Seen-set / early-exit         → stop at first match (first repeating)
  4. Bucket sort by frequency      → O(n) top-K (no sorting needed)
  5. Frequency signature as key    → group anagrams without sorting
"""

# ==========================================================
# 1) Character Frequency
#    → Build a freq map of every character in the string.
#    → Foundation of nearly all frequency problems.
# ==========================================================
def char_frequency(s):
    """Return dict of character counts."""
    freq = {}
    for ch in s:
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] += 1
    return freq

print("\n--- 1) Character Frequency ---")
print("Input : 'programming'")
print("Output:", char_frequency("programming"))
# Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
#
# HOW IT WORKS:
#   p→1, r→2, o→1, g→2, a→1, m→2, i→1, n→1
#   'r', 'g', 'm' each appear TWICE → duplicates


# ==========================================================
# 2) First Non-Repeating Character
#    → Build freq map first, then scan left-to-right for freq==1.
#    → Two-pass O(n) is better than checking each char in a loop O(n²).
# ==========================================================
def first_non_repeating_char(s):
    """Return index of first char with frequency 1. Returns -1 if none."""
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1          # pass 1: build freq map

    for i in range(len(s)):
        if freq[s[i]] == 1:                      # pass 2: first freq-1 char
            return i
    return -1

print("\n--- 2) First Non-Repeating Character ---")
s2 = "programming"
idx2 = first_non_repeating_char(s2)
print("Input : 'programming'")
print("Output index:", idx2)                     # Output index: 0
print("Output char :", s2[idx2] if idx2 != -1 else None)  # Output char : p
#
# TRACE: freq = {p:1, r:2, o:1, g:2, a:1, m:2, i:1, n:1}
#   Scan: s[0]='p' → freq['p']==1 → return 0
#   'p' is the first character that appears only once.

print("\nEdge case — all repeating:")
s2b = "aabbcc"
idx2b = first_non_repeating_char(s2b)
print("Input : 'aabbcc'  →  Output index:", idx2b)  # Output index: -1


# ==========================================================
# 3) First Repeating Character
#    → Single-pass with a 'seen' set/dict.
#    → Return the moment we hit a character already in 'seen'.
# ==========================================================
def first_repeating_char(s):
    """Return first character that appears for the second time."""
    seen = {}
    for ch in s:
        if ch in seen:
            return ch                            # second occurrence = first repeat
        seen[ch] = 1
    return None

print("\n--- 3) First Repeating Character ---")
print("Input : 'programming'")
print("Output:", first_repeating_char("programming"))   # Output: r
#
# TRACE: seen = {}
#   p → not seen, add p
#   r → not seen, add r
#   o → not seen, add o
#   g → not seen, add g
#   r → SEEN! → return 'r'  ✓

print("Input : 'abcdef'  →  Output:", first_repeating_char("abcdef"))  # Output: None


# ==========================================================
# 4) All Repeating Characters (unique list)
#    → Build freq map, collect all chars where freq > 1.
# ==========================================================
def all_repeating_chars(s):
    """Return list of characters that appear more than once (unique)."""
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    return [ch for ch in freq if freq[ch] > 1]

print("\n--- 4) All Repeating Characters ---")
print("Input : 'programming'")
print("Output:", all_repeating_chars("programming"))    # Output: ['r', 'g', 'm']
#
# WHY: r→2, g→2, m→2 — all others appear exactly once.

print("Input : 'abcabc'  →  Output:", all_repeating_chars("abcabc"))   # Output: ['a', 'b', 'c']


# ==========================================================
# 5) Remove Duplicates (preserve insertion order)
#    → Use a 'seen' dict as an ordered set (Python 3.7+ dicts are ordered).
#    → Only append character on FIRST encounter.
# ==========================================================
def remove_duplicates_preserve_order(s):
    """Remove duplicates while preserving first occurrence order."""
    seen = {}
    result = ""
    for ch in s:
        if ch not in seen:
            seen[ch] = 1
            result += ch
    return result

print("\n--- 5) Remove Duplicates (preserve order) ---")
print("Input : 'programming'")
print("Output:", remove_duplicates_preserve_order("programming"))  # Output: progamin
#
# TRACE: p-r-o-g-r(skip)-a-m-m(skip)-i-n-g(skip)
#   Result: p r o g a m i n  → "progamin"

print("Input : 'aabbccdd'  →  Output:", remove_duplicates_preserve_order("aabbccdd"))  # Output: abcd


# ==========================================================
# 6) Count Duplicates (total extra occurrences)
#    → For each char with freq f, there are (f-1) extra copies.
#    → Sum all (freq - 1) for chars with freq > 1.
# ==========================================================
def count_duplicates(s):
    """Return total number of extra (duplicate) occurrences."""
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    return sum(freq[ch] - 1 for ch in freq if freq[ch] > 1)

print("\n--- 6) Count Duplicates (extra occurrences) ---")
print("Input : 'aabccc'")
print("Output:", count_duplicates("aabccc"))   # Output: 3
#
# BREAKDOWN: a→2 (1 extra), b→1 (0 extra), c→3 (2 extra)
#   Total extras = 1 + 0 + 2 = 3  ✓

print("Input : 'programming'  →  Output:", count_duplicates("programming"))  # Output: 3
# r→2(+1), g→2(+1), m→2(+1) → total = 3


# ==========================================================
# 7) Anagram Check — Single Map Decrement Pattern ⭐ BEST
#    → Increment for string A, decrement for string B.
#    → All values must reach 0 if truly anagrams.
#    → Better than two-map compare; only one dict needed.
# ==========================================================
def are_anagrams(a, b):
    """Return True if a and b are anagrams (same chars, same counts)."""
    if len(a) != len(b):
        return False

    freq = {}
    for ch in a:
        freq[ch] = freq.get(ch, 0) + 1          # +1 for every char in A

    for ch in b:
        if ch not in freq or freq[ch] == 0:
            return False                         # char missing or over-used
        freq[ch] -= 1                            # -1 for every char in B

    return True                                  # all counts cancelled to 0

print("\n--- 7) Anagram Check (Single Map Decrement) ---")
print("Input : 'listen', 'silent'")
print("Output:", are_anagrams("listen", "silent"))     # Output: True

print("Input : 'hello', 'world'  →  Output:", are_anagrams("hello", "world"))   # Output: False
print("Input : 'rat', 'car'      →  Output:", are_anagrams("rat", "car"))        # Output: False
#
# TRICK: Same length + same char counts = anagram.
#   'listen' and 'silent' both have l:1 i:1 s:1 t:1 e:1 n:1  ✓


# ==========================================================
# 8) Permutation of Palindrome
#    → A string can form a palindrome iff AT MOST 1 char has odd frequency.
#    → Even-freq chars go on both sides; one odd-freq char goes in the middle.
# ==========================================================
def is_permutation_of_palindrome(s):
    """Return True if any permutation of s can be a palindrome."""
    freq = {}
    for ch in s:
        if ch == " ":
            continue
        ch = ch.lower()
        freq[ch] = freq.get(ch, 0) + 1

    odd_count = sum(1 for ch in freq if freq[ch] % 2 != 0)
    return odd_count <= 1

print("\n--- 8) Permutation of Palindrome ---")
print("Input : 'Tact Coa'")
print("Output:", is_permutation_of_palindrome("Tact Coa"), "→ can form 'taco cat'")  # Output: True
#
# freq (ignore spaces, lowercase): t:2, a:2, c:2, o:1
#   Only 'o' has odd count → 1 odd ≤ 1 → True  ✓
#   Palindrome: t-a-c-o-c-a-t  (taco cat)

print("Input : 'racecar'  →  Output:", is_permutation_of_palindrome("racecar"))  # Output: True
print("Input : 'hello'    →  Output:", is_permutation_of_palindrome("hello"))     # Output: False
# h:1 e:1 l:2 o:1 → 3 odd counts → False


# ==========================================================
# 9) Group Anagrams
#    → Use a frequency-count tuple as the key (avoids sorting O(k log k)).
#    → All anagrams produce the same 26-element count signature.
# ==========================================================
def group_anagrams(words):
    """Group words that are anagrams of each other."""
    groups = {}
    for w in words:
        sig = [0] * 26
        for ch in w:
            idx = ord(ch) - ord('a')
            if 0 <= idx < 26:
                sig[idx] += 1
        key = tuple(sig)                         # e.g. "eat","tea","ate" → same key

        if key not in groups:
            groups[key] = [w]
        else:
            groups[key].append(w)

    return list(groups.values())

print("\n--- 9) Group Anagrams ---")
words9 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("Input :", words9)
print("Output:", group_anagrams(words9))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
#
# KEY INSIGHT:
#   "eat", "tea", "ate" → all have e:1, a:1, t:1 → same signature → same group
#   "tan", "nat"        → a:1, n:1, t:1            → same signature → same group
#   "bat"               → b:1, a:1, t:1            → unique         → own group


# ==========================================================
# 10) Most Frequent Character
#     → Single pass to build freq, single pass to find max.
#     → O(n) — no sorting needed.
# ==========================================================
def most_frequent_char(s):
    """Return (char, count) of the most frequent character."""
    if not s:
        return None, 0

    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    best_char = max(freq, key=lambda c: freq[c])
    return best_char, freq[best_char]

print("\n--- 10) Most Frequent Character ---")
print("Input : 'programming'")
print("Output:", most_frequent_char("programming"))    # Output: ('r', 2)
#
# freq: p:1 r:2 o:1 g:2 a:1 m:2 i:1 n:1
#   r, g, m all tie at count=2 → first max found is 'r'

print("Input : 'mississippi'  →  Output:", most_frequent_char("mississippi"))  # Output: ('s', 4) or ('i', 4)


# ==========================================================
# 11) K Most Frequent Elements — Bucket Sort Approach ⭐
#     → Instead of heap/sorting (O(n log n)), use bucket sort O(n).
#     → Bucket index = frequency; scan buckets from high to low.
# ==========================================================
def k_most_frequent(nums, k):
    """Return k elements with highest frequency using bucket sort."""
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1

    # bucket[i] = list of numbers that appear exactly i times
    buckets = [[] for _ in range(len(nums) + 1)]
    for x in freq:
        buckets[freq[x]].append(x)

    result = []
    for count in range(len(buckets) - 1, 0, -1):   # scan high → low frequency
        for x in buckets[count]:
            result.append(x)
            if len(result) == k:
                return result
    return result

print("\n--- 11) K Most Frequent Elements (Bucket Sort) ---")
nums11 = [1, 1, 1, 2, 2, 3]
print("Input : [1, 1, 1, 2, 2, 3],  k=2")
print("Output:", k_most_frequent(nums11, 2))    # Output: [1, 2]
#
# freq: {1:3, 2:2, 3:1}
# buckets[3]=[1], buckets[2]=[2], buckets[1]=[3]
# Scan from end: take 1 (count=3), take 2 (count=2) → [1, 2]  ✓

print("Input : [4,4,4,6,6,7,7,7,7],  k=2  →  Output:", k_most_frequent([4,4,4,6,6,7,7,7,7], 2))  # Output: [7, 4]


# ==========================================================
# 12) Same Frequency in Two Strings
#     → Identical to anagram check — same chars, same counts.
#     → Decrement pattern: works for any two strings.
# ==========================================================
def same_frequency_in_two_strings(a, b):
    """Return True if both strings have identical character frequencies."""
    if len(a) != len(b):
        return False

    freq = {}
    for ch in a:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in b:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1

    return True

print("\n--- 12) Same Frequency in Two Strings ---")
print("Input : 'aabbcc', 'baccab'")
print("Output:", same_frequency_in_two_strings("aabbcc", "baccab"))  # Output: True
#
# 'aabbcc': a:2 b:2 c:2
# 'baccab': b:2 a:2 c:2  → same frequencies → True  ✓

print("Input : 'abc', 'aab'  →  Output:", same_frequency_in_two_strings("abc", "aab"))  # Output: False


# ==========================================================
# 13) Find Missing Number in Range [0..n]
#     → Given n numbers from 0..n with exactly one missing.
#     → Hash map presence check: O(n) time & space.
#     → BONUS: Math trick — expected_sum - actual_sum = missing (O(1) space).
# ==========================================================
def find_missing_number(nums):
    """Return the missing number from range [0..len(nums)]."""
    n = len(nums)
    present = {x: 1 for x in nums}

    for val in range(n + 1):
        if val not in present:
            return val
    return None

def find_missing_number_math(nums):
    """O(1) space using sum formula: n*(n+1)//2 - sum(nums)."""
    n = len(nums)
    expected = n * (n + 1) // 2
    return expected - sum(nums)

print("\n--- 13) Find Missing Number in [0..n] ---")
nums13 = [3, 0, 1]
print("Input : [3, 0, 1]")
print("Output (hash map):", find_missing_number(nums13))       # Output: 2
print("Output (math)    :", find_missing_number_math(nums13))  # Output: 2
#
# Range should be [0,1,2,3]. Missing = 2.
# Math: expected = 3*4//2 = 6; actual = 3+0+1 = 4; missing = 6-4 = 2  ✓

print("Input : [9,6,4,2,3,5,7,0,1]  →  Output:", find_missing_number([9,6,4,2,3,5,7,0,1]))  # Output: 8


# ==========================================================
# 14) Intersection of Two Lists (with duplicate counts)
#     → Include an element as many times as it appears in BOTH lists.
#     → Freq map on A, then consume counts as we scan B.
# ==========================================================
def intersection_with_counts(a, b):
    """Return intersection keeping duplicate counts from both lists."""
    freq = {}
    for x in a:
        freq[x] = freq.get(x, 0) + 1

    out = []
    for x in b:
        if x in freq and freq[x] > 0:
            out.append(x)
            freq[x] -= 1                         # consume one occurrence
    return out

print("\n--- 14) Intersection with Counts ---")
a14 = [1, 2, 2, 1]
b14 = [2, 2]
print("Input : [1, 2, 2, 1]  &  [2, 2]")
print("Output:", intersection_with_counts(a14, b14))   # Output: [2, 2]
#
# freq(A): {1:2, 2:2}
# Scan B: 2 → in freq (count=2) → add, freq[2]=1
#          2 → in freq (count=1) → add, freq[2]=0
# Result: [2, 2]  ✓

print("Input : [4,9,5] & [9,4,9,8,4]  →  Output:", intersection_with_counts([4,9,5],[9,4,9,8,4]))  # Output: [9, 4]


# ==========================================================
# 15) Min Deletions to Make Two Strings Anagrams
#     → Delete chars from EITHER string until they're anagrams.
#     → Use +1/-1 trick: surplus in A or deficit in B = deletions.
# ==========================================================
def min_deletions_to_make_anagrams(a, b):
    """Return min total deletions to make a and b anagrams of each other."""
    freq = {}
    for ch in a:
        freq[ch] = freq.get(ch, 0) + 1          # +1 for chars in A

    for ch in b:
        freq[ch] = freq.get(ch, 0) - 1          # -1 for chars in B

    # sum of all absolute differences = total deletions needed
    return sum(abs(v) for v in freq.values())

print("\n--- 15) Min Deletions to Make Anagrams ---")
print("Input : 'cde', 'abc'")
print("Output:", min_deletions_to_make_anagrams("cde", "abc"))  # Output: 4
#
# freq after both passes: a:-1, b:-1, c:0, d:+1, e:+1
#   |−1|+|−1|+|0|+|1|+|1| = 4 deletions
# Delete 'a','b' from "abc"  and  'd','e' from "cde"  → both become "c"  ✓

print("Input : 'fcrxzwscanmligyxyvym', 'jxwtrhvujlmktgjxycfv'")
print("Output:", min_deletions_to_make_anagrams("fcrxzwscanmligyxyvym", "jxwtrhvujlmktgjxycfv"))  # Output: 30


# ==========================================================
# INTERVIEW CHEAT SHEET
# ==========================================================
print("""
╔══════════════════════════════════════════════════════════════╗
║              FREQUENCY MAP — INTERVIEW CHEAT SHEET           ║
╠══════════════════════════════════════════════════════════════╣
║  Problem                     Pattern Used          Time      ║
║  ─────────────────────────────────────────────────────────   ║
║  Char frequency              freq[ch]++             O(n)     ║
║  First non-repeating         2-pass, find freq==1   O(n)     ║
║  First repeating             seen-set, early exit   O(n)     ║
║  All repeating               freq > 1 filter        O(n)     ║
║  Remove duplicates           seen-set, preserve ord O(n)     ║
║  Count duplicates            Σ(freq-1)              O(n)     ║
║  Anagram check               +1/-1 decrement        O(n)     ║
║  Palindrome permutation      count odd freqs ≤ 1    O(n)     ║
║  Group anagrams              freq-tuple as key       O(n·k)  ║
║  Most frequent char          single pass max        O(n)     ║
║  K most frequent             bucket sort            O(n)     ║
║  Same freq two strings       +1/-1 decrement        O(n)     ║
║  Missing number              presence map / math    O(n)     ║
║  Intersection w/ counts      freq map + consume     O(n)     ║
║  Min deletions → anagram     |surplus| + |deficit|  O(n)     ║
╚══════════════════════════════════════════════════════════════╝
""")
