# 🚀 Node.js & JavaScript — Complete Interview Prep Guide

> **How to use this guide:** Each section has the core question, a clear answer, follow-up questions an interviewer might ask, and real code snippets you can write on a whiteboard or in a code editor.

---

## 📚 TABLE OF CONTENTS

1. [JavaScript Core](#1-javascript-core)
   - Event Loop & Execution Model
   - Heap & Stack
   - Hoisting
   - Closures
   - Prototypes & Prototype Chaining
   - `this` Keyword
   - Shallow Copy vs Deep Copy
2. [Asynchronous JavaScript](#2-asynchronous-javascript)
   - Callbacks & Callback Hell
   - Promises & Variations
   - Async/Await
   - Event Emitter
   - Blocking vs Non-Blocking
   - Error Handling & Rejections
3. [Node.js Internals](#3-nodejs-internals)
   - fs Module
   - Child Process (exec, execFile, spawn, fork)
   - Worker Threads
   - Shell Scripting
4. [Express & Backend APIs](#4-express--backend-apis)
   - Middleware
   - Authentication Middleware
   - Rate Limiting
   - CORS
5. [Databases](#5-databases)
   - MongoDB
   - SQL
   - Indexing
6. [System Design & Architecture](#6-system-design--architecture)
   - Microservices
   - RabbitMQ & Queueing
   - Latency & Throughput
   - Distributing Load
7. [Networking & Protocols](#7-networking--protocols)
   - HTTP vs HTTPS
   - TCP vs UDP
   - SDP & SIP
8. [Linux Essentials](#8-linux-essentials)

---

# 1. JavaScript Core

---

## 🔄 Event Loop

### Q: What is the Event Loop and how does it work?

**Answer:**
The Event Loop is the mechanism that allows JavaScript (single-threaded) to perform non-blocking operations by offloading tasks to the browser/Node.js runtime and picking up results when the call stack is empty.

**Execution Order:**
1. Synchronous code runs first (Call Stack)
2. Microtasks run next (Promise `.then`, `queueMicrotask`, `MutationObserver`)
3. Macrotasks run last (setTimeout, setInterval, setImmediate, I/O)

```js
console.log('1 - sync');

setTimeout(() => console.log('2 - macrotask'), 0);

Promise.resolve().then(() => console.log('3 - microtask'));

console.log('4 - sync');

// Output order:
// 1 - sync
// 4 - sync
// 3 - microtask   ← runs before macrotask!
// 2 - macrotask
```

---

### Q: What is the difference between Macrotasks and Microtasks?

| Feature | Macrotask | Microtask |
|---|---|---|
| Examples | `setTimeout`, `setInterval`, `setImmediate`, I/O | `Promise.then`, `queueMicrotask`, `MutationObserver` |
| Queue | Macrotask Queue | Microtask Queue |
| Priority | Lower — runs after microtasks | Higher — runs before next macrotask |
| Runs after | Each macrotask | Each task, before next macrotask |

```js
console.log('Start');

setTimeout(() => console.log('setTimeout'), 0);       // macrotask

Promise.resolve()
  .then(() => console.log('Promise 1'))               // microtask
  .then(() => console.log('Promise 2'));              // microtask

queueMicrotask(() => console.log('queueMicrotask')); // microtask

console.log('End');

// Output:
// Start
// End
// Promise 1
// queueMicrotask
// Promise 2
// setTimeout
```

---

### Q: What is `setImmediate` vs `setTimeout(fn, 0)`?

```js
// In Node.js:
setImmediate(() => console.log('setImmediate'));    // runs in Check phase
setTimeout(() => console.log('setTimeout'), 0);    // runs in Timers phase

// When called from I/O callback — setImmediate ALWAYS runs first
const fs = require('fs');
fs.readFile('file.txt', () => {
  setTimeout(() => console.log('timeout'), 0);
  setImmediate(() => console.log('immediate'));   // ← always first inside I/O
});
```

---

## 🧠 Heap & Stack

### Q: What is the difference between the Heap and the Stack?

**Answer:**

| Feature | Call Stack | Heap |
|---|---|---|
| Stores | Function calls, primitives | Objects, arrays, closures |
| Structure | LIFO (Last In, First Out) | Unstructured / dynamic |
| Size | Fixed, limited | Large, dynamic |
| Speed | Very fast | Slower (GC managed) |
| Error | Stack overflow | Memory leak |

```js
// STACK — primitives stored directly
let a = 10;
let b = a;  // b is a COPY
b = 20;
console.log(a); // 10 — unaffected

// HEAP — objects stored by reference
let obj1 = { name: 'Alice' };
let obj2 = obj1;  // obj2 points to SAME heap memory
obj2.name = 'Bob';
console.log(obj1.name); // 'Bob' — both point to same object!
```

```js
// Stack overflow example
function infinite() {
  return infinite(); // adds frame to stack until it crashes
}
infinite(); // RangeError: Maximum call stack size exceeded
```

---

## 📦 Hoisting

### Q: What is hoisting in JavaScript?

**Answer:**
Hoisting is JavaScript's behavior of moving variable and function declarations to the top of their scope during the compilation phase — before code runs.

```js
// var is hoisted and initialized to undefined
console.log(x); // undefined (NOT ReferenceError)
var x = 5;
console.log(x); // 5

// let/const are hoisted but NOT initialized (Temporal Dead Zone)
console.log(y); // ReferenceError: Cannot access 'y' before initialization
let y = 10;
```

```js
// Function declarations are fully hoisted
greet(); // "Hello!" ← works!
function greet() {
  console.log('Hello!');
}

// Function expressions are NOT fully hoisted
sayHi(); // TypeError: sayHi is not a function
var sayHi = function() {
  console.log('Hi!');
};
```

### Q: What is the Temporal Dead Zone (TDZ)?

```js
// The period between entering scope and initialization is the TDZ
{
  // TDZ for `name` starts here
  console.log(name); // ReferenceError!
  let name = 'Alice'; // TDZ ends here
}
```

---

## 🔒 Closures

### Q: What is a closure?

**Answer:**
A closure is a function that "remembers" variables from its outer (lexical) scope even after that scope has finished executing.

```js
function makeCounter() {
  let count = 0; // this variable is "closed over"
  
  return function() {
    count++;
    return count;
  };
}

const counter = makeCounter();
console.log(counter()); // 1
console.log(counter()); // 2
console.log(counter()); // 3

// 'count' is private — can't be accessed directly from outside
```

```js
// Practical use: factory functions
function multiplier(factor) {
  return (number) => number * factor; // closes over 'factor'
}

const double = multiplier(2);
const triple = multiplier(3);

console.log(double(5)); // 10
console.log(triple(5)); // 15
```

### Q: Classic closure gotcha with var in loops

```js
// Problem: all closures share the SAME `i`
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// Output: 3, 3, 3

// Fix 1: use let (block scoped)
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// Output: 0, 1, 2

// Fix 2: IIFE
for (var i = 0; i < 3; i++) {
  (function(j) {
    setTimeout(() => console.log(j), 100);
  })(i);
}
// Output: 0, 1, 2
```

---

## 🧬 Prototype & Prototype Chaining

### Q: What is a prototype in JavaScript?

**Answer:**
Every JavaScript object has an internal link (`[[Prototype]]`) to another object called its **prototype**. When you access a property, JS first looks at the object itself, then walks up the prototype chain until it finds it or reaches `null`.

```js
const animal = {
  breathe() {
    return 'breathing...';
  }
};

const dog = {
  bark() {
    return 'Woof!';
  }
};

// Set animal as the prototype of dog
Object.setPrototypeOf(dog, animal);

console.log(dog.bark());    // 'Woof!' — own method
console.log(dog.breathe()); // 'breathing...' — found on prototype!
console.log(dog.toString()); // found on Object.prototype (top of chain)
```

### Q: What are the two types of prototype?

```js
// Type 1: __proto__ (instance prototype — the [[Prototype]] link)
const obj = {};
console.log(obj.__proto__ === Object.prototype); // true

// Type 2: .prototype (constructor function property)
function Person(name) {
  this.name = name;
}
Person.prototype.greet = function() {
  return `Hi, I'm ${this.name}`;
};

const alice = new Person('Alice');
console.log(alice.__proto__ === Person.prototype); // true
console.log(alice.greet()); // "Hi, I'm Alice"
```

### Q: How do you create objects with a specific prototype? (4 ways)

```js
// Way 1: Object.create()
const proto = {
  greet() { return `Hello, ${this.name}`; }
};
const obj = Object.create(proto);
obj.name = 'Alice';
console.log(obj.greet()); // "Hello, Alice"

// Way 2: Constructor Function
function Animal(name) {
  this.name = name;
}
Animal.prototype.speak = function() {
  return `${this.name} makes a sound`;
};
const cat = new Animal('Cat');

// Way 3: ES6 Class (syntactic sugar over prototype)
class Vehicle {
  constructor(brand) {
    this.brand = brand;
  }
  describe() {
    return `I am a ${this.brand}`;
  }
}
const car = new Vehicle('Toyota');

// Way 4: Object literal (prototype is Object.prototype)
const plain = { x: 1 };
```

### Q: How does inheritance work using prototype?

```js
// ES5 Prototype Inheritance
function Animal(name) {
  this.name = name;
}
Animal.prototype.eat = function() {
  return `${this.name} is eating`;
};

function Dog(name, breed) {
  Animal.call(this, name); // inherit properties
  this.breed = breed;
}

// Inherit methods
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog; // fix constructor reference

Dog.prototype.bark = function() {
  return `${this.name} barks!`;
};

const rex = new Dog('Rex', 'Labrador');
console.log(rex.eat());  // "Rex is eating" — from Animal
console.log(rex.bark()); // "Rex barks!" — from Dog

// ES6 Class version (cleaner)
class AnimalES6 {
  constructor(name) {
    this.name = name;
  }
  eat() {
    return `${this.name} is eating`;
  }
}

class DogES6 extends AnimalES6 {
  constructor(name, breed) {
    super(name); // calls parent constructor
    this.breed = breed;
  }
  bark() {
    return `${this.name} barks!`;
  }
}

const buddy = new DogES6('Buddy', 'Golden');
console.log(buddy.eat());  // inherited from AnimalES6
console.log(buddy.bark()); // DogES6 method
```

---

## 🎯 `this` Keyword

### Q: How does `this` work in JavaScript?

**Answer:**
`this` refers to the **execution context** — the object that is calling the function. Its value depends on **how** the function is called.

```js
// 1. Global context
console.log(this); // window (browser) or {} (Node.js module)

// 2. Object method — this = the object
const user = {
  name: 'Alice',
  greet() {
    return `Hello, ${this.name}`; // this = user
  }
};
console.log(user.greet()); // "Hello, Alice"

// 3. Regular function — this = global (or undefined in strict mode)
function show() {
  console.log(this);
}
show(); // window / global

// 4. Arrow function — inherits `this` from surrounding scope
const timer = {
  delay: 1000,
  start() {
    setTimeout(() => {
      console.log(this.delay); // `this` = timer object ✅
    }, 100);
  }
};
timer.start(); // 1000

// 5. Explicit binding: call, apply, bind
function introduce(greeting) {
  return `${greeting}, I'm ${this.name}`;
}
const person = { name: 'Bob' };

introduce.call(person, 'Hello');          // call: args one by one
introduce.apply(person, ['Hi']);          // apply: args as array
const bound = introduce.bind(person);     // bind: returns new function
bound('Hey');
```

---

## 📋 Shallow Copy vs Deep Copy

### Q: What is the difference between shallow copy and deep copy?

**Answer:**
- **Shallow Copy**: Copies only the top-level properties. Nested objects still share the same reference.
- **Deep Copy**: Copies everything recursively. No shared references at any level.

```js
const original = {
  name: 'Alice',
  address: { city: 'NYC' }, // nested object
  hobbies: ['reading', 'coding']
};

// ── SHALLOW COPY METHODS ──

// Method 1: Object.assign
const shallow1 = Object.assign({}, original);

// Method 2: Spread operator
const shallow2 = { ...original };

// Problem: nested objects still shared!
shallow1.name = 'Bob';          // ✅ doesn't affect original
shallow1.address.city = 'LA';   // ❌ AFFECTS original!
console.log(original.address.city); // 'LA' — oops!

// ── DEEP COPY METHODS ──

// Method 1: JSON (simple, but loses functions, Date, undefined)
const deep1 = JSON.parse(JSON.stringify(original));

// Method 2: structuredClone (modern, recommended)
const deep2 = structuredClone(original);

// Method 3: recursive custom function
function deepClone(obj) {
  if (obj === null || typeof obj !== 'object') return obj;
  if (Array.isArray(obj)) return obj.map(deepClone);
  
  return Object.fromEntries(
    Object.entries(obj).map(([k, v]) => [k, deepClone(v)])
  );
}

const deep3 = deepClone(original);
deep3.address.city = 'Chicago';
console.log(original.address.city); // 'LA' — unaffected ✅
```

---

# 2. Asynchronous JavaScript

---

## 💀 Callback Hell

### Q: What is callback hell and how do you solve it?

**Answer:**
Callback hell (also called the "pyramid of doom") happens when multiple async operations are nested inside each other, making code hard to read, debug, and maintain.

```js
// ❌ CALLBACK HELL — hard to read, error-prone
getUserData(userId, function(user) {
  getOrders(user.id, function(orders) {
    getOrderDetails(orders[0].id, function(details) {
      getPaymentInfo(details.paymentId, function(payment) {
        console.log(payment);
        // Error handling? What goes where? 😱
      }, function(err) { console.error(err); });
    }, function(err) { console.error(err); });
  }, function(err) { console.error(err); });
}, function(err) { console.error(err); });

// ✅ SOLUTION 1: Promises
getUserData(userId)
  .then(user => getOrders(user.id))
  .then(orders => getOrderDetails(orders[0].id))
  .then(details => getPaymentInfo(details.paymentId))
  .then(payment => console.log(payment))
  .catch(err => console.error(err)); // one catch for all!

// ✅ SOLUTION 2: Async/Await (cleanest)
async function loadPaymentInfo(userId) {
  try {
    const user = await getUserData(userId);
    const orders = await getOrders(user.id);
    const details = await getOrderDetails(orders[0].id);
    const payment = await getPaymentInfo(details.paymentId);
    console.log(payment);
  } catch (err) {
    console.error(err);
  }
}
```

---

## 🤝 Promises & Variations

### Q: What is a Promise and what are its states?

**Answer:**
A Promise is an object representing the eventual completion or failure of an async operation.

**Three states:** `pending` → `fulfilled` OR `rejected`

```js
// Creating a Promise
const fetchData = new Promise((resolve, reject) => {
  setTimeout(() => {
    const success = true;
    if (success) {
      resolve({ data: 'here is your data' });
    } else {
      reject(new Error('Something went wrong'));
    }
  }, 1000);
});

// Consuming a Promise
fetchData
  .then(result => console.log(result))
  .catch(err => console.error(err))
  .finally(() => console.log('always runs'));
```

### Q: What are the Promise variations/combinators?

```js
const p1 = fetch('/api/users');
const p2 = fetch('/api/products');
const p3 = fetch('/api/orders');

// Promise.all — waits for ALL to resolve, fails if ANY rejects
Promise.all([p1, p2, p3])
  .then(([users, products, orders]) => console.log('all loaded'))
  .catch(err => console.error('one failed:', err));

// Promise.allSettled — waits for ALL, NEVER fails, gives status of each
Promise.allSettled([p1, p2, p3])
  .then(results => {
    results.forEach(result => {
      if (result.status === 'fulfilled') {
        console.log('success:', result.value);
      } else {
        console.log('failed:', result.reason);
      }
    });
  });

// Promise.race — resolves/rejects as soon as FIRST one settles
Promise.race([p1, p2, p3])
  .then(firstResult => console.log('first done:', firstResult));

// Promise.any — resolves with FIRST success, rejects only if ALL fail
Promise.any([p1, p2, p3])
  .then(firstSuccess => console.log('first success:', firstSuccess))
  .catch(err => console.log('all failed'));

// Creating resolved/rejected promises directly
const resolved = Promise.resolve(42);
const rejected = Promise.reject(new Error('nope'));
```

### Q: How does async/await work under the hood?

```js
// async/await is syntactic sugar over Promises
async function getData() {
  const response = await fetch('/api/data'); // pauses here
  const json = await response.json();        // pauses here
  return json;
}

// Equivalent Promise chain:
function getData() {
  return fetch('/api/data')
    .then(response => response.json());
}

// Error handling patterns
async function loadUser(id) {
  try {
    const user = await fetchUser(id);
    return user;
  } catch (error) {
    console.error('Failed to load user:', error.message);
    throw error; // re-throw if needed
  }
}

// Running promises in parallel with async/await
async function loadDashboard() {
  // ❌ Sequential — slow (waits one by one)
  const user = await fetchUser();
  const posts = await fetchPosts();

  // ✅ Parallel — fast (both fire at same time)
  const [user2, posts2] = await Promise.all([fetchUser(), fetchPosts()]);
}
```

---

## 📡 Event Emitter

### Q: What is EventEmitter in Node.js?

**Answer:**
EventEmitter is a Node.js core class that implements the observer/pub-sub pattern — objects can emit named events, and other objects can listen and react.

```js
const EventEmitter = require('events');

// Create an emitter
const emitter = new EventEmitter();

// Register a listener
emitter.on('data', (payload) => {
  console.log('Received data:', payload);
});

// One-time listener
emitter.once('connect', () => {
  console.log('Connected! This fires only once.');
});

// Emit events
emitter.emit('data', { id: 1, name: 'Alice' });
emitter.emit('connect');
emitter.emit('connect'); // ← 'once' listener won't fire again

// Remove a listener
const handler = (data) => console.log(data);
emitter.on('message', handler);
emitter.off('message', handler); // or removeListener

// Extend EventEmitter (real-world pattern)
class DataStream extends EventEmitter {
  start() {
    let count = 0;
    const interval = setInterval(() => {
      this.emit('data', { count: ++count });
      if (count === 3) {
        this.emit('end');
        clearInterval(interval);
      }
    }, 500);
  }
}

const stream = new DataStream();
stream.on('data', chunk => console.log('chunk:', chunk));
stream.on('end', () => console.log('stream ended'));
stream.start();
```

---

## ⚡ Blocking vs Non-Blocking

### Q: What is the difference between blocking and non-blocking code?

```js
const fs = require('fs');

// ❌ BLOCKING — halts everything until file is read
const data = fs.readFileSync('large-file.txt', 'utf8');
console.log(data);
console.log('This runs AFTER file is fully read'); // blocked!

// ✅ NON-BLOCKING — doesn't halt the event loop
fs.readFile('large-file.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data); // runs when ready
});
console.log('This runs IMMEDIATELY while file loads'); // not blocked!

// ✅ NON-BLOCKING with Promises (modern)
async function readConfig() {
  const data = await fs.promises.readFile('config.json', 'utf8');
  return JSON.parse(data);
}
```

---

## 🚨 Error Handling & Exceptions

### Q: How do you capture and handle errors in async code?

```js
// 1. try/catch with async/await
async function fetchUser(id) {
  try {
    const res = await fetch(`/api/users/${id}`);
    if (!res.ok) throw new Error(`HTTP error: ${res.status}`);
    return await res.json();
  } catch (err) {
    console.error('fetchUser failed:', err.message);
    return null;
  }
}

// 2. Handle unhandled Promise rejections globally
process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled Rejection:', reason);
  // Gracefully shutdown
  process.exit(1);
});

// 3. Handle uncaught exceptions globally
process.on('uncaughtException', (err) => {
  console.error('Uncaught Exception:', err);
  process.exit(1);
});

// 4. Custom error classes
class ValidationError extends Error {
  constructor(field, message) {
    super(message);
    this.name = 'ValidationError';
    this.field = field;
    this.statusCode = 400;
  }
}

class NotFoundError extends Error {
  constructor(resource) {
    super(`${resource} not found`);
    this.name = 'NotFoundError';
    this.statusCode = 404;
  }
}

// Usage
function validateAge(age) {
  if (typeof age !== 'number') {
    throw new ValidationError('age', 'Age must be a number');
  }
  if (age < 0) {
    throw new ValidationError('age', 'Age cannot be negative');
  }
}

try {
  validateAge(-5);
} catch (err) {
  if (err instanceof ValidationError) {
    console.log(`Validation failed on field: ${err.field}`);
  }
}
```

---

# 3. Node.js Internals

---

## 📁 fs Module

### Q: How does the fs module work in Node.js?

```js
const fs = require('fs');
const path = require('path');
const fsPromises = require('fs').promises;

// ── READ ──
// Sync (blocking)
const content = fs.readFileSync('file.txt', 'utf8');

// Callback (non-blocking)
fs.readFile('file.txt', 'utf8', (err, data) => {
  if (err) return console.error(err);
  console.log(data);
});

// Promise (modern preferred)
async function readConfig() {
  const data = await fsPromises.readFile('config.json', 'utf8');
  return JSON.parse(data);
}

// ── WRITE ──
fs.writeFile('output.txt', 'Hello World', 'utf8', (err) => {
  if (err) throw err;
  console.log('File written!');
});

// Append
fs.appendFile('log.txt', 'New log entry\n', (err) => {
  if (err) throw err;
});

// ── CHECK / STAT ──
fs.stat('file.txt', (err, stats) => {
  if (err) return;
  console.log('Size:', stats.size);
  console.log('Is file:', stats.isFile());
  console.log('Is dir:', stats.isDirectory());
});

// ── DIRECTORY ──
fs.mkdir('new-folder', { recursive: true }, (err) => {
  if (err) throw err;
});

fs.readdir('./src', (err, files) => {
  if (err) throw err;
  console.log(files); // ['index.js', 'utils.js', ...]
});

// ── STREAMS (for large files) ──
const readStream = fs.createReadStream('large.csv');
const writeStream = fs.createWriteStream('output.csv');

readStream.pipe(writeStream); // efficient, low memory
```

---

## 👶 Child Process

### Q: What are the 4 ways to create a child process in Node.js?

**Answer:**
Node.js provides 4 methods in the `child_process` module — each suited for different use cases.

| Method | Use case | Returns |
|---|---|---|
| `exec` | Run shell command, buffer output | Buffer (whole output) |
| `execFile` | Run executable file directly | Buffer (whole output) |
| `spawn` | Stream large output, long-running | Streams |
| `fork` | Run another Node.js script with IPC | Child process with message channel |

```js
const { exec, execFile, spawn, fork } = require('child_process');

// ── 1. exec — runs in a shell, buffers output ──
exec('ls -la', (error, stdout, stderr) => {
  if (error) return console.error('Error:', error);
  if (stderr) return console.error('Stderr:', stderr);
  console.log('Output:', stdout);
});

// exec with Promise
const { promisify } = require('util');
const execAsync = promisify(exec);

async function listFiles() {
  const { stdout } = await execAsync('ls -la');
  return stdout;
}

// ── 2. execFile — runs a file directly (no shell, more secure) ──
execFile('/usr/bin/node', ['--version'], (error, stdout) => {
  console.log('Node version:', stdout);
});

// ── 3. spawn — streams data, good for large output ──
const ls = spawn('ls', ['-la', '/usr']);

ls.stdout.on('data', (chunk) => {
  process.stdout.write(chunk); // streams chunk by chunk
});

ls.stderr.on('data', (data) => {
  console.error('Error:', data.toString());
});

ls.on('close', (code) => {
  console.log(`Process exited with code ${code}`);
});

// Real world: running a Python script
const python = spawn('python3', ['script.py', '--input', 'data.csv']);
python.stdout.on('data', chunk => console.log(chunk.toString()));

// ── 4. fork — spawns another Node.js process with IPC ──
// parent.js
const child = fork('./worker.js');

child.send({ task: 'compute', data: [1, 2, 3, 4, 5] });

child.on('message', (result) => {
  console.log('Result from child:', result);
});

child.on('exit', (code) => {
  console.log('Child exited:', code);
});
```

```js
// worker.js (child process)
process.on('message', (msg) => {
  if (msg.task === 'compute') {
    const result = msg.data.reduce((sum, n) => sum + n, 0);
    process.send({ result });
    process.exit(0);
  }
});
```

---

## 🧵 Worker Threads

### Q: When do you use Worker Threads vs Child Process?

| Feature | Child Process | Worker Threads |
|---|---|---|
| Isolation | Separate memory | Shared memory possible |
| Communication | IPC / stdin/stdout | `postMessage`, `SharedArrayBuffer` |
| Startup cost | High | Low |
| Best for | Separate tasks, shell commands | CPU-heavy JS tasks |
| Crash isolation | ✅ crash won't affect parent | ❌ can crash main thread |

```js
// worker_threads example
const { Worker, isMainThread, parentPort, workerData } = require('worker_threads');

if (isMainThread) {
  // ── MAIN THREAD ──
  function runHeavyTask(data) {
    return new Promise((resolve, reject) => {
      const worker = new Worker(__filename, { workerData: data });
      
      worker.on('message', resolve);
      worker.on('error', reject);
      worker.on('exit', (code) => {
        if (code !== 0) reject(new Error(`Worker exited with code ${code}`));
      });
    });
  }

  async function main() {
    const results = await Promise.all([
      runHeavyTask({ start: 0, end: 1e8 }),
      runHeavyTask({ start: 1e8, end: 2e8 }),
    ]);
    console.log('Total:', results.reduce((a, b) => a + b, 0));
  }

  main();

} else {
  // ── WORKER THREAD ──
  const { start, end } = workerData;
  let sum = 0;
  for (let i = start; i < end; i++) {
    sum += i;
  }
  parentPort.postMessage(sum);
}
```

### Q: How do you distribute load across OOP and multiple workers?

```js
// Worker Pool Pattern — distributes tasks across N workers
const { Worker } = require('worker_threads');
const os = require('os');

class WorkerPool {
  constructor(workerFile, size = os.cpus().length) {
    this.workerFile = workerFile;
    this.size = size;
    this.workers = [];
    this.queue = [];
    this.initWorkers();
  }

  initWorkers() {
    for (let i = 0; i < this.size; i++) {
      this.addWorker();
    }
  }

  addWorker() {
    const worker = new Worker(this.workerFile);
    worker.busy = false;

    worker.on('message', (result) => {
      worker.busy = false;
      worker.currentResolve(result);
      this.processQueue();
    });

    this.workers.push(worker);
  }

  processQueue() {
    if (this.queue.length === 0) return;
    const freeWorker = this.workers.find(w => !w.busy);
    if (!freeWorker) return;

    const { task, resolve } = this.queue.shift();
    freeWorker.busy = true;
    freeWorker.currentResolve = resolve;
    freeWorker.postMessage(task);
  }

  run(task) {
    return new Promise((resolve) => {
      this.queue.push({ task, resolve });
      this.processQueue();
    });
  }
}

// Usage
const pool = new WorkerPool('./compute-worker.js', 4);

const tasks = [1, 2, 3, 4, 5, 6, 7, 8];
Promise.all(tasks.map(t => pool.run({ value: t })))
  .then(results => console.log('All done:', results));
```

---

# 4. Express & Backend APIs

---

## 🔌 Middleware

### Q: What is Express middleware and how does it work?

**Answer:**
Middleware is a function that has access to `req`, `res`, and `next`. It runs between the request being received and the response being sent. Middleware is chained — each calls `next()` to pass control to the next one.

```js
const express = require('express');
const app = express();

// ── BUILT-IN MIDDLEWARE ──
app.use(express.json());             // parse JSON bodies
app.use(express.urlencoded({ extended: true })); // parse form data
app.use(express.static('public'));   // serve static files

// ── CUSTOM MIDDLEWARE ──
// Logger middleware
const logger = (req, res, next) => {
  console.log(`${new Date().toISOString()} ${req.method} ${req.url}`);
  next(); // MUST call next() or request hangs!
};

app.use(logger);

// Error-handling middleware (4 params!)
const errorHandler = (err, req, res, next) => {
  console.error(err.stack);
  res.status(err.statusCode || 500).json({
    success: false,
    message: err.message || 'Internal Server Error'
  });
};

// Add AFTER all routes
app.use(errorHandler);

// ── ROUTE-SPECIFIC MIDDLEWARE ──
const validate = (req, res, next) => {
  if (!req.body.name) {
    return next(new Error('Name is required'));
  }
  next();
};

app.post('/users', validate, (req, res) => {
  res.json({ message: 'User created' });
});
```

### Q: How do you implement Authentication Middleware?

```js
const jwt = require('jsonwebtoken');
const JWT_SECRET = process.env.JWT_SECRET || 'your-secret';

// ── JWT AUTH MIDDLEWARE ──
const authenticate = (req, res, next) => {
  const authHeader = req.headers.authorization;

  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ message: 'No token provided' });
  }

  const token = authHeader.split(' ')[1];

  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    req.user = decoded; // attach user to request
    next();
  } catch (err) {
    if (err.name === 'TokenExpiredError') {
      return res.status(401).json({ message: 'Token expired' });
    }
    return res.status(401).json({ message: 'Invalid token' });
  }
};

