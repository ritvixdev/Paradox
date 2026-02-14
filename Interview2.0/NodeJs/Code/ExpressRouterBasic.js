// Express Router

// Project Structure

// project/
//  ├── server.js
//  ├── routes/
//  │     └── users.js
//  └── middleware/
//        └── auth.js


// server.js

const express = require("express");
const userRoutes = require("./routes/users");

const app = express();

app.use(express.json()); // built-in middleware

app.use("/api/users", userRoutes);

app.listen(3000, () => {
  console.log("Server running on port 3000");
});


// routes/users.js

const express = require("express");
const router = express.Router();
const { authMiddleware } = require("../middleware/auth");

// GET all users
router.get("/", (req, res) => {
  res.json({ message: "Get all users" });
});

// GET user by ID
router.get("/:id", (req, res) => {
  res.json({ id: req.params.id });
});

// POST create user
router.post("/", authMiddleware, (req, res) => {
  res.json({
    message: "User created",
    data: req.body
  });
});

// PUT update user
router.put("/:id", (req, res) => {
  res.json({
    message: "User updated",
    id: req.params.id
  });
});

// DELETE user
router.delete("/:id", (req, res) => {
  res.json({
    message: "User deleted",
    id: req.params.id
  });
});

module.exports = router;


// Interview Questions About Router



// 1️⃣ What is express.Router()?

// Answer: It allows you to:
// Modularize routes
// Separate concerns
// Keep code clean
// Instead of putting everything in server.js.


//2️⃣ Difference between app.use() and router.use()?
// app.use() → global middleware
// router.use() → middleware only for that router

// 3️⃣ What is route parameter?
// router.get("/:id")
// Accessed with:
// req.params.id

// 4️⃣ Difference between req.params, req.query, req.body?
// Property	    Used For
// req.params	  URL parameters
// req.query	  ?page=1
// req.body	    POST data
