const express = require("express");
const mongoose = require("mongoose");
const path = require("path");

// Always load .env from backend folder
require("dotenv").config({ path: path.resolve(__dirname, ".env") });

const app = express();

// Middleware to parse JSON and URL-encoded data
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

// Get environment variables
const port = process.env.PORT || 5000;
const mongoUri = process.env.MONGO_URI;

// Debugging log
if (!mongoUri) {
  console.error(" MONGO_URI is missing in .env file!");
  process.exit(1);
}
console.log(" Loaded MONGO_URI from .env");

// Database connection
mongoose
  .connect(mongoUri, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => {
    console.log(" MongoDB Connected");
  })
  .catch((err) => {
    console.error(" MongoDB Connection Error:", err);
  });

// Simple route to test server
app.get("/", (req, res) => {
  res.send("Hello World ");
});

// Start the server
app.listen(port, () => {
  console.log(` Server running on port ${port}`);
});