// ── ROLE-BASED AUTHORIZATION ──
const authorize = (...roles) => {
  return (req, res, next) => {
    if (!roles.includes(req.user.role)) {
      return res.status(403).json({ message: 'Forbidden: insufficient permissions' });
    }
    next();
  };
};

// Login route — generate token
app.post('/login', async (req, res) => {
  const { email, password } = req.body;
  // verify credentials (simplified)
  const user = await User.findOne({ email });
  
  if (!user || !await user.comparePassword(password)) {
    return res.status(401).json({ message: 'Invalid credentials' });
  }

  const token = jwt.sign(
    { id: user._id, role: user.role },
    JWT_SECRET,
    { expiresIn: '1h' }
  );

  res.json({ token });
});

// Protected routes
app.get('/profile', authenticate, (req, res) => {
  res.json({ user: req.user }); // only authenticated users
});

app.delete('/users/:id', authenticate, authorize('admin'), (req, res) => {
  res.json({ message: 'User deleted' }); // only admins
});
```

---

## 🚦 Rate Limiting

### Q: What is rate limiting and how do you implement it?

**Answer:**
Rate limiting restricts how many requests a client can make in a time window — prevents abuse, DDoS attacks, and API overuse.

```js
// Using express-rate-limit library
const rateLimit = require('express-rate-limit');

