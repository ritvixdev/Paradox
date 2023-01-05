// Reverse a String in JavaScript

// ==> Reverse with In-Built Function:-

function reverseString(str) {
  return str.split("").reverse().join("");
}
reverseString("hello");

// Explain:

function reverseString(str) {
  // Step 1. Use the split() method to return a new array
  var splitString = str.split(""); // var splitString = "hello".split("");
  // ["h", "e", "l", "l", "o"]

  // Step 2. Use the reverse() method to reverse the new created array
  var reverseArray = splitString.reverse(); // var reverseArray = ["h", "e", "l", "l", "o"].reverse();
  // ["o", "l", "l", "e", "h"]

  // Step 3. Use the join() method to join all elements of the array into a string
  var joinArray = reverseArray.join(""); // var joinArray = ["o", "l", "l", "e", "h"].join("");
  // "olleh"

  //Step 4. Return the reversed string
  return joinArray; // "olleh"
}

reverseString("hello");

// ==> Reverse a String With a Decrementing For Loop

function reverseString(str) {
  var newString = "";
  for (var i = str.length - 1; i >= 0; i--) {
    newString += str[i];
  }
  return newString;
}
reverseString("hello");

// ==> Reverse a String With Recursion

function reverseString(str) {
    if (str === "")
      return "";
    else
      return reverseString(str.substr(1)) + str.charAt(0);
  }
  reverseString("hello");

// Explain:

// The substr() method returns the characters in a string beginning at the 
// specified location through the specified number of characters.

// "hello".substr(1); // "ello"


// The charAt() method returns the specified character from a string.

// "hello".charAt(0); // "h"
