// Check how many times an Element appears in an Array


// Simple ways

let arr = ["David","Walsh","David","Tania","Lucretius"];
const count = arr.filter(x=>x==="David").length // => 2
console.log(count) // => 2

// simple way 2

let arr5 = ["David","Walsh","David","Tania","Lucretius"];
const count5 = arr.reduce((a, x) => (x == 'David') ? a + 1 : a, 0) 
console.log(count5) // => 2



// ✅ Using forEach()
const arr1 = ["a", "b", "a", "a"];

let count1 = 0;

arr.forEach((element) => {
  if (element === "a") {
    count1 += 1;
  }
});

console.log(count1); // 👉️ 3


// ✅ Using reduce()

const arr2 = ['a', 'b', 'a', 'a'];

const count2 = arr2.reduce((accumulator, value) => {
  accumulator[value] = ++accumulator[value] || 1;

  return accumulator;
}, {});

console.log(count2); // 👉️ { a: 3, b: 1 }

console.log(count2.a); // 👉️ 3
console.log(count2.b); // 👉️ 1


// Uisng Filter()

const arr3 = ['a', 'b', 'a', 'a'];

const count3 = arr.filter(element => {
  return element === 'a';
}).length;

console.log(count3); // 👉️ 3

// Using for...of loop

const arr4 = ['a', 'b', 'a', 'a'];

let count4 = 0;

for (const element of arr) {
  if (element === 'a') {
    count4 += 1;
  }
}

console.log(count4); // 👉️ 3