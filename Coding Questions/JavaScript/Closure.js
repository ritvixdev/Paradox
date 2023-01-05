// interview example for closures
// https://www.freecodecamp.org/news/lets-learn-javascript-closures-66feb44f6a44/


const numberGenerator = () => {
  // Local “free” variable that ends up within the closure
  var num = 1;
  function checkNumber() {
    console.log(num);
  }
  num++;
  return checkNumber;
};

var number = numberGenerator();
number(); // 2


// Explaination:

// The function checkNumber doesn’t have any local variables of its own — however,
// it does have access to the variables within the outer function, numberGenerator,
// because of a closure.

// Therefore, it can use the variable num declared in numberGenerator to successfully 
// log it to the console even after numberGenerator has returned.


// === Definition:

// closure is created when a child function keep the environment of the parent
// scope even after the parent function has already executed

// === Simple definition:

// Closure means that an inner function always has access to the vars and parameters
// of its outer function, even after the outer function has returned.
// In JavaScript, every time a closure is created with the creation of a function.

// -The closure has three scope chains listed as follows:

// Access to its own scope.
// Access to the variables of the outer function.
// Access to the global variables.

// ==> When to use Closure?

// Closure is useful in hiding implementation detail in JavaScript.
// In other words, it can be useful to create private variables or functions.

// The following example shows how to create private functions & variable.

var counter = (function () {
  var privateCounter = 0;
  function changeBy(val) {
    privateCounter += val;
  }
  return {
    increment: function () {
      changeBy(1);
    },
    decrement: function () {
      changeBy(-1);
    },
    value: function () {
      return privateCounter;
    },
  };
})();

console.log(counter.value()); // 0
counter.increment();
counter.increment();
console.log(counter.value()); // 2
counter.decrement();
console.log(counter.value()); // 1
