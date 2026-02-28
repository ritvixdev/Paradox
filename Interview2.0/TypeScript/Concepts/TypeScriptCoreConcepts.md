# 🟦 TypeScript Ultimate Interview Guide (JS dev → TS interview ready)

> This guide assumes you already know JavaScript.  
> Goal: **easy definitions + interview bullet points + practical snippets** ordered **easy → tough**.

---

## How to use this (fast)
- **Pass 1 (25 min):** Read only the **One‑liner** under each heading.
- **Pass 2 (60–90 min):** Type the snippets yourself (don’t just read).
- **Pass 3 (15 min):** Read the **Cheat Sheet** at the end before interviews.

---

## 30‑second mental model (memorize)
TypeScript = JavaScript + **types** (compile-time).  
It catches bugs earlier, improves refactoring, and produces normal JavaScript output.

```mermaid
flowchart LR
  TS[.ts/.tsx] --> TC[Type Checker (tsc)]
  TC --> JS[.js output]
  TC --> ERR[Compile-time errors]
```

---

# 1) What is TypeScript?

## What is TypeScript and how is it different from JavaScript?
**One‑liner:** TypeScript is a **typed superset** of JavaScript that adds a compile-time type system.

**Interview points**
- TS types are **erased at runtime** (no runtime overhead by default).
- TS helps with **autocompletion**, **refactoring**, and **early bug detection**.
- Output is plain JS that runs anywhere JS runs.

**Code**
```ts
let age: number = 26;
// age = "26"; // ❌ type error
```

---

## What does “TypeScript is a superset of JavaScript” mean?
**One‑liner:** Every valid JavaScript program is also valid TypeScript.

**Interview points**
- You can gradually migrate: rename `.js → .ts` and add types step-by-step.
- TS adds extra syntax (types), but it compiles back to JS.

---

# 2) Fundamentals you must know

## Basic types in TypeScript (most asked)
**One‑liner:** TS provides primitives and special types for safe typing.

### Core types
- `string`, `number`, `boolean`, `bigint`, `symbol`
- `null`, `undefined`
- `object`, `Array<T>`
- `any`, `unknown`, `never`, `void`

**Example**
```ts
let name: string = "Suvam";
let ids: number[] = [1, 2, 3];
let ok: boolean = true;
```

---

## `any` vs `unknown` (very common interview question)
**One‑liner:** `any` disables type checking; `unknown` forces you to narrow before use.

```ts
let x: any = 10;
x.toUpperCase(); // ✅ allowed (dangerous)

let y: unknown = 10;
// y.toUpperCase(); // ❌ not allowed
if (typeof y === "string") y.toUpperCase(); // ✅ safe
```

**What to say**
> “Prefer `unknown` for untrusted input; it forces type checks.”

---

## let vs const in TypeScript
**One‑liner:** Same as JS, but TS also infers narrower types with `const`.

```ts
let role = "admin";  // type: string (widened)
const mode = "dark"; // type: "dark" (literal type)
```

---

## Type inference (why TS feels smart)
**One‑liner:** If you don’t annotate, TypeScript infers types from values.

```ts
const count = 5; // inferred as number
// count = "5";  // ❌ error
```

---

## How do you compile TypeScript to JavaScript?
**One‑liner:** Use `tsc` (TypeScript compiler). It reads `tsconfig.json`.

**Commands**
```bash
npm i -D typescript
npx tsc --init
npx tsc
```

---

# 3) Objects: Interfaces vs Type Aliases

## Interfaces (must know)
**One‑liner:** Interfaces describe the shape of objects and support declaration merging.

```ts
interface User {
  id: string;
  name: string;
  isAdmin?: boolean; // optional
}

const u: User = { id: "1", name: "Alice" };
```

**Interview points**
- Interfaces are great for object shapes and library/public APIs.
- They can be extended: `interface Admin extends User { ... }`

---

## Type aliases (must know)
**One‑liner:** Type aliases define any type (objects, unions, primitives, tuples).

```ts
type ID = string | number;

type User = {
  id: ID;
  name: string;
};
```

---

## Interface vs type — what to say
**Short answer**
- Use **interface** for object shapes you expect to extend/merge.
- Use **type** for unions, mapped types, utility compositions, and complex types.

---

# 4) Unions, Intersections, Narrowing (core interview area)

## Union types
**One‑liner:** A union type means value can be one of multiple types.

```ts
type Status = "idle" | "loading" | "success" | "error";

function setStatus(s: Status) {}
setStatus("loading");
// setStatus("done"); // ❌
```

---

## Intersection types
**One‑liner:** Intersection combines multiple types into one.

