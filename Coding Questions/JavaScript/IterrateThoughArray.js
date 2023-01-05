// Ways to itterate through an array
// https://stackoverflow.com/questions/3010840/loop-through-an-array-in-javascript

// Three main options:

// 1- for (var i = 0; i < xs.length; i++) { console.log(xs[i]); }
// 2- arr.forEach((x, i) => console.log(x));
// 3- for (const x of xs) { console.log(x); }

// == for Loop ==

const array = ["one", "two", "three", "four", "five"];

for (var i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}

// Pros

// 1. Works on every environment
// 2. You can use break and continue flow control statements

// Cons

// 1. Too verbose
// 2. Imperative
// 3. Easy to have off-by-one errors (sometimes also called a fence post error)

// == for Each ==

const array2 = ["one", "two", "three", "four", "five"];

array2.forEach(function (item, index, array) {
  console.log(item, index, array);
});

// Pros

// 1. Very short and succinct.
// 2. Declarative

// Cons

// 1. Cannot use break / continue
// 2. "forEach does not wait for promises. Make sure you are aware of the implications 
//     while using promises (or async functions) as forEach callback."

// filter

array
  .filter((item) => item.condition < 10)
  .forEach((item) => console.log(item));


// Anti-Pattern [map]

const numbers = [1,2,3,4,5], doubled = [];

numbers.forEach((n, i) => { doubled[i] = n * 2 });


// map()

const numbers1 = [1,2,3,4,5];
const doubled1 = numbers.map(n => n * 2);

console.log(doubled1);

// Anti-Pattern [reduce]

const numbers2 = [1,2,3,4,5];
const sum = 0;
numbers2.forEach(num => { sum += num });

// reduce()

const numbers3 = [1,2,3,4,5];
const sum1 = numbers3.reduce((total, n) => total + n, 0);

console.log(sum1);

// == ES6 for-of == 

let colors = ['red', 'green', 'blue'];
for (const color of colors){
    console.log(color);
}

// This statement works for any kind of iterable object and also for generators 
// (any object that has a \[Symbol.iterator\] property).

// Pros

// 1. It can iterate over a large variety of objects.
// 2. Can use normal flow control statements (break / continue).
// 3. Useful to iterate serially asynchronous values.

// Cons

// 1. If you are targeting older browsers, the transpiled output might surprise you.
// 2. for iterating arrays for-in should be avoided, that statement is meant to enumerate object properties.
// It shouldn't be used for array-like objects because:
//      -The order of iteration is not guaranteed; the array indexes may not be visited in numeric order.
//      -Inherited properties are also enumerated.


// The for-in statement, is there to enumerate object properties, for example:

var obj = {
    "a": 1,
    "b": 2,
    "c": 3
};

for (var prop in obj) {
    if (obj.hasOwnProperty(prop)) {
        // or if (Object.prototype.hasOwnProperty.call(obj,prop)) for safety...
        console.log("prop: " + prop + " value: " + obj[prop])
    }
}