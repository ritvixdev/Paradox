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


// second method
var isAnagramUsingTwoMaps = function (str1, str2) {
  if (str1.length !== str2.length) return false;

  const freq1 = {};
  const freq2 = {};

  for (let i = 0; i < str1.length; i++) {
    const ch = str1[i];
    if (freq1[ch] === undefined) {
      freq1[ch] = 1;
    } else {
      freq1[ch]++;
    }
  }

  for (let i = 0; i < str2.length; i++) {
    const ch = str2[i];
    if (freq2[ch] === undefined) {
      freq2[ch] = 1;
    } else {
      freq2[ch]++;
    }
  }

  for (let key in freq1) {
    if (freq1[key] !== freq2[key]) {
      return false;
    }
  }

  return true;
};

console.log(isAnagramUsingTwoMaps('listen', 'silent'));



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