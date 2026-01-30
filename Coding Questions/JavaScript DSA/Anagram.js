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

var isAnagram = function (str1, str2) {
  if (str1.length !== str2.length) return false;

  const freq = {};

  for (let i = 0; i < str1.length; i++) {
    const ch = str1[i];

    if (freq[ch] === undefined) {
      freq[ch] = 1;
    } else {
      freq[ch]++;
    }
  }

  for (let i = 0; i < str2.length; i++) {
    const ch = str2[i];

    if (freq[ch] === undefined || freq[ch] === 0) {
      return false;
    }

    freq[ch]--;
  }

  return true;
};

console.log(isAnagram(str1,str2))





// Two Frequency Maps⭐⭐⭐

str1 = 'listen';
str2 = 'silent';

var isAnagramUsingTwoMaps = function (str1, str2) {
  if (str1.length !== str2.length) return false;

  const freq1 = {};
  const freq2 = {};

  for (let i = 0; i < str1.length; i++) {
    const ch = str1[i];
    freq1[ch] = (freq1[ch] || 0) + 1;
  }

  for (let i = 0; i < str2.length; i++) {
    const ch = str2[i];
    freq2[ch] = (freq2[ch] || 0) + 1;
  }

  for (let key in freq1) {
    if (freq1[key] !== freq2[key]) {
      return false;
    }
  }

  return true;
};

console.log(isAnagramUsingTwoMaps(str1,str2))

  
// Explain :

// Single Frequency Map (Increment–Decrement)

// Mental Map 
// COUNT → CANCEL → VALIDATE

var isAnagram = function (s, t) {

  // Step 1: Length mismatch → cannot be anagrams
  if (s.length !== t.length) return false;

  // Step 2: Create frequency map
  const freq = {};

  // Step 3: Count characters in first string
  for (let i = 0; i < s.length; i++) {
    const ch = s[i];

    if (freq[ch] === undefined) {
      freq[ch] = 1;
    } else {
      freq[ch]++;
    }
  }

  /*
    After processing "listen":
    {
      l: 1,
      i: 1,
      s: 1,
      t: 1,
      e: 1,
      n: 1
    }
  */

  // Step 4: Decrease counts using second string
  for (let i = 0; i < t.length; i++) {
    const ch = t[i];

    // If char missing or already exhausted → not anagram
    if (freq[ch] === undefined || freq[ch] === 0) {
      return false;
    }

    freq[ch]--;
  }

  // Step 5: All characters cancelled out
  return true;
};




// Two Frequency Objects (Compare Pattern)
var isAnagramUsingTwoMaps = function (s, t) {

  if (s.length !== t.length) return false;

  const freq1 = {};
  const freq2 = {};

  // Count characters in first string
  for (let ch of s) {
    freq1[ch] = (freq1[ch] || 0) + 1;
  }

  // Count characters in second string
  for (let ch of t) {
    freq2[ch] = (freq2[ch] || 0) + 1;
  }

  // Compare both maps
  for (let key in freq1) {
    if (freq1[key] !== freq2[key]) {
      return false;
    }
  }

  return true;
};