// General limiter
const generalLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100,                  // 100 requests per window
  standardHeaders: true,
  legacyHeaders: false,
  message: { error: 'Too many requests, please try again later' },
  keyGenerator: (req) => req.ip, // track by IP
});

// Strict limiter for auth routes
const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5, // only 5 login attempts per 15 min
  message: { error: 'Too many login attempts' },
  skipSuccessfulRequests: true, // don't count successful logins
});

app.use(generalLimiter);
app.post('/login', authLimiter, loginHandler);

// ── MANUAL RATE LIMIT with Redis ──
const redis = require('redis');
const client = redis.createClient();

const rateLimiter = async (req, res, next) => {
  const key = `rate:${req.ip}`;
  const limit = 100;
  const window = 60; // seconds

  const current = await client.incr(key);
  
  if (current === 1) {
    await client.expire(key, window);
  }

  if (current > limit) {
    return res.status(429).json({
      error: 'Rate limit exceeded',
      retryAfter: await client.ttl(key)
    });
  }

  res.setHeader('X-RateLimit-Limit', limit);
  res.setHeader('X-RateLimit-Remaining', Math.max(0, limit - current));
  next();
};
```

---

## 🌐 CORS

### Q: What is CORS and how do you handle it?

**Answer:**
CORS (Cross-Origin Resource Sharing) is a browser security feature that blocks requests from a different origin (protocol + domain + port) unless the server explicitly allows it.

```js
const cors = require('cors');

