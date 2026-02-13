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
    if(typeof arr[i] === "object" && arr[i] !== null && typeof arr[i].length === "number") {
      flatten(arr[i], result)
    } else {
      result.push(arr[i])
    }
  }
  return result
}

console.log(flatten(arr4))

// Program Explain:

// This code defines a recursive function flattenArray() that takes an array 
// as an argument and returns a new, flattened array. It does this by iterating
// over the elements in the array and adding them to a new array. If an element 
// is itself an array, it calls itself recursively to flatten the sub-array before 
// adding its elements to the new array.

function flatten(arr) {
  let result = [];

  for (let i = 0; i < arr.length; i++) {
    if (Array.isArray(arr[i])) {
      // Take the flattened sub-array and add its items to result
      result = result.concat(flatten(arr[i]));
      // or: result.push(...flatten(arr[i]));
    } else {
      result.push(arr[i]);
    }
  }
  return result;
}

console.log(flatten(arr4))
