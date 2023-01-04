// Count the number of times a same value appears in a javascript array

// By Reduce:

var arr = ['apple', 'mango', 'apple', 'orange', 'mango', 'mango'];

const count = arr.reduce((acc, curr) => {
  acc[curr] = ++acc[curr] || 1;
  return acc;
}, {});

console.log(count); // {apple: 2, mango: 3, orange: 1}
console.log(count.apple); // 2
console.log(count.mango); // 3

//