// Allow all origins (dev only!)
app.use(cors());

// Specific origins (production)
const corsOptions = {
  origin: ['https://myapp.com', 'https://admin.myapp.com'],
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true, // allow cookies
  maxAge: 86400,     // cache preflight for 24h
};

app.use(cors(corsOptions));

// Manual CORS headers (without library)
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', 'https://myapp.com');
  res.header('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE');
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');

  // Handle preflight
  if (req.method === 'OPTIONS') {
    return res.sendStatus(204);
  }
  next();
});
```

---

# 5. Databases

---

## 🍃 MongoDB

### Q: What are the key MongoDB concepts for an interview?

```js
const { MongoClient, ObjectId } = require('mongodb');
const mongoose = require('mongoose');

// ── MONGOOSE SCHEMA & MODEL ──
const userSchema = new mongoose.Schema({
  name: { type: String, required: true, trim: true },
  email: { type: String, required: true, unique: true, lowercase: true },
  age: { type: Number, min: 0, max: 120 },
  role: { type: String, enum: ['user', 'admin'], default: 'user' },
  createdAt: { type: Date, default: Date.now }
});

const User = mongoose.model('User', userSchema);

// ── CRUD OPERATIONS ──
// Create
const user = await User.create({ name: 'Alice', email: 'alice@example.com' });

