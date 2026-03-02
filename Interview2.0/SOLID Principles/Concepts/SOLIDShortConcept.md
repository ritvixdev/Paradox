# 🧱 SOLID Principles — JavaScript Interview Guide

> **Format per principle:** Definition → Memory trick → ❌ Wrong → ✅ Fixed → Diagram → Interview answer

---

## 📋 Quick Reference Table

| | Principle | One-liner | Violation signal |
|--|-----------|-----------|-----------------|
| **S** | Single Responsibility | One class = one job | "This class does X *and* Y" |
| **O** | Open / Closed | Extend yes, modify no | Growing `if/else` for each new type |
| **L** | Liskov Substitution | Child must not break parent's contract | Child `throw`s where parent returns a value |
| **I** | Interface Segregation | No forced unused methods | Stub methods that just `throw new Error()` |
| **D** | Dependency Inversion | Depend on abstractions, not concretions | `new MySQL()` hardcoded inside a service |

---

## SOLID vs Design Patterns — Interviewers love this question

```
SOLID Principles              Design Patterns
──────────────────────────    ──────────────────────────────────
Abstract rules / guidelines   Concrete, reusable solutions
"Rules of the road"           "Proven GPS routes to take"
Apply everywhere always       Apply to a specific problem

Analogy:
  SOLID = Traffic laws        Design Patterns = GPS routes

Pattern categories:
  Creational  → Factory, Singleton, Object Pool
  Structural  → Adapter, Decorator, Composite
  Behavioral  → Observer, Mediator, Chain of Responsibility
```

---

<a name="srp"></a>
## 1️⃣ S — Single Responsibility Principle (SRP)

### 📖 Definition
> **"A class should have only ONE reason to change."**
> One class = one job. If two different teams would both need to edit the same class, it's doing too much.

### 🧠 Memory Trick
> A chef cooks. A waiter serves. A cashier bills.
> **None of them do each other's job — that's SRP.**

---

### ❌ Wrong

```javascript
class User {
  constructor(name, email) {
    this.name  = name;
    this.email = email;
  }

  getUserInfo() {                              // ✅ user's job
    return `${this.name} - ${this.email}`;
  }

  saveToDatabase() {                           // ❌ database's job
    console.log(`Saving ${this.name} to DB`);
  }

  sendWelcomeEmail() {                         // ❌ email's job
    console.log(`Emailing ${this.email}`);
  }
}
```

**Problem:** Change the DB → touch `User`. Change the email → touch `User`. Every unrelated change risks breaking user logic.

---

### ✅ Fixed

```javascript
class User {                        // only user data
  constructor(name, email) {
    this.name  = name;
    this.email = email;
  }
  getUserInfo() { return `${this.name} - ${this.email}`; }
}

class UserRepository {              // only database
  save(user) { console.log(`Saving ${user.name} to DB`); }
}

class EmailService {                // only email
  sendWelcome(user) { console.log(`Emailing ${user.email}`); }
}

// Usage
const user = new User("Alice", "alice@example.com");
new UserRepository().save(user);
new EmailService().sendWelcome(user);
```

---

### 🗺 Diagram

```
BEFORE                              AFTER
──────────────────────────────────  ─────────────────────────────────────
         User                         User       UserRepository  EmailService
           │                        (data only)   (DB only)      (email only)
  ┌────────┼──────────┐
  │        │          │             Change DB?   → only UserRepository changes ✅
getUserInfo saveDB  sendEmail       Change email? → only EmailService changes  ✅
                                    Test User?    → no mocks needed            ✅
```

### 💡 Interview Answer
> *"SRP means one class has one reason to change. If the DB team and the email team both need to edit the same file, it's violating SRP. I split responsibilities so each change is isolated to one place."*

---

<a name="ocp"></a>
## 2️⃣ O — Open / Closed Principle (OCP)

### 📖 Definition
> **"Open for extension, closed for modification."**
> Add new features by writing new code — not by editing existing, working code.

### 🧠 Memory Trick
> VS Code is **closed** — you can't edit its core.
> But **open** — anyone can write a plugin.
> **Build your classes like VS Code.**

---

### ❌ Wrong

```javascript
class PaymentProcessor {
  process(amount, type) {
    if (type === "credit") {
      console.log(`$${amount} via Credit Card`);
    } else if (type === "paypal") {
      console.log(`$${amount} via PayPal`);
    }
    // ❌ Adding "crypto" means opening and editing this function
    // Every edit risks breaking existing credit/paypal logic
  }
}
```

