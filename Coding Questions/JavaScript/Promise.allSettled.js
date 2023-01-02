// Interview example for Promise.allSetteled()

const p1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    console.log("The first promise has resolved");
    resolve(10);
  }, 1 * 1000);
});

const p2 = new Promise((resolve, reject) => {
  setTimeout(() => {
    console.log("The second promise has rejected");
    reject(20);
  }, 2 * 1000);
});

Promise.allSettled([p1, p2]).then((result) => {
  console.log(result);
});

// ===> Defination Promise.allSetteled()

// The Promise is a JavaScript object which can be in three states pending, fulfilled or rejected. 

// The Promise.allSettled() method in JavaScript is used to get a promise when all inputs are 
// settled that is either fulfilled or rejected.


// ==== Promise.all vs Promise.allSetteled ====

// 1. In terms of rejecting promises:

// Promise.all() method rejects itself if any of the passed in promise input inside an array
//  is rejected. That is, this method will only run if and only if all the promises are 
// fulfilled or resolved successfully, otherwise, in the output, it would produce an error message.

// Promise.allSettled() method will not reject itself if any of the passed in promise input 
// inside an array is rejected. That is, this method will irrespective of any promise be in 
// the rejected state too.

// 2. In terms of their outputs:

// Promise.all() method returns an array as an output containing promise data inside several indexes.

// Promise.allSettled() method returns an array of objects and each of these objects further contains 
// two properties further status and value.