// Read
const allUsers = await User.find({});
const oneUser = await User.findById('64abc...id');
const adminUsers = await User.find({ role: 'admin' }).select('name email').limit(10);

// Update
await User.findByIdAndUpdate(id, { $set: { name: 'Bob' } }, { new: true });

// Delete
await User.findByIdAndDelete(id);

// ── AGGREGATION ──
const result = await User.aggregate([
  { $match: { role: 'user' } },                    // filter
  { $group: { _id: '$role', count: { $sum: 1 } } }, // group & count
  { $sort: { count: -1 } },                          // sort
  { $limit: 5 }                                      // limit
]);

// ── TRANSACTIONS ──
const session = await mongoose.startSession();
session.startTransaction();

try {
  await User.create([{ name: 'Alice' }], { session });
  await Account.create([{ userId: user._id }], { session });
  await session.commitTransaction();
} catch (err) {
  await session.abortTransaction();
  throw err;
} finally {
  session.endSession();
}
```

---

## 🗄️ SQL

### Q: What are the key SQL concepts for a Node.js interview?

```sql
-- ── BASIC QUERIES ──
SELECT * FROM users WHERE role = 'admin' ORDER BY created_at DESC LIMIT 10;

-- ── JOINS ──
-- INNER JOIN: only matching rows from both tables
SELECT u.name, o.amount
FROM users u
INNER JOIN orders o ON u.id = o.user_id;