---

### ✅ Fixed

```javascript
class Payment {
  pay(amount) { throw new Error("Implement pay()"); }
}

class CreditCardPayment extends Payment {
  pay(amount) { console.log(`$${amount} via Credit Card`); }
}

class PayPalPayment extends Payment {
  pay(amount) { console.log(`$${amount} via PayPal`); }
}

// ✅ New type = new class only. PaymentProcessor never changes.
class CryptoPayment extends Payment {
  pay(amount) { console.log(`$${amount} via Crypto`); }
}

class PaymentProcessor {
  process(payment, amount) { payment.pay(amount); }  // closed ✅
}

const p = new PaymentProcessor();
p.process(new CreditCardPayment(), 100);
p.process(new CryptoPayment(), 50);
```

---

### 🗺 Diagram

```
BEFORE                            AFTER
────────────────────────────────  ──────────────────────────────────────
PaymentProcessor                  PaymentProcessor  ← never changes ✅
  └── if credit  → ...                  │
  └── if paypal  → ...                  └── payment.pay(amount)
  └── if crypto  → ❌ EDIT FILE                  ▲ (abstraction)
  └── if apple   → ❌ EDIT AGAIN        │         │          │
                                   CreditCard  PayPal    Crypto ← just add new class
```

### 💡 Interview Answer
> *"OCP means I extend functionality by creating new classes, not editing old ones. Adding a new payment method is just a new class — the processor never changes. This prevents regression bugs in existing code."*

---

<a name="lsp"></a>
## 3️⃣ L — Liskov Substitution Principle (LSP)

### 📖 Definition
> **"You must be able to replace a parent with any of its subclasses without breaking the app."**
> A child class must honour every promise the parent makes.

### 🧠 Memory Trick
> Parent signs a contract: *"I always return a value from fly()."*
> If the child throws instead → **contract broken → LSP violated.**
> **Children must keep their parent's promises.**

---

### ❌ Wrong

```javascript
class Bird {
  fly() { return "flying"; }
}

class Parrot extends Bird {
  fly() { return "Parrot flying"; }   // ✅ keeps the promise
}

class Ostrich extends Bird {
  fly() { throw new Error("Can't fly!"); }  // ❌ breaks the promise
}

function letItFly(bird) { console.log(bird.fly()); }

letItFly(new Parrot());   // ✅ "Parrot flying"
letItFly(new Ostrich());  // ❌ CRASH — LSP violated
```

---

### ✅ Fixed

```javascript
class Animal {
  eat() { return "eating"; }
}

class Bird extends Animal {        // Bird = animals that CAN fly
  fly() { return "flying"; }
}

class Parrot extends Bird {
  fly() { return "Parrot flying"; } // ✅
}

class Ostrich extends Animal {     // extends Animal, NOT Bird
  walk() { return "Ostrich walking"; } // no fly() = no broken promise ✅
}

function letItFly(bird) { console.log(bird.fly()); }

letItFly(new Parrot());   // ✅ "Parrot flying"
// Ostrich is never passed here — it never promised to fly ✅
```

---

### 🗺 Diagram

```
BEFORE (broken)                   AFTER (fixed)
────────────────────────────────  ─────────────────────────────────────
Animal                            Animal  (eat)
  └── Bird (fly)                    ├── Bird  (eat + fly)
        ├── Parrot ✅ flies         │     ├── Parrot ✅
        └── Ostrich ❌ throws       │     └── Eagle  ✅
                                    └── Ostrich (eat + walk, NO fly promise)
```

### 💡 Interview Answer
> *"LSP means a subclass must safely substitute its parent. Ostrich extending Bird is the classic violation — Bird promises fly() but Ostrich can't fulfil it. The fix is to put Ostrich under Animal so it never inherits a promise it can't keep."*

---

<a name="isp"></a>
## 4️⃣ I — Interface Segregation Principle (ISP)

### 📖 Definition
> **"Don't force a class to implement methods it doesn't need."**
> Many small focused interfaces beat one large fat one.

### 🧠 Memory Trick
> A vegan restaurant doesn't need a menu listing every steak and seafood dish.
> **Give each class only the menu items it actually serves.**

> **JS note:** No native `interface` keyword in JS. Use **composition with `Object.assign()`** to mix in only what's needed.

---

### ❌ Wrong

