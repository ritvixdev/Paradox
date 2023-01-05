// Check weather a string is pallindrome or not

// For Loop

str = 'malayalam';

const palindrome = (str) => {
  var len = str.length;
  var mid = Math.floor(len / 2);

  for (var i = 0; i < mid; i++) {
    if (str[i] !== str[len - 1 - i]) {
      return false;
    }
  }

  return true;
};

console.log(palindrome(str));


// Build in method

str = 'malayalam';

const isPalindrome =  (str) => {
  if (str == str.split('').reverse().join('')) {
      console.log(' is palindrome.');
  }
  else {
      console.log(' is not palindrome.');
  }
}

isPalindrome(str)