-- LEFT JOIN: all users, even if no orders
SELECT u.name, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name;

-- ── AGGREGATION ──
SELECT 
  department,
  COUNT(*) as employee_count,
  AVG(salary) as avg_salary,
  MAX(salary) as max_salary
FROM employees
GROUP BY department
HAVING COUNT(*) > 5
ORDER BY avg_salary DESC;

-- ── SUBQUERY ──
SELECT name FROM users
WHERE id IN (
  SELECT user_id FROM orders WHERE amount > 1000
);

-- ── TRANSACTIONS ──
BEGIN TRANSACTION;
  UPDATE accounts SET balance = balance - 500 WHERE id = 1;
  UPDATE accounts SET balance = balance + 500 WHERE id = 2;
COMMIT;
-- or ROLLBACK if something fails
```

```js
// Node.js with pg (PostgreSQL)
const { Pool } = require('pg');
const pool = new Pool({ connectionString: process.env.DATABASE_URL });

async function getUserOrders(userId) {
  const { rows } = await pool.query(
    'SELECT u.name, o.amount FROM users u JOIN orders o ON u.id = o.user_id WHERE u.id = $1',
    [userId]
  );
  return rows;
}
```

---

## 📇 Indexing

### Q: What is indexing and why does it matter?

**Answer:**
An index is a data structure (usually a B-tree) that speeds up read queries by allowing the database to find rows without scanning every row. The trade-off is slightly slower writes and more storage.

```js
// ── MONGODB INDEXES ──
// Single field index
db.users.createIndex({ email: 1 });          // 1 = ascending
db.users.createIndex({ createdAt: -1 });     // -1 = descending

// Unique index
db.users.createIndex({ email: 1 }, { unique: true });

// Compound index (order matters!)
db.orders.createIndex({ userId: 1, createdAt: -1 });

// Text index for search
db.articles.createIndex({ title: 'text', body: 'text' });
db.articles.find({ $text: { $search: 'javascript' } });

