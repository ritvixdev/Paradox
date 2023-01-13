// Code to predict output:

(function () {
  setTimeout(() => console.log(1), 2000);
  console.log(2);
  setTimeout(() => console.log(3), 0);
  console.log(4);
})(); // 2,4,3,1

// second Code:

for (var i = 0; i < 3; i++) {
  setTimeout(() => {
    console.log(i);
  }, i * 1000);
} // 3,3,3

// third code:

function checkAge(data) {
  if (data === { age: 18 }) {
    console.log("You are an adult!");
  } else if (data == { age: 18 }) {
    console.log("You are still an adult.");
  } else {
    console.log(`Hmm.. You don't have an age I guess`);
  }
}
checkAge({ age: 18 }); // Hmm.. You don't have an age I guess


// Explaination:

//The output of this code will be false.
// The reason for this is that the == operator compares the references 
// of the two objects, rather than their values. Even though obj1 and obj2 
// have the same properties with the same values, they are two separate objects 
// in memory and therefore have different references.

// In javascript, Objects and arrays are compared by reference, they are not primitive types. 
// To compare two objects or arrays by their values, you would have to write a function 
// to iterate through the properties and compare them. you can use JSON.stringify method 
// and compare the result or you can use lodash library method like isEqual().


console.log(JSON.stringify(obj1) === JSON.stringify(obj2))

// or

const isEqual = require('lodash').isEqual;
console.log(isEqual(obj1, obj2))

// Both of the above will return true

// Keep in mind that deep comparison like this could be slower than just checking 
// for references, so it's important to use it only when it's necessary.


// ==> Fourth Code:

let arr = [1,2,3,4,5]
let obj = {...arr}
console.log(obj) // {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}

// Explaination:

// The code you provided uses the spread operator (...) to create a new object that has the
// same properties as the array arr. The spread operator creates a new object with the elements
// of the array as properties, with the index of the element being the key and the element being the value.