```ts
type WithId = { id: string };
type WithTime = { createdAt: number };

type Entity = WithId & WithTime;

const e: Entity = { id: "x", createdAt: Date.now() };
```

---

## Type narrowing (type guards)
**One‑liner:** Narrowing is how TS reduces a broad type into a specific type at runtime checks.

### Common narrowing patterns
- `typeof`, `in`, `instanceof`
- discriminated unions
- user-defined type guards

```ts
function print(v: string | number) {
  if (typeof v === "string") console.log(v.toUpperCase());
  else console.log(v.toFixed(2));
}
```

---

## Discriminated unions (big interview favorite)
**One‑liner:** Union of object types with a shared “tag” property.

```ts
type Shape =
  | { kind: "circle"; r: number }
  | { kind: "square"; size: number };

function area(s: Shape) {
  switch (s.kind) {
    case "circle": return Math.PI * s.r * s.r;
    case "square": return s.size * s.size;
  }
}
```

**Why interviewers like it**
- It’s the cleanest way to model state machines and API responses.

---

## `never` type (don’t skip)
**One‑liner:** `never` means “this should never happen” — used for exhaustive checks.

```ts
function assertNever(x: never): never {
  throw new Error("Unexpected: " + x);
}

function area2(s: Shape) {
  switch (s.kind) {
    case "circle": return Math.PI * s.r * s.r;
    case "square": return s.size * s.size;
    default: return assertNever(s); // ✅ ensures exhaustive
  }
}
```

---

# 5) Functions (typing, overloads, generics)

## Typing functions
**One‑liner:** Types go on params and return values.

```ts
function add(a: number, b: number): number {
  return a + b;
}

const mul = (a: number, b: number) => a * b; // return inferred
```

---

## Optional params & default values
```ts
function greet(name = "Guest") {
  return `Hello ${name}`;
}
```

---

## Function overloads (common)
**One‑liner:** Overloads define multiple call signatures with one implementation.

```ts
function parse(input: string): string[];
function parse(input: number): number[];
function parse(input: string | number) {
  return typeof input === "string" ? input.split(",") : [input];
}

parse("a,b"); // string[]
parse(1);     // number[]
```

---

# 6) Generics (very important)

## What are generics and why use them?
**One‑liner:** Generics make types reusable while preserving type safety.

```ts
function identity<T>(x: T): T {
  return x;
}
const a = identity(123);   // number
const b = identity("hi");  // string
```

---

## Generic constraints
**One‑liner:** Constraints restrict T to ensure required properties exist.

```ts
function len<T extends { length: number }>(x: T) {
  return x.length;
}
len("hello");
len([1, 2, 3]);
// len(123); // ❌
```

---

## Generics with interfaces/classes
```ts
interface ApiResponse<T> {
  data: T;
  error?: string;
}

class Box<T> {
  constructor(public value: T) {}
}

const r: ApiResponse<number> = { data: 42 };
const b = new Box("ok");
```

---

# 7) Arrays, Tuples, Enums

## Tuples (when to use)
**One‑liner:** Tuple is a fixed-length array with known positions/types.

```ts
type RGB = [number, number, number];
const color: RGB = [255, 0, 0];
```

---

## Enums (use carefully)
**One‑liner:** Enums create named constants; `const enum` compiles away but has build tradeoffs.

```ts
enum Role {
  Admin = "ADMIN",
  User = "USER",
}

function canDelete(role: Role) {
  return role === Role.Admin;
}
```

**Interview advice**
- Prefer string literal unions for simpler runtime unless you truly need enum behavior.

---

# 8) Classes (enough for interviews)

## Classes in TypeScript (vs ES6)
**One‑liner:** TS adds types + access modifiers + abstract classes on top of JS classes.

```ts
class Person {
  constructor(public name: string) {}
}
```

---

## Access modifiers
- `public` (default)
- `private` (only inside class)
- `protected` (class + subclasses)

```ts
class Base {
  protected token = "x";
}

class Child extends Base {
  print() { return this.token; } // ✅
}
```

---

## Abstract classes
**One‑liner:** Abstract classes define a base contract with some implementation; cannot be instantiated.

```ts
abstract class Animal {
  abstract sound(): string;
  move() { return "moving"; }
}

class Dog extends Animal {
  sound() { return "woof"; }
}
```

---

## Getters and setters
```ts
class Wallet {
  private _balance = 0;

  get balance() { return this._balance; }
  set balance(v: number) {
    if (v < 0) throw new Error("no");
    this._balance = v;
  }
}
```

---

## `static` keyword
**One‑liner:** Static members belong to the class, not instances.

```ts
class MathUtil {
  static add(a: number, b: number) { return a + b; }
}
MathUtil.add(1, 2);
```

---

