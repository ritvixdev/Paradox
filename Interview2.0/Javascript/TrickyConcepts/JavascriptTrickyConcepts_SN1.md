# ⚡ JavaScript Interview Tricks — Complete Guide
> Every gotcha, every output trap, every concept interviewers use to test depth.
> Divided into three levels so you can stop, absorb, and come back.

---

## How to Use This Guide

| Level | Who it's for | Topics |
|---|---|---|
| 🟢 **Basic** | First interview or JS refresher | typeof, ==, truthy/falsy, sort, var/let/const |
| 🟡 **Intermediate** | 1–2 years experience | Closures, this, hoisting, prototypes, event loop |
| 🔴 **Advanced** | Senior roles, deep dive | Currying, IIFE, call/apply/bind, Promises, edge cases |

**Tip:** Read one level per session. Each level ends with a quick-fire recap before you move to the next.

---

## Table of Contents

**🟢 Level 1 — Basic (Questions 1–10)**
1. [typeof — Every Surprise](#1-typeof--every-surprise)
2. [== vs === — Equality Trap](#2--vs----equality-trap)
3. [Truthy and Falsy — The Contradiction](#3-truthy-and-falsy--the-contradiction)
4. [null vs undefined vs NaN](#4-null-vs-undefined-vs-nan)
5. [Array.sort() — Not What You Think](#5-arraysort--not-what-you-think)
6. [The + Operator — Type Coercion](#6-the--operator--type-coercion)
7. [const is NOT Immutable](#7-const-is-not-immutable)
8. [Array and Object Reference Trap](#8-array-and-object-reference-trap)
9. [Floating Point — 0.1 + 0.2 ≠ 0.3](#9-floating-point--01--02--03)
10. [for...in vs for...of — The Danger](#10-forin-vs-forof--the-danger)

**🟡 Level 2 — Intermediate (Questions 11–22)**
11. [var / let / const + Hoisting](#11-var--let--const--hoisting)
12. [Variable Shadowing](#12-variable-shadowing)
13. [Closures — The Loop Trap](#13-closures--the-loop-trap)
14. [this — Every Tricky Scenario](#14-this--every-tricky-scenario)
15. [Prototypes and Prototype Chain](#15-prototypes-and-prototype-chain)
16. [Shallow Copy vs Deep Copy](#16-shallow-copy-vs-deep-copy)
17. [Array Methods — Mutate vs Return New](#17-array-methods--mutate-vs-return-new)
18. [delete Operator Surprises](#18-delete-operator-surprises)
19. [arguments vs Rest Params](#19-arguments-vs-rest-params)
20. [Destructuring Edge Cases](#20-destructuring-edge-cases)
21. [Optional Chaining and Nullish Coalescing](#21-optional-chaining-and-nullish-coalescing)
22. [Object Keys Are Always Strings](#22-object-keys-are-always-strings)

**🔴 Level 3 — Advanced (Questions 23–35)**
23. [Event Loop — Full Execution Order](#23-event-loop--full-execution-order)
24. [Promise Chaining + Promise Methods](#24-promise-chaining--promise-methods)
25. [call / apply / bind](#25-call--apply--bind)
26. [new Keyword — What It Really Does](#26-new-keyword--what-it-really-does)
27. [IIFE — Syntax Trap + var Leak](#27-iife--syntax-trap--var-leak)
28. [Undeclared Variables Become Global](#28-undeclared-variables-become-global)
29. [Currying and Partial Application](#29-currying-and-partial-application)
30. [Memoization — Closure + Cache Pattern](#30-memoization--closure--cache-pattern)
31. [Getter and Setter Trap](#31-getter-and-setter-trap)
32. [setTimeout(fn, 0) Is Never Instant](#32-settimeoutfn-0-is-never-instant)
33. [Weird + Combinations — Every Edge Case](#33-weird--combinations--every-edge-case)
34. [String Methods That Surprise](#34-string-methods-that-surprise)
35. [Object.is() vs === vs ==](#35-objectis-vs--vs-)

**📋 Master Summary**
36. [Every Rule in One Place](#36-master-summary--every-rule-in-one-place)

---

---

# 🟢 LEVEL 1 — BASIC
### What to expect: Output questions on fundamentals. These come up in every interview regardless of level.
### Goal: Read through all 10 questions. If any surprise you, that's your study target.

---

## 1. typeof — Every Surprise

### ❓ Output?
```js
console.log(typeof null);
console.log(typeof []);
console.log(typeof NaN);
console.log(typeof function(){});
console.log(typeof undefined);
```

### 😱 Answer
```
"object"    ← famous 1995 bug — null is NOT an object
"object"    ← use Array.isArray() to distinguish arrays
"number"    ← NaN is of type number, surprising
"function"  ← functions get their own type
"undefined"
```

### 🧠 Why It Matters
`typeof null === "object"` is a bug from 1995 that was never fixed — null's internal bit pattern matched the object type tag. Too much old code relied on it so it stayed.

**The correct checks:**
```js
x === null                                           // ✅ check null
Array.isArray(x)                                     // ✅ check array
Number.isNaN(x)                                      // ✅ check NaN
typeof x === "object" && x !== null && !Array.isArray(x)  // ✅ true object
```

### 📌 Full typeof Reference
| Value | typeof |
|---|---|
| `42` | `"number"` |
| `"hello"` | `"string"` |
| `true` | `"boolean"` |
| `undefined` | `"undefined"` |
| `null` | `"object"` ← bug |
| `[]` | `"object"` ← use Array.isArray |
| `{}` | `"object"` |
| `function(){}` | `"function"` |
| `NaN` | `"number"` ← quirk |
| `Symbol()` | `"symbol"` |

---

## 2. == vs === — Equality Trap

### ❓ Output every one:
```js
console.log(5 == "5");
console.log(5 === "5");
console.log(0 == false);
console.log(null == undefined);
console.log(null == 0);
console.log(NaN == NaN);
```

### 😱 Answer
```
true    // "5" coerced to 5
false   // strict — different types
true    // false → 0, 0 == 0
true    // special rule: only these two are equal with ==
false   // null only equals undefined, nothing else
false   // NaN never equals anything including itself
```

### 🧠 The Rule
`==` converts types before comparing (coercion). `===` checks value AND type — no conversion.

**Memorise these pairs:**
| Expression | Result | Reason |
|---|---|---|
| `0 == false` | `true` | false → 0 |
| `"" == false` | `true` | both → 0 |
| `null == undefined` | `true` | special rule |
| `null == 0` | `false` | null only equals undefined |
| `NaN == NaN` | `false` | NaN ≠ anything |
| `[] == false` | `true` | [] → "" → 0, false → 0 |
| `[] == ![]` | `true` | ![] = false, then [] == false |

> **Rule: Always use `===`. The only acceptable `==` is `x == null` to catch both null and undefined at once.**

---

## 3. Truthy and Falsy — The Contradiction

### ❓ Output?
```js
console.log(Boolean([]));
console.log(Boolean("0"));
console.log([] == false);
if ([]) console.log("array is truthy");
```

### 😱 Answer
```
true    // [] is truthy — it's an object
true    // "0" is truthy — non-empty string
true    // but [] == false is ALSO true (coercion!)
"array is truthy"
```

### 🧠 The Contradiction
- `if ([])` → truthy — no coercion, just checks truthiness
- `[] == false` → `true` — `==` does coercion: `[] → "" → 0`, `false → 0`

Same value, opposite behaviour depending on context. This is one of the most asked trick questions.

**The 6 falsy values — memorise exactly these, nothing else:**
```
false    0    ""    null    undefined    NaN
```
**Everything else is truthy** — including: `[]`, `{}`, `"0"`, `"false"`, `-1`, `Infinity`

---

## 4. null vs undefined vs NaN

### ❓ Output?
```js
console.log(null + 1);
console.log(undefined + 1);
console.log(NaN + 1);
console.log(isNaN("hello"));
console.log(Number.isNaN("hello"));
```

### 😱 Answer
```
1      // null → 0 in arithmetic
NaN    // undefined → NaN in arithmetic
NaN    // NaN contaminates all math
true   // converts "hello" to NaN first, then checks
false  // doesn't coerce — "hello" is a string, not NaN
```

### 🧠 The Key Difference
- `isNaN(x)` — converts `x` to number first, THEN checks. `isNaN("hello")` = true because `Number("hello")` = `NaN`
- `Number.isNaN(x)` — no conversion. Only true if `x` is literally `NaN`.

| | Meaning |
|---|---|
| `null` | Intentional absence — you set it |
| `undefined` | Variable exists but never assigned a value |
| `NaN` | Result of invalid math (`"abc" / 2`) |

---

## 5. Array.sort() — Not What You Think

### ❓ Output?
```js
console.log([10, 9, 2, 21, 3].sort());
console.log([1, "10", 2, "100", 20].sort());
```

### 😱 Answer
```
[10, 2, 21, 3, 9]
[1, "10", "100", 2, 20]
```

### 🧠 Concept
`.sort()` converts everything to **strings** first, then sorts **alphabetically**. "10" comes before "2" because the character "1" comes before "2" in the alphabet.

**Fix — always pass a compare function for numbers:**
```js
[10, 9, 2, 21, 3].sort((a, b) => a - b);  // [2, 3, 9, 10, 21] ascending
[10, 9, 2, 21, 3].sort((a, b) => b - a);  // [21, 10, 9, 3, 2] descending
```

Compare function rules: negative → a first, positive → b first, zero → unchanged.

> **⚠️ `.sort()` also mutates the original array — it returns the same array, sorted.**

---

## 6. The + Operator — Type Coercion

### ❓ Output?
```js
let k = 0;
for (let val of [1, 2, 3, "10", 4]) {
  k += val;
}
console.log(k);

console.log("5" - 2);
console.log("5" + 2);
console.log(+"5");
```

### 😱 Answer
```
"6104"    // once "10" enters, + flips to concatenation
3         // subtraction always forces numeric
"52"      // + sees a string → concatenation
5         // unary + converts string to number
```

### 🧠 Concept
`+` has two jobs — **addition** or **string concatenation**. The moment a string enters the chain, everything flips to concatenation permanently.

- `-`, `*`, `/`, `%` → always numeric, strings coerced
- Only `+` has this dual behaviour

**Unary `+`** before a value converts it to a number: `+"5"` = `5`, `+true` = `1`, `+null` = `0`, `+undefined` = `NaN`

---

## 7. const is NOT Immutable

### ❓ Output?
```js
const obj = { name: "Ash" };
obj.name = "Bob";
obj.age = 25;
console.log(obj);

const arr = [1, 2, 3];
arr.push(4);
console.log(arr);

obj = {};  // what happens here?
```

### 😱 Answer
```
{ name: "Bob", age: 25 }    // mutation is fine
[1, 2, 3, 4]                 // mutation is fine
TypeError: Assignment to constant variable
```

### 🧠 Concept
`const` prevents **reassignment** of the variable binding — it does NOT prevent mutation of the value.

```js
const x = { a: 1 };
x.a = 2;    // ✅ mutating the object — allowed
x = {};     // ❌ reassigning the variable — TypeError
```

**To truly freeze an object:** `Object.freeze(obj)` — prevents adding, removing, or changing properties (shallow only).

---

## 8. Array and Object Reference Trap

### ❓ Output?
```js
console.log([] === []);
console.log({} === {});

const a = [1, 2, 3];
const b = a;
b.push(4);
console.log(a);

function addItem(arr) { arr.push(99); }
const myArr = [1, 2, 3];
addItem(myArr);
console.log(myArr);
```

### 😱 Answer
```
false            // different references — different memory addresses
false            // same reason
[1, 2, 3, 4]    // b and a point to the SAME array
[1, 2, 3, 99]   // function mutated the original!
```

### 🧠 Concept
Objects and arrays are compared and passed by **reference**, not by value.
- `[] === []` — two separate arrays at different memory addresses → not equal
- `const b = a` — b holds the same reference as a → same array → mutation affects both
- Passing to a function → function gets the reference → mutations affect the original

**Primitives** (numbers, strings, booleans) are copied by value — functions cannot mutate them.

---

## 9. Floating Point — 0.1 + 0.2 ≠ 0.3

### ❓ Output?
```js
console.log(0.1 + 0.2);
console.log(0.1 + 0.2 === 0.3);
```

### 😱 Answer
```
0.30000000000000004
false
```

### 🧠 Concept
Computers store numbers in binary. `0.1` cannot be represented exactly — like `1/3` = `0.333...` in decimal. This is IEEE 754 floating point. Happens in every language, not just JS.

**Safe comparison:** `Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON` → `true`

> **Never compare floats with `===`. Always use a tolerance.**

---

## 10. for...in vs for...of — The Danger

### ❓ Output?
```js
const arr = [10, 20, 30];
arr.custom = "hello";

for (let i in arr) {
  console.log(i);
}

for (let v of arr) {
  console.log(v);
}
```

### 😱 Answer
```
// for...in:
0        // key
1        // key
2        // key
custom   // ← also picks up custom properties!

// for...of:
10
20
30       // only actual values
```

### 🧠 Concept
| | Iterates | Safe for arrays? |
|---|---|---|
| `for...in` | Keys + all enumerable properties including inherited | ❌ No |
| `for...of` | Values of iterables only | ✅ Yes |

> **Never use `for...in` on arrays. Use `for...of` or `.forEach()`.**

---

### 🟢 Level 1 Recap — Before You Move On

Quick-fire — what do these print?

```js
typeof null          // ?
[] === []            // ?
0 == false           // ?
Boolean([])          // ?
0.1 + 0.2 === 0.3    // ?
[2, 10, 1].sort()    // ?
const a = {}; a.x = 1; a = {};  // ?
```

**Answers:** `"object"` / `false` / `true` / `true` / `false` / `[1, 10, 2]` / `TypeError`

If you got all 7 → move to Level 2. If not → re-read the ones you missed.

---

---

# 🟡 LEVEL 2 — INTERMEDIATE
### What to expect: These questions test how well you understand scope, closures, and how JavaScript executes code — not just what it looks like.
### Goal: Understand each answer before moving on. These are the most common mid-level interview questions.

---

## 11. var / let / const + Hoisting

### ❓ Output?
```js
console.log(a);
console.log(b);
var a = 5;
let b = 10;
```

### 😱 Answer
```
undefined
ReferenceError: Cannot access 'b' before initialization
```

### ❓ Another one:
```js
function test() {
  if (true) {
    var x = 1;
    let y = 2;
  }
  console.log(x);
  console.log(y);
}
test();
```

### 😱 Answer
```
1
ReferenceError: y is not defined
```

### 🧠 Concept — Hoisting

JavaScript reads through your file before running it. During this read, it **hoists** (moves up) declarations.

- `var` → hoisted to top of function, initialised as `undefined`
- `let`/`const` → hoisted but stuck in the **Temporal Dead Zone (TDZ)** — accessing it before the declaration line throws `ReferenceError`
- `var` is **function-scoped** — it escapes `if/for` blocks
- `let`/`const` are **block-scoped** — they die at the closing `}`

| | Scope | Hoisted as | Safe before declaration? |
|---|---|---|---|
| `var` | Function | `undefined` | Returns `undefined` |
| `let` | Block | TDZ | `ReferenceError` |
| `const` | Block | TDZ | `ReferenceError` |

### ❓ Function hoisting:
```js
console.log(sayHello());
console.log(sayHi());

function sayHello() { return "Hello!"; }
var sayHi = function() { return "Hi!"; };
```

### 😱 Answer
```
"Hello!"
TypeError: sayHi is not a function
```

Function **declarations** are fully hoisted. Function **expressions** assigned to `var` — only the `var` is hoisted (as `undefined`). Calling `undefined()` = `TypeError`.

---

## 12. Variable Shadowing

### ❓ Output?
```js
var name = "global";

function sayName() {
  console.log(name);    // line A
  var name = "local";
  console.log(name);    // line B
}

sayName();
```

### 😱 Answer
```
undefined
"local"
```

### 🧠 Concept
This combines **hoisting + shadowing**.

Inside `sayName`, `var name` is hoisted to the top of the function. It **shadows** the global `name` — but at line A, the local `name` exists (hoisted) yet hasn't been assigned → `undefined`. At line B, it's assigned → `"local"`.

The global `name` is never read at all — the local hoisted declaration blocks it from the start.

---

## 13. Closures — The Loop Trap

### ❓ Output?
```js
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
```

### 😱 Answer
```
3
3
3
```

### ❓ Same but with let:
```js
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
```

### 😱 Answer
```
0
1
2
```

### 🧠 Concept — Why This Happens
`var` is function-scoped — there is **one shared `i`** for the whole loop. `setTimeout` fires after the loop ends. By then `i = 3`. All three callbacks share the same reference to the same `i`.

`let` creates a **brand new `i`** for every iteration. Each closure captures its own independent copy.

**Three fixes for the var version:**
```js
// Fix 1: use let (simplest)
for (let i = 0; i < 3; i++) { ... }

// Fix 2: IIFE — immediately capture the value
for (var i = 0; i < 3; i++) {
  ((j) => setTimeout(() => console.log(j), 0))(i);
}

// Fix 3: bind
for (var i = 0; i < 3; i++) {
  setTimeout(console.log.bind(null, i), 0);
}
```

### ❓ Closure private counter:
```js
function makeCounter() {
  let count = 0;
  return {
    increment() { count++; },
    get() { return count; }
  };
}
const c = makeCounter();
c.increment();
c.increment();
console.log(c.get());
console.log(c.count);
```

### 😱 Answer
```
2
undefined   // count is private — not accessible from outside
```

This is the **closure as private state** pattern. `count` lives in `makeCounter`'s scope. The returned object has access via closure, but external code cannot reach `count` directly.

---

## 14. this — Every Tricky Scenario

### ❓ Output?
```js
const user = {
  name: "Suvam",
  getName: function() { return this.name; },
  getNameArrow: () => this.name,
  nested: {
    name: "Nested",
    getName: function() { return this.name; }
  }
};

console.log(user.getName());
console.log(user.getNameArrow());
console.log(user.nested.getName());

const fn = user.getName;
console.log(fn());
```

### 😱 Answer
```
"Suvam"
undefined       // arrow — this = global, no name property there
"Nested"        // this = user.nested (object before the dot)
undefined       // detached — this = global, no name there
```

### ❓ The forEach trap:
```js
const obj = {
  name: "Suvam",
  items: [1, 2, 3],
  print: function() {
    this.items.forEach(function(item) {
      console.log(this.name, item);
    });
  }
};
obj.print();
```

### 😱 Answer
```
undefined 1
undefined 2
undefined 3
```

Inside `forEach`, the callback is a plain function — `this` = global (no object before the dot). Fix: use an arrow function which borrows `this` from `print`.

### 🧠 The 4 this Rules (priority order)

| Priority | Rule | How | `this` value |
|---|---|---|---|
| 1 | `new` | `new Fn()` | New empty object |
| 2 | Explicit | `.call()` / `.apply()` / `.bind()` | What you pass |
| 3 | Implicit | `obj.method()` | Object before the dot |
| 4 | Default | `fn()` | Global / `undefined` (strict mode) |

**Arrow functions ignore all 4 rules** — always inherit `this` from where they were **defined**.

---

## 15. Prototypes and Prototype Chain

### ❓ Output?
```js
function Animal(name) { this.name = name; }
Animal.prototype.speak = function() { return this.name + " speaks"; };

const a1 = new Animal("Dog");
const a2 = new Animal("Cat");

console.log(a1.speak === a2.speak);
console.log(a1.hasOwnProperty("name"));
console.log(a1.hasOwnProperty("speak"));
console.log(a1 instanceof Animal);
```

### 😱 Answer
```
true    // same function — lives once on prototype, shared by all
true    // name set directly on instance by constructor
false   // speak lives on Animal.prototype, not on a1
true
```

### ❓ Live prototype — tricky:
```js
function Foo() {}
const f1 = new Foo();
const f2 = new Foo();

Foo.prototype.greet = function() { return "hello"; };

console.log(f1.greet());
```

### 😱 Answer
```
"hello"
```

Adding to prototype **after** creating instances still works. Instances don't copy the prototype — they hold a **live reference** to it.

### 🧠 Concept — The Chain
```
instance  →  Constructor.prototype  →  Object.prototype  →  null
```
When you access `instance.method()`, JS looks on the instance first. Not found? Looks up the chain. This continues until `null`.

- `prototype` → property on **constructor functions** — what instances will inherit
- `__proto__` → property on every **instance** — the actual live link

```js
Animal.prototype === a1.__proto__   // true
```

**ES6 class = same prototype chain, cleaner syntax.** Classes are syntactic sugar — under the hood, identical prototype behaviour.

---

## 16. Shallow Copy vs Deep Copy

### ❓ Output?
```js
const original = { name: "Ash", scores: [1, 2, 3] };
const copy = { ...original };

copy.name = "Bob";
copy.scores.push(4);

console.log(original.name);
console.log(original.scores);
```

### 😱 Answer
```
"Ash"           // string is primitive — separate copy
[1, 2, 3, 4]   // array is reference — both point to same array!
```

### 🧠 Concept
`{...obj}` (spread) creates a **shallow copy** — top-level primitives are truly copied, but nested objects/arrays are still shared references.

| Method | Top-level primitives | Nested objects | Functions |
|---|---|---|---|
| `= assignment` | Shared | Shared | Shared |
| `{...spread}` | ✅ Copied | ❌ Shared | ❌ Shared |
| `JSON.parse(JSON.stringify())` | ✅ Copied | ✅ Copied | ❌ Lost |
| `structuredClone()` | ✅ Copied | ✅ Copied | ❌ Lost |

**Use `structuredClone(obj)` for deep copies — it's modern, built-in, and recommended.**

---

## 17. Array Methods — Mutate vs Return New

### ❓ Output?
```js
const arr = [3, 1, 4, 1, 5];

const sorted = arr.sort();
console.log(arr === sorted);
console.log(arr);

const mapped = arr.map(x => x * 2);
console.log(arr === mapped);
```

### 😱 Answer
```
true              // sort returns the same array
[1, 1, 3, 4, 5]  // original was mutated!
false             // map returns a NEW array
```

### 🧠 Concept

| Mutates original ⚠️ | Returns new array ✅ |
|---|---|
| `.sort()` | `.map()` |
| `.reverse()` | `.filter()` |
| `.push()` / `.pop()` | `.slice()` |
| `.shift()` / `.unshift()` | `.concat()` |
| `.splice()` | `.flat()` |
| `.fill()` | `.reduce()` → single value |

> **`.sort()` and `.reverse()` both mutate AND return the same array. People always forget this.**

---

## 18. delete Operator Surprises

### ❓ Output?
```js
const obj = { a: 1, b: 2 };
delete obj.a;
console.log(obj);

const arr = [1, 2, 3, 4];
delete arr[1];
console.log(arr);
console.log(arr.length);
```

### 😱 Answer
```
{ b: 2 }
[1, empty, 3, 4]   // hole — not removed!
4                   // length unchanged!
```

### 🧠 Concept
- `delete obj.prop` → removes property ✅
- `delete arr[index]` → leaves a **hole** (empty slot), length stays the same ❌
- Use `.splice(index, 1)` to properly remove an array element

---

## 19. arguments vs Rest Params

### ❓ Output?
```js
function regular(a, b) {
  console.log(arguments[0]);
  console.log(Array.isArray(arguments));
}

const arrow = () => {
  console.log(arguments[0]);
};

regular(1, 2);
arrow(1, 2);
```

### 😱 Answer
```
1
false                                  // arguments is NOT a real array
ReferenceError: arguments is not defined  // arrow functions have no arguments
```

### 🧠 Concept
- `arguments` — only in **regular functions**. Array-like (has indices, `length`) but NOT a real array. No `.map()`, no `.filter()`.
- Arrow functions have **no `arguments` object** — use rest params instead.

**Modern way — rest params (always a real array):**
```js
function sum(...args) {
  return args.reduce((a, b) => a + b, 0);  // args is a real array
}
```

---

## 20. Destructuring Edge Cases

### ❓ Output?
```js
const [a, , b, c = 10] = [1, 2, 3];
console.log(a, b, c);

const { x: renamed, y = 5, ...rest } = { x: 1, z: 9 };
console.log(renamed, y, rest);

function fn({ name, age = 25 } = {}) {
  console.log(name, age);
}
fn({ name: "Ash" });
fn();
```

### 😱 Answer
```
1 3 10              // skip middle, c defaults (3rd slot has no 4th value)
1 5 { z: 9 }        // renamed, y defaults, rest gets remaining
"Ash" 25
undefined 25        // default {} prevents crash when no argument passed
```

### 🧠 Key Tricks
- `, ,` — skip an element
- `= default` — use when value is `undefined`
- `{ key: newName }` — rename while destructuring
- `...rest` — collect remaining
- `= {}` in params — prevents TypeError on missing argument

---

## 21. Optional Chaining and Nullish Coalescing

### ❓ Output?
```js
const user = { profile: { name: "Ash" } };

console.log(user?.profile?.name);
console.log(user?.address?.city);

console.log(null ?? "default");
console.log(0 ?? "default");
console.log(0 || "default");
console.log("" ?? "default");
console.log("" || "default");
```

### 😱 Answer
```
"Ash"
undefined     // no error — optional chaining returns undefined
"default"     // null → use right side
0             // 0 is not null/undefined → keep 0
"default"     // || treats 0 as falsy → use right side
""            // "" is not null/undefined → keep ""
"default"     // || treats "" as falsy → use right side
```

### 🧠 Concept
- `?.` (optional chaining) → returns `undefined` instead of throwing if anything in the chain is `null`/`undefined`
- `??` (nullish coalescing) → right side ONLY if left is `null` or `undefined`
- `||` → right side for ANY falsy value including `0`, `""`, `false`

**Use `??` when `0` and `""` are valid values you want to keep.**

---

## 22. Object Keys Are Always Strings

### ❓ Output?
```js
const a = {};
const b = { key: "b" };
const c = { key: "c" };

a[b] = "value1";
a[c] = "value2";

console.log(a[b]);
console.log(Object.keys(a));
```

### 😱 Answer
```
"value2"             // not "value1"!
["[object Object]"]  // only one key!
```

### 🧠 Concept
Object keys are always **strings** (or Symbols). Using an object as a key converts it to a string via `.toString()` — both `b` and `c` become `"[object Object]"`. So `a[c] = "value2"` overwrites `a[b] = "value1"`.

**Use `Map` when you need object keys:**
```js
const map = new Map();
map.set(b, "value1");
map.set(c, "value2");
map.get(b);  // "value1" — Map preserves identity
```

---

### 🟡 Level 2 Recap — Before You Move On

Quick-fire:

```js
// What prints?
for (var i = 0; i < 3; i++) { setTimeout(() => console.log(i), 0); }

const obj = { x: 1, arr: [1,2] };
const copy = {...obj};
copy.arr.push(3);
console.log(obj.arr);   // ?

console.log(0 ?? "x");  // ?
console.log(0 || "x");  // ?
```

**Answers:** `3 3 3` / `[1, 2, 3]` / `0` / `"x"`

All correct → you're ready for Level 3. Missed some → reread those sections.

---

---

# 🔴 LEVEL 3 — ADVANCED
### What to expect: These are the questions that separate junior from senior. Async execution, prototype manipulation, function patterns, and the really weird edge cases.
### Goal: Understanding here shows depth. You don't need to memorise all of it — understanding WHY matters more.

---

## 23. Event Loop — Full Execution Order

### ❓ Output?
```js
console.log("A");
setTimeout(() => console.log("B"), 0);
Promise.resolve().then(() => console.log("C"));
console.log("D");
```

### 😱 Answer
```
A
D
C
B
```

### ❓ Harder — with Promise constructor:
```js
console.log("1");

new Promise((resolve) => {
  console.log("2");
  resolve();
}).then(() => console.log("3"))
  .then(() => console.log("4"));

queueMicrotask(() => console.log("5"));

setTimeout(() => console.log("6"), 0);

console.log("7");
```

### 😱 Answer
```
1    // sync
2    // Promise constructor is SYNC
7    // sync
3    // microtask (first .then)
5    // microtask (queueMicrotask)
4    // microtask (second .then, queued after 3 ran)
6    // macrotask (setTimeout)
```

### 🧠 Concept — Three Queues

```
1. Call Stack (synchronous)     — runs first, always
   ↓ when stack is empty:
2. Microtask Queue              — drains COMPLETELY
   - Promise .then() / .catch()
   - queueMicrotask()
   ↓ after microtasks are empty:
3. Macrotask Queue              — one task, then microtasks drain again
   - setTimeout
   - setInterval
   - fetch callbacks
```

**Key facts:**
- Promise **constructor** runs synchronously — only `.then()` is async
- `setTimeout(fn, 0)` is minimum delay, not instant — still goes through macrotask queue
- Microtasks completely drain after every macrotask

---

## 24. Promise Chaining + Promise Methods

### ❓ Output?
```js
Promise.resolve(1)
  .then(v => { console.log(v); return v + 1; })
  .then(v => { console.log(v); throw new Error("oops"); })
  .then(v => { console.log("never:", v); })
  .catch(e => { console.log("caught:", e.message); return 99; })
  .then(v => { console.log("after:", v); });
```

### 😱 Answer
```
1
2
caught: oops
after: 99
```

### ❓ Promise.all vs allSettled:
```js
Promise.all([
  Promise.resolve(1),
  Promise.reject("error"),
  Promise.resolve(3)
]).catch(e => console.log("all failed:", e));

Promise.allSettled([
  Promise.resolve(1),
  Promise.reject("error"),
  Promise.resolve(3)
]).then(results => console.log(results.map(r => r.status)));
```

### 😱 Answer
```
all failed: error
["fulfilled", "rejected", "fulfilled"]
```

### 🧠 Promise Methods Compared

| Method | Resolves when | Rejects when |
|---|---|---|
| `Promise.all` | ALL resolve | ANY rejects — fails fast |
| `Promise.allSettled` | ALL settle (any result) | Never |
| `Promise.any` | FIRST resolves | ALL reject |
| `Promise.race` | FIRST settles (any) | FIRST rejects |

**Chaining rule:** If any `.then()` throws, it skips all following `.then()` until the next `.catch()`. After `.catch()` handles it, chaining resumes normally.

---

## 25. call / apply / bind

### ❓ Output?
```js
function greet(greeting) { return greeting + " " + this.name; }
const person = { name: "Suvam" };

console.log(greet.call(person, "Hello"));
console.log(greet.apply(person, ["Hi"]));
const bound = greet.bind(person, "Hey");
console.log(bound());
```

### 😱 Answer
```
"Hello Suvam"
"Hi Suvam"
"Hey Suvam"
```

### ❓ Can you rebind?
```js
function show() { return this.val; }
const b1 = show.bind({ val: 1 });
const b2 = b1.bind({ val: 2 });
console.log(b2());
```

### 😱 Answer
```
1   // first bind is permanent — cannot be overridden
```

### 🧠 Concept

| Method | Runs immediately? | Args format |
|---|---|---|
| `call(obj, a, b)` | ✅ Yes | Individual |
| `apply(obj, [a, b])` | ✅ Yes | Array |
| `bind(obj, a)` | ❌ Returns new function | Individual (pre-set) |

**Memory trick:** A for Apply = Array. B for Bind = does not run (Better call later).

Once bound, **cannot be rebound**. First `bind` wins forever.

---

## 26. new Keyword — What It Really Does

### ❓ Output?
```js
function Person(name) { this.name = name; }

const p = new Person("Ash");
const q = Person("Bob");  // no new!

console.log(p.name);
console.log(q);
console.log(typeof name);  // global scope
```

### 😱 Answer
```
"Ash"
undefined          // Person() returned nothing
"string"           // "Bob" leaked to global scope!
```

### ❓ What if constructor returns an object?
```js
function Trick() {
  this.x = 1;
  return { y: 2 };
}
const t = new Trick();
console.log(t.x);
console.log(t.y);
```

### 😱 Answer
```
undefined   // this.x = 1 is discarded
2           // explicit object return wins over this
```

### 🧠 What `new` does — 4 steps:
1. Creates empty object `{}`
2. Sets its `__proto__` to `Constructor.prototype`
3. Calls constructor with `this` = the new object
4. Returns the object — **unless** constructor explicitly returns a different object

Without `new`: `this` = global → properties leak to global scope.

---

## 27. IIFE — Syntax Trap + var Leak

### ❓ Which ones work and what prints?
```js
function foo() {}();        // A
(function foo() {})();      // B — prints nothing (empty)
!function() { return 1; }() // C
```

### 😱 Answer
```
A → SyntaxError — function declaration can't be immediately invoked
B → runs silently ✅
C → runs, returns false (! negates the return value 1) ✅
```

### ❓ The a=b=3 trap:
```js
(function() {
  var a = b = 3;
})();

console.log(typeof a);
console.log(typeof b);
```

### 😱 Answer
```
"undefined"   // a is scoped to IIFE — gone outside
"number"      // b leaked to global scope!
```

### 🧠 Concept — Two Tricks in One

**IIFE syntax:** A function **declaration** cannot be immediately invoked. Wrap in `()` or prefix with `!`, `+`, `-`, `~` to make it an expression, then call it.

**The `var a = b = 3` trap:** This evaluates right-to-left:
1. `b = 3` — no declaration keyword → `b` becomes **global**
2. `var a = b` — `a` is scoped to the IIFE

`"use strict"` prevents this — assigning to undeclared variable throws `ReferenceError`.

---

## 28. Undeclared Variables Become Global

### ❓ Output?
```js
function leaker() {
  leakedVar = "I escaped!";
}
leaker();
console.log(leakedVar);
```

### 😱 Answer
```
"I escaped!"
```

### 🧠 Concept
Assigning to a variable without `var`, `let`, or `const` creates a **global variable** from anywhere — even inside a function. It's equivalent to `window.leakedVar = "..."` in browsers.

**Fix:** Add `"use strict"` at the top of your file or function. Strict mode makes this throw a `ReferenceError` immediately.

---

## 29. Currying and Partial Application

### ❓ Output?
```js
function multiply(a) {
  return function(b) { return a * b; };
}

const double = multiply(2);
const triple = multiply(3);

console.log(double(5));
console.log(triple(5));
console.log(multiply(2)(3));
console.log(typeof multiply(2));
```

### 😱 Answer
```
10
15
6
"function"   // multiply(2) returns a function, not a value
```

### 🧠 Concept
**Currying** — transforms `fn(a, b)` into `fn(a)(b)`. Each call takes one argument and returns a new function waiting for the next.

- `multiply(2)` → returns a function, doesn't calculate yet
- `double(5)` → now it calculates: `2 * 5 = 10`

**Why useful:** Create specialised functions from general ones:
```js
const add = a => b => a + b;
const add5 = add(5);    // pre-set first argument
add5(3);  // 8
add5(10); // 15
```

---

## 30. Memoization — Closure + Cache Pattern

### ❓ What prints and how many times does it calculate?
```js
function memoize(fn) {
  const cache = {};
  return function(n) {
    if (n in cache) {
      console.log("cached");
      return cache[n];
    }
    console.log("calculating");
    cache[n] = fn(n);
    return cache[n];
  };
}

const square = memoize(x => x * x);
console.log(square(4));
console.log(square(4));
console.log(square(5));
```

### 😱 Answer
```
calculating
16
cached
16
calculating
25
```

### 🧠 Concept
Memoization caches results — same input, skip recalculating.
Uses a **closure** to keep `cache` alive and private between calls.
The returned function has access to `cache` via closure — but nothing outside does.

This pattern is used for expensive computations (Fibonacci, API calls, heavy processing).

---

## 31. Getter and Setter Trap

### ❓ Output?
```js
const obj = {
  _count: 0,
  get count() { return this._count; },
  set count(v) {
    if (typeof v === "number" && v >= 0) this._count = v;
  }
};

obj.count = 5;
console.log(obj.count);
obj.count = -1;
console.log(obj.count);
obj.count = "hello";
console.log(obj.count);
```

### 😱 Answer
```
5       // setter accepted 5
5       // setter rejected -1 — count stays 5
5       // setter rejected "hello" — count stays 5
```

### 🧠 Concept
Getters and setters look like regular property access but run functions.
- `obj.count = 5` → calls the **setter** with `v = 5`
- `obj.count` → calls the **getter**, returns `_count`

Used for validation, computed properties, and read-only properties. Setting a getter-only property silently fails (or throws in strict mode).

---

## 32. setTimeout(fn, 0) Is Never Instant

### ❓ Output (approximate)?
```js
const start = Date.now();
setTimeout(() => {
  console.log("timeout fired after:", Date.now() - start, "ms");
}, 0);

let i = 0;
while (i < 1_000_000_000) i++;  // 1 billion iterations

console.log("loop done after:", Date.now() - start, "ms");
```

### 😱 Answer (approximate)
```
loop done after: ~800ms
timeout fired after: ~800ms   // NOT 0ms!
```

### 🧠 Concept
`setTimeout(fn, 0)` means "run this as soon as the call stack is empty, after at least 0ms". It does NOT mean "run now".

JavaScript is **single-threaded**. If the call stack is busy with a loop, the `setTimeout` callback waits in the macrotask queue. It only runs when the stack clears.

> **`0ms` is a minimum delay, not an exact delay.**

---

## 33. Weird + Combinations — Every Edge Case

### ❓ Output?
```js
console.log([] + []);
console.log([] + {});
console.log({} + []);
console.log(true + true);
console.log(true + "1");
console.log(null + 1);
console.log(undefined + 1);
```

### 😱 Answer
```
""                   // [] → "", "" + "" = ""
"[object Object]"    // [] → "", {} → "[object Object]"
0                    // {} treated as empty block, then +[] = 0
2                    // true → 1, 1 + 1 = 2
"true1"              // string wins in +
1                    // null → 0, 0 + 1 = 1
NaN                  // undefined → NaN, NaN + 1 = NaN
```

### 🧠 Conversion to Number Reference
```js
Number("")         // 0
Number(" ")        // 0
Number("5")        // 5
Number("5px")      // NaN
Number(null)       // 0
Number(undefined)  // NaN
Number(true)       // 1
Number(false)      // 0
Number([])         // 0
Number([5])        // 5
Number([1,2])      // NaN
Number({})         // NaN
```

---

## 34. String Methods That Surprise

### ❓ Output?
```js
console.log("hello"[10]);
console.log("hello".charAt(10));
console.log(typeof "hello".split(""));
console.log("  hello  ".trim());
console.log("hello".padStart(8, "*"));
```

### 😱 Answer
```
undefined     // bracket notation → undefined for out-of-range
""            // charAt → empty string for out-of-range (not undefined!)
"object"      // split returns an ARRAY — typeof array is "object"
"hello"
"***hello"
```

### 🧠 Key String Gotchas
- `str[i]` → `undefined` for out of range
- `str.charAt(i)` → `""` for out of range (different!)
- `split("")` returns an **array** — people forget `typeof []` = `"object"`
- Strings are **immutable** — all string methods return new strings

---

## 35. Object.is() vs === vs ==

### ❓ Output?
```js
console.log(0 === -0);
console.log(Object.is(0, -0));
console.log(NaN === NaN);
console.log(Object.is(NaN, NaN));
```

### 😱 Answer
```
true    // === says 0 and -0 are equal
false   // Object.is says they are NOT equal
false   // === says NaN ≠ NaN
true    // Object.is correctly handles NaN
```

### 🧠 Concept

| Comparison | `0 === -0` | `NaN === NaN` |
|---|---|---|
| `==` | `true` | `false` |
| `===` | `true` | `false` |
| `Object.is()` | `false` ← correct | `true` ← correct |

`Object.is()` is the most precise comparison — use it when you need to distinguish `0` from `-0` or correctly detect `NaN`.

---

### 🔴 Level 3 Recap — Final Check

```js
// What prints?
console.log("1");
setTimeout(() => console.log("2"), 0);
Promise.resolve().then(() => console.log("3"));
console.log("4");

// Rebind?
const f = (() => this.x).bind({x: 1});
f();  // ?

// IIFE var leak?
(function() { var a = b = 5; })();
console.log(typeof b);  // ?
```

**Answers:** `1 4 3 2` / `undefined` (arrow, this isn't the object) / `"number"` (b leaked globally)

---

---

# 📋 MASTER SUMMARY
### Everything in one place. Use this for last-minute revision before an interview.

---

## 36. Master Summary — Every Rule in One Place

---

### 🔑 The 6 Falsy Values
```
false    0    ""    null    undefined    NaN
```
Everything else is truthy: `[]`, `{}`, `"0"`, `"false"`, `-1`, `Infinity`

---

### 🔑 == Tricky Pairs — All of Them
```js
0 == false          // true
"" == false         // true
"0" == false        // true
"0" == 0            // true
null == undefined   // true  (only these two)
null == 0           // false
null == false       // false
NaN == NaN          // false (NaN ≠ anything)
[] == false         // true
[] == ![]           // true
[] == ""            // true
[] == 0             // true
[] === []           // false (reference)
```

---

### 🔑 typeof Quick Reference
```js
typeof null         // "object" ← 1995 bug
typeof undefined    // "undefined"
typeof []           // "object" ← use Array.isArray()
typeof {}           // "object"
typeof function(){} // "function"
typeof NaN          // "number" ← quirk
typeof 42           // "number"
typeof "str"        // "string"
typeof true         // "boolean"
typeof Symbol()     // "symbol"
```

---

### 🔑 this — The 4 Rules (priority order)
```
1. new binding      new Fn()           → new empty object
2. explicit         .call/.apply/.bind → what you pass
3. implicit         obj.method()       → object before dot
4. default          fn()               → global / undefined (strict)

Arrow functions ignore all 4 — always lexical this from definition site
```

---

### 🔑 Hoisting
```
var x           → hoisted as undefined    → returns undefined before line
let / const x   → hoisted in TDZ         → ReferenceError before line
function f(){}  → fully hoisted           → callable before declaration
var f = fn      → var hoisted (undefined) → TypeError if called before assignment
```

---

### 🔑 Closures
```
1. Functions remember their outer scope — even after outer function returns
2. Closures hold REFERENCES, not copies of values
3. var in loops  → one shared variable → all closures see final value
4. let in loops  → new variable per iteration → each closure is independent
```

---

### 🔑 Prototype Chain
```
instance → Constructor.prototype → ParentConstructor.prototype → Object.prototype → null
```
- `hasOwnProperty(key)` → true only if on the instance itself (not inherited)
- `prototype` → on constructor functions
- `__proto__` → on every instance (live link to its prototype)
- Adding to `.prototype` after creating instances → instances immediately see it

---

### 🔑 Event Loop Order — Every Time
```
1. Call Stack (synchronous code)         ← always first
2. Microtask Queue (drain completely)    ← Promise .then, queueMicrotask
3. Macrotask Queue (one task at a time)  ← setTimeout, setInterval
   → after each macrotask, microtasks drain again
```
Promise constructor = synchronous. `.then()` = async (microtask).

---

### 🔑 Shallow vs Deep Copy
```
= assignment            → same reference (not a copy)
{...spread}             → shallow (nested objects still shared)
JSON.parse/stringify    → deep (loses functions, Dates, undefined)
structuredClone()       → deep, modern, recommended
```

---

### 🔑 Array Mutation
```
MUTATES:    sort, reverse, push, pop, shift, unshift, splice, fill
NEW ARRAY:  map, filter, slice, concat, flat, flatMap
VALUE:      reduce, find, findIndex, some, every, indexOf
```
`sort()` and `reverse()` both mutate AND return the same array.

---

### 🔑 call / apply / bind
```
call(obj, a, b)    → runs immediately, args listed
apply(obj, [a,b])  → runs immediately, args as array
bind(obj, a)       → returns new function, doesn't run

Once bound → cannot be rebound. First bind is permanent.
```

---

### 🔑 Promise Methods
```
Promise.all         → all resolve, OR fails fast on first rejection
Promise.allSettled  → all settle, never rejects, includes status
Promise.any         → first to resolve
Promise.race        → first to settle (resolve or reject)
```

---

### 🔑 Nullish Coalescing vs OR
```js
0 ?? "x"    // 0     — 0 is not null/undefined → keep left
0 || "x"    // "x"   — 0 is falsy → use right
"" ?? "x"   // ""    — "" is not null/undefined → keep left
"" || "x"   // "x"   — "" is falsy → use right
```
Use `??` when `0` and `""` are valid values. Use `||` for any falsy fallback.

---

### 🔑 Easy-to-Forget Rules
```
delete arr[i]       → hole, length unchanged — use splice() instead
for...in            → keys + inherited — never use on arrays
for...of            → values only — safe for arrays
const obj           → prevents reassignment, NOT mutation
Object keys         → always strings — objects become "[object Object]"
0.1 + 0.2           → 0.30000000000000004 — never === compare floats
sort()              → mutates original — make a copy first if needed
undeclared assign   → global variable — fixed by "use strict"
arguments object    → only in regular functions, not arrow functions
bind rebinding      → impossible — first bind is permanent
typeof null         → "object" — use === null instead
NaN === NaN         → false — use Number.isNaN()
setTimeout(fn, 0)   → not instant — waits for call stack to clear
```

---

### 🔑 5 Sentences Every Interviewer Wants to Hear

1. **"I always use `===` — `==` causes coercion surprises"**
2. **"Arrow functions don't have their own `this` — never use them as object methods"**
3. **"I use `let`/`const`, never `var` — `var`'s function scope causes the loop closure trap"**
4. **"Promises (microtasks) always run before `setTimeout` (macrotask)"**
5. **"Spread is shallow — for nested objects I use `structuredClone()`"**

---

*JavaScript Complete Tricks & Gotchas — three levels, one guide, every interview situation covered.*