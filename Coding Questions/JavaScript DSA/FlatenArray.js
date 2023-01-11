// recursion and flat method


// By flat Method:

const arr4 = [1, 2, [3, 4, [5, 6, [7, 8, [9, 10]]]]];
arr4.flat(Infinity);
// [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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