# 9) Utility Types (very common in real projects)

## Must-know utility types
- `Partial<T>`: makes fields optional
- `Required<T>`: makes optional fields required
- `Readonly<T>`: makes fields readonly
- `Pick<T, K>`: select subset
- `Omit<T, K>`: remove subset
- `Record<K, V>`: map type

```ts
type User = { id: string; name: string; age?: number };

type UserPatch = Partial<User>;
type UserPublic = Pick<User, "id" | "name">;
type UserMap = Record<string, User>;
```

---

# 10) Advanced Types (learn after basics)

## `keyof` and indexed access
**One‑liner:** `keyof` gives union of property keys.

```ts
type User = { id: string; name: string };
type UserKey = keyof User; // "id" | "name"

function get<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
```

---

## Mapped types (simple version)
**One‑liner:** Create new types by transforming keys.

```ts
type Readonlyish<T> = { readonly [K in keyof T]: T[K] };
```

---

## Conditional types (basic)
**One‑liner:** Types that depend on a condition.

```ts
type IsString<T> = T extends string ? true : false;

type A = IsString<"x">; // true
type B = IsString<1>;   // false
```

---

## Type assertions (use carefully)
**One‑liner:** Assertions tell TS “trust me”, but don’t change runtime.

```ts
const el = document.getElementById("root") as HTMLDivElement;
// el.value // ❌ div has no value
```

**Rule**
- Prefer narrowing checks; use assertions only when you’re sure.

---

# 11) Modules, Imports/Exports (practical TS)

## ES Modules
**One‑liner:** Use `export` / `import` like modern JS. TS compiles based on `module` setting in tsconfig.

```ts
// math.ts
export const add = (a: number, b: number) => a + b;

// app.ts
import { add } from "./math";
console.log(add(1, 2));
```

---

# 12) tsconfig.json (only the options interviewers care about)

## What is tsconfig.json?
**One‑liner:** Configuration file that tells TS compiler how to type-check and compile your project.

### Must-know options
- `target`: JS output version
- `module`: ESM vs CJS
- `strict`: enables strict type checking
- `noImplicitAny`: disallow implicit any
- `strictNullChecks`: null safety
- `esModuleInterop`: smoother commonjs imports
- `skipLibCheck`: speed up builds (tradeoff)

**Example**
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "strict": true,
    "strictNullChecks": true,
    "noImplicitAny": true,
    "esModuleInterop": true
  }
}
```

---

# 13) Typings and @types (real-world interview topic)

## How do you manage type definitions for external libraries?
**One‑liner:** Many libraries ship types; if not, install `@types/...` from DefinitelyTyped.

**Commands**
```bash
npm i lodash
npm i -D @types/lodash
```

## What is DefinitelyTyped?
**One‑liner:** A community repo that hosts type definitions for JS libraries (published as `@types/*`).

---

# 14) TypeScript with React / Node (only essentials)

## TS with React (patterns you must know)
```tsx
type ButtonProps = {
  title: string;
  onClick: () => void;
  variant?: "primary" | "secondary";
};

export function Button({ title, onClick, variant = "primary" }: ButtonProps) {
  return <button onClick={onClick} data-variant={variant}>{title}</button>;
}
```

**Key tips**
- Use union literals for variants
- Prefer `type Props = { ... }` for React props
- Use generics for reusable components when needed

---

## TS with Express (minimal example)
```ts
import express, { Request, Response } from "express";

const app = express();
app.use(express.json());

app.get("/health", (req: Request, res: Response) => {
  res.json({ ok: true });
});

app.listen(3000);
```

---

# 15) Migration tips (JS → TS)

**Best steps**
1) Add TS: `npm i -D typescript` + `tsc --init`
2) Rename one file at a time: `.js → .ts`
3) Start with **types at boundaries**:
   - API inputs/outputs
   - DB models
   - Component props
4) Turn on `strict` gradually if project is big

---

# ✅ TypeScript Interview Cheat Sheet (15 minutes)

### Most asked answers (quick)
- TS vs JS: compile-time safety, types erased in output
- any vs unknown: unknown forces checks
- interface vs type: interface for shapes/extension, type for unions/complex
- union + narrowing: `typeof`, `in`, discriminated unions
- generics: reusable safe types
- keyof + mapped + utility types: core for large apps
- tsconfig: `strict`, `noImplicitAny`, `strictNullChecks`

### Memory trick
> “TS is **types at compile-time**, runtime is still JS.”

---

# Common TS interview traps (avoid)
- Thinking TS types exist at runtime (they don’t)
- Using `any` everywhere (kills TS value)
- Overusing type assertions instead of narrowing
- Ignoring `strictNullChecks` (causes real bugs)