// Explain a query (check if index is used)
db.users.find({ email: 'a@b.com' }).explain('executionStats');
```

```sql
-- ── SQL INDEXES ──
-- Create index
CREATE INDEX idx_users_email ON users(email);

-- Composite index
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at DESC);

-- Unique index
CREATE UNIQUE INDEX idx_users_email_unique ON users(email);

-- Check query plan
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'a@b.com';
```

**When NOT to index:**
- Small tables (full scan is faster)
- Columns with very low cardinality (e.g., boolean fields)
- Heavily written tables (indexes slow down writes)

---

# 6. System Design & Architecture

---

## 🏗️ Microservices

### Q: What are microservices and when should you use them?

**Answer:**
Microservices is an architecture where an application is split into small, independent services, each responsible for a specific business capability, communicating via APIs or message queues.

```
Monolith:                  Microservices:
┌─────────────────┐        ┌────────┐ ┌─────────┐ ┌──────────┐
│   Single App    │        │  User  │ │  Order  │ │ Payment  │
│  - User logic   │  →     │Service │ │ Service │ │ Service  │
│  - Order logic  │        └────────┘ └─────────┘ └──────────┘
│  - Payment logic│              ↑          ↑           ↑
└─────────────────┘         ┌───────────────────────┐
                            │      API Gateway       │
                            └───────────────────────┘
```

```js
// API Gateway pattern with Express
const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const gateway = express();

gateway.use('/users', createProxyMiddleware({
  target: 'http://user-service:3001',
  changeOrigin: true,
}));

gateway.use('/orders', createProxyMiddleware({
  target: 'http://order-service:3002',
  changeOrigin: true,
}));

gateway.listen(3000, () => console.log('Gateway running on :3000'));
```

---

## 🐰 RabbitMQ & Queuing

### Q: What is a message queue and how does RabbitMQ work?

**Answer:**
A message queue decouples services by allowing them to communicate asynchronously. Producer sends a message to a queue; consumer processes it independently.

```
Producer → [Queue] → Consumer
  (fast)               (slow OK, processes at own pace)
```

```js
const amqp = require('amqplib');

// ── PRODUCER (sends messages) ──
async function sendTask(task) {
  const connection = await amqp.connect('amqp://localhost');
  const channel = await connection.createChannel();
  const queue = 'task_queue';

  await channel.assertQueue(queue, { durable: true }); // survives restart

  const message = JSON.stringify(task);
  channel.sendToQueue(queue, Buffer.from(message), {
    persistent: true // message survives broker restart
  });

  console.log('Sent:', message);
  await channel.close();
  await connection.close();
}

sendTask({ type: 'send_email', to: 'user@example.com', subject: 'Welcome!' });

// ── CONSUMER (processes messages) ──
async function startConsumer() {
  const connection = await amqp.connect('amqp://localhost');
  const channel = await connection.createChannel();
  const queue = 'task_queue';

  await channel.assertQueue(queue, { durable: true });
  channel.prefetch(1); // only 1 unacked message at a time (fair dispatch)

  console.log('Waiting for messages...');

  channel.consume(queue, async (msg) => {
    const task = JSON.parse(msg.content.toString());
    console.log('Processing:', task);

    try {
      await processTask(task); // do the actual work
      channel.ack(msg);        // acknowledge success
    } catch (err) {
      channel.nack(msg, false, true); // nack = put back in queue
    }
  });
}
```

---

## 📊 Latency & Throughput

### Q: What is the difference between latency and throughput?

**Answer:**
- **Latency**: How long a single request takes (milliseconds) — *speed*
- **Throughput**: How many requests are processed per second (RPS) — *volume*

```
Low latency + High throughput = ideal system
High latency + Low throughput = system under stress
```

```js
// Measuring latency in Express
app.use((req, res, next) => {
  const start = process.hrtime.bigint();

  res.on('finish', () => {
    const end = process.hrtime.bigint();
    const latencyMs = Number(end - start) / 1e6;
    console.log(`${req.method} ${req.url} — ${latencyMs.toFixed(2)}ms`);
  });

  next();
});

// Improving throughput strategies:
// 1. Caching (Redis)
const redis = require('redis');
const cache = redis.createClient();

async function getUser(id) {
  const cached = await cache.get(`user:${id}`);
  if (cached) return JSON.parse(cached); // fast path

  const user = await User.findById(id);  // slow path (DB)
  await cache.setEx(`user:${id}`, 3600, JSON.stringify(user));
  return user;
}

// 2. Connection pooling
const pool = new Pool({
  max: 20,         // max connections
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000,
});

// 3. Horizontal scaling with cluster
const cluster = require('cluster');
const os = require('os');

if (cluster.isPrimary) {
  const numCPUs = os.cpus().length;
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork(); // spawn one worker per CPU
  }
  cluster.on('exit', (worker) => {
    console.log(`Worker ${worker.process.pid} died, restarting...`);
    cluster.fork();
  });
} else {
  // Each worker runs the Express app
  const app = require('./app');
  app.listen(3000);
}
```

---

# 7. Networking & Protocols

---

## 🌍 HTTP vs HTTPS

### Q: What is the difference between HTTP and HTTPS?

| Feature | HTTP | HTTPS |
|---|---|---|
| Encryption | ❌ None | ✅ TLS/SSL |
| Port | 80 | 443 |
| Security | Data sent in plaintext | Data encrypted in transit |
| Certificate | Not needed | SSL certificate required |
| Use case | Internal/dev | Production, anything with user data |

```js
// HTTP server
const http = require('http');
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello HTTP!');
});
server.listen(80);

// HTTPS server
const https = require('https');
const fs = require('fs');

const options = {
  key: fs.readFileSync('private-key.pem'),
  cert: fs.readFileSync('certificate.pem'),
};

const secureServer = https.createServer(options, (req, res) => {
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ message: 'Secure!' }));
});
secureServer.listen(443);

