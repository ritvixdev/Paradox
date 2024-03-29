// Check Whether Two Strings Are Anagram Of Each Other


// For Loop

str1 = 'listen';
str2 = 'silent';

const anagram = (str1, str2) => {
  if (str1.length !== str2.length) {
    return false;
  }
  const result = {};
  for (let i = 0; i < str1.length; i++) {
    let char = str1[i];
    result[char] = result[char] ? (result[char] += 1) : (result[char] = 1);
  }

  for (let i = 0; i < str2.length; i++) {
    let char = str2[i];
    if (!result[char]) {
      return false;
    } else {
      result[char] = -1;
    }
  }
  return true;
}

console.log(anagram(str1, str2));

// Key and object

str1 = 'listen';
str2 = 'silent';

const findAnagram = (str1, str2) => {
    let obj1 = {},
      obj2 = {};
  
    for (let item of str1) {
      obj1[item] = (obj1[item] || 0) + 1;
    }
  
    for (let item2 of str2) {
      obj2[item2] = (obj2[item2] || 0) + 1;
    }
  
    for (let key in obj1) {
      if (!obj2[key]) {
        return false;
      }
  
      if (obj1[key] !== obj2[key]) {
        return false;
      }
    }
  
    return true;
  };
  console.log(findAnagram(str1, str2));
  



// In build method

a = 'listen';
b = 'silent';

const checkStringsAnagram = (a, b) => {
  let len1 = a.length;
  let len2 = b.length;
  if (len1 !== len2) {
    console.log('Invalid Input');
    return;
  }
  let str1 = a.split('').sort().join('');
  let str2 = b.split('').sort().join('');
  if (str1 === str2) {
    console.log('True');
  } else {
    console.log('False');
  }
};
checkStringsAnagram(a, b);