```javascript
class Worker {
  work()  { throw new Error("not implemented"); }
  eat()   { throw new Error("not implemented"); }  // humans only
  sleep() { throw new Error("not implemented"); }  // humans only
}

class RobotWorker extends Worker {
  work()  { console.log("Robot working"); }         // ✅
  eat()   { throw new Error("Robots don't eat"); }  // ❌ forced stub
  sleep() { throw new Error("Robots don't sleep"); }// ❌ forced stub
}
```

---

### ✅ Fixed

```javascript
// Small, focused behaviour objects (mixins)
const canWork   = { work()   { console.log(`${this.name} working`);  } };
const canEat    = { eat()    { console.log(`${this.name} eating`);   } };
const canSleep  = { sleep()  { console.log(`${this.name} sleeping`); } };
const canCharge = { charge() { console.log(`${this.name} charging`); } };

class Worker { constructor(name) { this.name = name; } }

class HumanWorker extends Worker {}
class RobotWorker extends Worker {}

// Each class gets ONLY what it needs
Object.assign(HumanWorker.prototype, canWork, canEat, canSleep);
Object.assign(RobotWorker.prototype, canWork, canCharge);

const human = new HumanWorker("Alice");
human.work();  human.eat();  human.sleep(); // ✅ all work

const robot = new RobotWorker("R2D2");
robot.work();  robot.charge();              // ✅ works
// robot.eat() → TypeError — correctly unavailable ✅
```

---

### 🗺 Diagram

```
BEFORE                            AFTER
────────────────────────────────  ──────────────────────────────────────
Worker (work + eat + sleep)       canWork   canEat  canSleep  canCharge
  ├── HumanWorker ✅ all ok                │        │         │
  └── RobotWorker ❌                HumanWorker ←───┘──────┘  │
        eat()  → stub throws        work + eat + sleep         │
        sleep()→ stub throws        RobotWorker ←──────────────┘
                                    work + charge only
```

### 💡 Interview Answer
> *"ISP says don't make a class depend on what it won't use. In JavaScript I use Object.assign() to compose only the behaviours each class actually needs — so robots never get eat() and stub-throwing methods never appear."*

---

<a name="dip"></a>
## 5️⃣ D — Dependency Inversion Principle (DIP)

### 📖 Definition
> **"High-level modules should not depend on low-level modules. Depend on abstractions."**
> Don't hardwire your logic to a specific tool. Wire to an interface — then swap tools freely.

### 🧠 Memory Trick
> Your laptop plugs into a **standard socket** — it doesn't care if electricity comes from solar or coal.
> **Code to the socket (abstraction), not the power plant (implementation).**

---

### ❌ Wrong

```javascript
class MySQLDatabase {
  save(user) { console.log(`MySQL: saving ${user.name}`); }
}

class UserService {
  constructor() {
    this.db = new MySQLDatabase();  // ❌ hardwired
  }
  createUser(user) { this.db.save(user); }
}
// Switch to MongoDB → must rewrite UserService
// Write a unit test  → need a real MySQL connection
```

---

### ✅ Fixed

```javascript
// Abstraction — the "socket"
class Database {
  save(user) { throw new Error("Implement save()"); }
}

class MySQLDatabase extends Database {
  save(user) { console.log(`MySQL: saving ${user.name}`); }
}

class MongoDB extends Database {
  save(user) { console.log(`MongoDB: saving ${user.name}`); }
}

class InMemoryDatabase extends Database {     // for unit tests
  constructor() { super(); this.store = []; }
  save(user) { this.store.push(user); }
}

class UserService {
  constructor(db) { this.db = db; }           // ✅ injected, not hardwired
  createUser(user) { this.db.save(user); }
}

// Production
const svc = new UserService(new MySQLDatabase());
svc.createUser({ name: "Alice" });            // MySQL: saving Alice

// Tests — no real DB needed ✅
const testSvc = new UserService(new InMemoryDatabase());
testSvc.createUser({ name: "Bob" });
```

---

### 🗺 Diagram

```
BEFORE                            AFTER
────────────────────────────────  ──────────────────────────────────────
UserService                       UserService
  └── new MySQLDatabase() ❌           └── Database  ← abstraction (socket)
       tightly coupled                         ▲
       can't test without DB                   │ injected
       switch DB = rewrite service        MySQL | MongoDB | InMemory
```

### 💡 Interview Answer
> *"DIP means inject dependencies rather than creating them inside the class. I pass the database to UserService via the constructor — so I can swap MySQL for MongoDB, or use InMemory in tests, with zero changes to business logic."*

---

<a name="dry"></a>
## 🎁 Bonus — DRY (Don't Repeat Yourself)

