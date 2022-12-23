//interview example for Currying

const addCurry = (a) => {
  return (b) => {
    return (c) => {
      return a + b + c;
    };
  };
};

console.log(addCurry(1)(2)(3));

// by normal function

const add = (a, b, c) => {
  return a + b + c;
};

console.log(add(1, 2, 3));

// Advance Currying

const curry = (fn) => {
  return (curried = (...args) => {
    if (fn.length !== args.length) {
      return curried.bind(null, ...args);
    }
    return fn(...args);
  });
};
const totalNum = (x, y, z) => {
  return x + y + z;
};
const curriedTotal = curry(totalNum);
console.log(curriedTotal(10)(20)(30));

// Modern Currying with ES6

const sendRequest = (greet) => (name) => (message) =>
  console.log(`${greet} ${name}, ${message}`);
sendRequest("Hello")("John")("Please can you add me to your Linkedin network?");
