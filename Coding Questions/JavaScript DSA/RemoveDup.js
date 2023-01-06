// Write a program to remove duplicate form Array

// By inbuilt methods:

const arr5 = [1, 2, 3, 4, 5, 1, 5, 4, 3];

const removeDupl = (arr) => {
  const result = [];
  let idx = 0;
  let tmp = {};

  for (let i = 0; i <= arr.length - 1; i++) {
    if (!tmp[arr[i]]) {
      tmp[arr[i]] = 1;
      result[idx] = arr[i];
      idx++;
    }
  }
  return result;
};

console.log(removeDupl(arr));

// By reduce()

var arr = ["apple", "mango", "apple", "orange", "mango", "mango"];

const removeDup = arr.reduce(function (acc, curr) {
  if (!acc.includes(curr)) {
    acc.push(curr);
  }
  return acc;
}, []);

console.log(removeDup);


// By Filter()

var arr = ["apple", "mango", "apple", "orange", "mango", "mango"];

const removeDuplicate = () => {
  return arr.filter((element, index) => arr.indexOf(element) === index);
};

console.log(removeDuplicate());


// By Set()

var arr = ["apple", "mango", "apple", "orange", "mango", "mango"];

const removeDuplicates = (arr) => {
  return [...new Set(arr)];
};

console.log(removeDuplicates());


// For Each()

var arr = ["apple", "mango", "apple", "orange", "mango", "mango"];

const removeDuplicat = (arr) => {
  var unique = [];
  arr.forEach((element) => {
    if (!unique.includes(element)) {
      unique.push(element);
    }
  });
  return unique;
};
console.log(removeDuplicat(arr));


// javascript ..of.. arr

const unique = (arr) => {
  const result = [];

  for (const item of arr) {
    // 👉 Option 1
    if (!result.includes(item)) {
      result.push(item);
    }

    // 👉 Option 2
    // if (result.indexOf(item) === -1) {
    //   result.push(item);
    // }
  }

  return result;
};
console.log(unique(arr));
