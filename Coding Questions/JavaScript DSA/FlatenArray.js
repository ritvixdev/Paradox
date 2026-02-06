// recursion and flat method

// important
typeof 10          // "number"
typeof "hello"     // "string"
typeof true        // "boolean"
typeof undefined   // "undefined"
typeof function(){}// "function"
typeof {}          // "object"
typeof []          // "object"  ← IMPORTANT
typeof null        // "object"  ← JS BUG


// By flat Method:

const arr4 = [1, 2, [3, 4, [5, 6, [7, 8, [9, 10]]]]];
arr4.flat(Infinity);
// [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// By recrusion without using javascript methods

function flatten(arr, result = []) {
  for (let i = 0; i < arr.length; i++) {
    if(typeof arr[i] === "object" && arr[i] !== null) {
      flatten(arr[i], result)
    } else {
      result.push(arr[i])
    }
  }
  return result
}

console.log(flatten(arr4))

// By recursion chatGPT:

function flattenArray(arr) {
  let flatArr = [];
  for (let i = 0; i < arr.length; i++) {
    if (Array.isArray(arr[i])) {
      flatArr = flatArr.concat(flattenArray(arr[i]));
    } else {
      flatArr.push(arr[i]);
    }
  }
  return flatArr;
}

let arr = [1, [2, 3], [4, [5, 6]]];
let flatArr = flattenArray(arr);
console.log(flatArr);

// Program Explain:

// This code defines a recursive function flattenArray() that takes an array 
// as an argument and returns a new, flattened array. It does this by iterating
// over the elements in the array and adding them to a new array. If an element 
// is itself an array, it calls itself recursively to flatten the sub-array before 
// adding its elements to the new array.

// recursion and without using build in methods

const arr5 = [1, 2, [3, 4, [5, 6, [7, 8, [9, 10]]]]];

function flattenArray(arr) {
  let result = [];

  for (let i = 0; i < arr.length; i++) {
    if (typeof arr[i] === "object") {
      const flat = flattenArray(arr[i]);
      for (let j = 0; j < flat.length; j++) {
        result.push(flat[j]);
      }
    } else {
      result.push(arr[i]);
    }
  }

  return result;
}

console.log(flattenArray(arr5));