> **Write logic once. Reference it everywhere. Never copy-paste business logic.**

```javascript
// ❌ BAD — discount logic copy-pasted 3 times
processWeb(o)    { let t = o.price; if (o.premium) t *= 0.8; }
processMobile(o) { let t = o.price; if (o.premium) t *= 0.8; } // duplicate
processPhone(o)  { let t = o.price; if (o.premium) t *= 0.8; } // duplicate
// Change discount rate? Must find and fix 3 places → easy to miss one

// ✅ GOOD — single source of truth
getPrice(price, isPremium) { return isPremium ? price * 0.8 : price; }

processWeb(o)    { const t = this.getPrice(o.price, o.premium); }
processMobile(o) { const t = this.getPrice(o.price, o.premium); }
processPhone(o)  { const t = this.getPrice(o.price, o.premium); }
// Change discount rate? One line. Done. ✅
```

---

<a name="cheatsheet"></a>
# 🧠 Master Cheatsheet

```
┌──────┬────────────────────────────┬────────────────────────────┬──────────────────────────────┐
│      │ Definition (one line)      │ Classic violation          │ The fix                      │
├──────┼────────────────────────────┼────────────────────────────┼──────────────────────────────┤
│ SRP  │ 1 class = 1 reason         │ User saves DB + sends      │ Split: User / UserRepo /     │
│      │ to change                  │ email + holds user data    │ EmailService                 │
├──────┼────────────────────────────┼────────────────────────────┼──────────────────────────────┤
│ OCP  │ Extend yes,                │ if/else grows every time   │ Each type = its own class,   │
│      │ modify no                  │ a new payment type added   │ Processor never changes      │
├──────┼────────────────────────────┼────────────────────────────┼──────────────────────────────┤
│ LSP  │ Subclass must safely       │ Ostrich extends Bird but   │ Ostrich extends Animal —     │
│      │ replace its parent         │ throws on fly()            │ never promises to fly        │
├──────┼────────────────────────────┼────────────────────────────┼──────────────────────────────┤
│ ISP  │ No forced unused           │ RobotWorker forced to      │ Object.assign() — mix only   │
│      │ methods                    │ implement eat() / sleep()  │ needed behaviours per class  │
├──────┼────────────────────────────┼────────────────────────────┼──────────────────────────────┤
│ DIP  │ Depend on abstractions,    │ new MySQLDatabase()        │ Inject via constructor,      │
│      │ inject dependencies        │ hardcoded in UserService   │ depend on Database interface │
└──────┴────────────────────────────┴────────────────────────────┴──────────────────────────────┘
```

## How the 5 principles connect

```
SRP  → each class has one job
  ↓
OCP  → isolated classes are easy to extend without touching
  ↓
LSP  → extensions safely substitute the parent
  ↓
ISP  → substitutes stay lean, no dead stub methods
  ↓
DIP  → everything becomes testable and swappable

Result:  readable (SRP) · extensible (OCP) · safe (LSP) · lean (ISP) · testable (DIP)
```

## ⚡ 5-second answers for each principle

| Principle | Say this |
|-----------|---------|
| **SRP** | "One class, one reason to change." |
| **OCP** | "Add new behaviour via new code, not by editing old code." |
| **LSP** | "Swap a parent for its child — nothing should break." |
| **ISP** | "Don't force a class to implement what it doesn't use." |
| **DIP** | "Inject dependencies — depend on abstractions, not concretions." |

## 🔥 Top 4 interview questions

**"What are SOLID principles?"**
> "Five design principles for maintainable, testable, extensible code — SRP, OCP, LSP, ISP, DIP. Together they keep each class focused, safe to extend, and decoupled from specific implementations."

**"Which do you apply most in JavaScript?"**
> "SRP and DIP. SRP: I ask 'which team would ask me to change this file?' — if two teams would, I split it. DIP: I always inject dependencies via the constructor, never instantiate concrete classes inside a service."

**"How do you apply ISP in JavaScript? There are no interfaces."**
> "With composition — I define small behaviour objects and use Object.assign() to mix only the relevant ones into each class. A Robot gets work() and charge() but never eat() or sleep()."

**"How does SOLID help with unit testing?"**
> "DIP is the most direct win. If I hardcode new MySQL() inside a service, every test needs a real database. Injecting it means I pass new InMemoryDatabase() in tests — fast, isolated, no infrastructure."

---
*All examples run in Node.js 14+ or any modern browser console.*
