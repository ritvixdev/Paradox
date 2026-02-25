# JavaScript Interview Preparation Guide

> **Covers:** Basic → Intermediate → Advanced  
> All key concepts, definitions, code examples, and common interview questions grouped by topic.

---

## Table of Contents

| # | Topic |
|---|-------|
| 1 | [Variables, Scope & Hoisting](#1-variables-scope--hoisting) |
| 2 | [Data Types & Type Coercion](#2-data-types--type-coercion) |
| 3 | [Operators](#3-operators) |
| 4 | [Control Flow](#4-control-flow) |
| 5 | [Functions](#5-functions) |
| 6 | [Arrays & Array Methods](#6-arrays--array-methods) |
| 7 | [Objects & OOP](#7-objects--oop) |
| 8 | [Prototypes & Inheritance](#8-prototypes--inheritance) |
| 9 | [Closures & Lexical Scope](#9-closures--lexical-scope) |
| 10 | [Higher-Order Functions, Callbacks & Currying](#10-higher-order-functions-callbacks--currying) |
| 11 | [The `this` Keyword, Call, Apply & Bind](#11-the-this-keyword-call-apply--bind) |
| 12 | [Spread, Rest & Destructuring](#12-spread-rest--destructuring) |
| 13 | [ES6+ Features](#13-es6-features) |
| 14 | [DOM & Browser Events](#14-dom--browser-events) |
| 15 | [Asynchronous JavaScript](#15-asynchronous-javascript) |
| 16 | [Promises & Async/Await](#16-promises--asyncawait) |
| 17 | [Error Handling](#17-error-handling) |
| 18 | [Set, Map & WeakMap/WeakSet](#18-set-map--weakmapweakset) |
| 19 | [Memory Management & Performance](#19-memory-management--performance) |
| 20 | [Browser APIs & Web Storage](#20-browser-apis--web-storage) |
| 21 | [Modules](#21-modules) |
| 22 | [Design Patterns](#22-design-patterns) |
| 23 | [Security](#23-security) |
| 24 | [Interview Q&A — Tricky Concepts](#24-interview-qa--tricky-concepts) |

---

## 1. Variables, Scope & Hoisting

### `var`, `let`, `const` — Key Differences

| Feature | `var` | `let` | `const` |
|---------|-------|-------|---------|
| Scope | Function-scoped | Block-scoped | Block-scoped |
| Hoisting | Yes (initialized as `undefined`) | Yes (but in TDZ — not accessible) | Yes (but in TDZ — not accessible) |
| Re-declaration | Allowed | Not allowed | Not allowed |
| Re-assignment | Allowed | Allowed | Not allowed |
| Global object property | Yes (`window.x`) | No | No |

```js
// var is function-scoped
function example() {
  if (true) {
    var x = 10;
  }
  console.log(x); // Output: 10 (accessible outside block)
}

// let is block-scoped
function example2() {
  if (true) {
    let y = 20;
  }
  console.log(y); // ReferenceError: y is not defined
}

// const cannot be reassigned
const PI = 3.14;
PI = 3; // TypeError: Assignment to constant variable
```

---

### Hoisting

**Definition:** JavaScript moves function and variable **declarations** to the top of their scope during the compilation phase — before code runs.

- `var` declarations are hoisted and initialized as `undefined`
- `let` and `const` are hoisted but placed in the **Temporal Dead Zone (TDZ)** — accessing them before declaration throws a `ReferenceError`
- Function **declarations** are fully hoisted (both declaration and body)
- Function **expressions** are NOT fully hoisted (only the variable, not the function)

```js
console.log(a); // Output: undefined  (var is hoisted)
var a = 5;

console.log(b); // ReferenceError  (let is in TDZ)
let b = 10;

// Function declaration — fully hoisted
greet(); // Output: "Hello"
function greet() { console.log("Hello"); }

// Function expression — NOT hoisted
sayHi(); // TypeError: sayHi is not a function
var sayHi = function() { console.log("Hi"); };
```

---

### Scope

**Definition:** Scope determines where variables are defined and where they can be accessed.

- **Global Scope** — Variables accessible everywhere
- **Function Scope** — Variables declared inside a function, only accessible within it
- **Block Scope** — Variables declared with `let`/`const` inside `{}`, only accessible within that block
- **Lexical Scope** — Inner functions can access variables from their outer (enclosing) scope

```js
let globalVar = "I am global";

function outer() {
  let outerVar = "I am outer";

  function inner() {
    let innerVar = "I am inner";
    console.log(globalVar); // accessible
    console.log(outerVar);  // accessible (lexical scope)
    console.log(innerVar);  // accessible
  }

  inner();
  console.log(innerVar); // ReferenceError
}
```

---

### Temporal Dead Zone (TDZ)

**Definition:** The period between the start of a block and the point where a `let` or `const` variable is declared. Accessing the variable in this zone throws a `ReferenceError`.

```js
{
  // TDZ starts here for 'name'
  console.log(name); // ReferenceError
  let name = "Alice"; // TDZ ends here
  console.log(name);  // "Alice"
}
```

---

## 2. Data Types & Type Coercion

### Primitive vs Non-Primitive

**Primitive Data Types** — Immutable, hold a single value, stored by value.
- `string`, `number`, `boolean`, `undefined`, `null`, `symbol`, `bigint`

**Non-Primitive Data Types** — Mutable, can hold multiple values, stored by reference.
- `object`, `array`, `function`

```js
// Primitive — stored by VALUE
let a = 10;
let b = a;
b = 20;
console.log(a); // Output: 10 (unchanged)

// Non-primitive — stored by REFERENCE
let obj1 = { name: "Alice" };
let obj2 = obj1;
obj2.name = "Bob";
console.log(obj1.name); // Output: "Bob" (changed!)
```

---

### `undefined` vs `null`

- **`undefined`** — Variable declared but not yet assigned a value. JavaScript sets this automatically.
- **`null`** — Intentionally assigned to represent "no value" or "empty". Set by the developer.

```js
let x;
console.log(x);        // undefined
console.log(typeof x); // "undefined"

let y = null;
console.log(y);        // null
console.log(typeof y); // "object"  (known JS quirk/bug)
```

---

### `typeof` Operator

```js
typeof "hello"      // "string"
typeof 42           // "number"
typeof true         // "boolean"
typeof undefined    // "undefined"
typeof null         // "object"   (JS quirk)
typeof {}           // "object"
typeof []           // "object"
typeof function(){} // "function"
typeof Symbol()     // "symbol"
```

---

### Type Coercion

**Definition:** The automatic (implicit) conversion of values from one data type to another during operations or comparisons.

```js
// Implicit coercion
console.log("5" + 3);   // "53"  (number coerced to string)
console.log("5" - 3);   // 2     (string coerced to number)
console.log(true + 1);  // 2     (true = 1)
console.log(false + 1); // 1     (false = 0)
console.log("" == false); // true (both coerce to 0)

// Explicit coercion
Number("42");   // 42
String(100);    // "100"
Boolean(0);     // false
Boolean("hi");  // true
```

---

### `==` vs `===`

- **`==`** (loose equality) — Compares values **after type coercion**
- **`===`** (strict equality) — Compares values **without type coercion** (type must also match)

```js
console.log(0 == false);         // true  (false coerces to 0)
console.log(0 === false);        // false (different types)
console.log(null == undefined);  // true
console.log(null === undefined); // false
```

> **Interview Tip:** Always prefer `===` to avoid unexpected bugs from coercion.

---

### Falsy & Truthy Values

**Falsy values** (evaluate to `false` in a boolean context):
`false`, `0`, `""`, `null`, `undefined`, `NaN`

**Everything else is truthy**, including `[]`, `{}`, `"0"`, `"false"`

```js
if ([]) console.log("truthy"); // "truthy"  (empty array is truthy!)
if ({}) console.log("truthy"); // "truthy"  (empty object is truthy!)
if (0)  console.log("truthy"); // (nothing) — 0 is falsy
```

---

## 3. Operators

### Spread Operator (`...`)

**Definition:** Expands an iterable (array, string, object) into individual elements.

**Uses:** Copying arrays, merging arrays, passing multiple arguments to a function.

```js
const arr = [1, 2, 3];
console.log(...arr); // 1 2 3

// Copy array
const copy = [...arr]; // [1, 2, 3]

// Merge arrays
const merged = [...arr, 4, 5]; // [1, 2, 3, 4, 5]

// Copy object
const obj    = { a: 1 };
const newObj = { ...obj, b: 2 }; // { a: 1, b: 2 }

// Pass as function arguments
function sum(a, b, c) { return a + b + c; }
sum(...arr); // 6
```

---

### Rest Operator (`...`)

**Definition:** Collects remaining function arguments into a single array. Used in function parameters.

```js
function display(first, second, ...rest) {
  console.log(first);  // 1
  console.log(second); // 2
  console.log(rest);   // [3, 4, 5]
}
display(1, 2, 3, 4, 5);
```

> **Key difference:** Spread **expands** elements. Rest **collects** elements.

---

### Optional Chaining (`?.`)

**Definition:** Safely access deeply nested properties without throwing an error if a value is `null` or `undefined`.

```js
const user = { address: { city: "Delhi" } };

console.log(user.address?.city);  // "Delhi"
console.log(user.phone?.number);  // undefined (no error!)
console.log(user.getAge?.());     // undefined (no error!)
```

---

### Nullish Coalescing (`??`)

**Definition:** Returns the right-hand value only if the left-hand value is `null` or `undefined`. Unlike `||`, it does NOT treat `0` or `""` as falsy.

```js
let name = null;
console.log(name ?? "Guest"); // "Guest"

let count = 0;
console.log(count ?? 10);    // 0  (0 is NOT null/undefined)
console.log(count || 10);    // 10 (0 is falsy for ||)
```

---

## 4. Control Flow

### `break` vs `continue`

- **`break`** — Exits the loop entirely.
- **`continue`** — Skips the current iteration and moves to the next.

```js
// break
for (let i = 1; i <= 5; i++) {
  if (i === 3) break;
  console.log(i);
}
// Output: 1 2

// continue
for (let i = 1; i <= 5; i++) {
  if (i === 3) continue;
  console.log(i);
}
// Output: 1 2 4 5
```

---

### `for...of` vs `for...in`

- **`for...of`** — Iterates over the **values** of an iterable (arrays, strings, Sets, Maps).
- **`for...in`** — Iterates over the **keys/property names** of an object.

```js
// for...of — values
const arr = [10, 20, 30];
for (let val of arr) {
  console.log(val); // 10, 20, 30
}

// for...in — keys
const person = { name: "Alice", age: 25 };
for (let key in person) {
  console.log(key, person[key]); // name Alice / age 25
}
```

> **Interview Tip:** Don't use `for...in` on arrays — it iterates over all enumerable properties, which can include prototype properties.

---

### Ternary Operator

```js
const age = 20;
const status = age >= 18 ? "Adult" : "Minor";
console.log(status); // "Adult"
```

---

## 5. Functions

### Function Types

**Function Declaration** — Hoisted, can be called before it is defined.

```js
function greet(name) {
  return `Hello, ${name}!`;
}
greet("Alice"); // "Hello, Alice!"
```

**Function Expression** — Not fully hoisted. Assigned to a variable.

```js
// Anonymous
const add = function(a, b) { return a + b; };

// Named (useful for recursion and debugging)
const factorial = function fact(n) {
  return n <= 1 ? 1 : n * fact(n - 1);
};
```

**Arrow Function** — Shorter syntax. Does NOT have its own `this`, `arguments`, or `prototype`.

```js
const multiply = (a, b) => a * b;

const greet = (name) => {
  const msg = `Hello, ${name}`;
  return msg;
};
```

**IIFE (Immediately Invoked Function Expression)** — Runs immediately when defined.

```js
(function () {
  console.log("I run immediately!");
})();

// Arrow function IIFE
(() => {
  console.log("Arrow IIFE");
})();
```

---

### Parameters vs Arguments

- **Parameters** — Placeholders defined in the function declaration.
- **Arguments** — Actual values passed when the function is called.

```js
// a, b are parameters
function add(a, b) {
  return a + b;
}
add(3, 4); // 3 and 4 are arguments
```

---

### Default Parameters

```js
function greet(name = "Guest") {
  return `Hello, ${name}!`;
}
greet();        // "Hello, Guest!"
greet("Alice"); // "Hello, Alice!"
```

---

### Pure Functions

**Definition:** A function that always returns the same output for the same input, and has no side effects.

```js
// Pure function
function add(a, b) { return a + b; }

// Impure function (modifies external state)
let total = 0;
function addToTotal(n) {
  total += n; // side effect
}
```

---

### First-Class Functions

**Definition:** JavaScript treats functions as first-class citizens — they can be assigned to variables, passed as arguments, and returned from other functions.

```js
// 1. Assigned to a variable
const sayHi = function() { console.log("Hi!"); };
sayHi();

// 2. Passed as an argument
function runFn(fn) { fn(); }
runFn(sayHi);

// 3. Returned from a function
function createGreeter() {
  return function(name) { console.log(`Hello, ${name}`); };
}
const greet = createGreeter();
greet("Bob"); // "Hello, Bob"
```

---

## 6. Arrays & Array Methods

**Definition:** An array is a data type that stores multiple ordered values in a single variable.

### Quick Reference Table

| Category | Method | Mutates? | Returns |
|----------|--------|----------|---------|
| **Get** | `find()` | No | First matching element |
| | `filter()` | No | New array of matches |
| | `indexOf()` | No | Index or -1 |
| | `slice(s, e)` | No | New sub-array |
| | `includes()` | No | Boolean |
| **Add** | `push()` | Yes | New length |
| | `unshift()` | Yes | New length |
| | `concat()` | No | New merged array |
| **Remove** | `pop()` | Yes | Removed element |
| | `shift()` | Yes | Removed element |
| | `splice(i,n)` | Yes | Removed elements |
| **Transform** | `map()` | No | New array (same length) |
| | `reduce()` | No | Single accumulated value |
| | `flat()` | No | Flattened array |
| **Iterate** | `forEach()` | No | `undefined` |
| | `some()` | No | Boolean |
| | `every()` | No | Boolean |
| **Other** | `sort()` | Yes | Sorted array |
| | `reverse()` | Yes | Reversed array |
| | `join(sep)` | No | String |

---

### Key Method Code Examples

```js
const nums = [1, 2, 3, 4, 5];

// find — first match
nums.find(n => n > 3);       // 4

// filter — all matches
nums.filter(n => n > 3);     // [4, 5]

// map — transform each element
nums.map(n => n * 2);        // [2, 4, 6, 8, 10]

// reduce — accumulate
nums.reduce((acc, n) => acc + n, 0); // 15

// some / every
nums.some(n => n > 4);   // true  (at least one is > 4)
nums.every(n => n > 0);  // true  (all are > 0)

// includes
nums.includes(3);  // true

// splice — mutates
let arr = [1, 2, 3];
arr.splice(1, 1, 9); // removes 1 at index 1, inserts 9
// arr = [1, 9, 3]

// slice — does NOT mutate
[1, 2, 3, 4].slice(1, 3); // [2, 3]
```

---

### `map()` vs `forEach()` vs `filter()` vs `reduce()`

| Method | Returns | Use When |
|--------|---------|----------|
| `map()` | New array (same length) | Transform each element |
| `forEach()` | `undefined` | Execute side effects only |
| `filter()` | New shorter/equal array | Keep elements matching a condition |
| `reduce()` | Single value | Sum, count, build object from array |

---

### Array Destructuring

```js
const fruits = ["apple", "banana", "orange"];
const [first, second, third] = fruits;
console.log(first); // "apple"

// Skip elements
const [, , last] = fruits;
console.log(last); // "orange"

// Default values
const [a = 1, b = 2] = [10];
console.log(a, b); // 10  2

// Swap variables
let x = 1, y = 2;
[x, y] = [y, x];
console.log(x, y); // 2  1
```

---

### Array-Like Objects

**Definition:** Objects that have indexed elements and a `length` property, but are not true arrays and lack array methods like `push()`, `pop()`.

**Examples:** `arguments` object, strings, `NodeList`, `HTMLCollection`

```js
// arguments — available in non-arrow functions
function sum() {
  console.log(arguments);        // { 0: 1, 1: 2, 2: 3 }
  console.log(arguments.length); // 3
  const arr = Array.from(arguments); // convert to array
}
sum(1, 2, 3);

// String — array-like
const str = "Hello";
console.log(str[0]);     // H
console.log(str.length); // 5

// NodeList (from DOM) — convert to array
const divs = document.querySelectorAll("div");
const divsArray = [...divs];
```

> **Interview Tip:** Use `Array.from()` or `[...arrayLike]` to convert array-like objects to real arrays.

---

## 7. Objects & OOP

### Object Basics

```js
const person = {
  name: "Alice",
  age: 25,
  greet() {
    console.log(`Hi, I'm ${this.name}`);
  }
};

person.greet();    // "Hi, I'm Alice"
person.name;       // dot notation
person["name"];    // bracket notation (useful for dynamic keys)
```

---

### Object Destructuring

```js
const { name, age } = person;

// Rename on destructure
const { name: fullName } = person;

// Default values
const { city = "Unknown" } = person;

// Nested destructuring
const user = { address: { city: "Delhi" } };
const { address: { city: userCity } } = user;
console.log(userCity); // "Delhi"
```

---

### Classes & OOP Concepts

**OOP Pillars:**
1. **Encapsulation** — Bundling data and methods together; hiding internal details
2. **Inheritance** — A class can extend another class and inherit its properties/methods
3. **Polymorphism** — Same method behaves differently based on the object
4. **Abstraction** — Hiding complexity, exposing only what is necessary

```js
class Animal {
  constructor(name) {
    this.name = name;
  }
  speak() {
    console.log(`${this.name} makes a sound.`);
  }
}

// Inheritance
class Dog extends Animal {
  speak() {
    console.log(`${this.name} barks.`); // Polymorphism
  }
}

const dog = new Dog("Rex");
dog.speak();                        // "Rex barks."
console.log(dog instanceof Animal); // true
```

---

### Constructor & `new` Keyword

**Constructors** are special methods within classes, automatically called when an object is created using the `new` keyword.

```js
class Person {
  constructor(name, age) {
    this.name = name;
    this.age  = age;
  }
  sayHello() {
    console.log(`${this.name} - ${this.age}`);
  }
}

const p1 = new Person("Alice", 25);
p1.sayHello(); // "Alice - 25"
```

**Constructor Functions (ES5 style):**

```js
function Person(name, age) {
  this.name = name;
  this.age  = age;
}
Person.prototype.sayHello = function() {
  console.log(this.name);
};
const p = new Person("Bob", 30);
```

---

### Deep Copy vs Shallow Copy

**Shallow Copy** — Copies only the top-level properties. Nested objects are still referenced (shared).

**Deep Copy** — Copies all levels. Fully independent from the original.

```js
const person = {
  name: "Happy",
  address: { city: "Delhi" }
};

// Shallow copy — nested object is still linked
const shallowCopy = Object.assign({}, person);
shallowCopy.address.city = "Mumbai";
console.log(person.address.city); // "Mumbai"  (CHANGED!)

// Deep copy — fully independent
const deepCopy = JSON.parse(JSON.stringify(person));
deepCopy.address.city = "Bangalore";
console.log(person.address.city); // "Delhi"   (UNCHANGED)

// Modern deep copy
const deepCopy2 = structuredClone(person);
```

> **`JSON.parse(JSON.stringify())` limitations:** Doesn't handle `functions`, `undefined`, `Date`, `RegExp`, or circular references. Use `structuredClone()` for complex objects.

---

### Object Methods Cheat Sheet

```js
const obj = { a: 1, b: 2, c: 3 };

Object.keys(obj);    // ["a", "b", "c"]
Object.values(obj);  // [1, 2, 3]
Object.entries(obj); // [["a",1], ["b",2], ["c",3]]

// Check if property exists
"a" in obj;              // true
obj.hasOwnProperty("a"); // true

// Merge objects
const merged = { ...obj1, ...obj2 };

// Freeze — prevent modification
const frozen = Object.freeze({ x: 1 });
frozen.x = 2; // silently fails
```

---

## 8. Prototypes & Inheritance

### Prototype Chain

**Definition:** Every JavaScript object has an internal link to another object called its **prototype**. When a property is not found on the object, JavaScript looks up the prototype chain until it finds it or reaches `null`.

```js
function Animal(name) {
  this.name = name;
}
Animal.prototype.speak = function() {
  console.log(`${this.name} speaks`);
};

const dog = new Animal("Rex");
dog.speak(); // "Rex speaks"
console.log(dog.__proto__ === Animal.prototype); // true
```

---

### `__proto__` vs `prototype`

- **`prototype`** — Property on **constructor functions/classes**. This is the object assigned as the prototype to all instances created by that constructor.
- **`__proto__`** — Property on **instances**. Points to the prototype of the constructor that created them.

```js
function Car() {}
const myCar = new Car();

console.log(Car.prototype);                    // { constructor: Car }
console.log(myCar.__proto__ === Car.prototype); // true
```

---

### Class-Based Inheritance

```js
class Vehicle {
  constructor(brand) {
    this.brand = brand;
  }
  drive() { console.log(`${this.brand} is driving`); }
}

class Car extends Vehicle {
  constructor(brand, model) {
    super(brand); // calls Vehicle's constructor
    this.model = model;
  }
  describe() { console.log(`${this.brand} ${this.model}`); }
}

const car = new Car("Toyota", "Camry");
car.drive();    // "Toyota is driving"
car.describe(); // "Toyota Camry"
```

---

## 9. Closures & Lexical Scope

### Lexical Scoping

**Definition:** An inner function has access to variables from its outer (enclosing) function, based on where the function is **defined** — not where it is called.

```js
function outer() {
  const outerVar = "outer scope";

  function inner() {
    console.log(outerVar); // accessible via lexical scope
  }
  inner();
}
outer(); // Output: outer scope
```

---

### Closure

**Definition:** A closure is when an inner function **retains access to its outer function's variables even after the outer function has finished executing**.

**Three scope chains a closure has access to:**
1. Its own scope
2. Variables of the outer function
3. Global variables

```js
function outerFunction() {
  const outerVariable = "outer scope";

  function innerFunction() {
    console.log(outerVariable); // still accessible!
  }
  return innerFunction;
}

const closure = outerFunction(); // outer has returned
closure(); // Output: "outer scope"  (closure remembered it)
```

---

### Benefits of Closures

**1. Data Privacy / Encapsulation**

```js
function createCounter() {
  let count = 0; // private variable

  return {
    increment() { count++; console.log(count); },
    decrement() { count--; console.log(count); },
    getCount()  { return count; }
  };
}

const counter = createCounter();
counter.increment(); // 1
counter.increment(); // 2
// count is not directly accessible from outside
```

**2. Persistent State**

```js
const counter1 = createCounter();
const counter2 = createCounter(); // independent counter

counter1.increment(); // 1
counter1.increment(); // 2
counter2.increment(); // 1 (independent state)
```

**3. Function Factories**

```js
function multiplier(factor) {
  return (number) => number * factor;
}
const double = multiplier(2);
const triple = multiplier(3);
console.log(double(5)); // 10
console.log(triple(5)); // 15
```

---

### Common Closure Pitfall — `var` in Loops

```js
// Problem: var is function-scoped, all closures share the same 'i'
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// Output: 3 3 3

// Fix 1: use let (block-scoped, new binding each iteration)
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// Output: 0 1 2

// Fix 2: use IIFE
for (var i = 0; i < 3; i++) {
  ((j) => setTimeout(() => console.log(j), 100))(i);
}
// Output: 0 1 2
```

---

## 10. Higher-Order Functions, Callbacks & Currying

### Higher-Order Functions (HOF)

**Definition:** A function that either takes one or more functions as arguments, or returns a function as a result.

```js
// Takes a function as argument
function hof(func) {
  func();
}
hof(() => console.log("Hello!")); // "Hello!"

// Returns a function
function createAdder(n) {
  return (value) => value + n;
}
const addFive = createAdder(5);
console.log(addFive(3)); // 8
```

---

### Callback Function

**Definition:** A function passed as an argument to another function, to be executed later.

```js
function display(x, y, operation) {
  const result = operation(x, y);
  console.log(result);
}

function add(a, b)      { return a + b; }
function multiply(a, b) { return a * b; }

display(10, 5, add);      // 15
display(10, 5, multiply); // 50
```

---

### Callback Hell

**Definition:** Deeply nested callbacks that make code hard to read and maintain.

```js
// Callback hell
getData(function(a) {
  getMoreData(a, function(b) {
    getEvenMoreData(b, function(c) {
      console.log(c);
    });
  });
});

// Solved with async/await
const a = await getData();
const b = await getMoreData(a);
const c = await getEvenMoreData(b);
console.log(c);
```

---

### Function Currying

**Definition:** Transforms a function with multiple arguments into a sequence of nested functions, each taking a single argument.

**Advantages:** Reusability, partial application, modularity, specialization.

```js
// Regular function
function multiply(a, b) { return a * b; }

// Curried version
function curriedMultiply(a) {
  return function(b) {
    return a * b;
  };
}

const double = curriedMultiply(2);
const triple = curriedMultiply(3);

console.log(double(5)); // 10
console.log(triple(5)); // 15

// Arrow function style
const curriedAdd = a => b => c => a + b + c;
console.log(curriedAdd(1)(2)(3)); // 6
```

---

### Memoization

**Definition:** An optimization technique where function results are cached so repeated calls with the same arguments return the cached result instead of recalculating.

```js
function memoize(fn) {
  const cache = {};
  return function(...args) {
    const key = JSON.stringify(args);
    if (cache[key] !== undefined) {
      return cache[key]; // return from cache
    }
    cache[key] = fn(...args);
    return cache[key];
  };
}

const expensiveAdd = memoize((a, b) => a + b);
expensiveAdd(2, 3); // calculates
expensiveAdd(2, 3); // returns from cache
```

---

## 11. The `this` Keyword, Call, Apply & Bind

### `this` Keyword

**Definition:** `this` refers to the object that is currently executing the function. Its value depends on **how the function is called**.

| Context | `this` value |
|---------|-------------|
| Global scope | `window` (browser) / `global` (Node) |
| Regular function | `window` (non-strict) / `undefined` (strict) |
| Method | The object before the dot |
| Arrow function | Lexically bound — inherits from enclosing scope |
| Constructor / class | The newly created object |
| Event handler | The element that fired the event |

```js
// Method — this is the object
const obj = {
  name: "Alice",
  greet() {
    console.log(this.name); // "Alice"
  }
};
obj.greet();

// Arrow function — no own `this`, uses outer scope
const obj2 = {
  name: "Bob",
  greet: () => {
    console.log(this.name); // undefined (arrow uses outer `this`)
  }
};

// Common bug — losing `this` context
const greet = obj.greet;
greet();                          // undefined (lost context)
const boundGreet = obj.greet.bind(obj);
boundGreet();                     // "Alice" (preserved)
```

---

### `call`, `apply`, `bind`

All three allow you to explicitly set the value of `this` in a function.

| Method | Invokes immediately | Arguments format |
|--------|---------------------|-----------------|
| `call` | Yes | Comma-separated |
| `apply` | Yes | As an array |
| `bind` | No — returns new function | Comma-separated |

```js
function greet(greeting, punctuation) {
  console.log(`${greeting}, ${this.name}${punctuation}`);
}
const person = { name: "Happy" };

greet.call(person, "Hello", "!");   // "Hello, Happy!"
greet.apply(person, ["Hi", "."]);   // "Hi, Happy."

const boundGreet = greet.bind(person, "Hey");
boundGreet("?"); // "Hey, Happy?"
```

---

## 12. Spread, Rest & Destructuring

> Spread and Rest are covered in Section 3. Key destructuring patterns are below.

### Nested Destructuring

```js
const user = {
  name: "Alice",
  address: { city: "Delhi", zip: "110001" }
};

const { name, address: { city } } = user;
console.log(name, city); // "Alice" "Delhi"
```

---

### Destructuring in Function Parameters

```js
function display({ name, age = 0 }) {
  console.log(`${name} is ${age}`);
}
display({ name: "Alice", age: 25 }); // "Alice is 25"
display({ name: "Bob" });            // "Bob is 0"
```

---

### Mixed Destructuring (Array + Object)

```js
const data = {
  users: [
    { id: 1, name: "Alice" },
    { id: 2, name: "Bob" }
  ]
};

const { users: [firstUser] } = data;
console.log(firstUser.name); // "Alice"
```

---

## 13. ES6+ Features

### Template Literals

```js
const name = "Alice";
const greeting = `Hello, ${name}! You are ${2024 - 1999} years old.`;

// Multi-line strings
const multiLine = `
  Line 1
  Line 2
`;
```

---

### Symbols

**Definition:** A unique and immutable primitive value, often used as object property keys to avoid name collisions.

```js
const id = Symbol("id");
const obj = { [id]: 123, name: "Alice" };

console.log(obj[id]);              // 123
Symbol("id") === Symbol("id");     // false (always unique)
```

---

### Generators

**Definition:** Functions that can be paused and resumed. Use `function*` syntax and `yield` to pause execution.

```js
function* counter() {
  yield 1;
  yield 2;
  yield 3;
}

const gen = counter();
console.log(gen.next()); // { value: 1, done: false }
console.log(gen.next()); // { value: 2, done: false }
console.log(gen.next()); // { value: 3, done: false }
console.log(gen.next()); // { value: undefined, done: true }
```

---

### ES6+ Feature Cheat Sheet

| Feature | Example |
|---------|---------|
| `let` / `const` | Block-scoped variables |
| Arrow functions | `(a, b) => a + b` |
| Template literals | `` `Hello, ${name}` `` |
| Destructuring | `const { a, b } = obj` |
| Default params | `function f(x = 0)` |
| Rest / Spread | `...args` / `...arr` |
| Classes | `class Dog extends Animal` |
| Modules | `import` / `export` |
| Promises | `.then()` / `.catch()` |
| Async/Await | `async function` / `await` |
| Optional chaining | `obj?.prop?.nested` |
| Nullish coalescing | `val ?? "default"` |
| `Symbol` | Unique identifiers |
| `Map` / `Set` | Key-value & unique collections |
| `WeakMap` / `WeakSet` | GC-friendly collections |
| `for...of` | Iterate over iterable values |
| Generators | `function*` / `yield` |

---

## 14. DOM & Browser Events

### DOM (Document Object Model)

**Definition:** The DOM represents a web page as a tree-like structure that allows JavaScript to dynamically access and manipulate content and structure.

```js
// Selecting elements
document.getElementById("id");
document.querySelector(".class");       // first match
document.querySelectorAll("div");       // all matches (NodeList)
document.getElementsByClassName("box"); // HTMLCollection

// Creating / modifying elements
const div = document.createElement("div");
div.textContent = "Hello";
div.classList.add("my-class");
document.body.appendChild(div);

// Removing elements
div.remove();
```

---

### Event Handling

```js
const button = document.getElementById("btn");

button.addEventListener("click", function(event) {
  console.log("Clicked!", event.target);
});

// Remove event listener (must use named function reference)
function handleClick() { console.log("Clicked"); }
button.addEventListener("click", handleClick);
button.removeEventListener("click", handleClick);
```

---

### Event Bubbling vs Event Capturing

**Event Bubbling** — Event fires on the target first, then propagates **up** to parent elements (default behavior).

**Event Capturing** — Event fires at the root first, then travels **down** to the target element.

```
Capturing (down): Document → html → body → div → button
Bubbling  (up):   button → div → body → html → Document
```

```js
// Bubbling (default — no 3rd argument)
outer.addEventListener("click", () => console.log("outer"));
inner.addEventListener("click", () => console.log("inner"));
// Click inner → Output: "inner" then "outer"

// Capturing (pass true as 3rd argument)
outer.addEventListener("click", () => console.log("outer"), true);
inner.addEventListener("click", () => console.log("inner"), true);
// Click inner → Output: "outer" then "inner"

// Stop propagation
button.addEventListener("click", (e) => {
  e.stopPropagation(); // prevent bubbling up
});
```

---

### Event Delegation

**Definition:** Attach one event listener to a **parent** element instead of many child elements. Use `event.target` to determine which child was interacted with.

```js
// Efficient — one listener on parent
document.getElementById("list").addEventListener("click", function(e) {
  if (e.target.tagName === "LI") {
    console.log("Clicked:", e.target.textContent);
  }
});
```

---

### `preventDefault` vs `stopPropagation`

- **`e.preventDefault()`** — Prevents the browser's default action (e.g., form submit, link navigation).
- **`e.stopPropagation()`** — Stops the event from bubbling up (or capturing down) to parent elements.

---

## 15. Asynchronous JavaScript

### How JavaScript Handles Async

JavaScript is **single-threaded** — it executes one task at a time. The **Event Loop** allows it to handle async operations without blocking.

**Event Loop Components:**
1. **Call Stack** — Executes synchronous code
2. **Web APIs** — Browser handles async tasks (`setTimeout`, `fetch`, DOM events)
3. **Task Queue (Macrotask Queue)** — Completed async callbacks wait here (`setTimeout`, `setInterval`)
4. **Microtask Queue** — Promise callbacks wait here (higher priority than Task Queue)
5. **Event Loop** — Moves tasks from queues to the call stack when it is empty

```js
console.log("1 - start");

setTimeout(() => console.log("3 - setTimeout"), 0);

Promise.resolve().then(() => console.log("2 - promise"));

console.log("4 - end");

// Output order:
// 1 - start
// 4 - end
// 2 - promise    (Microtask Queue — higher priority)
// 3 - setTimeout (Task Queue)
```

---

### `setTimeout` & `setInterval`

```js
// setTimeout — executes once after delay
const id = setTimeout(() => {
  console.log("Runs once after 2s");
}, 2000);
clearTimeout(id); // cancel

// setInterval — executes repeatedly
const intervalId = setInterval(() => {
  console.log("Runs every 1s");
}, 1000);
clearInterval(intervalId); // stop
```

---

### Async Techniques Comparison

| Technique | Pros | Cons |
|-----------|------|------|
| Callbacks | Simple, universal | Callback hell, hard to read |
| Promises | Chainable, readable | Verbose `.then()` chains |
| Async/Await | Clean, synchronous-looking code | Needs try/catch |
| Generators | Pausable execution | Complex, rarely used directly |
| Event-driven | Reactive, loosely coupled | Hard to trace flow |

---

## 16. Promises & Async/Await

### Promise

**Definition:** An object representing the eventual **completion** or **failure** of an asynchronous operation.

**Three states:**
1. **Pending** — Initial state, neither fulfilled nor rejected
2. **Fulfilled** — Operation completed successfully
3. **Rejected** — Operation failed

```js
const promise = new Promise((resolve, reject) => {
  const success = true;
  if (success) {
    resolve("Data received");
  } else {
    reject("Something went wrong");
  }
});

promise
  .then(result => console.log(result))   // "Data received"
  .catch(error  => console.log(error))
  .finally(()   => console.log("Done")); // always runs
```

---

### Promise Methods

| Method | Description |
|--------|-------------|
| `Promise.all([...])` | Waits for ALL to resolve. Rejects if ANY reject |
| `Promise.allSettled([...])` | Waits for ALL to settle. Never rejects. Returns status of each |
| `Promise.race([...])` | Resolves/rejects with the FIRST settled promise |
| `Promise.any([...])` | Resolves with the FIRST fulfilled. Rejects only if ALL reject |

```js
const p1 = Promise.resolve("Hello");
const p2 = new Promise((_, reject) => setTimeout(() => reject("Error"), 1000));
const p3 = Promise.resolve("Happy");

// Promise.all — fails if any reject
Promise.all([p1, p3]).then(r => console.log(r)); // ["Hello", "Happy"]

// Promise.allSettled — shows all outcomes
Promise.allSettled([p1, p2, p3]).then(results =>
  results.forEach(r => console.log(r.status, r.value ?? r.reason))
);

// Promise.race — first to settle wins
Promise.race([p1, p2]).then(r => console.log(r)); // "Hello"
```

---

### Async/Await

**Definition:** Syntactic sugar over Promises that makes async code look like synchronous code.

- **`async`** — Marks a function as asynchronous; it always returns a Promise.
- **`await`** — Pauses the async function until the Promise resolves or rejects.

```js
async function fetchUser() {
  try {
    const response = await fetch("/api/user");
    const user     = await response.json();
    console.log(user);
  } catch (error) {
    console.error("Error:", error);
  } finally {
    console.log("Request finished");
  }
}
```

---

### Sequential vs Parallel Execution

```js
// Sequential — total wait = 1s + 2s = 3s
const a = await fetchA(); // 1s
const b = await fetchB(); // 2s

// Parallel — total wait = max(1s, 2s) = 2s
const [a, b] = await Promise.all([fetchA(), fetchB()]);
```

---

## 17. Error Handling

### `try...catch...finally`

```js
try {
  const result = JSON.parse("invalid json");
} catch (error) {
  console.log("Error caught:", error.message);
} finally {
  console.log("Always runs");
}
```

> **`finally`** block executes code **irrespective of whether an error was thrown**.

---

### `throw` Statement

**Definition:** Stops the current function execution and passes the error to the nearest `catch` block.

```js
function divide(a, b) {
  if (b === 0) throw new Error("Division by zero!");
  return a / b;
}

try {
  divide(10, 0);
} catch (e) {
  console.log(e.message); // "Division by zero!"
}
```

---

### Error Types

```js
new Error("message")           // Generic error
new TypeError("type mismatch") // Wrong type used
new RangeError("out of range") // Value out of valid range
new ReferenceError("undefined")// Variable not defined
new SyntaxError("bad syntax")  // Parsing/syntax error
```

---

### Error Propagation

**Definition:** An error "bubbles up" the call stack through `throw` until it is caught by a `try...catch` block.

```js
function level3() { throw new Error("Deep error"); }
function level2() { level3(); }
function level1() {
  try {
    level2();
  } catch (e) {
    console.log("Caught at level1:", e.message); // "Deep error"
  }
}
level1();
```

---

## 18. Set, Map & WeakMap/WeakSet

### Set

**Definition:** A collection of **unique** values — duplicates are automatically ignored.

```js
const set = new Set([1, 2, 3, 2, 1]);
console.log(set);       // {1, 2, 3}
console.log(set.size);  // 3
set.add(4);
set.has(2);             // true
set.delete(2);

// Iteration
for (let val of set) console.log(val);

// Remove duplicates from array
const unique = [...new Set([1, 2, 2, 3, 3])]; // [1, 2, 3]
```

---

### Map

**Definition:** A collection of key-value pairs where **keys can be of any type**. Maintains insertion order.

```js
const map = new Map();
map.set("name", "Alice");
map.set(1, "one");
map.set(true, "bool key");

map.get("name");  // "Alice"
map.has(1);       // true
map.size;         // 3

for (let [key, value] of map) {
  console.log(key, value);
}
```

---

### Map vs Object

| Feature | Map | Object |
|---------|-----|--------|
| Key types | Any (objects, functions, primitives) | Strings and Symbols only |
| Insertion order | Always maintained | Not guaranteed (older JS) |
| Size | `.size` property | `Object.keys().length` |
| Default keys | None | Has prototype-inherited keys |
| Iteration | Direct `for...of` | Needs `Object.keys()` etc. |
| Performance | Better for frequent add/remove | Better for fixed key lookup |

---

### WeakMap & WeakSet

**Definition:** Like Map/Set, but keys (WeakMap) or values (WeakSet) must be **objects**, and they are held with **weak references** — they don't prevent garbage collection.

```js
let obj = { name: "Alice" };
const weakMap = new WeakMap();
weakMap.set(obj, "some data");

obj = null; // obj can be garbage collected; weakMap entry auto-removed
```

> **Use case:** Storing private data associated with objects or DOM nodes without preventing their garbage collection.

---

## 19. Memory Management & Performance

### Garbage Collection

JavaScript uses **automatic garbage collection**. Objects are removed from memory when they are no longer reachable (no references pointing to them).

```js
let user = { name: "Alice" }; // reachable
user = null;                  // unreachable — garbage collected
```

---

### Memory Leaks — Common Causes

1. **Global variables** — Never garbage collected while the page is open
2. **Forgotten timers** — `setInterval` that is never cleared
3. **Detached DOM nodes** — Removed from DOM but still referenced in JS
4. **Closures** — Holding references to data longer than needed

```js
// Memory leak — setInterval never cleared
setInterval(() => bigData.process(), 1000);

// Fix — clear when done
const id = setInterval(() => bigData.process(), 1000);
clearInterval(id);
```

---

### Debounce vs Throttle

**Debounce** — Delays execution until a specified time has passed since the last call. Best for search inputs, form validation.

**Throttle** — Limits execution to at most once per time interval. Best for scroll, resize, and mouse move events.

```js
// Debounce
function debounce(fn, delay) {
  let timer;
  return function(...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

const handleSearch = debounce((query) => {
  console.log("Searching:", query);
}, 300);

// Throttle
function throttle(fn, limit) {
  let lastRun = 0;
  return function(...args) {
    const now = Date.now();
    if (now - lastRun >= limit) {
      lastRun = now;
      fn.apply(this, args);
    }
  };
}

const handleScroll = throttle(() => console.log("Scrolled"), 200);
```

---

## 20. Browser APIs & Web Storage

### Browser APIs Overview

| API | Key Methods |
|-----|-------------|
| **DOM API** | `getElementById()`, `querySelector()`, `createElement()`, `appendChild()`, `addEventListener()` |
| **Fetch API** | `fetch()`, `.then()`, `.json()`, `headers.get()` |
| **XMLHttpRequest** | `open()`, `send()`, `setRequestHeader()`, `onreadystatechange` |
| **Storage API** | `localStorage`, `sessionStorage` |
| **History API** | `pushState()`, `replaceState()`, `go()`, `back()` |
| **Geolocation API** | `getCurrentPosition()`, `watchPosition()`, `clearWatch()` |
| **Notifications API** | `Notification.requestPermission()`, `new Notification()` |
| **Canvas API** | `getContext()`, `fillRect()`, `drawImage()`, `beginPath()` |
| **Audio/Video** | `play()`, `pause()`, `currentTime`, `volume` |

---

### Fetch API

```js
// GET request
fetch("https://api.example.com/users")
  .then(res  => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));

// POST request
fetch("https://api.example.com/users", {
  method:  "POST",
  headers: { "Content-Type": "application/json" },
  body:    JSON.stringify({ name: "Alice" })
})
  .then(res => res.json())
  .then(data => console.log(data));

// With async/await
async function getUsers() {
  const res  = await fetch("/api/users");
  const data = await res.json();
  return data;
}
```

---

### Web Storage

```js
// localStorage — persists after browser close
localStorage.setItem("theme", "dark");
const theme = localStorage.getItem("theme"); // "dark"
localStorage.removeItem("theme");
localStorage.clear();

// sessionStorage — same API, cleared on tab/window close
sessionStorage.setItem("token", "abc123");
```

---

### Local Storage vs Session Storage vs Cookies

| Feature | Local Storage | Session Storage | Cookies |
|---------|---------------|-----------------|---------|
| Capacity | 5–10 MB | 5–10 MB | ~4 KB |
| Expiry | Never (manual only) | Tab/window close | Configurable |
| Sent to server | No | No | Yes (automatically) |
| Accessible from | Client only | Client only | Client + Server |
| Scope | All tabs (same origin) | Single tab only | All tabs (same origin) |

---

## 21. Modules

### CommonJS (Node.js)

```js
// Exporting
module.exports = { add, subtract };

// Importing
const { add } = require("./math");
```

---

### ES Modules (Browser / Modern Node.js)

```js
// Named exports
export const PI = 3.14;
export function add(a, b) { return a + b; }

// Default export (one per file)
export default class Calculator { ... }

// Importing
import Calculator, { PI, add } from "./math.js";

// Dynamic import (lazy loading)
const module = await import("./heavy-module.js");
```

> **`export default`** — One per file, imported without curly braces.  
> **Named exports** — Multiple per file, imported with curly braces.  
> **CommonJS** is synchronous. **ES Modules** are asynchronous.

---

## 22. Design Patterns

### Singleton Pattern

Ensures only **one instance** of a class exists.

```js
class Database {
  constructor() {
    if (Database.instance) return Database.instance;
    this.connection = "DB Connected";
    Database.instance = this;
  }
}

const db1 = new Database();
const db2 = new Database();
console.log(db1 === db2); // true
```

---

### Module Pattern

Uses IIFE + closures to encapsulate private state.

```js
const counter = (() => {
  let count = 0; // private

  return {
    increment() { count++; },
    decrement() { count--; },
    getCount()  { return count; }
  };
})();

counter.increment();
console.log(counter.getCount()); // 1
```

---

### Observer Pattern

One subject notifies multiple observers when its state changes.

```js
class EventEmitter {
  constructor() { this.events = {}; }

  on(event, listener) {
    if (!this.events[event]) this.events[event] = [];
    this.events[event].push(listener);
  }

  emit(event, data) {
    (this.events[event] || []).forEach(listener => listener(data));
  }
}

const emitter = new EventEmitter();
emitter.on("data", d => console.log("Received:", d));
emitter.emit("data", { name: "Alice" }); // "Received: { name: 'Alice' }"
```

---

### Factory Pattern

Creates objects without specifying the exact class or constructor.

```js
function createUser(role) {
  if (role === "admin") return { role, permissions: ["read", "write", "delete"] };
  if (role === "user")  return { role, permissions: ["read"] };
}

const admin = createUser("admin");
const user  = createUser("user");
```

---

## 23. Security

### XSS (Cross-Site Scripting)

**Definition:** An attacker injects malicious scripts into web pages viewed by other users.

**Prevention:**
- Sanitize user input before rendering
- Use `textContent` instead of `innerHTML`
- Set Content Security Policy (CSP) headers
- Avoid `eval()`

```js
// Vulnerable
element.innerHTML = userInput;

// Safe
element.textContent = userInput;
```

---

### SQL Injection

**Definition:** Attacker inserts malicious SQL code into a query to manipulate the database.

**Prevention:** Use parameterized queries/prepared statements. Validate and sanitize all user inputs.

---

### CSRF (Cross-Site Request Forgery)

**Definition:** Tricks an authenticated user into submitting unwanted requests to a site they are logged into.

**Prevention:** Use CSRF tokens, `SameSite` cookie attribute, verify `Origin`/`Referer` headers.

---

### `eval()` — Avoid in Production

**Definition:** Evaluates a string as JavaScript code. Poses severe security risks and performance issues.

```js
// Dangerous — never use with user input
eval("alert('hacked!')");

// Safe alternatives
JSON.parse(jsonString); // for JSON parsing
```

---

## 24. Interview Q&A — Tricky Concepts

### Q: What is the difference between `null` and `undefined`?
- `undefined` — JS assigned it automatically (variable declared, no value)
- `null` — Developer intentionally set it to represent "no value"

---

### Q: What is `typeof null`?
```js
console.log(typeof null); // "object"
```
This is a long-standing JavaScript bug that was never fixed for backward compatibility reasons.

---

### Q: Explain the event loop.
JavaScript is single-threaded. The event loop enables async behavior. Synchronous code runs first (call stack). Async callbacks go to the Task Queue, and Promise callbacks go to the Microtask Queue. The event loop moves tasks to the call stack only when it is empty. **Microtasks always run before macrotasks.**

---

### Q: What is the output?
```js
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
// Output: 3 3 3
// Reason: var is function-scoped; all closures share the same 'i' = 3
```

---

### Q: What is the output?
```js
console.log(1);
setTimeout(() => console.log(2), 0);
Promise.resolve().then(() => console.log(3));
console.log(4);

// Output: 1  4  3  2
// Sync first (1, 4), then microtasks (3), then macrotasks (2)
```

---

### Q: Difference between `call`, `apply`, and `bind`?
- `call(ctx, a, b)` — Invokes immediately, comma-separated args
- `apply(ctx, [a, b])` — Invokes immediately, args as array
- `bind(ctx, a)` — Returns a new function, does NOT invoke immediately

---

### Q: What is `NaN` and how do you check for it?
`NaN` (Not a Number) is the result of a failed numeric operation. `NaN !== NaN` is always `true`.

```js
isNaN("hello");         // true  (unreliable — coerces first)
Number.isNaN("hello");  // false (reliable — no coercion)
Number.isNaN(NaN);      // true
```

---

### Q: Difference between `slice` and `splice`?

| | `slice` | `splice` |
|--|---------|---------|
| Mutates original | No | Yes |
| Returns | New sub-array | Array of removed elements |
| Use | Read-only copy of a portion | Add/remove/replace in-place |

---

### Q: What is `Promise.all` vs `Promise.allSettled`?
- `Promise.all` — Fails fast: rejects immediately if **any** promise rejects
- `Promise.allSettled` — Waits for all to finish regardless; never rejects; returns status of each

---

### Q: What are the ways to create objects in JavaScript?
```js
// 1. Object literal
const obj = { name: "Alice" };

// 2. Constructor function
function Person(name) { this.name = name; }
const p = new Person("Bob");

// 3. Object.create()
const proto = { greet() { return "Hi"; } };
const obj2  = Object.create(proto);

// 4. Class
class Car { constructor(brand) { this.brand = brand; } }
const car = new Car("Toyota");

// 5. Factory function
const createUser = (name) => ({ name, role: "user" });
```

---

### Q: What is the difference between `function declaration` and `function expression`?

| | Declaration | Expression |
|--|-------------|------------|
| Hoisted | Fully (can call before definition) | Only variable (not value) |
| Name | Required | Optional |
| Call before definition | Yes | No |

---

### Q: What is debouncing vs throttling?
- **Debounce** — Waits for a pause in calls before executing. Used for search input, resize handlers.
- **Throttle** — Executes at most once per interval. Used for scroll events, mouse move.

---

### Q: How does `async/await` handle errors?
```js
async function fetchData() {
  try {
    const res = await fetch("/api");
    return await res.json();
  } catch (err) {
    console.error("Failed:", err);
  }
}
```
Without `try/catch`, unhandled promise rejections occur. You can also use `.catch()` on the async function's returned Promise.

---

### Q: What is the prototype chain?
Every object has `__proto__` pointing to its prototype. When a property is not found on the object, JavaScript looks up the chain until it finds it or reaches `null`. This is the basis of JavaScript inheritance.

---

> **Final Interview Tips:**
> - Always explain your reasoning step-by-step out loud
> - When tracing output, go line by line mentally — check sync, then microtask, then macrotask order
> - Mention edge cases: `typeof null === "object"`, `NaN !== NaN`, empty array `[]` is truthy
> - Relate abstract concepts to real use-cases — closures for private state, debounce for search boxes, event delegation for dynamic lists
> - Write clean, readable code without an IDE — naming matters
