# 🍃 MongoDB Interview Preparation Guide

> **Goal:** Read this once and confidently crack any MongoDB interview.
> All concepts are grouped logically — from basics to advanced.

---

## 📋 Table of Contents

| # | Section |
|---|---------|
| 1 | [Fundamentals](#1-fundamentals) |
| 2 | [Data Model — Documents, Collections & BSON](#2-data-model--documents-collections--bson) |
| 3 | [CRUD Operations](#3-crud-operations) |
| 4 | [Querying — Operators, Projection & Cursor Methods](#4-querying--operators-projection--cursor-methods) |
| 5 | [Indexes](#5-indexes) |
| 6 | [Aggregation Pipeline](#6-aggregation-pipeline) |
| 7 | [Relationships & Joins](#7-relationships--joins) |
| 8 | [Replication & High Availability](#8-replication--high-availability) |
| 9 | [Sharding & Scalability](#9-sharding--scalability) |
| 10 | [Transactions & Data Consistency](#10-transactions--data-consistency) |
| 11 | [Security](#11-security) |
| 12 | [Backup & Recovery](#12-backup--recovery) |
| 13 | [Mongoose — ODM for Node.js](#13-mongoose--odm-for-nodejs) |
| 14 | [Top 20 Interview Q&A](#14-top-20-interview-qa) |
| 15 | [Quick Cheatsheet](#15-quick-cheatsheet) |

---

## 1. Fundamentals

### What is MongoDB?

**MongoDB** is an open-source, **NoSQL (Not Only SQL)** document-oriented database that stores data in **JSON-like documents** with **dynamic schemas**, offering developers flexibility to work with evolving data models.

### What is NoSQL?

**NoSQL** databases are designed to handle **structured, semi-structured, and unstructured data** at scale. They don't use traditional relational tables — they use documents, key-value pairs, graphs, or columns instead.

### MongoDB vs SQL — Key Differences

| Feature | SQL (RDBMS) | MongoDB (NoSQL) |
|---|---|---|
| Data structure | Tables (rows & columns) | Documents (JSON/BSON) |
| Schema | Fixed, predefined | Dynamic, flexible |
| Scalability | Vertical | Horizontal + Vertical |
| Joins | Full JOIN support | `$lookup` (limited) |
| Transactions | Full ACID | Multi-document ACID (v4.0+) |
| Relationships | Foreign keys | Embedded docs or references |
| Best for | Banking, finance, e-commerce | Social media, IoT, real-time apps |

### When to Use MongoDB vs SQL?

| Use MongoDB When | Use SQL When |
|---|---|
| Data is unstructured or semi-structured | Data has strict relationships and complex joins |
| Schema changes frequently | Schema is stable and rarely changes |
| High read/write throughput is needed | Strong ACID compliance is critical |
| Horizontal scalability is required | Complex reporting and analytics |
| Social media, IoT, gaming, real-time apps | Banking, finance, inventory systems |

### 7 Key Features of MongoDB

1. **Document-Oriented** — Data stored in flexible BSON documents
2. **Dynamic Schema** — No fixed schema; fields can vary per document
3. **Indexes** — Multiple index types for fast querying
4. **Replication** — Replica sets for high availability
5. **Sharding** — Horizontal scaling across multiple servers
6. **Aggregation Pipeline** — Powerful multi-stage data transformation
7. **Rich Query Language** — Filtering, sorting, regex, projection, and more

### What is Eventual Consistency in NoSQL?

**Eventual consistency** means all nodes in a distributed system will **eventually** have the same data — but not necessarily at the same instant. In MongoDB, secondary replicas may briefly lag behind the primary. The system becomes consistent over time.

### What is a Namespace in MongoDB?

A **namespace** is the full path to a collection — combining the database name and collection name.

```
myDatabase.users     <- full namespace
myDatabase.products  <- full namespace
```

---

## 2. Data Model — Documents, Collections & BSON

### What is a Document?

A **document** is a set of **key-value pairs** stored in **BSON format** — equivalent to a **row in SQL**. Documents in the same collection don't need to have identical fields.

```js
{
  "_id": ObjectId("64a1b2c3d4e5f6789abc0001"),
  "name": "Happy",
  "age": 25,
  "address": { "city": "Mumbai", "zip": "400001" },  // embedded document
  "hobbies": ["football", "coding"]                  // array
}
```

### What is a Collection?

A **collection** is a **group of documents** stored together — equivalent to a **table in SQL**. Collections do NOT enforce a schema.

```
Users Collection
|-- { "_id": 1, "name": "Happy", "age": 25 }
|-- { "_id": 2, "name": "Amit", "city": "Delhi" }      <- different fields, still valid
|-- { "_id": 3, "name": "Rawat", "score": 99 }
```

**Create and drop a collection:**

```js
db.createCollection("users")   // create collection
db.users.drop()                // drop collection
```

### What is BSON?

**BSON (Binary JSON)** is the binary-encoded format MongoDB uses internally to store documents. It extends JSON by adding extra data types like `Date`, `ObjectId`, `Binary`, and `Decimal128`.

```
JSON  -> Human-readable text  -> "age": 25
BSON  -> Binary encoding      -> Faster parsing + more data types
```

### What is ObjectId?

**ObjectId** is the **default unique identifier** for every MongoDB document stored in the `_id` field. It is a **12-byte** value made up of:

| Bytes | Content |
|---|---|
| 4 bytes | Unix timestamp (seconds since epoch) |
| 5 bytes | Random value (unique per machine & process) |
| 3 bytes | Incrementing counter |

```js
ObjectId("64a1b2c3 d4e5f678 9abc0001")
//         timestamp  random   counter
```

### What is the _id Field?

- **Uniquely identifies** every document in a collection
- MongoDB **auto-generates** it if not provided
- Always the **first field** in a document
- A **unique index** is automatically created on `_id`
- Can be **excluded** from results using `{ _id: 0 }` in projection

### What is the Maximum Document Size?

The maximum size of a single MongoDB document is **16 MB**.

### What is GridFS?

**GridFS** is MongoDB's specification for storing and retrieving **files larger than 16 MB** (images, videos, PDFs). It splits large files into **255 KB chunks** stored as separate documents.

> Use GridFS when your files exceed 16 MB — the document size limit.

### Is MongoDB Schema-less?

MongoDB is **schema-flexible by default** — documents in the same collection can have different fields. But you can enforce a schema using **Mongoose** (ODM) or MongoDB's built-in **schema validation**.

```js
// Both documents in the same collection — perfectly valid
{ "_id": 1, "name": "Happy", "age": 25 }
{ "_id": 2, "name": "Amit", "city": "Delhi", "score": 99 }  // extra fields, no error
```

### What is a Capped Collection?

A **capped collection** is a **fixed-size collection** that:
- Maintains **insertion order**
- **Automatically deletes** the oldest documents when full
- Useful for **logs, caching, and audit trails**

```js
db.createCollection("logs", { capped: true, size: 1000000, max: 1000 });
// max size: 1MB | max documents: 1000
```

### Supported Data Types in MongoDB

| Type | Example |
|---|---|
| `String` | `"Hello"` |
| `Integer` | `25` |
| `Double` | `3.14` |
| `Boolean` | `true` |
| `Date` | `ISODate("2024-01-01")` |
| `ObjectId` | `ObjectId("...")` |
| `Array` | `["a", "b", "c"]` |
| `Object` | `{ "city": "Mumbai" }` |
| `Null` | `null` |
| `Regular Expression` | `/pattern/` |
| `Binary` | Binary data (for files) |

---

## 3. CRUD Operations

### Create — Inserting Documents

```js
// insertOne() — insert a single document
db.users.insertOne({ name: "Happy", age: 25 });

// insertMany() — insert multiple documents at once
db.users.insertMany([
  { name: "Amit",  age: 30 },
  { name: "Rawat", age: 22 }
]);
```

> `insert()` is **deprecated** — always use `insertOne()` or `insertMany()`.

### Read — Querying Documents

```js
// find() — all documents
db.users.find({});

// find() with filter
db.users.find({ age: { $gte: 25 } });

// findOne() — first matching document
db.users.findOne({ name: "Happy" });

// pretty() — format output for readability (mongo shell only)
db.users.find({}).pretty();
```

### Update — Modifying Documents

```js
// updateOne() — update first matching document
db.users.updateOne(
  { name: "Happy" },        // filter
  { $set: { age: 26 } }    // $set updates ONLY the specified fields
);

// updateMany() — update all matching documents
db.users.updateMany(
  { city: "Mumbai" },
  { $set: { country: "India" } }
);

// replaceOne() — replace the ENTIRE document (only _id preserved)
db.users.replaceOne(
  { name: "Happy" },
  { name: "Happy", age: 27, city: "Bangalore" }
);
```

### What is the Use of $set?

**`$set`** updates **only the specified fields** in a document without affecting other existing fields.

```js
// Before: { name: "Happy", age: 25, city: "Mumbai" }
db.users.updateOne({ name: "Happy" }, { $set: { age: 26 } });
// After:  { name: "Happy", age: 26, city: "Mumbai" }  <- city untouched
```

### update() vs save()

| `updateOne()` | `save()` |
|---|---|
| Modifies only the specified fields of matching documents. | Updates if `_id` exists; inserts a new document if it doesn't. |
| Precise control using operators like `$set`, `$inc`, etc. | Replaces the entire document. |

### Delete — Removing Documents

```js
// deleteOne() — delete first matching document
db.users.deleteOne({ name: "Happy" });

// deleteMany() — delete all matching documents
db.users.deleteMany({ age: { $lt: 18 } });

// drop() — delete the entire collection
db.users.drop();
```

### What is Bulk Write Operation?

**Bulk write** performs **multiple write operations in a single request** — reducing round trips to the server and improving performance.

```js
db.users.bulkWrite([
  { insertOne: { document: { name: "New User", age: 20 } } },
  { updateOne: { filter: { name: "Happy" }, update: { $set: { age: 27 } } } },
  { deleteOne: { filter: { name: "OldUser" } } }
]);
```

---

## 4. Querying — Operators, Projection & Cursor Methods

### Comparison Operators

```js
{ field: { $operator: value } }   // syntax
```

| Operator | Meaning | Example |
|---|---|---|
| `$eq` | Equal to | `{ age: { $eq: 25 } }` |
| `$ne` | Not equal | `{ age: { $ne: 25 } }` |
| `$gt` | Greater than | `{ age: { $gt: 20 } }` |
| `$gte` | Greater than or equal | `{ age: { $gte: 25 } }` |
| `$lt` | Less than | `{ age: { $lt: 30 } }` |
| `$lte` | Less than or equal | `{ age: { $lte: 30 } }` |
| `$in` | Any value in array | `{ city: { $in: ["Mumbai", "Delhi"] } }` |
| `$nin` | None of the values | `{ city: { $nin: ["Pune"] } }` |

### Logical Operators

```js
// $and — ALL conditions must match
db.users.find({ $and: [{ age: { $gte: 20 } }, { city: "Mumbai" }] });

// $or — at least ONE condition must match
db.users.find({ $or: [{ age: { $lt: 20 } }, { city: "Delhi" }] });

// $not — negates a condition
db.users.find({ age: { $not: { $gt: 30 } } });
```

### $in vs $all — Common Interview Question

| `$in` | `$all` |
|---|---|
| Returns docs where the field matches **any one** of the values. | Returns docs where the array contains **all** of the values. |

```js
// $in — user has EITHER "mongodb" OR "react" skill
db.users.find({ skills: { $in: ["mongodb", "react"] } });

// $all — user must have BOTH "mongodb" AND "react" skills
db.users.find({ skills: { $all: ["mongodb", "react"] } });
```

### Projection — Selecting Which Fields to Return

**Projection** specifies which fields to **include (1) or exclude (0)** from query results.

```js
// Include only name and email
db.users.find({}, { name: 1, email: 1, _id: 0 });
// Output: { name: "Happy", email: "happy@example.com" }

// Exclude password field from all results
db.users.find({}, { password: 0 });
```

> You **cannot mix** include and exclude in the same projection — **except for `_id`**.

### Cursor Methods — limit(), sort(), skip()

```js
// limit() — restrict number of results
db.users.find({}).limit(5);

// sort() — sort results (1 = ascending, -1 = descending)
db.users.find({}).sort({ age: 1 });    // oldest first
db.users.find({}).sort({ age: -1 });   // youngest first

// skip() — skip N documents (pagination)
db.users.find({}).skip(10).limit(5);   // page 3 of 5 results/page

// Chain them together
db.users.find({}).sort({ age: -1 }).skip(0).limit(10);
```

### Regular Expressions in MongoDB

```js
// Names starting with "H"
db.users.find({ name: /^H/ });

// Case-insensitive search
db.users.find({ name: { $regex: "happy", $options: "i" } });
```

### Does MongoDB Support Foreign Keys?

**No.** MongoDB does not natively enforce foreign key relationships. Relationships are handled via **embedded documents** or **manual references** (storing an `_id` of another document).

---

## 5. Indexes

### What is an Index in MongoDB?

An **index** is a data structure (B-tree) that speeds up data retrieval by avoiding a **full collection scan**. Without an index, MongoDB reads every single document to find matches.

> **Analogy:** Like a book's index — jump directly to the right page instead of reading every page.

### How Indexing Works

```
Without index:  MongoDB scans ALL documents -> slow for large collections
With index:     MongoDB uses index tree to jump directly to matches -> fast
```

```
Index tree on "name" field:
"Anurag" -> points to document with _id: 1
"Happy"  -> points to document with _id: 2
"Rawat"  -> points to document with _id: 3
```

### Which Index is Created by Default?

MongoDB **automatically creates a unique index on the `_id` field** for every collection.

### Creating Indexes

```js
// Single field index
db.users.createIndex({ name: 1 });           // 1=ascending, -1=descending

// Compound index — multiple fields
db.users.createIndex({ name: 1, age: -1 });

// Unique index — prevents duplicate values
db.users.createIndex({ email: 1 }, { unique: true });

// Text index — full-text search
db.users.createIndex({ bio: "text" });

// View all indexes on a collection
db.users.getIndexes();

// Drop an index
db.users.dropIndex({ name: 1 });
```

### Types of Indexes in MongoDB

| Type | Description | Use Case |
|---|---|---|
| **Single Field** | Index on one field | Most common queries |
| **Compound** | Index on multiple fields | Multi-field queries |
| **Multi-key** | Index on array fields | Querying array elements |
| **Text** | Full-text search | Search by keywords |
| **Geospatial** | Location-based data | Nearby places, maps |
| **Hashed** | Hash-based index | Sharding, equality queries |
| **Wildcard** | Dynamically indexes all fields | Dynamic/unknown schemas |

---

## 6. Aggregation Pipeline

### What is Aggregation?

**Aggregation** processes groups of documents through a **series of stages (pipeline)**, transforming and computing results. Think of it as SQL's `GROUP BY` + `JOIN` + `HAVING` — but more powerful.

### Pipeline Example

```js
db.orders.aggregate([
  { $match:   { status: "completed" } },                         // filter
  { $group:   { _id: "$city", total: { $sum: "$amount" } } },    // group & sum
  { $sort:    { total: -1 } },                                   // sort descending
  { $limit:   5 },                                               // top 5 results
  { $project: { _id: 0, city: "$_id", total: 1 } }              // shape output
]);
```

### Common Pipeline Stages

| Stage | Purpose | SQL Equivalent |
|---|---|---|
| `$match` | Filter documents | `WHERE` |
| `$group` | Group and aggregate | `GROUP BY` |
| `$project` | Include/exclude/rename fields | `SELECT` |
| `$sort` | Sort results | `ORDER BY` |
| `$limit` | Limit number of results | `LIMIT` |
| `$skip` | Skip documents | `OFFSET` |
| `$unwind` | Deconstruct array into separate docs | — |
| `$lookup` | Join with another collection | `JOIN` |
| `$addFields` | Add computed fields | computed columns |
| `$count` | Count matching documents | `COUNT(*)` |

### Accumulator Operators (used inside $group)

| Operator | Purpose | Example |
|---|---|---|
| `$sum` | Total sum | `{ $sum: "$price" }` |
| `$avg` | Average | `{ $avg: "$age" }` |
| `$min` | Minimum value | `{ $min: "$score" }` |
| `$max` | Maximum value | `{ $max: "$score" }` |
| `$push` | Push values into array | `{ $push: "$name" }` |
| `$first` | First value in group | `{ $first: "$name" }` |
| `$last` | Last value in group | `{ $last: "$name" }` |

### $unwind Example

```js
// Explodes each element of an array into a separate document
db.users.aggregate([{ $unwind: "$hobbies" }]);

// Input:  { name: "Happy", hobbies: ["football", "coding"] }
// Output: { name: "Happy", hobbies: "football" }
//         { name: "Happy", hobbies: "coding" }
```

### What is MapReduce?

**MapReduce** is an older data processing technique with two steps:
1. **Map** — Map data to key-value pairs
2. **Reduce** — Aggregate the values by key

> **Note:** The **Aggregation Pipeline is preferred** over MapReduce — it is faster, easier, and more expressive.

```js
db.orders.mapReduce(
  function() { emit(this.city, this.amount); },           // Map
  function(key, values) { return Array.sum(values); },    // Reduce
  { out: "city_totals" }
);
```

### Aggregation vs MapReduce

| Aggregation Pipeline | MapReduce |
|---|---|
| Faster and more expressive | Slower, complex syntax |
| Uses native operators | Uses JavaScript functions |
| Preferred for all modern use cases | Legacy, mostly deprecated |
| Runs entirely in C++ | Runs JavaScript — slower |

---

## 7. Relationships & Joins

### Two Ways to Model Relationships

#### 1. Embedded Documents (Denormalization) — One-to-One / One-to-Few

Embed related data **inside the same document**.

```js
// User with embedded address (One-to-One)
{
  "_id": 1,
  "name": "Happy",
  "address": {
    "street": "123 Main St",
    "city": "Mumbai"
  }
}
```

**Use Embedded When:**
- Relationship is **one-to-few** (not unlimited)
- Data is **retrieved together** frequently
- Updates happen to both at the same time
- The embedded field is **rarely updated independently**

#### 2. References (Normalization) — One-to-Many / Many-to-Many

Store a **reference ID** to a document in another collection — like a foreign key.

```js
// Users collection
{ "_id": 1, "name": "Happy" }

// Orders collection — references user by ID
{ "_id": 101, "userId": 1, "product": "Laptop", "price": 50000 }
{ "_id": 102, "userId": 1, "product": "Mouse",  "price": 500   }
```

**Use References When:**
- Relationship is **one-to-many or many-to-many**
- Related data is large or **updated independently**
- Data is **reused across multiple documents**

### $lookup — MongoDB's Equivalent of JOIN

```js
db.orders.aggregate([
  {
    $lookup: {
      from: "users",          // collection to join with
      localField: "userId",   // field in orders
      foreignField: "_id",    // field in users
      as: "userDetails"       // result stored in this array field
    }
  }
]);
// Output: orders + embedded user info in "userDetails" array
```

> **Limitation:** `$lookup` does **NOT work on sharded collections**.

### NoSQL == No Joins?

MongoDB avoids joins by design. Instead, developers **denormalize data** (embed related data). When a join-like operation is needed, `$lookup` is used — but it has limitations.

### Tree Structures in MongoDB

| Pattern | Description | Best For |
|---|---|---|
| **Parent Reference** | Each node stores its parent's `_id` | Simple hierarchies |
| **Child Reference** | Each node stores array of children's `_id` | One-to-few children |
| **Array of Ancestors** | Each node stores all ancestor IDs | Fast ancestor queries |
| **Materialized Path** | Each node stores path string | Path-based queries |

---

## 8. Replication & High Availability

### What is Replication?

**Replication** means **duplicating the same data across multiple MongoDB servers** to provide **redundancy, high availability, and failover** protection.

### What is a Replica Set?

A **Replica Set** is a group of MongoDB servers (nodes) that maintain the **same copy of data**.

- Minimum **3 nodes** required
- **One Primary** — receives all write operations
- **One or more Secondaries** — replicate data from the primary
- If the Primary fails — secondaries **auto-elect a new Primary**
- Recovered failed node rejoins as a **secondary**

```
Replica Set (3 nodes)
|-- Primary    <- ALL writes go here
|-- Secondary  <- replicates from Primary, can serve reads
|-- Secondary  <- replicates from Primary, can serve reads

Primary fails -> election -> Secondary becomes new Primary automatically
```

### Primary vs Secondary Node

| Primary | Secondary |
|---|---|
| Receives ALL write operations | Replicates data from Primary |
| Only ONE primary at any time | Multiple secondaries allowed |
| Can also serve reads (default) | Can serve reads (if configured) |
| If it fails, election happens | Becomes Primary if Primary fails |

### What is the Replica Set Oplog?

The **oplog (operations log)** is a special capped collection that **records all write operations** on the primary. Secondaries use the oplog to replicate changes from the primary in order.

### Does Adding More Secondaries Improve Write Speed?

**FALSE.** All writes **always go to the Primary only**. Adding more secondaries only improves **read** performance (if reads are distributed to secondaries). Write performance depends solely on the Primary.

### How Does MongoDB Ensure High Availability?

1. **Replica Sets** — Multiple copies of data across servers
2. **Automatic Failover** — If primary goes down, secondary is auto-elected as new primary
3. **Data Redundancy** — Copies distributed across servers and data centers

---

## 9. Sharding & Scalability

### What is Sharding?

**Sharding** is a method of **distributing data across multiple servers (shards)** to handle large datasets and high throughput. Each shard holds a **subset** of the total data.

### Vertical vs Horizontal Scaling

| Vertical Scaling | Horizontal Scaling |
|---|---|
| Add more CPU/RAM/Disk to a **single server** | Add **more servers** to distribute the load |
| Limited by hardware capacity | Can scale indefinitely |
| Traditional SQL databases | **MongoDB scales horizontally via Sharding** |

### Components of a Sharded Cluster

1. **Shards** — Each shard stores a portion of the data (can itself be a replica set)
2. **mongos** — The **query router** — routes client requests to the correct shard
3. **Config Servers** — Store **metadata** about which data lives on which shard

```
Client -> mongos (router) -> Shard 1 (users A-M)
                          -> Shard 2 (users N-Z)
```

### What is a Shard Key?

A **shard key** is a field used by MongoDB to **distribute documents across shards**. Choosing a good shard key ensures balanced data distribution.

```js
// Enable sharding on a database
sh.enableSharding("myDatabase");

// Shard a collection using "city" as the shard key
sh.shardCollection("myDatabase.users", { city: 1 });
```

> A poorly chosen shard key causes **hotspots** — uneven distribution where one shard handles most of the load.

---

## 10. Transactions & Data Consistency

### Does MongoDB Support Transactions?

Yes. Since **MongoDB 4.0**, MongoDB supports **multi-document ACID transactions** across multiple documents and collections.

```js
const session = client.startSession();
session.startTransaction();

try {
  await ordersCollection.insertOne(
    { userId: 1, product: "Laptop" }, { session }
  );
  await inventoryCollection.updateOne(
    { product: "Laptop" },
    { $inc: { stock: -1 } },
    { session }
  );
  await session.commitTransaction();
  console.log("Transaction committed!");
} catch (error) {
  await session.abortTransaction();
  console.error("Transaction aborted:", error);
} finally {
  session.endSession();
}
```

### What is ACID?

| Property | Meaning |
|---|---|
| **Atomicity** | All operations succeed or all fail — no partial updates |
| **Consistency** | Data remains valid before and after the transaction |
| **Isolation** | Concurrent transactions don't interfere with each other |
| **Durability** | Committed data is permanently saved even if server crashes |

### How Does MongoDB Ensure Data Consistency?

MongoDB uses a **two-phase commit protocol** and **write concerns** for consistency in distributed environments.

```js
// Write concern: ensure data written to majority of replica set members
db.users.insertOne(
  { name: "Happy" },
  { writeConcern: { w: "majority" } }
);
```

---

## 11. Security

### How Does MongoDB Handle Security?

MongoDB provides **5 layers of security**:

1. **Authentication** — Verifies identity (username/password, LDAP, X.509 certificates)
2. **Authorization** — Role-Based Access Control (RBAC) — controls what each user can do
3. **Encryption** — TLS/SSL for data in transit; encrypted storage for data at rest
4. **Auditing** — Logs all database activities for compliance
5. **Network Security** — IP whitelisting, firewall rules, VPC peering

```js
// Create a user with read-only access
db.createUser({
  user: "readOnlyUser",
  pwd: "securePassword",
  roles: [{ role: "read", db: "myDatabase" }]
});
```

### What is the Role of the mongod Process?

**`mongod`** is the **primary daemon process** in MongoDB — it manages data storage, indexing, memory, and all database access. It is the actual MongoDB server running in the background.

### What is the Mongo Shell?

**`mongosh`** (mongo shell) is a **command-line interface** that allows users to interact with MongoDB, run queries, create databases/collections, and perform administrative tasks.

---

## 12. Backup & Recovery

### Backup and Restore Utilities

| Utility | Purpose |
|---|---|
| `mongodump` | Export database data to BSON files |
| `mongorestore` | Restore data from `mongodump` backup files |
| `mongoexport` | Export collection data to JSON or CSV |
| `mongoimport` | Import data from JSON or CSV files |

```bash
# Backup a database
mongodump --db myDatabase --out /backup/

# Restore a database
mongorestore --db myDatabase /backup/myDatabase/

# Export collection to JSON
mongoexport --db myDatabase --collection users --out users.json

# Import from JSON
mongoimport --db myDatabase --collection users --file users.json
```

### Backup Methods in MongoDB

| Method | Description |
|---|---|
| **Hot Backup** | Backup while database is running — no downtime |
| **Point-in-time Recovery** | Restore to a specific moment using oplog |
| **Incremental Backup** | Only backs up data changed since the last backup |
| **mongodump/mongorestore** | Simple full backup and restore via command line |

### What is MongoDB Ops Manager?

**MongoDB Ops Manager** is a management platform that provides monitoring, automated backups, deployment automation, and performance optimization for MongoDB.

### What is the Role of the Profiler?

The **Database Profiler** collects performance data about operations — especially **slow queries** — to help identify bottlenecks.

```js
// Enable profiler (0=off, 1=slow queries only, 2=all queries)
db.setProfilingLevel(1, { slowms: 100 });  // log queries > 100ms

// View profiler results
db.system.profile.find().sort({ ts: -1 }).limit(5).pretty();
```

---

## 13. Mongoose — ODM for Node.js

### What is Mongoose?

**Mongoose** is an **Object Data Modeling (ODM)** library for MongoDB and Node.js. It adds **structure, validation, and middleware** on top of MongoDB's flexible documents.

### Mongoose vs Direct MongoDB Driver

| Feature | Direct MongoDB Driver | Mongoose |
|---|---|---|
| Schema validation | None built-in | Full schema validation |
| Middleware/Hooks | Not available | Pre/Post hooks |
| Relationships | Manual | `populate()` for references |
| Code organization | Less structured | Model-based, organized |
| Best for | Flexibility, performance | Structured Node.js apps |

### Connecting to MongoDB with Mongoose

```js
const mongoose = require("mongoose");

mongoose.connect("mongodb://localhost:27017/myDatabase")
  .then(() => console.log("Connected via Mongoose"))
  .catch((err) => console.error("Error:", err));
```

### Define a Schema and Model

```js
const mongoose = require("mongoose");

const userSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    minlength: 3,
    trim: true
  },
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true
  },
  age: { type: Number, min: 0, max: 120 },
  createdAt: { type: Date, default: Date.now }
});

const User = mongoose.model("User", userSchema);
module.exports = User;
```

### CRUD with Mongoose

```js
// CREATE
await User.create({ name: "Happy", email: "happy@example.com", age: 25 });

// READ
const all     = await User.find({});
const one     = await User.findById("64a1b2c3...");
const byEmail = await User.findOne({ email: "happy@example.com" });

// UPDATE — new: true returns the updated document
await User.findByIdAndUpdate("64a1b2c3...", { $set: { age: 26 } }, { new: true });

// DELETE
await User.findByIdAndDelete("64a1b2c3...");
```

### Mongoose populate() — Reference Joins

```js
// Order schema with reference to User
const orderSchema = new mongoose.Schema({
  product: String,
  price:   Number,
  user:    { type: mongoose.Schema.Types.ObjectId, ref: "User" }
});
const Order = mongoose.model("Order", orderSchema);

// populate() replaces userId with full user document
const orders = await Order.find({}).populate("user", "name email");
// Output: orders with { name: "Happy", email: "..." } instead of just the ID
```

---

## 14. Top 20 Interview Q&A

### Q1. What is MongoDB?

MongoDB is a **NoSQL document-oriented database** that stores data in **JSON-like documents with dynamic schemas**, offering flexibility for evolving data models and high-volume data storage.

---

### Q2. What is a Document in MongoDB?

A document is a **set of key-value pairs stored in BSON format** — equivalent to a row in SQL. Documents in the same collection can have different fields.

---

### Q3. What is a Collection in MongoDB?

A collection is a **group of documents** that share a similar structure — equivalent to a table in SQL. Collections do not enforce a fixed schema.

---

### Q4. What is a Replica Set in MongoDB?

A replica set is a **group of MongoDB servers that store the same data** to provide redundancy and high availability. It has one Primary (receives writes) and one or more Secondaries (replicate data). If the Primary fails, a new one is automatically elected.

---

### Q5. What is Sharding in MongoDB?

Sharding is a method of **partitioning data across multiple servers** (shards) to improve performance and horizontal scalability for large datasets.

---

### Q6. What is Indexing in MongoDB?

Indexing is the process of **creating a data structure (B-tree) on a field** to speed up query performance by avoiding a full collection scan. By default, MongoDB creates a unique index on the `_id` field.

---

### Q7. What are the Different Types of Indexes?

MongoDB supports: **Single Field, Compound, Multi-key (arrays), Text (full-text search), Geospatial, Hashed, and Wildcard** indexes.

---

### Q8. What is MapReduce in MongoDB?

MapReduce is a **data processing technique** that maps data to key-value pairs and reduces (aggregates) the values by key. It is now superseded by the **Aggregation Pipeline**, which is faster and easier.

---

### Q9. What is the Aggregation Pipeline?

The Aggregation Pipeline is a framework for processing documents through a **series of stages** (match, group, sort, project, lookup, etc.) to filter, transform, and compute results.

---

### Q10. What is the Difference Between update() and save()?

- **`updateOne()`** — Modifies only specified fields of matching documents using operators like `$set`
- **`save()`** — Updates the entire document if `_id` exists; otherwise inserts a new document

---

### Q11. What is GridFS in MongoDB?

GridFS is a specification for **storing and retrieving files larger than 16 MB** in MongoDB, by splitting them into 255 KB chunks stored as separate documents.

---

### Q12. What is the Difference Between a Primary Key and Secondary Key?

- **Primary Key (`_id`)** — Unique identifier for every document; auto-generated by MongoDB
- **Secondary Key (index)** — An index on any other field, used to speed up queries and lookups

---

### Q13. How Does MongoDB Ensure Data Consistency?

MongoDB uses a **two-phase commit protocol** and **write concerns** (e.g., `{ w: "majority" }`) to ensure data is written to the required number of replica set members before confirming success.

---

### Q14. How Does MongoDB Handle Schema Changes?

MongoDB supports **flexible schemas** — schema changes can be made without affecting existing data. New fields are simply added to new documents; old documents are unaffected.

---

### Q15. How Does MongoDB Handle Transactions?

Since v4.0, MongoDB supports **multi-document ACID transactions** — ensuring Atomicity, Consistency, Isolation, and Durability across multiple documents and collections in a single transaction.

---

### Q16. What is the Role of the mongod Process?

**`mongod`** is the **primary daemon process** — the actual MongoDB server that manages data storage, indexing, memory, and all database access.

---

### Q17. What is the Role of the Mongo Shell?

**`mongosh`** is a **command-line interface** that allows users to run queries, manage databases, and perform administrative tasks against a MongoDB server.

---

### Q18. How Does MongoDB Handle Security?

MongoDB provides **authentication** (verifying identity), **authorization** (role-based access control), **encryption** (TLS/SSL for transit, encrypted storage at rest), **auditing** (activity logs), and **network security** (IP whitelisting, firewalls).

---

### Q19. What is the Difference Between a Join and a Lookup?

- **JOIN** (SQL) — Combines data from multiple tables at query time
- **`$lookup`** (MongoDB) — Aggregation stage that retrieves related data from another collection; does NOT work on sharded collections

MongoDB developers often **denormalize data** (embed related data) to avoid needing joins altogether.

---

### Q20. How Does MongoDB Handle Data Backup and Recovery?

MongoDB provides **`mongodump`/`mongorestore`** for manual backups, **hot backups** (no downtime), **point-in-time recovery** (using oplog), and **incremental backups** (only changed data). MongoDB Ops Manager automates all of this.

---

## 15. Quick Cheatsheet

### One-Line Definitions

| Term | One-Line Definition |
|---|---|
| **MongoDB** | Open-source NoSQL document database storing data in BSON documents. |
| **NoSQL** | Database for structured, semi-structured, and unstructured data without fixed schemas. |
| **Document** | A JSON/BSON object — equivalent to a row in SQL. |
| **Collection** | A group of documents — equivalent to a table in SQL. |
| **BSON** | Binary JSON — MongoDB's storage format with extra data types. |
| **ObjectId** | Auto-generated 12-byte unique `_id` for every document. |
| **_id** | Unique identifier field automatically added to every document. |
| **GridFS** | Specification for storing files > 16 MB by splitting into 255 KB chunks. |
| **Capped Collection** | Fixed-size collection that auto-deletes oldest docs when full. |
| **Index** | B-tree data structure that speeds up queries by avoiding full scans. |
| **Aggregation** | Multi-stage pipeline for filtering, grouping, and transforming documents. |
| **$lookup** | Aggregation stage for joining with another collection (SQL JOIN equivalent). |
| **$match** | Filter stage — equivalent to SQL WHERE. |
| **$group** | Grouping stage — equivalent to SQL GROUP BY. |
| **$set** | Update operator that modifies only specified fields, leaving others untouched. |
| **Replica Set** | Group of MongoDB nodes maintaining identical data for high availability. |
| **Primary Node** | The only replica set node that receives all write operations. |
| **Secondary Node** | Nodes that replicate from Primary; can serve reads. |
| **Oplog** | Operations log used by secondaries to replicate writes from the Primary. |
| **Sharding** | Distributing data across multiple servers for horizontal scalability. |
| **Shard Key** | Field used to distribute documents across shards. |
| **mongos** | Query router in a sharded cluster directing requests to correct shards. |
| **ACID** | Atomicity, Consistency, Isolation, Durability — transaction guarantees. |
| **Eventual Consistency** | All nodes eventually have the same data, but may briefly lag. |
| **MapReduce** | Legacy data processing technique — replaced by Aggregation Pipeline. |
| **Mongoose** | ODM library for MongoDB and Node.js with schema validation and middleware. |
| **populate()** | Mongoose method to replace reference IDs with full document data. |
| **mongodump** | Utility to export MongoDB data as BSON files for backup. |
| **mongorestore** | Utility to restore data from mongodump backup files. |
| **Profiler** | Tool for collecting performance data about slow database operations. |
| **mongod** | Primary MongoDB server daemon process. |

---

### Key Commands at a Glance

```js
// DATABASE
show dbs               // list all databases
use myDatabase         // switch to database
db.dropDatabase()      // drop current database

// COLLECTIONS
show collections
db.createCollection("users")
db.users.drop()
db.users.countDocuments()

// INSERT
db.users.insertOne({ name: "Happy", age: 25 })
db.users.insertMany([{ name: "A" }, { name: "B" }])

// READ
db.users.find({})
db.users.find({ age: { $gte: 25 } }, { name: 1, _id: 0 })
db.users.findOne({ name: "Happy" })
db.users.find({}).sort({ age: -1 }).skip(0).limit(10)

// UPDATE
db.users.updateOne({ name: "Happy" }, { $set: { age: 26 } })
db.users.updateMany({ city: "Mumbai" }, { $set: { country: "India" } })

// DELETE
db.users.deleteOne({ name: "Happy" })
db.users.deleteMany({ age: { $lt: 18 } })

// INDEXES
db.users.createIndex({ email: 1 }, { unique: true })
db.users.getIndexes()
db.users.dropIndex({ email: 1 })

// AGGREGATION
db.orders.aggregate([
  { $match:   { status: "completed" } },
  { $group:   { _id: "$city", total: { $sum: "$amount" } } },
  { $sort:    { total: -1 } },
  { $limit:   5 }
])
```

---

### Study Priority Guide

| Level | Topics to Focus On |
|---|---|
| **Junior** | Documents, Collections, BSON, ObjectId, CRUD, Basic queries, Projection, Indexes, Replica Sets basics |
| **Mid-level** | Aggregation Pipeline ($match, $group, $lookup), Sharding basics, Transactions, Mongoose schema + CRUD, $all vs $in |
| **Senior** | Sharding internals, Oplog, Write concerns, MapReduce, GridFS, Security & Auth, Performance profiling, Backup strategies |

---

> **Interview Tip:** Interviewers love to ask about **Replica Sets vs Sharding**, **$in vs $all**, **Embedded vs Referenced documents**, and **Aggregation Pipeline stages**. Make sure you can explain these clearly and write basic code examples from memory.
