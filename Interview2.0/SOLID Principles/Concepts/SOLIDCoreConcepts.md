# 🧱 SOLID Principles — Ultimate JavaScript Interview Guide

> **One file. No fluff. Crack any interview on SOLID Principles.**
> Every principle is explained with: plain-English definition → wrong code (what you're doing) → right code (the fix) → ASCII architecture diagram → memory trick → interview answer.

---

## 📖 Table of Contents

| Principle | One-Line Summary |
|-----------|-----------------|
| [S — Single Responsibility](#srp) | One class = One job |
| [O — Open/Closed](#ocp) | Extend yes, modify no |
| [L — Liskov Substitution](#lsp) | Subclass must not break parent's contract |
| [I — Interface Segregation](#isp) | Don't force unused methods |
| [D — Dependency Inversion](#dip) | Depend on abstractions, not concretions |
| [🎁 DRY Principle](#dry) | Don't Repeat Yourself |
| [🧠 Master Cheatsheet](#cheatsheet) | All 5 in one page |

---

## 🆚 SOLID Principles vs Design Patterns

Before diving in — interviewers love this question:

> **"What is the difference between SOLID Principles and Design Patterns?"**

```
SOLID PRINCIPLES                     DESIGN PATTERNS
────────────────────────────────     ────────────────────────────────
Abstract guidelines / rules          Concrete, proven solutions
"HOW you should think"               "WHAT you should build"
Apply everywhere always              Apply to specific problems
Can't copy-paste them                Can copy-paste the pattern

Think of it like:
SOLID = Traffic laws (abstract rules for all drivers)
Design Patterns = GPS routes (specific proven paths to take)

Design Pattern Categories:
┌─────────────────────────────────────────────────────────┐
│               Software Design Patterns                  │
│                                                         │
│  Creational          Structural         Behavioral      │
│  ────────────        ──────────         ─────────────   │
│  Factory Pattern     Adapter Pattern    Chain of        │
│  Object Pool         Decorator Pattern  Responsibility  │
│  Singleton           Composite Pattern  Mediator        │
│                                         Observer        │
└─────────────────────────────────────────────────────────┘
```

---

<a name="srp"></a>
## 1️⃣ S — Single Responsibility Principle (SRP)

### 📖 Dead-Simple Definition

> **"A class/function should have only ONE reason to change."**
> One class = one job. If a class does two different things, split it into two classes.

### 🧠 Memory Trick

> Think of your phone:
> - 📱 Calling people = Phone's job
> - 💡 Being a flashlight = Phone does it but it's NOT the phone's primary job
>
> **SRP says: every class should be the "calling" part, not the flashlight bolt-on.**

---

### ❌ WRONG — Violating SRP

**Scenario:** You have a `UserService` class that handles user data AND sends emails AND writes logs.

```
VIOLATION DIAGRAM:
─────────────────────────────────────────────────────────────
         UserService (doing TOO MUCH)
              │
    ┌─────────┼──────────┬─────────────┐
    ▼         ▼          ▼             ▼
 getUser()  saveUser() sendEmail()  writeLog()
    │         │          │             │
  Own Job   Own Job   ❌ Extra!    ❌ Extra!
                    (Email dept)  (Infra dept)

Problem: If email provider changes → you must modify UserService
         If log format changes     → you must modify UserService
         Every change = entire class retested + risk of breaking user logic
─────────────────────────────────────────────────────────────
```

```javascript
// ❌ BAD — UserService doing too many jobs
class UserService {
  constructor() {
    this.users = [];
  }

  // ✅ Own responsibility — user data management
  getUser(userId) {
    return this.users.find(u => u.id === userId);
  }

  // ✅ Own responsibility — user data management
  saveUser(user) {
    this.users.push(user);
  }

  // ❌ Extra responsibility — this is EMAIL's job
  sendWelcomeEmail(user) {
    console.log(`Sending email to ${user.email}...`);
    // Imagine: calls SMTP, builds HTML template, etc.
  }

  // ❌ Extra responsibility — this is LOGGING's job
  logUserActivity(userId, action) {
    const timestamp = new Date().toISOString();
    console.log(`[${timestamp}] User ${userId}: ${action}`);
    // Imagine: writes to file, sends to Datadog, etc.
  }
}

// The problem in action:
const service = new UserService();
service.saveUser({ id: 1, name: "Alice", email: "alice@example.com" });
service.sendWelcomeEmail({ email: "alice@example.com" });  // 😬 Why is UserService sending emails?
service.logUserActivity(1, "registered");                  // 😬 Why is UserService managing logs?
```

**Why this hurts:**
- Your team's email developer needs to change `UserService` to update email templates
- Your infra team needs to change `UserService` to update log format
- Testing user logic now requires mocking email + logging
- One bug in email code can crash user operations

---

### ✅ CORRECT — Following SRP

```
FIX DIAGRAM:
─────────────────────────────────────────────────────────────
  UserService       EmailService        LoggerService
  (User data)       (Email only)        (Logging only)
      │                  │                    │
  getUser()         sendWelcomeEmail()    logActivity()
  saveUser()        sendResetEmail()      logError()
  deleteUser()      sendInvoiceEmail()    logInfo()

Now:
  Email team changes EmailService    → UserService unaffected ✅
  Infra team changes LoggerService   → UserService unaffected ✅
  Testing UserService = no mocking needed for email/logs ✅
─────────────────────────────────────────────────────────────
```

```javascript
// ✅ GOOD — Each class has ONE responsibility

// 1. UserService: only manages user data
class UserService {
  constructor() {
    this.users = [];
  }

  getUser(userId) {
    return this.users.find(u => u.id === userId);
  }

  saveUser(user) {
    this.users.push(user);
    return user;
  }

  deleteUser(userId) {
    this.users = this.users.filter(u => u.id !== userId);
  }
}

// 2. EmailService: only handles emails
class EmailService {
  sendWelcomeEmail(user) {
    console.log(`📧 Sending welcome email to ${user.email}`);
    // All email logic isolated here
    // Change SMTP provider? Only this file changes.
  }

  sendPasswordResetEmail(user, resetToken) {
    console.log(`📧 Sending reset email to ${user.email} with token ${resetToken}`);
  }
}

// 3. LoggerService: only handles logging
class LoggerService {
  logActivity(userId, action) {
    const timestamp = new Date().toISOString();
    console.log(`[${timestamp}] User ${userId}: ${action}`);
    // Change log format? Only this file changes.
  }

  logError(error) {
    console.error(`[ERROR] ${error.message}`);
  }
}

// 4. UserRegistrationController: orchestrates the flow (uses all three)
class UserRegistrationController {
  constructor() {
    this.userService = new UserService();
    this.emailService = new EmailService();
    this.logger = new LoggerService();
  }

  registerUser(userData) {
    // Each service does its ONE job
    const user = this.userService.saveUser(userData);      // Save user
    this.emailService.sendWelcomeEmail(user);              // Send email
    this.logger.logActivity(user.id, "registered");        // Log it

    return user;
  }
}

// Usage — clean and readable
const controller = new UserRegistrationController();
controller.registerUser({ id: 1, name: "Alice", email: "alice@example.com" });
// Output:
// 📧 Sending welcome email to alice@example.com
// [2024-01-15T10:30:00.000Z] User 1: registered
```

### 💡 Interview Tips

> 🔥 **Best one-liner:** "SRP means one class should have only one reason to change. If a marketing team change and an engineering team change both require editing the same file, that file is violating SRP."

> 🔥 **Common follow-up:** "Doesn't SRP lead to too many small files?" → Answer: "Yes, more files — but each is simpler, easier to test, and changes in isolation. It's a worthwhile trade-off."

---

<a name="ocp"></a>
## 2️⃣ O — Open/Closed Principle (OCP)

### 📖 Dead-Simple Definition

> **"Open for extension, Closed for modification."**
> You should be able to add new features WITHOUT changing existing working code.

### 🧠 Memory Trick

> Think of a **plugin system** (like VS Code extensions):
> - VS Code's core code is **closed** — you can't edit it
> - But it's **open** for extension — anyone can add a plugin
>
> **OCP says: build your classes like VS Code — pluggable, not hackable.**

---

### ❌ WRONG — Violating OCP

**Scenario:** A payment system that needs modification every time a new payment method is added.

```
VIOLATION DIAGRAM:
─────────────────────────────────────────────────────────────
PaymentProcessor.processPayment()
        │
        ├── if (type === "credit")  → process credit card
        ├── if (type === "paypal")  → process paypal
        └── if (type === "crypto")  → process crypto  ← you ADD this

PROBLEM:
Every new payment method requires opening and editing
the SAME processPayment() function.
  → Risk of breaking existing Stripe/PayPal logic
  → Must retest ALL payment types every time
  → The more types you add, the more complex the if-else grows
─────────────────────────────────────────────────────────────
```

```javascript
// ❌ BAD — must open and modify this class for every new payment type
class PaymentProcessor {
  processPayment(amount, type) {
    if (type === 'credit') {
      console.log(`Processing $${amount} via Credit Card`);
      // ... Stripe API calls
    } else if (type === 'paypal') {
      console.log(`Processing $${amount} via PayPal`);
      // ... PayPal API calls
    } else if (type === 'crypto') {
      // ❌ Someone just MODIFIED this function to add crypto
      console.log(`Processing $${amount} via Crypto`);
      // ... Coinbase API calls
    }
    // Next month: someone adds 'applepay'... and modifies AGAIN
    // And 'googlepay'... and modifies AGAIN
    // EVERY addition = risk of breaking existing payments!
  }
}

const processor = new PaymentProcessor();
processor.processPayment(100, 'credit');   // Works
processor.processPayment(50, 'paypal');    // Works  
processor.processPayment(200, 'crypto');   // Works... until someone makes a typo above
```

---

### ✅ CORRECT — Following OCP

```
FIX DIAGRAM:
─────────────────────────────────────────────────────────────
PaymentProcessor (CLOSED — never changes)
        │
        └── process(paymentMethod, amount)
                │
                └── calls paymentMethod.pay(amount)
                          ← the only dependency

Payment methods (OPEN for extension — add new ones freely):
  CreditCardPayment   .pay(amount) → Stripe API
  PayPalPayment       .pay(amount) → PayPal API
  CryptoPayment       .pay(amount) → Coinbase API
  ApplePayPayment     .pay(amount) → Apple Pay API ← NEW: no change to processor!

PaymentProcessor NEVER changes.
Adding ApplePay = create one new class. Done.
─────────────────────────────────────────────────────────────
```

```javascript
// ✅ GOOD — PaymentProcessor never changes, new methods are plugged in

// Base contract — every payment method must implement pay()
class PaymentMethod {
  pay(amount) {
    throw new Error('pay() must be implemented');
  }
}

// Each payment type is its own class — isolated and independent
class CreditCardPayment extends PaymentMethod {
  pay(amount) {
    console.log(`💳 Processing $${amount} via Credit Card (Stripe API)`);
    // All Stripe-specific code here — completely isolated
  }
}

class PayPalPayment extends PaymentMethod {
  pay(amount) {
    console.log(`🅿️  Processing $${amount} via PayPal API`);
    // All PayPal-specific code here
  }
}

class CryptoPayment extends PaymentMethod {
  pay(amount) {
    console.log(`₿  Processing $${amount} via Crypto (Coinbase API)`);
  }
}

// Adding Apple Pay? Just add a NEW class — PaymentProcessor stays untouched!
class ApplePayPayment extends PaymentMethod {
  pay(amount) {
    console.log(`🍎 Processing $${amount} via Apple Pay`);
  }
}

// PaymentProcessor: CLOSED for modification — this never changes
class PaymentProcessor {
  process(paymentMethod, amount) {
    // Doesn't care what type it is — just calls .pay()
    paymentMethod.pay(amount);
  }
}

// Usage — add new payment types without touching PaymentProcessor
const processor = new PaymentProcessor();

processor.process(new CreditCardPayment(), 100);   // 💳 Processing $100 via Credit Card
processor.process(new PayPalPayment(), 50);         // 🅿️  Processing $50 via PayPal
processor.process(new CryptoPayment(), 200);        // ₿  Processing $200 via Crypto
processor.process(new ApplePayPayment(), 75);       // 🍎 Processing $75 via Apple Pay
// Added Apple Pay with ZERO changes to PaymentProcessor ✅
```

### 💡 Real-World Example (Salary Rates from the source material)

```javascript
// ✅ OCP with salary calculation — from Syncfusion's example
class ManageSalaries {
  constructor() {
    this.salaryRates = [
      { id: 1, role: 'developer', rate: 100 },
      { id: 2, role: 'architect', rate: 200 },
      { id: 3, role: 'manager', rate: 300 },
    ];
  }

  calculateSalary(empId, hoursWorked) {
    const salaryObj = this.salaryRates.find(s => s.id === empId);
    if (!salaryObj) throw new Error(`No rate for employee ${empId}`);
    return hoursWorked * salaryObj.rate;
  }

  // ✅ EXTEND via this method — never directly edit salaryRates array
  addSalaryRate(id, role, rate) {
    this.salaryRates.push({ id, role, rate });
  }
}

const mgr = new ManageSalaries();

// ❌ BAD: mgr.salaryRates.push({ id: 4, role: 'designer', rate: 150 }); ← direct modification
// ✅ GOOD:
mgr.addSalaryRate(4, 'designer', 150);

console.log(mgr.calculateSalary(4, 40));  // 6000
```

### 💡 Interview Tips

> 🔥 **Best one-liner:** "OCP means I should be able to add new features by writing new code, not by editing old code. Like adding a new payment method by creating a new class, not by adding another `if` to an existing function."

> 🔥 **Follow-up:** "How do you achieve OCP in JavaScript?" → "Through inheritance (extends), composition, and strategy pattern — define a common interface, then create separate classes for each behaviour."

---

<a name="lsp"></a>
## 3️⃣ L — Liskov Substitution Principle (LSP)

### 📖 Dead-Simple Definition

> **"If B extends A, then anywhere you use A, you should be able to swap in B without anything breaking."**
> A subclass must be a proper substitute for its parent — it must honour all the parent's promises.

### 🧠 Memory Trick

> Think of a **contract**:
> Your parent class makes a promise: "I will always return a number from `calculateBonus()`"
> If your child class throws an exception instead → **contract broken → LSP violated**
>
> **LSP says: children must keep their parents' promises.**

---

### ❌ WRONG — Violating LSP

**Scenario:** An `Ostrich` extends `Bird`, but birds can fly — ostriches can't. Calling `fly()` on an ostrich breaks everything.

```
VIOLATION DIAGRAM:
─────────────────────────────────────────────────────────────
Animal
  └── Bird  (has fly() method)
        └── Ostrich (extends Bird... but CANNOT fly!)

Code does this:
  function makeItFly(bird) {
    bird.fly();   // Works for Parrot ✅
  }
  makeItFly(new Parrot());   // ✅ "Parrot flies"
  makeItFly(new Ostrich());  // ❌ CRASH — "Ostriches do not fly"

LSP says: if you swap Bird for Ostrich, it must STILL work.
Here it doesn't → LSP VIOLATED.
─────────────────────────────────────────────────────────────
```

```javascript
// ❌ BAD — Ostrich extends Bird but violates the fly() contract

class Animal {
  eat() {
    return "Animal eats";
  }
}

class Bird extends Animal {
  fly() {
    return "Bird flies";
  }
}

class Parrot extends Bird {
  fly() {
    return "Parrot flies beautifully";  // ✅ Keeps the contract
  }
}

class Ostrich extends Bird {
  fly() {
    // ❌ Violates LSP — ostrich can't fly, but it inherited this promise!
    throw new Error("Ostriches cannot fly!");
  }
}

// The function expects ANY Bird to be able to fly
function makeBirdFly(bird) {
  console.log(bird.fly());
}

makeBirdFly(new Parrot());    // ✅ "Parrot flies beautifully"
makeBirdFly(new Ostrich());   // ❌ CRASH! — breaks LSP

// In a real app: imagine a List<Bird> in a loop calling .fly()
// One ostrich object in the list crashes your entire app
```

---

### ✅ CORRECT — Following LSP

```
FIX DIAGRAM:
─────────────────────────────────────────────────────────────
Animal (eat)
  │
  ├── Bird (eat + fly)   ← ONLY birds that CAN fly extend Bird
  │     └── Parrot       ← can fly ✅
  │     └── Eagle        ← can fly ✅
  │
  └── Ostrich (eat + walk)  ← extends Animal directly, not Bird
        ← no fly() promise made ✅

Now: makeItFly(bird) only receives objects that honour fly()
     Ostrich is never passed to makeItFly — it never promises to fly
─────────────────────────────────────────────────────────────
```

```javascript
// ✅ GOOD — hierarchy matches real-world capabilities

class Animal {
  constructor(name) {
    this.name = name;
  }
  eat() {
    return `${this.name} eats`;
  }
}

// Bird: ONLY for animals that can actually fly
class Bird extends Animal {
  fly() {
    return `${this.name} flies`;
  }
}

// Parrot extends Bird — can fly ✅ — LSP upheld
class Parrot extends Bird {
  fly() {
    return `${this.name} flies beautifully and talks`;
  }
  talk() {
    return `${this.name} says "Hello!"`;
  }
}

// Eagle extends Bird — can fly ✅ — LSP upheld
class Eagle extends Bird {
  fly() {
    return `${this.name} soars high above`;
  }
}

// Ostrich extends Animal (NOT Bird) — it does NOT promise to fly
class Ostrich extends Animal {
  walk() {
    return `${this.name} runs very fast on land`;
  }
  // No fly() here → no broken promises
}

// Function uses Bird — any Bird can substitute here ✅
function makeBirdFly(bird) {
  console.log(bird.fly());
}

makeBirdFly(new Parrot("Polly"));   // ✅ Polly flies beautifully and talks
makeBirdFly(new Eagle("Eddie"));    // ✅ Eddie soars high above
// makeBirdFly(new Ostrich("Otto")); // TypeScript would catch this at compile time ✅

// Ostrich is used correctly — only with methods it actually has
const ostrich = new Ostrich("Otto");
console.log(ostrich.eat());   // ✅ Otto eats
console.log(ostrich.walk());  // ✅ Otto runs very fast on land
```

### 💡 Real App Example — Employee Bonus (from source material)

```javascript
// ✅ GOOD — LSP with employees

class Employee {
  calculateSalary() {
    return 50000;
  }
  calculateBonus() {
    return 5000;     // Parent promises: always returns a number
  }
}

class PermanentEmployee extends Employee {
  calculateSalary() {
    return 80000;   // ✅ Still returns a number
  }
  calculateBonus() {
    return 10000;   // ✅ Still returns a number — LSP upheld
  }
}

// ❌ BAD — ContractualEmployee throws instead of returning a number
class ContractualEmployee extends Employee {
  calculateSalary() {
    return 60000;
  }
  calculateBonus() {
    throw new Error("Contractual employees have no bonus!");
    // ❌ Parent promised a number — child throws instead
    // Anywhere you use Employee, swapping in ContractualEmployee breaks the bonus calculation
  }
}

// ✅ FIX — Use a different base class or remove the bonus promise
class ContractualEmployeeFixed extends Employee {
  calculateSalary() {
    return 60000;
  }
  calculateBonus() {
    return 0;  // ✅ Returns a number (0) — keeps the contract
  }
}

// OR better — restructure the hierarchy
class EmployeeBase {
  calculateSalary() { return 0; }
}

class BonusEligibleEmployee extends EmployeeBase {
  calculateBonus() { return 0; }    // Only in THIS branch
}

class PermanentEmp extends BonusEligibleEmployee {
  calculateSalary() { return 80000; }
  calculateBonus() { return 10000; }   // ✅
}

class ContractEmp extends EmployeeBase {
  calculateSalary() { return 60000; }
  // No calculateBonus() — never promised it
}
```

### 💡 Interview Tips

> 🔥 **Best one-liner:** "LSP means a subclass must be substitutable for its parent class without breaking the application. If a child class throws where the parent returns a value, that's an LSP violation."

> 🔥 **Practical tip to mention:** "When I catch an LSP violation, I usually fix it by flattening the hierarchy — make the subclass extend a higher ancestor that only promises what the subclass can actually deliver."

---

<a name="isp"></a>
## 4️⃣ I — Interface Segregation Principle (ISP)

### 📖 Dead-Simple Definition

> **"Don't force a class to implement methods it doesn't need."**
> Split large, fat interfaces into smaller, focused ones. Classes implement only what they use.

### 🧠 Memory Trick

> Think of a **restaurant menu**:
> A vegan restaurant doesn't need to print a 50-page menu with every meat dish.
> They get a **focused** menu with only what they serve.
>
> **ISP says: give each class only the menu items it actually uses.**

> **JS Note:** JavaScript has no built-in `interface` keyword (unlike TypeScript). ISP in JS is implemented using **composition** — mixing specific behaviours into classes using `Object.assign()` or mixin patterns.

---

### ❌ WRONG — Violating ISP

**Scenario:** A `Worker` interface forces all workers to implement both `work()` and `eat()` — even robots that don't eat.

```
VIOLATION DIAGRAM:
─────────────────────────────────────────────────────────────
IWorker (fat interface)
  ├── work()
  ├── eat()        ← makes sense for humans, NOT for robots
  └── sleep()      ← makes sense for humans, NOT for robots

HumanWorker implements IWorker → ✅ uses all three
RobotWorker implements IWorker → ❌ forced to implement eat() and sleep()
                                     even though robots don't eat/sleep!

RobotWorker.eat() → throws NotImplementedError  ← LSP violation too!
─────────────────────────────────────────────────────────────
```

```javascript
// ❌ BAD — Fat "interface" forces Robot to implement eat() and sleep()

// JavaScript uses a base class as a pseudo-interface
class Worker {
  work() { throw new Error("work() not implemented"); }
  eat()  { throw new Error("eat() not implemented"); }
  sleep(){ throw new Error("sleep() not implemented"); }
}

class HumanWorker extends Worker {
  work()  { console.log("👷 Human is working"); }     // ✅ makes sense
  eat()   { console.log("🍕 Human is eating");  }     // ✅ makes sense
  sleep() { console.log("😴 Human is sleeping"); }    // ✅ makes sense
}

class RobotWorker extends Worker {
  work()  { console.log("🤖 Robot is working"); }     // ✅ makes sense
  eat()   { throw new Error("Robots don't eat!"); }   // ❌ FORCED, doesn't make sense
  sleep() { throw new Error("Robots don't sleep!"); } // ❌ FORCED, doesn't make sense
}

// Problem: any code calling worker.eat() will crash on a RobotWorker
function takeBreak(worker) {
  worker.eat();   // ✅ HumanWorker — fine
                  // ❌ RobotWorker — CRASH
}
```

---

### ✅ CORRECT — Following ISP (using Composition / Mixins)

```
FIX DIAGRAM:
─────────────────────────────────────────────────────────────
Split into FOCUSED capabilities (mixins):

  workable  = { work() }      ← both humans and robots need this
  eatable   = { eat() }       ← only humans need this
  sleepable = { sleep() }     ← only humans need this
  chargeable = { charge() }   ← only robots need this

HumanWorker gets: workable + eatable + sleepable
RobotWorker gets: workable + chargeable

No class gets methods it doesn't use ✅
─────────────────────────────────────────────────────────────
```

```javascript
// ✅ GOOD — Composition: mix only what each class needs

// Small, focused behaviours (mixins)
const workable = {
  work() {
    console.log(`${this.name} is working`);
  }
};

const eatable = {
  eat() {
    console.log(`${this.name} is eating lunch`);
  }
};

const sleepable = {
  sleep() {
    console.log(`${this.name} is sleeping`);
  }
};

const chargeable = {
  charge() {
    console.log(`${this.name} is charging its battery`);
  }
};

// Base class (lean)
class Worker {
  constructor(name) {
    this.name = name;
  }
}

class HumanWorker extends Worker {}
class RobotWorker extends Worker {}

// ✅ Assign ONLY relevant mixins — humans get human behaviours
Object.assign(HumanWorker.prototype, workable, eatable, sleepable);

// ✅ Robots get ONLY robot behaviours — no eat(), no sleep()
Object.assign(RobotWorker.prototype, workable, chargeable);

// Usage
const human = new HumanWorker("Alice");
human.work();    // ✅ Alice is working
human.eat();     // ✅ Alice is eating lunch
human.sleep();   // ✅ Alice is sleeping

const robot = new RobotWorker("R2D2");
robot.work();    // ✅ R2D2 is working
robot.charge();  // ✅ R2D2 is charging its battery
// robot.eat()   // ❌ TypeError — correctly not available! ✅
```

### 💡 Driving School Example (from Syncfusion)

```javascript
// ✅ ISP — Driving test: each class gets only its relevant test

class DrivingSchool {
  constructor(studentName) {
    this.studentName = studentName;
  }
}

// Focused test modules (mixins)
const carTestMixin = {
  startCarTest() {
    return `${this.studentName} — Car test started ✅`;
  }
};

const truckTestMixin = {
  startTruckTest() {
    return `${this.studentName} — Truck test started ✅`;
  }
};

const motorcycleTestMixin = {
  startMotorcycleTest() {
    return `${this.studentName} — Motorcycle test started ✅`;
  }
};

// Car student — ONLY gets car test
class CarStudent extends DrivingSchool {}
Object.assign(CarStudent.prototype, carTestMixin);

// Truck student — ONLY gets truck test
class TruckStudent extends DrivingSchool {}
Object.assign(TruckStudent.prototype, truckTestMixin);

// Full licence student — gets all tests
class FullLicenceStudent extends DrivingSchool {}
Object.assign(FullLicenceStudent.prototype, carTestMixin, truckTestMixin, motorcycleTestMixin);

const carStudent = new CarStudent("Bob");
console.log(carStudent.startCarTest());         // ✅ Bob — Car test started
// carStudent.startTruckTest()                  // ❌ TypeError — correctly blocked ✅

const fullStudent = new FullLicenceStudent("Carol");
console.log(fullStudent.startCarTest());        // ✅
console.log(fullStudent.startTruckTest());      // ✅
console.log(fullStudent.startMotorcycleTest()); // ✅
```

### 💡 Interview Tips

> 🔥 **Best one-liner:** "ISP says don't force a class to implement methods it doesn't use. In JavaScript, since we have no native interfaces, I implement ISP using composition — mixing in only the specific behaviours each class needs using `Object.assign()`."

> 🔥 **Follow-up:** "How is this different from SRP?" → "SRP is about a class having one reason to change (one job). ISP is about not being forced to depend on things you don't use. They're complementary — ISP helps enforce SRP on the interface/dependency side."

---

<a name="dip"></a>
## 5️⃣ D — Dependency Inversion Principle (DIP)

### 📖 Dead-Simple Definition

> **"High-level modules should not depend on low-level modules. Both should depend on abstractions."**
> Your core business logic should not be wired directly to specific tools (MySQL, Stripe, SendGrid). Wire them to an interface — then swap tools freely.

### 🧠 Memory Trick

> Think of a **power socket**:
> Your laptop doesn't care if the power comes from solar, nuclear, or coal.
> It just plugs into the **standard socket (the abstraction)**.
>
> **DIP says: code to the socket, not to the power plant.**

---

### ❌ WRONG — Violating DIP

**Scenario:** A `UserController` that directly creates and uses a `MySQLDatabase`. If you switch to MongoDB, you must rewrite the controller.

```
VIOLATION DIAGRAM:
─────────────────────────────────────────────────────────────
UserController
       │
       └── new MySQLDatabase()   ← tightly coupled!
                │
             MySQL-specific code

Switch to MongoDB:
  UserController MUST change (violates OCP too!)
  All controllers using MySQLDatabase must ALL change
  Production code touched = risk of regression
─────────────────────────────────────────────────────────────
```

```javascript
// ❌ BAD — UserController directly depends on MySQLDatabase

class MySQLDatabase {
  save(user) {
    console.log(`Saving user to MySQL: ${user.name}`);
    // MySQL-specific connection, SQL queries, etc.
  }

  find(userId) {
    console.log(`Finding user ${userId} in MySQL`);
    return { id: userId, name: "Alice" };
  }
}

// ❌ UserController creates and OWNS MySQLDatabase — tightly coupled
class UserController {
  constructor() {
    this.database = new MySQLDatabase();  // ← hard dependency!
  }

  createUser(user) {
    // business logic mixed with database dependency
    this.database.save(user);
  }

  getUser(userId) {
    return this.database.find(userId);
  }
}

// Problem: Switch to MongoDB?
// → Must open UserController and change it
// → 20 controllers all using MySQLDatabase? → change all 20!
// → Can't test UserController without a real MySQL connection
```

---

### ✅ CORRECT — Following DIP

```
FIX DIAGRAM:
─────────────────────────────────────────────────────────────
UserController
       │
       └── IDatabase (abstraction / interface)
                │
      ┌─────────┴──────────┐
      ▼                    ▼
MySQLDatabase           MongoDatabase
(concrete)              (concrete)

UserController is wired to the ABSTRACTION, not the concrete class.
Switch database: change the injected implementation only.
UserController code: ZERO changes ✅

This is "Dependency INJECTION" — inject the dependency from outside.
─────────────────────────────────────────────────────────────
```

```javascript
// ✅ GOOD — UserController depends on abstraction, not a specific DB

// 1. The abstraction — every database must implement these methods
class IDatabase {
  save(user)      { throw new Error("save() not implemented"); }
  find(userId)    { throw new Error("find() not implemented"); }
  delete(userId)  { throw new Error("delete() not implemented"); }
}

// 2. Concrete implementations — each database does it its own way
class MySQLDatabase extends IDatabase {
  save(user) {
    console.log(`💾 MySQL: INSERT INTO users VALUES (${user.id}, '${user.name}')`);
  }
  find(userId) {
    console.log(`🔍 MySQL: SELECT * FROM users WHERE id = ${userId}`);
    return { id: userId, name: "Alice (from MySQL)" };
  }
  delete(userId) {
    console.log(`🗑️  MySQL: DELETE FROM users WHERE id = ${userId}`);
  }
}

class MongoDatabase extends IDatabase {
  save(user) {
    console.log(`💾 MongoDB: db.users.insertOne({ id: ${user.id}, name: '${user.name}' })`);
  }
  find(userId) {
    console.log(`🔍 MongoDB: db.users.findOne({ id: ${userId} })`);
    return { id: userId, name: "Alice (from MongoDB)" };
  }
  delete(userId) {
    console.log(`🗑️  MongoDB: db.users.deleteOne({ id: ${userId} })`);
  }
}

// In-memory DB for testing — no real DB needed in unit tests!
class InMemoryDatabase extends IDatabase {
  constructor() {
    super();
    this.store = {};
  }
  save(user)     { this.store[user.id] = user; }
  find(userId)   { return this.store[userId]; }
  delete(userId) { delete this.store[userId]; }
}

// 3. UserController depends on the ABSTRACTION (IDatabase)
//    It doesn't know or care which DB is being used
class UserController {
  constructor(database) {          // ← database is INJECTED, not created here
    this.database = database;      // ← dependency inversion + injection
  }

  createUser(userData) {
    const user = { id: Date.now(), ...userData };
    this.database.save(user);      // ← calls abstraction method
    console.log(`✅ User ${user.name} created`);
    return user;
  }

  getUser(userId) {
    return this.database.find(userId);
  }
}

// ── Switch between databases by changing ONE LINE at the top ────────────
// Production with MySQL:
const mysqlController = new UserController(new MySQLDatabase());
mysqlController.createUser({ name: "Alice" });

// Production with MongoDB:
const mongoController = new UserController(new MongoDatabase());
mongoController.createUser({ name: "Bob" });

// Unit testing — no real DB needed!
const testController = new UserController(new InMemoryDatabase());
testController.createUser({ name: "Test User" });
console.log(testController.getUser(Object.keys(testController.database.store)[0]));
```

### 💡 Email API Example (from Medium article)

```javascript
// ✅ DIP with Email API — easy to switch providers

// Abstraction
class IEmailProvider {
  sendEmail(to, subject, body) {
    throw new Error("sendEmail() not implemented");
  }
}

// Concrete: Yahoo
class YahooEmailProvider extends IEmailProvider {
  sendEmail(to, subject, body) {
    console.log(`📧 [Yahoo] Sending to ${to}: "${subject}"`);
    // Yahoo-specific SDK calls here
  }
}

// Concrete: Gmail — NEW provider, zero changes to EmailService!
class GmailEmailProvider extends IEmailProvider {
  sendEmail(to, subject, body) {
    console.log(`📧 [Gmail] Sending to ${to}: "${subject}"`);
    // Gmail-specific SDK calls here
  }
}

// High-level service — depends on abstraction
class EmailService {
  constructor(emailProvider) {    // ← provider injected from outside
    this.emailProvider = emailProvider;
  }

  sendWelcomeEmail(user) {
    this.emailProvider.sendEmail(
      user.email,
      "Welcome to our app!",
      `Hi ${user.name}, welcome aboard!`
    );
  }
}

// Switching from Yahoo to Gmail = change ONE line in app startup
const emailService = new EmailService(new GmailEmailProvider());
// const emailService = new EmailService(new YahooEmailProvider()); ← old line

emailService.sendWelcomeEmail({ name: "Alice", email: "alice@example.com" });
// 📧 [Gmail] Sending to alice@example.com: "Welcome to our app!"
```

### 💡 Interview Tips

> 🔥 **Best one-liner:** "DIP says high-level modules shouldn't depend on low-level modules. I apply it through Dependency Injection — I inject the database, logger, or API client into a class's constructor rather than creating it inside. This means I can swap implementations — including mock ones for testing — without touching business logic."

> 🔥 **DIP vs DI (Dependency Injection):** "DIP is the principle; DI is the technique for implementing it. You can implement DIP through constructor injection, method injection, or using a DI container."

---

<a name="dry"></a>
## 🎁 Bonus: DRY Principle — Don't Repeat Yourself

### 📖 Definition

> **"Every piece of knowledge must have a single, unambiguous representation in the system."**
> Write a piece of logic once. Reuse it everywhere. Never copy-paste business logic.

### ❌ WRONG — Violating DRY

```javascript
// ❌ BAD — same discount logic repeated in 3 places
class OrderProcessor {
  processWebOrder(order) {
    let total = order.price;
    if (order.isPremiumUser) {
      total = total - (total * 0.2);   // 20% discount
    }
    console.log(`Web order total: $${total}`);
  }

  processMobileOrder(order) {
    let total = order.price;
    if (order.isPremiumUser) {
      total = total - (total * 0.2);   // ❌ Same logic copy-pasted!
    }
    console.log(`Mobile order total: $${total}`);
  }

  processPhoneOrder(order) {
    let total = order.price;
    if (order.isPremiumUser) {
      total = total - (total * 0.2);   // ❌ Copy-pasted AGAIN!
    }
    console.log(`Phone order total: $${total}`);
  }
  // Discount changes to 25%? Must change in 3 places → bugs guaranteed
}
```

### ✅ CORRECT — Following DRY

```javascript
// ✅ GOOD — discount logic defined ONCE, used everywhere
class OrderProcessor {
  // Single source of truth for discount calculation
  calculateDiscountedPrice(price, isPremiumUser) {
    return isPremiumUser ? price * 0.8 : price;   // 20% off for premium
  }

  processWebOrder(order) {
    const total = this.calculateDiscountedPrice(order.price, order.isPremiumUser);
    console.log(`Web order total: $${total}`);
  }

  processMobileOrder(order) {
    const total = this.calculateDiscountedPrice(order.price, order.isPremiumUser);
    console.log(`Mobile order total: $${total}`);
  }

  processPhoneOrder(order) {
    const total = this.calculateDiscountedPrice(order.price, order.isPremiumUser);
    console.log(`Phone order total: $${total}`);
  }
  // Discount changes to 25%? Change ONE LINE in calculateDiscountedPrice() ✅
}
```

---

<a name="cheatsheet"></a>
# 🧠 Master Cheatsheet — All 5 Principles in One View

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SOLID PRINCIPLES — QUICK RECALL                          │
├────────┬──────────────────────┬──────────────────────────┬──────────────────┤
│  SRP   │ 1 class = 1 job      │ UserService splits into: │ Reason: isolate  │
│        │ 1 reason to change   │ UserService + EmailSvc   │ changes to 1 area│
├────────┼──────────────────────┼──────────────────────────┼──────────────────┤
│  OCP   │ Extend yes           │ Add CryptoPayment class  │ Reason: no risk  │
│        │ Modify no            │ not edit PaymentProcessor│ to existing code │
├────────┼──────────────────────┼──────────────────────────┼──────────────────┤
│  LSP   │ Subclass must replace│ Ostrich → extends Animal │ Reason: no       │
│        │ parent without break │ NOT Bird (can't fly)     │ surprises when   │
│        │                      │                          │ swapping objects │
├────────┼──────────────────────┼──────────────────────────┼──────────────────┤
│  ISP   │ No unused methods    │ RobotWorker gets          │ Reason: no dead  │
│        │ Split fat interfaces │ workable + chargeable    │ code, no errors  │
│        │                      │ NOT eatable + sleepable  │ from throw stubs │
├────────┼──────────────────────┼──────────────────────────┼──────────────────┤
│  DIP   │ Depend on abstract   │ UserController gets DB   │ Reason: swap     │
│        │ Inject dependencies  │ injected, not new MySQL()│ implementations  │
│        │                      │                          │ + easy testing   │
└────────┴──────────────────────┴──────────────────────────┴──────────────────┘
```

## 🎯 How the Principles Connect

```
SOLID PRINCIPLES ARE RELATED:

SRP ensures each class has one job
    ↓
OCP becomes easy because isolated classes are easier to extend
    ↓
LSP ensures safe substitution when you extend
    ↓
ISP keeps extended classes lean (no unused methods)
    ↓
DIP decouples high-level from low-level, enabling all the above

Together: you get code that is:
  ✅ Easy to read (SRP)
  ✅ Easy to extend (OCP)
  ✅ Safe to substitute (LSP)
  ✅ Lean, no dead code (ISP)
  ✅ Testable and swappable (DIP)
```

## ⚡ 5-Second Interview Answers

| Principle | If asked "What is...?" | If asked "Show me a violation" |
|-----------|----------------------|-------------------------------|
| **SRP** | "One class, one reason to change" | "A class that saves to DB AND sends emails" |
| **OCP** | "Add features without editing old code" | "An if-else that grows with every new type" |
| **LSP** | "Subclass must honour parent's contract" | "Ostrich extends Bird but throws on fly()" |
| **ISP** | "Don't force unused methods" | "Robot implements eat() and throws" |
| **DIP** | "Inject dependencies, depend on abstractions" | "new MySQLDatabase() inside a controller" |

## 🔥 Top 5 Interview Questions + Answers

**Q: "What are SOLID principles?"**
> "SOLID is a set of 5 design principles — Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion. They guide you toward code that is maintainable, testable, and easy to extend. I apply them daily: SRP means each module does one thing, OCP means I extend via new classes rather than editing existing ones, and DIP means I inject dependencies rather than hard-coding them."

**Q: "Which SOLID principle do you use most?"**
> "DIP and SRP are the ones I consciously apply most in JavaScript. DIP through constructor injection — I never do `new Database()` inside a service class. SRP I enforce by asking 'what department would ask me to change this class?' — if two different departments would, the class is doing too much."

**Q: "How do you implement Interface Segregation in JavaScript since there are no interfaces?"**
> "I use composition with Object.assign() or ES6 mixins. Rather than inheriting a fat class, I define small focused behaviour objects and mix only the relevant ones into each class. This gives the same effect as ISP in typed languages."

**Q: "What is the difference between SOLID and Design Patterns?"**
> "SOLID principles are abstract guidelines — rules about how code should be structured. Design patterns are concrete, reusable solutions — like Factory, Observer, or Singleton. SOLID tells you the rules of the road; design patterns give you specific well-known routes to take."

**Q: "Can you show how SOLID makes code testable?"**
> "The clearest example is DIP. If a UserService creates `new MySQLDatabase()` internally, you can't unit test it without a real database. But if you inject the database via the constructor, in tests you pass `new InMemoryDatabase()` — no real DB needed. SRP helps too — a class with one job has a focused, easy-to-write unit test."

---

*All JavaScript examples are runnable in Node.js 14+ or any modern browser console.*
