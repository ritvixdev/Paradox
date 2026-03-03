"""
Palindrome Patterns (Interview Pack) - Python
Author: Suvam Das

Updated Version:
✅ Multiple palindrome interview variants
✅ Output shown immediately after each solution
✅ Expected output written as inline comments
✅ No main block
"""


# ==========================================================
# 1) Basic Palindrome Check (Two Pointer Method) ⭐⭐⭐⭐⭐
# ==========================================================
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


print("1) is_palindrome:", is_palindrome("madam"))
# Expected: True

print("1) is_palindrome:", is_palindrome("hello"))
# Expected: False


# ==========================================================
# 2) Palindrome Using Reverse (Slicing)
# ==========================================================
def is_palindrome_reverse(s):
    return s == s[::-1]


print("2) is_palindrome_reverse:", is_palindrome_reverse("racecar"))
# Expected: True


# ==========================================================
# 3) Palindrome Ignoring Case and Spaces
# ==========================================================
def is_palindrome_ignore_case_space(s):
    cleaned = ""
    for ch in s:
        if ch != " ":
            cleaned += ch.lower()

    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True


print("3) is_palindrome_ignore_case_space:", is_palindrome_ignore_case_space("Taco Cat"))
# Expected: True


# ==========================================================
# 4) Palindrome Number (Without Converting to String)
# ==========================================================
def is_palindrome_number(num):
    if num < 0:
        return False

    original = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    return original == reversed_num


print("4) is_palindrome_number:", is_palindrome_number(121))
# Expected: True

print("4) is_palindrome_number:", is_palindrome_number(123))
# Expected: False


# ==========================================================
# 5) Longest Palindromic Substring (Brute Force O(n^3))
# ==========================================================
def longest_palindrome_substring(s):
    max_len = 0
    result = ""

    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = ""
            for k in range(i, j + 1):
                substring += s[k]

            if substring == substring[::-1] and len(substring) > max_len:
                max_len = len(substring)
                result = substring

    return result


print("5) longest_palindrome_substring:", longest_palindrome_substring("babad"))
# Expected: "bab" or "aba"


# ==========================================================
# 6) Count Palindromic Substrings (Expand Around Center)
# ==========================================================
def count_palindromes(s):
    count = 0

    for center in range(len(s)):
        # Odd length
        left = center
        right = center
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

        # Even length
        left = center
        right = center + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    return count


print("6) count_palindromes:", count_palindromes("aaa"))
# Expected: 6  (a,a,a,aa,aa,aaa)


# ==========================================================
# 7) Check If String Can Become Palindrome After One Removal
# ==========================================================
def valid_palindrome_with_one_removal(s):
    def is_sub_palindrome(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return is_sub_palindrome(left + 1, right) or is_sub_palindrome(left, right - 1)
        left += 1
        right -= 1

    return True


print("7) valid_palindrome_with_one_removal:", valid_palindrome_with_one_removal("abca"))
# Expected: True  (remove 'b' or 'c')
