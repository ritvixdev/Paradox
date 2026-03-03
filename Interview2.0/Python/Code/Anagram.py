"""
Anagram Problem Variants
Author: Suvam Das
Description:
Different approaches to check whether two strings are anagrams.
All solutions avoid heavy Python built-in shortcuts like sorted() or Counter.
Time Complexity: O(n)
"""

# ==========================================================
# 1️⃣ Single Frequency Map (DECREMENT Pattern) ⭐⭐⭐⭐⭐
# ==========================================================

def is_anagram_single_map(str1, str2):
    """
    Best interview approach.
    Uses one dictionary and decrement pattern.
    """

    # Step 1: Length check
    if len(str1) != len(str2):
        return False

    freq = {}

    # Step 2: Count characters from first string
    for ch in str1:
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] += 1

    # Step 3: Decrement using second string
    for ch in str2:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1

    return True


# ==========================================================
# 2️⃣ Two Frequency Maps ⭐⭐⭐
# ==========================================================

def is_anagram_two_maps(str1, str2):
    """
    Beginner-friendly but uses more memory.
    """

    if len(str1) != len(str2):
        return False

    freq1 = {}
    freq2 = {}

    # Count for first string
    for ch in str1:
        if ch not in freq1:
            freq1[ch] = 1
        else:
            freq1[ch] += 1

    # Count for second string
    for ch in str2:
        if ch not in freq2:
            freq2[ch] = 1
        else:
            freq2[ch] += 1

    # Compare maps
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False

    return True


# ==========================================================
# 3️⃣ Cleaner Python Version (Still Manual)
# ==========================================================

def is_anagram_clean(str1, str2):
    """
    Cleaner syntax using dict.get()
    """

    if len(str1) != len(str2):
        return False

    freq = {}

    for ch in str1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in str2:
        if freq.get(ch, 0) == 0:
            return False
        freq[ch] -= 1

    return True


# ==========================================================
# 4️⃣ Single Loop Balanced Version (Advanced Variant)
# ==========================================================

def is_anagram_single_loop(str1, str2):
    """
    Increment and decrement in same loop.
    Slightly more advanced approach.
    """

    if len(str1) != len(str2):
        return False

    freq = {}

    for i in range(len(str1)):
        ch1 = str1[i]
        ch2 = str2[i]

        # Increment for first string
        if ch1 not in freq:
            freq[ch1] = 1
        else:
            freq[ch1] += 1

        # Decrement for second string
        if ch2 not in freq:
            freq[ch2] = -1
        else:
            freq[ch2] -= 1

    # Validate all values are zero
    for value in freq.values():
        if value != 0:
            return False

    return True


# ==========================================================
# Main Testing Block
# ==========================================================

if __name__ == "__main__":
    str1 = "listen"
    str2 = "silent"

    print("Single Map:", is_anagram_single_map(str1, str2))
    print("Two Maps:", is_anagram_two_maps(str1, str2))
    print("Clean Version:", is_anagram_clean(str1, str2))
    print("Single Loop:", is_anagram_single_loop(str1, str2))

# What is if __name__ == "__main__"?
# It ensures that certain code runs only when the file is executed directly, not when imported as a module. It is mainly used for test/demo execution.