# 🎙️ JavaScript — Interview Verbal Answers Guide
### No code. Pure understanding. Speak with confidence.

> **How to use this:** The **bold sentence** after each question is your opening line — say that first, pause, then expand. The 🎤 blocks are counter questions your interviewer will likely throw — your answer follows immediately. Read every answer out loud at least once before the interview.

---

## 📋 Table of Contents

| Topic | Questions Covered |
|-------|------------------|
| [Closures](#closures) | What is a closure · Output question |
| [Event Loop](#eventloop) | How it works · Output question |
| [Call / Apply / Bind](#cab) | What they do · When to use each |
| [this Keyword](#this) | What this is · How context changes |
| [Array Methods](#arrays) | map vs filter · When to use each · Loop alternative |
| [let, var, Scope, Hoisting](#scope) | Differences · Block vs function scope · Hoisting |
| [Promises & Async/Await](#promises) | What a Promise is · async/await · Output question |
| [Sorting Algorithm](#sorting) | Approach · Time complexity · Number of loops |
| [Deep Copy](#deepcopy) | How to deep copy · Nested objects |
| [Quick Recall Cheatsheet](#cheatsheet) | Opening lines for every topic |

---

<a name="closures"></a>
## 1️⃣ Closures

---

### Q: Can you explain closures?

**A closure is when a function remembers and continues to have access to the variables from the scope in which it was created, even after that outer scope has completely finished executing.**

To really understand this, you need to understand how JavaScript manages memory. Normally, when a function finishes running, all the local variables it created are cleaned up and freed from memory. But closures break this rule in a deliberate and useful way. When an inner function is defined inside an outer function, the inner function forms a bond with the variables around it. Even when the outer function finishes and its execution context is gone, those variables are kept alive in memory because the inner function still holds a reference to them. The garbage collector sees that something is still using those variables, so it does not clean them up.

Think of it like a backpack. When a function is born, it packs a backpack with everything in its surrounding environment. It carries this backpack wherever it goes. Even if the place where it was created no longer exists, the function still has its backpack and can reach into it at any time.

This is not an accidental feature — it is one of JavaScript's most powerful design patterns. Closures are the mechanism behind private variables, factory functions, callback functions that remember their context, and the entire module pattern that was the backbone of JavaScript architecture for years before ES6 classes were introduced.

---

🎤 **"Why doesn't the variable reset every time you call the inner function?"**

> Because the inner function does not hold a snapshot or a copy of the variable — it holds a live reference to the actual variable in memory. That same memory slot persists across every call. Think of it like a shared whiteboard in a room. Every time the inner function runs, it walks up to the same whiteboard and reads or writes the current value. Nobody is erasing that whiteboard between calls. The value accumulates because it is the same variable every time, not a new one.

---

🎤 **"Can closures lead to memory leaks?"**

> Yes, absolutely, and this is a real-world concern. Because a closure keeps the outer scope's variables alive, those variables cannot be garbage collected for as long as the closure function itself exists. If you create closures and store them in places that are never cleaned up — like event listeners on DOM elements that you remove from the page but never detach the listener from — the memory they hold onto keeps growing. The fix is always to remove event listeners when they are no longer needed, and be mindful of long-lived closures that hold references to large objects they no longer actually need.

---

🎤 **"What is a real practical use case for closures?"**

> The most concrete example is creating private state. JavaScript before classes had no concept of private variables, but with closures you could hide data inside a function and expose only a controlled interface to interact with it. A counter is the simple version, but a fuller example is a bank account — you wrap the balance in a closure and only expose deposit, withdraw, and getBalance as the ways to interact with it. The balance itself is completely unreachable from outside the closure. Nobody can set it to an arbitrary value directly; they can only go through the functions you provide. This is the module pattern, and understanding it shows deep knowledge of how JavaScript works.

---

### Q: Given a closure snippet with a `for` loop and `var`, what will the output be?

**All the callbacks will print the final value of the loop variable, not the value at the time each iteration ran, because `var` is function-scoped and the entire loop shares one single variable.**

The trap here is the assumption that each callback captures the value of the loop variable at the moment it was created. It does not. What each callback captures is a reference to the variable itself — a pointer to the same place in memory. The loop runs to completion almost instantly — it is synchronous code. By the time any of the asynchronous callbacks are picked up by the event loop and executed, the loop is completely done and the variable has already reached its final value. Every single callback then reads that same final value because they all share the same variable reference.

The fix is to use `let` instead of `var`. Because `let` is block-scoped, each iteration of the loop creates its own fresh, independent variable. Each callback then closes over a completely separate variable, and they no longer interfere with each other.

---

🎤 **"Can you explain why `let` fixes this but `var` doesn't in one sentence?"**

> With `var` there is one shared variable across all iterations; with `let` each iteration creates a completely new, independent variable, so each callback closes over its own copy.

---

<a name="eventloop"></a>
## 2️⃣ The Event Loop

---

### Q: Can you explain the event loop in JavaScript?

**The event loop is the system that allows JavaScript — which can only do one thing at a time — to handle asynchronous operations without freezing or blocking.**

JavaScript runs on a single thread. That means there is exactly one call stack, and only one piece of code can run at any given moment. This sounds like a severe limitation, but the event loop is the engineering solution that makes a single thread surprisingly powerful.

Here is how it works. The call stack is where your synchronous code runs. When you call a function it goes on the stack, when it returns it comes off the stack. When you trigger an asynchronous operation — a network request, a timer, reading a file — that operation is handed off to the environment, meaning the browser or Node.js, which handles it in the background using its own threads. Your JavaScript thread is now free to keep running other synchronous code without waiting.

When the background operation finishes, its callback is not immediately run. Instead it is placed into a queue. The event loop sits between the call stack and the queues and continuously monitors them. Its one job is to ask: is the call stack currently empty? If yes, take the next item from the queue and push it onto the stack to be executed. If no, wait.

There are actually two distinct queues that matter here, and the priority between them is critical knowledge. The microtask queue holds callbacks from Promises — `.then()` handlers and `await` continuations. The macrotask queue holds callbacks from `setTimeout`, `setInterval`, and similar APIs. The rule is that after every single piece of code that runs, the event loop completely drains the entire microtask queue before it ever picks up a single item from the macrotask queue. Promise callbacks always take priority over timer callbacks.

---

🎤 **"Why is JavaScript single-threaded? Isn't that a design flaw?"**

> It is an intentional design choice, not a flaw. The problem with multiple threads sharing the same memory is that they can accidentally modify the same data at the same time, causing unpredictable bugs called race conditions. Preventing this requires complex mechanisms like locks and semaphores, which are hard to reason about and easy to get wrong. JavaScript sidesteps all of this by having a single thread where code runs sequentially and predictably. The event loop gives you the benefits of asynchronous behaviour — not blocking on slow operations — without any of the complexity of multi-threaded programming. For CPU-intensive work, Web Workers provide true parallelism, but they communicate through message passing rather than shared memory, which keeps things safe.

---

🎤 **"What is the difference between a microtask and a macrotask?"**

> A microtask is a callback from a Promise — created by `.then()` or `await`. A macrotask is a callback from a timer — created by `setTimeout` or `setInterval`. The critical difference is priority. After any piece of code finishes running, the entire microtask queue is emptied before a single macrotask is processed. This means if a Promise resolution creates another Promise, and that creates another, all of them will complete before any timer fires. This property is important because it means Promise-based code behaves with higher urgency than timer-based code, which matters when reasoning about execution order.

---

### Q: Given a snippet with `console.log`, `setTimeout`, and `Promise.resolve`, what is the output?

**The two synchronous console logs run first in order, then the Promise callback runs, and the setTimeout callback runs last — even if its delay is zero milliseconds.**

The reasoning flows directly from the event loop's priority rules. Anything written directly in the script, not inside a callback, is synchronous and executes on the call stack immediately. Nothing queued can run until the current synchronous block finishes. Once the synchronous block is done and the stack empties, the event loop checks the microtask queue first. The Promise that was already resolved has its `.then()` callback sitting there waiting, so it runs next. Only after the microtask queue is completely empty does the event loop look at the macrotask queue and pick up the setTimeout callback.

Zero milliseconds on a `setTimeout` does not mean "run immediately." It means "run as soon as possible, but still only after the current synchronous work and all queued microtasks are complete." Zero milliseconds is a minimum delay, not an exact timing.

---

🎤 **"What if there were five chained Promise `.then()` calls — would they all run before the setTimeout?"**

> Yes, all five would run before the setTimeout. Each `.then()` in a chain produces a new microtask when it resolves. The event loop will keep processing microtasks — including new ones that are generated during microtask processing — until the entire microtask queue is empty. Only at that point, with the queue completely drained, does it pick up the first macrotask. No matter how many chained Promises you have, they all get priority over any setTimeout, regardless of the timer's delay.

---

<a name="cab"></a>
## 3️⃣ Call, Apply, and Bind

---

### Q: Explain call, apply, and bind with examples.

**All three are methods that let you explicitly control what `this` refers to when a function runs — they are tools for borrowing functions and executing them in a different context.**

To understand why these methods exist, you first need to accept that in JavaScript, `this` is not determined by where a function is defined but by how it is called. The same function can have a completely different `this` depending on the context in which it is invoked. Sometimes you have a function on one object that you want to use in the context of a completely different object, without rewriting the function. That is exactly the problem these three methods solve.

**`call`** is the most direct. It invokes the function immediately and lets you pass in the object you want as `this` as the first argument. Any arguments the function itself needs come after, separated by commas, just like a normal function call. You use `call` when you want to execute a function right now with a specific context.

**`apply`** is functionally identical to `call` — it also invokes the function immediately and takes the same first argument for `this`. The only difference is that instead of passing the function's own arguments individually, you pass them all together as an array. Historically this was useful when your data was already in array form and you did not want to unpack it. With modern spread syntax this distinction matters less, but it is still important conceptually.

**`bind`** is where it gets more interesting. Unlike `call` and `apply`, `bind` does not invoke the function at all. Instead it creates and returns a brand new function that has `this` permanently locked to whatever object you specified. You can call this new function later, pass it to a timer, attach it as an event handler — no matter what, `this` will always be what you bound it to. The binding cannot be overridden by how the function is subsequently called. You can also partially apply arguments when binding, meaning you can lock in some of a function's arguments in advance and leave the rest to be provided when the function is eventually called.

---

🎤 **"When would you actually need bind in a real application?"**

> The most common real-world scenario is class methods used as callbacks. When you define a method on a class and then pass it to a `setTimeout` or an event listener, the method gets detached from the class instance. When the browser or timer later calls it, it is calling it as a plain function, not as a method on your object — so `this` is no longer your class instance. Using `bind` when attaching the callback permanently locks `this` to the correct instance. Arrow functions in class fields solve the same problem in a more modern way, but understanding why you need `bind` shows you understand the underlying mechanics.

---

🎤 **"What is the practical difference between call and apply today?"**

> Very little in practice, because spread syntax covers most cases where `apply` was the traditional choice. Both execute the function immediately with a specified `this`. The old reason to prefer `apply` was when you had an array of arguments — rather than unpacking them manually, you could pass the array directly to `apply`. Today you can achieve the same thing with `call` and a spread operator. Knowing both is important for reading older code and for interview questions, even if in new code you would default to `call` or spread.

---

<a name="this"></a>
## 4️⃣ The `this` Keyword

---

### Q: Explain `this` with an example.

**`this` is a keyword that refers to the object currently executing the function, and its value is determined entirely by how the function is called — not where it is written.**

This is arguably the most misunderstood concept in JavaScript. In most class-based languages, `this` or `self` is stable — it always refers to the instance of the class the method belongs to. In JavaScript, `this` is dynamic. It can change based on the call site, meaning the exact same function can have a completely different `this` depending on the context in which someone invokes it.

There are four rules that govern what `this` will be at any point.

The first rule is **method invocation**. When you call a function as a property of an object — with a dot between the object and the function name — `this` is that object. This is the intuitive case and what most people expect.

The second rule is **plain function invocation**. When you call a function on its own, without any object before it, `this` is either the global object in non-strict mode or `undefined` in strict mode. This is the rule that catches people off guard and causes bugs.

The third rule is **constructor invocation**. When you use the `new` keyword, a brand new empty object is created, and inside the constructor function, `this` refers to that newly created object.

The fourth rule is **explicit binding**. When you use `call`, `apply`, or `bind`, you are manually overriding all other rules and directly telling JavaScript what `this` should be.

Arrow functions are the important exception that does not fit any of these four rules. An arrow function has no `this` of its own. Instead it inherits `this` from the lexical scope — the surrounding code where the arrow function was written. This is called lexical `this`, and it is one of the primary reasons arrow functions were introduced. They make `this` predictable in callbacks and nested functions.

---

🎤 **"Why does `this` break when you pass a method as a callback?"**

> When you take a method from an object and pass it as a callback — to `setTimeout`, to `addEventListener`, to anything that will call it later — you are handing over just the function reference. You are detaching it from the object it came from. JavaScript has no mechanism for remembering that this function "belongs to" that object once the reference is passed around. When the callback is eventually invoked by the browser or the timer, it is called as a plain function, triggering rule two — `this` becomes the global object or `undefined`. The method thinks it is floating free with no owner. Arrow functions solve this because they do not have their own `this` at all; they look outward to where they were defined and whatever `this` was there stays fixed permanently.

---

🎤 **"What does `this` refer to in an arrow function inside a class method?"**

> It refers to the class instance, because the arrow function inherits `this` from the surrounding method, and the method's `this` is the instance. This is actually a deliberately useful pattern. When you write a callback inside a class method as an arrow function, `this` is captured at the time the method runs, and that captured value follows the arrow function wherever it goes. This is why React developers write event handler class fields as arrow functions — to ensure `this` is always the component instance regardless of how React calls the handler.

---

🎤 **"Can `this` be explicitly set to null or something unusual?"**

> Yes. You can pass `null` or `undefined` as the first argument to `call` or `apply`, and in non-strict mode JavaScript will replace `null` with the global object. In strict mode, `this` will actually be `null` or `undefined` as you specified. Using `null` with `call` or `apply` is sometimes done intentionally when you just want to borrow a function and the function does not actually use `this` — it is a way of making the intent clear that the context is irrelevant.

---

<a name="arrays"></a>
## 5️⃣ Array Methods — map and filter

---

### Q: What is the difference between map and filter?

**`map` transforms every element in an array into something new and always returns an array of the same length. `filter` selects which elements survive based on a condition and returns an array that may be shorter.**

The distinction comes down to purpose and what they do to the array's length.

When you use `map`, you are making a statement: "I want to do something to every single element in this collection, and I want the results." Every element gets processed. Every element produces an output. If you start with ten items, you end with ten items — the shape of the collection is preserved, but the content of each element is transformed. You are not deciding whether items should be included; you are deciding what they should become.

When you use `filter`, you are making a different statement: "From this collection, I want only the elements that meet this condition." You are not changing the elements themselves — the ones that survive are returned exactly as they were. The array can shrink dramatically or even become empty if nothing meets the condition. The shape of the collection can change, but the surviving elements are unchanged.

Both always return a brand new array. Neither mutates the original. This is an important property — your original data is always safe, which is fundamental to writing predictable, bug-resistant code, especially in frameworks like React where immutability is central to how updates are detected.

---

🎤 **"When would you use map and when would you use filter?"**

> I reach for `map` when my goal is transformation — I have data in one shape and I need it in a different shape. The most common example is extracting a specific property from each object in an array, or converting raw data into a formatted display version. The signal is that I want something for every element.

> I reach for `filter` when my goal is selection — I have a collection and I want a subset of it. Showing only active users, finding products under a certain price, isolating incomplete tasks. The signal is that I want to exclude some elements based on a rule.

> In practice they are often chained together. First filter down to the items you care about, then map those items into the format you need. The order matters for performance — filtering first means you run the transformation on fewer items.

---

🎤 **"If we don't use filter, can we achieve the same result with a loop?"**

> Absolutely. `filter` is fundamentally a loop with a conditional push. You write a `for` loop, check the condition for each item, and push the matching ones into a new array. The end result is identical. The reason `filter` is preferred has nothing to do with capability — a loop is equally capable. It is about readability and intent. When someone reads a `filter` call, they immediately understand what is happening without reading any implementation detail. With a loop, they have to read through the body to figure out the intent. `filter` also removes common loop pitfalls — off-by-one errors, forgetting to initialize the result array, accidentally mutating the original collection. The built-in method handles all of that correctly by design, every time.

---

<a name="scope"></a>
## 6️⃣ let, var, Scope, and Hoisting

---

### Q: Can you explain let and var?

**`var` is the old way to declare variables — it is function-scoped and has quirky hoisting behaviour. `let` is the modern way — it is block-scoped, safer, and behaves much more predictably.**

The most critical practical difference is how they relate to scope boundaries. A `var` declaration belongs to the nearest enclosing function, or the global scope if there is no function. It completely ignores the boundaries of blocks — `if` statements, `for` loops, `while` loops, or any standalone pair of curly braces. This means a `var` declared inside an `if` block is fully accessible outside that block, within the same function. This is almost never what you intend, and it is a persistent source of subtle, hard-to-track bugs.

`let` was introduced specifically to fix this behaviour. A `let` declaration belongs to the nearest pair of curly braces — the nearest block. When that block ends, the variable ceases to exist. It is contained exactly where you put it. This matches the intuition most developers have when they declare a variable inside a block — they expect it to stay there.

The second important difference is their hoisting behaviour, which we can explore more deeply, but at a high level: `var` declarations are silently initialized to `undefined` before code runs, which masks mistakes. `let` declarations throw a clear, explicit error if you try to access them before their declaration line.

In modern JavaScript there is very little reason to use `var`. `let` for variables that change and `const` for variables that do not is the standard, and it produces code that is far easier to reason about.

---

🎤 **"What do you mean by block scope and function scope?"**

> Scope describes where in your code a variable is visible and accessible. Function scope means the variable is visible anywhere inside the function it was declared in — all the way through, regardless of any nested structures like `if` blocks or loops. Block scope means the variable is visible only within the specific pair of curly braces it was declared inside. Any `{ }` pair creates a block — an `if` body, a `for` loop, a `while` loop, or even a standalone block. `var` only respects function boundaries. `let` and `const` respect every boundary. Block scope gives you much finer-grained control and eliminates an entire category of accidental variable leakage and naming collisions.

---

### Q: What is hoisting?

**Hoisting is JavaScript's behaviour of processing and registering all declarations before any code actually executes, which makes certain variables and functions available earlier in the code than where they were written.**

The useful mental model is that JavaScript makes two passes through your code. In the first pass, before a single line executes, it scans the entire scope and registers all `var` declarations and function declarations. It does not run any logic — it just takes note of what exists. In the second pass, it executes the code from top to bottom.

Because declarations are registered in the first pass, referencing a `var` variable before its declaration line does not produce a "variable is not defined" error. Instead, the variable exists but has the value `undefined` because only the declaration was hoisted, not the assignment. The assignment stays exactly where you wrote it in the source code.

Function declarations are hoisted more completely — both the declaration and the entire function body are registered in the first pass. This is why you can call a named function before it appears in the file.

`let` and `const` occupy a middle ground that is important to understand correctly. They are technically hoisted — JavaScript registers their existence in the first pass. But they are placed in what is called the Temporal Dead Zone from the start of their block until the line where you declare them. Any attempt to access them during this zone throws a `ReferenceError`. This is intentional — it makes the mistake loud and obvious rather than silently returning `undefined`, which is what `var` does.

---

🎤 **"Why is the Temporal Dead Zone for `let` considered a good thing?"**

> Because it surfaces bugs immediately. With `var`, if you accidentally reference a variable before setting it, you silently get `undefined`. Your code keeps running, the value is wrong, and you might not discover the bug until much later — perhaps through a broken UI or incorrect calculation. With `let`, you get a `ReferenceError` right at the line where the mistake is. The programme stops and tells you exactly what went wrong. This is called failing fast, and it is universally considered better than failing silently. The Temporal Dead Zone transforms a silent bug into a loud, obvious one.

---

🎤 **"What is the difference between hoisting a `var` and hoisting a function declaration?"**

> With `var`, only the declaration is hoisted — the variable is registered and initialised to `undefined`, but its value is not set until execution reaches the assignment line. With a function declaration, both the declaration and the full function body are hoisted — the function is fully available and callable before its line in the source code. This is why function declarations can be called before they appear in the file, which is not true of function expressions assigned to `var` or `let` variables.

---

<a name="promises"></a>
## 7️⃣ Promises and Async/Await

---

### Q: What is a Promise?

**A Promise is an object that represents the eventual outcome of an asynchronous operation — it is JavaScript's way of saying "I don't have this value right now, but I promise to give it to you when it is ready, or to tell you if something went wrong."**

Before Promises, asynchronous code was handled entirely through callbacks — you passed a function to be called when an operation completed. For simple cases this worked. But as applications grew more complex, you often needed to perform multiple asynchronous operations in sequence, where each step depended on the result of the previous. This produced deeply nested callbacks — callbacks inside callbacks inside callbacks — a structure developers called "callback hell." It was extremely difficult to read, nearly impossible to maintain, and error handling was fragmented because you had to handle errors independently at each level of nesting.

A Promise completely rethinks this model. Instead of handing in a callback and hoping it gets called correctly, an asynchronous function gives you back an object immediately. That object is the Promise. It is a handle for the future value. You can store it, pass it around, and attach handlers to it at any point. The Promise will eventually settle into one of two states: fulfilled, meaning the operation succeeded and the resolved value is available; or rejected, meaning the operation failed and the error is available. A Promise starts in a pending state and can only ever move to fulfilled or rejected once, and it never changes again after that.

You interact with the Promise by attaching handlers. `.then()` runs when it is fulfilled and receives the resolved value. `.catch()` runs when it is rejected and receives the error. `.finally()` runs regardless of which way it went. Critically, `.then()` itself returns a new Promise, so you can chain operations in a flat, readable sequence. Each step in the chain receives the result of the previous step. Error handling is centralised — one `.catch()` at the end of the chain catches failures from any step. This is the transformation that made asynchronous code manageable.

---

🎤 **"What is the difference between a Promise and a callback?"**

> A callback is a function you hand to someone else and trust them to call at the right time. You lose control — you cannot choose when it runs, you cannot easily chain multiple callbacks cleanly, and error handling is spread throughout. A Promise hands control back to you. You get an object you can work with on your own terms. You can chain operations predictably, handle all errors in one place, and compose complex async logic in a readable way. The mental model shifts from "here, you call this for me" to "give me an object representing the future result and I will handle it myself."

---

### Q: What do you mean by async and await?

**`async` and `await` are keywords built on top of Promises that allow you to write asynchronous code that reads like synchronous, top-to-bottom code — removing the complexity of `.then()` chains entirely.**

The problem that `async/await` solves is that even with Promises and chaining, complex asynchronous logic involving conditionals, loops, or many sequential steps can still become difficult to follow. A long chain of `.then()` calls is better than callback hell, but it still requires a particular mental model to read fluently.

`async/await` removes that friction by making asynchronous code look ordinary. When you mark a function with `async`, two things happen. The function automatically returns a Promise, even if you return a plain value — it is automatically wrapped. And you gain the ability to use `await` inside it. `await` can only be used inside an `async` function. When you place `await` before a Promise, execution of the current async function pauses at that line until the Promise settles, and then resumes with the resolved value assigned to whatever variable you put it in. It looks exactly like a synchronous assignment.

The rest of your application does not pause — only the current async function is suspended. The event loop is free to handle other work during the wait. When the Promise resolves, the function resumes from exactly where it left off.

Error handling goes back to the standard `try/catch` pattern that every developer is already familiar with from synchronous code. You wrap your `await` calls in a `try` block, and if any awaited Promise rejects, the error is thrown as an exception and caught by the `catch` block. This unification of sync and async error handling is one of the most significant ergonomic improvements.

---

🎤 **"Is async/await actually faster than using Promises with .then()?"**

> No. `async/await` is syntax on top of Promises — it compiles down to Promise-based code. There is no performance difference. It is purely a readability and ergonomics improvement. Some people have the misconception that `await` blocks the thread like a synchronous operation would, but it does not. It suspends the async function and returns control to the event loop, which is exactly what `.then()` does. The only difference is how the code looks on the screen.

---

🎤 **"What happens if you forget to write `await` before a Promise?"**

> The function does not wait — it moves to the next line immediately, and the variable you assigned receives the Promise object itself rather than the resolved value. This is a silent bug that does not throw an error immediately. You only discover it later when you try to use the variable and find it is a Promise instead of the data you expected. It is also dangerous in cases where sequence matters — if you are supposed to verify something before acting on it, forgetting `await` means both operations fire simultaneously without the intended ordering. It is one of the most common async mistakes.

---

### Q: Given a snippet with `console.log`, `setTimeout`, and a Promise, what will be the output?

**The synchronous logs run first, then the Promise callback, and the setTimeout runs last — even with a zero millisecond delay.**

This is a direct application of the event loop's priority rules. Synchronous code always runs first because it is on the call stack. Nothing from any queue can run until the current synchronous execution finishes. Once the call stack empties, the event loop checks the microtask queue — where the resolved Promise's `.then()` callback is waiting — and runs everything in it. Only after the microtask queue is completely empty does the event loop pick up the setTimeout callback from the macrotask queue.

The zero millisecond delay on `setTimeout` is commonly misunderstood. It does not mean "execute now" or "execute synchronously." It means "execute as soon as possible after the current work, but still honour the queue priorities." The minimum delay is effectively zero — but it will still always wait until after all microtasks are complete.

---

🎤 **"What if the Promise's `.then()` triggered another Promise — would that still run before the setTimeout?"**

> Yes. Every new `.then()` in a chain adds a new microtask to the microtask queue. The event loop processes all microtasks, including newly generated ones, before it ever touches the macrotask queue. So if you have a chain of ten Promises, all ten will complete before a single setTimeout fires. The only way to interrupt this would be if you explicitly delayed something inside a Promise chain with a `setTimeout` of its own.

---

<a name="sorting"></a>
## 8️⃣ Sorting Algorithm

---

### Q: What is your approach to sorting an array without built-in functions?

**My approach would be Bubble Sort — it is the most intuitive sorting algorithm and easy to implement correctly from memory, which is exactly what interview conditions call for.**

The core idea of Bubble Sort is straightforward. You go through the array and compare each element to the one immediately next to it. If they are in the wrong order — meaning the left one is larger than the right one — you swap them. You keep doing this, pass after pass through the array. On each pass, the largest unsorted element "bubbles up" to its correct position at the end, like a bubble rising through water. After the first pass, the largest element is in its final place. After the second pass, the second largest is in its final place. You continue until no swaps happen in a complete pass, which tells you the array is sorted.

The name comes directly from this visual — large values gradually float towards the end of the array while smaller values inch towards the front.

---

🎤 **"What is the time complexity of Bubble Sort?"**

> Bubble Sort is O(n²) in the worst and average case. The reason is that for an array of n elements, you make up to n-1 passes, and within each pass you make up to n-1 comparisons. Multiplying those together gives you approximately n squared operations. If you double the size of the input, the number of operations quadruples. This makes it very inefficient for large datasets. The best case is O(n), which only happens when the array is already sorted and you implement an early exit optimisation — if you complete a full pass without making any swaps, you know the array is sorted and can stop immediately.

---

🎤 **"How many loops are required to solve this?"**

> Two loops. The outer loop controls the number of passes through the array. It runs n minus one times because after each complete pass, one more element is guaranteed to be in its correct final position — it has bubbled up to where it belongs. The inner loop does the actual comparison work, going through the unsorted portion of the array and swapping adjacent elements that are out of order. The range of the inner loop shrinks by one with each pass of the outer loop, because the end of the array fills up progressively with correctly placed elements that no longer need to be examined.

---

🎤 **"Do you think this can be solved in a single loop?"**

> Not in the general case using a pure comparison-based approach. The two levels of iteration in Bubble Sort are both necessary — you need one level to iterate over elements for comparison, and another level to repeat the process multiple times until the array is fully sorted. You could restructure it by replacing the outer loop with recursion — call the same function again if a swap was made — but that is still equivalent to two levels of iteration; you are just expressing the outer loop through the call stack instead of an explicit loop.

> There are specialised sorting algorithms that appear simpler — Counting Sort and Radix Sort are examples that work in closer to linear time. But they only work under specific constraints: the values must be integers within a bounded, known range. For a general-purpose sort of arbitrary values, the theoretical minimum number of operations is O(n log n), which is what algorithms like merge sort and quicksort achieve. But all of them still fundamentally require more than a single pass through the data.

---

<a name="deepcopy"></a>
## 9️⃣ Deep Copy

---

### Q: How do you deep copy an object?

**A deep copy creates a completely independent duplicate of an object — a clone where changes to the copy, at any level of nesting, have absolutely no effect on the original.**

To understand why this matters, you first need to understand the problem with ordinary copying. When you copy an object in the simple way — using the spread operator or `Object.assign` — you create what is called a shallow copy. It copies the top-level properties, but if any of those properties are themselves objects or arrays, what gets copied is the reference — a pointer to the same underlying object in memory. Both the original and the copy end up pointing to the same nested object. If you then change something inside that nested object through the copy, you have inadvertently changed it in the original too, because they are sharing the same memory. This is a very common source of bugs, especially in applications where you think you are safely working with a copy of your data.

A deep copy fixes this by copying every level of the structure — not just the outer properties, but every nested object, every array, every array within an object, all the way down to the bottom. The result is two completely separate structures in memory with no shared references anywhere.

The most widely known method is using `JSON.parse` combined with `JSON.stringify`. You first serialize the entire object into a JSON string, producing a text representation of the complete data structure. You then parse that string back into a fresh JavaScript object. Because the round trip went through a string, every object and array in the result is newly created with no connection to the original.

The modern, recommended approach is `structuredClone`, a built-in global function available in all modern browsers and recent Node.js versions. It deep clones natively and handles many things that the JSON method cannot.

---

🎤 **"What are the limitations of the JSON stringify and parse approach?"**

> It works well for simple data objects, but it has meaningful gaps. Functions are silently dropped — any property that is a function disappears entirely in the copy. The value `undefined` is also removed without warning. `Date` objects are converted to strings and lose their identity as Date instances. `Map` and `Set` objects are not handled correctly — they come out as empty objects. Circular references — where an object contains a reference to itself — cause `JSON.stringify` to throw an error rather than handle it. `structuredClone` handles all of these cases correctly. It preserves Dates, Maps, Sets, and it can handle circular references. The only thing `structuredClone` does not copy is functions, because functions are not transferable data — but this is by design.

---

🎤 **"If I give you a deeply nested object, can you deep copy it correctly?"**

> Yes. Both `structuredClone` and the JSON method work recursively regardless of depth — they do not just handle one or two levels, they traverse the entire structure however deep it goes. If you needed to implement it manually without any built-in methods, you would write a recursive function. The function receives a value and checks what type it is. If it is a primitive — a string, number, boolean, null, or undefined — it is returned as-is because primitives are always copied by value in JavaScript. If it is an array, you create a new empty array and recursively copy each element into it. If it is a plain object, you create a new empty object and recursively copy each key-value pair into it. This recursion continues until every branch of the nested structure reaches a primitive at the bottom, guaranteeing that no object reference is shared between the original and the copy at any level.

---

🎤 **"When would deep copying actually be a bad idea?"**

> Deep copying large, complex objects can be expensive in both time and memory — you are duplicating every piece of data in the entire structure. If you have objects with thousands of nested items or a deeply branching tree, the copy operation could be a noticeable performance bottleneck in a hot code path. Beyond performance, there are cases where you intentionally want two parts of your application to share the same reference — for example, a shared state object that multiple components observe and react to. Deep copying would sever that connection and break the reactivity. The rule of thumb is: use deep copy when you need to protect the original from mutation and work with the data independently. Use shared references when you want changes in one place to propagate elsewhere by design.

---

<a name="cheatsheet"></a>
## 🧠 Quick Recall — Your Opening Line for Every Topic

> Say this first. Then expand. Interviewers form their impression in the first few seconds.

---

| Topic | Your Opening Line |
|-------|------------------|
| **Closure** | "A closure is when an inner function remembers variables from its outer scope even after the outer function has finished running." |
| **Closure output (var loop)** | "All callbacks will print the final loop value, not the per-iteration value, because var is function-scoped and the whole loop shares one variable." |
| **Event Loop** | "The event loop is how JavaScript — which is single-threaded — handles asynchronous operations without blocking everything." |
| **Microtask vs Macrotask** | "Microtasks like Promises always drain completely before any macrotask like setTimeout runs — that is the priority rule." |
| **Output (log/setTimeout/Promise)** | "Synchronous code runs first, then Promise callbacks, then setTimeout — even with zero milliseconds delay." |
| **call / apply / bind** | "All three let you control what this refers to when a function runs — call and apply invoke immediately, bind returns a new locked function." |
| **this** | "this refers to the object currently executing the function, and its value is determined by how the function is called, not where it is defined." |
| **Arrow function this** | "Arrow functions have no this of their own — they inherit it from the surrounding scope where they were written." |
| **map** | "map transforms every element and always returns a new array of the same length." |
| **filter** | "filter selects a subset of elements based on a condition and returns a shorter array — the elements themselves are unchanged." |
| **Loop vs filter** | "Yes, a loop can do exactly what filter does — filter is just a cleaner, more readable abstraction over that same loop." |
| **var vs let** | "var is function-scoped and leaks out of blocks. let is block-scoped and stays exactly where you put it." |
| **Block vs function scope** | "Function scope means visible anywhere in the function. Block scope means visible only inside the specific curly braces it was declared in." |
| **Hoisting** | "Hoisting is JavaScript processing declarations before code runs — var gets undefined, function declarations are fully available, let gets a Temporal Dead Zone error." |
| **Temporal Dead Zone** | "let exists but is inaccessible from the start of its block until the declaration line — this is intentional to surface mistakes loudly." |
| **Promise** | "A Promise is an object representing a future value — it is pending until it either fulfils with a value or rejects with an error." |
| **async / await** | "async/await is syntax built on Promises that makes asynchronous code read like synchronous, top-to-bottom code." |
| **Bubble Sort** | "Bubble Sort repeatedly compares adjacent elements and swaps them if they are out of order, bubbling the largest unsorted value to its final position each pass." |
| **Time complexity** | "O(n²) — two nested loops, n passes times n comparisons, so the work grows as the square of the input size." |
| **Single loop sorting** | "Not in the general case — comparison-based sorting inherently requires multiple passes. Specialised algorithms exist for integers in a known range, but not for general data." |
| **Deep copy** | "A deep copy creates a completely independent clone at every level of nesting — no shared references between the original and the copy anywhere." |
| **Shallow vs deep** | "Shallow copy duplicates only the top level — nested objects are still shared. Deep copy duplicates every level — nothing is shared." |
| **structuredClone** | "structuredClone is the modern built-in for deep copying — it handles Dates, Maps, Sets, and circular references, unlike the JSON method." |