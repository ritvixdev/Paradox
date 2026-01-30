// Check Whether Two Strings Are Anagram Of Each Other

// | Criteria               | Single Map | Two Maps |
// | -----------------      | ---------- | -------- |
// | Performance       | ⭐⭐⭐⭐⭐      | ⭐⭐⭐      |
// | Reusable patterns | ⭐⭐⭐⭐⭐      | ⭐⭐       |
// | Interview depth   | ⭐⭐⭐⭐⭐      | ⭐⭐⭐      |
// | Advanced problems | ⭐⭐⭐⭐⭐      | ⭐        |
// | Beginner clarity  | ⭐⭐⭐        | ⭐⭐⭐⭐     |

// Remember
// Frequency problems → O(n) time
// Sorting problems → O(n log n) time

// Method	          Time	      Space	               Notes
// Single map	      O(n)	      O(1) / O(n)	    ⭐Best
// Two maps	        O(n)	      O(n)	              More memory


// Single Frequency Map (DECREMENT pattern) ⭐⭐⭐⭐⭐

// Time Complexit = O(n)

str1 = 'listen';
str2 = 'silent';

const anagram = (str1, str2) => {
  if (str1.length !== str2.length) return false;

  const count = {};

  for (let i = 0; i < str1.length; i++) {
    const ch = str1[i];
    count[ch] = (count[ch] || 0) + 1;
  }

  for (let i = 0; i < str2.length; i++) {
    const ch = str2[i];
    if (!count[ch]) return false;
    count[ch]--;
  }

  return true;
};

// Two Objects Comparison ⭐⭐⭐

str1 = 'listen';
str2 = 'silent';

const findAnagram = (str1, str2) => {
  if (str1.length !== str2.length) return false;

  let obj1 = {}, obj2 = {};

  for (let ch of str1) {
    obj1[ch] = (obj1[ch] || 0) + 1;
  }

  for (let ch of str2) {
    obj2[ch] = (obj2[ch] || 0) + 1;
  }

  for (let key in obj1) {
    if (obj1[key] !== obj2[key]) return false;
  }

  return true;
};

  
// Explain :

// Single Frequency Map (Increment–Decrement)

const anagram2 = (str1, str2) => {

  // 1️⃣ If lengths are different, they can never be anagrams
  // Example: "abc" and "ab" → impossible
  if (str1.length !== str2.length) return false;

  // 2️⃣ Create an empty object to store character counts
  // This will work like a frequency table
  const count = {};

  // 3️⃣ Loop through the FIRST string
  // Goal: count how many times each character appears
  for (let i = 0; i < str1.length; i++) {

    // Get the current character
    const ch = str1[i];

    // If character already exists → increment count
    // Else → initialize with 1
    count[ch] = (count[ch] || 0) + 1;
  }

  /*
    Example after this loop for "listen":
    {
      l: 1,
      i: 1,
      s: 1,
      t: 1,
      e: 1,
      n: 1
    }
  */

  // 4️⃣ Loop through the SECOND string
  // Goal: "cancel out" the characters from the first string
  for (let i = 0; i < str2.length; i++) {

    const ch = str2[i];

    // ❌ If character doesn't exist or count is already 0
    // it means second string has extra or mismatched character
    if (!count[ch]) return false;

    // Reduce the count because this character is matched
    count[ch]--;
  }

  /*
    After processing "silent", all counts become:
    {
      l: 0,
      i: 0,
      s: 0,
      t: 0,
      e: 0,
      n: 0
    }
  */

  // 5️⃣ If all characters cancel out correctly → anagram
  return true;
};


// Two Frequency Objects (Compare Pattern)

const findAnagram2 = (str1, str2) => {

  // 1️⃣ Different lengths → not anagrams
  if (str1.length !== str2.length) return false;

  // 2️⃣ Create two objects to store character frequencies
  let obj1 = {};
  let obj2 = {};

  // 3️⃣ Count characters in the FIRST string
  for (let ch of str1) {
    obj1[ch] = (obj1[ch] || 0) + 1;
  }

  /*
    obj1 for "listen":
    {
      l: 1,
      i: 1,
      s: 1,
      t: 1,
      e: 1,
      n: 1
    }
  */

  // 4️⃣ Count characters in the SECOND string
  for (let ch of str2) {
    obj2[ch] = (obj2[ch] || 0) + 1;
  }

  /*
    obj2 for "silent":
    {
      s: 1,
      i: 1,
      l: 1,
      e: 1,
      n: 1,
      t: 1
    }
  */

  // 5️⃣ Compare both frequency objects
  for (let key in obj1) {

    // If a character count differs → not an anagram
    if (obj1[key] !== obj2[key]) {
      return false;
    }
  }

  // 6️⃣ All counts match → anagram
  return true;
};