// Redirect HTTP to HTTPS
http.createServer((req, res) => {
  res.writeHead(301, { Location: `https://${req.headers.host}${req.url}` });
  res.end();
}).listen(80);
```

### Q: What are HTTP status codes?

```
1xx — Informational
2xx — Success:       200 OK, 201 Created, 204 No Content
3xx — Redirect:      301 Moved Permanently, 302 Found
4xx — Client Error:  400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests
5xx — Server Error:  500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable
```

---

## 🔌 TCP vs UDP

### Q: What is the difference between TCP and UDP?

| Feature | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented (3-way handshake) | Connectionless |
| Reliability | Guaranteed delivery, ordered | No guarantee, can lose packets |
| Speed | Slower | Faster |
| Error checking | Yes | Minimal |
| Use case | HTTP, FTP, email | Video streaming, gaming, DNS, VoIP |

```
TCP 3-way Handshake:
Client          Server
  |—— SYN ——→     |   "I want to connect"
  |  ←—— SYN-ACK —|   "OK, I acknowledge"
  |—— ACK ——→     |   "Great, connected!"
  |=== Data ======|
```

---

## 📞 SDP & SIP

### Q: What are SDP and SIP used for?

**Answer:**
Both are used in real-time communication (VoIP, video calls, WebRTC).

- **SIP (Session Initiation Protocol)**: Handles *signaling* — setting up, managing, and tearing down communication sessions (like the "phone ringing" part).
- **SDP (Session Description Protocol)**: Describes the *media parameters* of a session — what codecs, what IP, what port, what format.

```
Call flow:
  Alice                   Bob
    |—— SIP INVITE ——→    |   "Hey, want to call?"
    |    (with SDP offer) |   codec: opus, port: 5004
    |  ←—— 200 OK ————    |   "Yes! I support opus too"
    |    (with SDP answer) |
    |—— ACK ————————→    |   "Great, let's go"
    |=== RTP Media ======|   (actual audio/video)
    |—— BYE ————————→    |   "Hanging up"
```

```js
// WebRTC SDP example (browser/Node.js)
const peerConnection = new RTCPeerConnection();

// Create offer (generates SDP)
const offer = await peerConnection.createOffer();
await peerConnection.setLocalDescription(offer);

// The SDP looks like:
const sdpExample = `
v=0
o=alice 123 456 IN IP4 192.168.1.1
s=Call
c=IN IP4 192.168.1.1
t=0 0
m=audio 5004 RTP/AVP 0
a=rtpmap:0 PCMU/8000
m=video 5006 RTP/AVP 96
a=rtpmap:96 VP8/90000
`.trim();
```

---

# 8. Linux Essentials

---

## 🐧 Linux Basic Commands

### Q: What are the most important Linux commands for a Node.js developer?

```bash
# ── FILE & DIRECTORY ──
ls -la              # list all files with details
pwd                 # print working directory
cd /path/to/dir     # change directory
mkdir -p a/b/c      # create nested directories
rm -rf folder/      # remove directory recursively (careful!)
cp -r src/ dest/    # copy recursively
mv old.txt new.txt  # move / rename
touch file.txt      # create empty file
cat file.txt        # print file contents
less file.txt       # paginate file contents
head -n 20 file.txt # first 20 lines
tail -f app.log     # live tail a log file
grep -rn "error" .  # search recursively for "error"
find . -name "*.js" # find files by name

# ── PROCESS MANAGEMENT ──
ps aux              # list all processes
ps aux | grep node  # find Node processes
kill -9 <PID>       # force kill a process
pkill node          # kill all node processes
top                 # live process viewer
htop                # better live process viewer

# ── NETWORK ──
curl -X GET https://api.example.com/users         # HTTP GET
curl -X POST -H "Content-Type: application/json" \
  -d '{"name":"Alice"}' https://api.example.com/users
netstat -tulpn      # show open ports and listeners
lsof -i :3000       # what's using port 3000?
ping google.com     # test connectivity
nslookup domain.com # DNS lookup
ss -tlnp            # socket statistics

# ── PERMISSIONS ──
chmod 755 script.sh    # rwxr-xr-x
chmod +x script.sh     # make executable
chown user:group file  # change owner

# ── SYSTEM INFO ──
df -h               # disk usage
free -m             # memory usage (MB)
uptime              # system uptime + load average
uname -a            # OS info
nproc               # number of CPU cores

# ── NODE.JS SPECIFIC ──
node -e "console.log('hello')"   # run inline JS
node --inspect app.js            # enable debugger
NODE_ENV=production node app.js  # set env variable
nohup node app.js &              # run in background
pm2 start app.js --name myapp   # process manager
pm2 logs myapp                   # view logs
pm2 restart myapp                # restart
pm2 list                         # list all processes

# ── ENVIRONMENT ──
echo $HOME            # print variable
export PORT=3000      # set env variable
env                   # list all env variables
cat .env              # view env file
source .env           # load env file into shell
```

---

## 🎯 Quick Reference Cheat Sheet

| Topic | Key Points |
|---|---|
| **Event Loop** | Sync → Microtasks → Macrotasks |
| **Heap vs Stack** | Stack: primitives, LIFO. Heap: objects, GC managed |
| **Hoisting** | `var` → undefined. `let/const` → TDZ error. Functions → fully hoisted |
| **Closure** | Inner function remembers outer scope even after outer returns |
| **Prototype** | Every object has `[[Prototype]]`. Chain ends at `Object.prototype → null` |
| **`this`** | Depends on call site. Arrow functions inherit `this` |
| **Shallow/Deep Copy** | Shallow: `{...obj}`. Deep: `structuredClone()` or `JSON.parse(JSON.stringify())` |
| **Promise states** | pending → fulfilled or rejected |
| **exec vs spawn** | exec: buffers all output. spawn: streams output |
| **fork** | Spawn Node.js child with IPC channel |
| **Worker Threads** | Shared memory, CPU tasks. Child Process: isolation, shell commands |
| **Middleware** | `(req, res, next)` — always call `next()` or send response |
| **JWT Auth** | Sign on login, verify on every protected request |
| **Rate limiting** | Track requests by IP/user, return 429 when exceeded |
| **MongoDB Index** | Speeds up reads, slows writes. Use `explain()` to verify |
| **TCP vs UDP** | TCP: reliable, ordered. UDP: fast, no guarantee |
| **Latency** | Time per request (ms). Throughput: requests per second |
| **RabbitMQ** | Producer → Queue → Consumer. `ack()` confirms processing |

---

*Good luck with your interviews! 🚀*
