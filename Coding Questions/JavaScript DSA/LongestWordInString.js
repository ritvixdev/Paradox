// Find the Longest Word in a String in JavaScript

// By For loop
 
str = 'Hello guys this is geeksforgeeks where students learn programming';

let longestWord = (string) => {
  let str = string.split(' ');
  let longest = 0;
  let longest_word = null;
  for (let i = 0; i < str.length; i++) {
    if (longest < str[i].length) {
      longest = str[i].length;
      longest_word = str[i];
    }
  }
  return longest_word;
};

console.log(longestWord(str)); // geeksforgeeks



