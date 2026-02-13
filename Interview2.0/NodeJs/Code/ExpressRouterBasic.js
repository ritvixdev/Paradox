// Express Router

// Project Structure

// project/
// ├── app.js
// ├── routes/
// │   └── user.routes.js
// └── controllers/
//     └── user.controller.js


// app.js (Main entry)

const express = require("express");
const app = express();

app.use(express.json());

// Mount router
app.use("/api/users", require("./routes/user.routes"));

app.listen(3000, () => {
  console.log("Server running on port 3000");
});


// routes/user.routes.js (Router)

const express = require("express");
const router = express.Router();
const userController = require("../controllers/user.controller");

// GET /api/users
router.get("/", userController.getUsers);

// GET /api/users/:id
router.get("/:id", userController.getUserById);

// POST /api/users
router.post("/", userController.createUser);

module.exports = router;


// controllers/user.controller.js (Logic)

exports.getUsers = (req, res) => {
  res.json({ message: "List of users" });
};

exports.getUserById = (req, res) => {
  res.json({ userId: req.params.id });
};

exports.createUser = (req, res) => {
  res.json({
    message: "User created",
    data: req.body
  });
};
