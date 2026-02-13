// Middleware Fetching Data

// Middleware: fetchUser.middleware.js

const fetchUser = async (req, res, next) => {
  try {
    const { userId } = req.params;

    // Simulating DB / API fetch
    const user = {
      id: userId,
      name: "John Doe",
      role: "admin"
    };

    if (!user) {
      return res.status(404).json({ message: "User not found" });
    }

    // Attach data to request object
    req.user = user;

    next(); // move to next middleware/controller
  } catch (error) {
    next(error); // pass error to error handler
  }
};

module.exports = fetchUser;


// Route using the middleware

const express = require("express");
const router = express.Router();
const fetchUser = require("../middleware/fetchUser.middleware");

// Middleware runs BEFORE controller
router.get("/users/:userId", fetchUser, (req, res) => {
  res.json({
    message: "User fetched successfully",
    user: req.user
  });
});

module.exports = router;


// app.js

const express = require("express");
const app = express();

app.use(express.json());
app.use("/api", require("./routes/user.routes"));

// Error handler
app.use((err, req, res, next) => {
  res.status(500).json({ error: err.message });
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});


// Middleware to Parse JSON

const express = require("express");
const app = express();

// JSON parsing middleware
app.use(express.json());

app.post("/data", (req, res) => {
  res.json({
    message: "JSON parsed successfully",
    body: req.body
  });
});

app.listen(3000, () => console.log("Server running"));
