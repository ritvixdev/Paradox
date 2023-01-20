// CORS Explained for React and Node


// CORS stands for Cross-Origin Resource Sharing. It allows us to relax the security
// applied to an API. This is done by bypassing the Access-Control-Allow-Origin headers,
// which specify which origins can access the API.

// In other words, CORS is a browser security feature that restricts cross-origin HTTP requests
// with other servers and specifies which domains access your resources.

// Example:

const cors = require('cors');
app.use(cors({
    origin: ['https://www.section.io', 'https://www.google.com/']
}));

// Example: 

const whitelist = ['http://developer1.com', 'http://developer2.com']
const corsOptions = {
  origin: (origin, callback) => {
    if (whitelist.indexOf(origin) !== -1) {
      callback(null, true)
    } else {
      callback(new Error())
    }
  }
}


// CORS (Cross-Origin Resource Sharing) is a security feature implemented by web browsers
// that blocks web pages from making requests to a different domain than the one that served
// the web page. This is to prevent malicious websites from making unauthorized requests
// to a user's sensitive data.

// When building a web application using React on the frontend and Node.js on the backend,
// CORS can become an issue if the React application is running on one domain 
// (e.g. http://localhost:3000) and the Node.js API is running on another domain 
// (e.g. http://localhost:5000).

// To handle CORS in a React and Node.js application, you can use a middleware in the Node.js
// API that sets the appropriate headers to allow requests from the React application's domain.
// One popular middleware for this purpose is the cors package.

// Here's an example of how to use the cors package in a Node.js express application:

const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());

app.get('/', (req, res) => {
  res.json({ message: 'Hello from the API' });
});

app.listen(5000, () => {
  console.log('API running on port 5000');
});


// In this example, the cors() middleware is applied to the express application, allowing all
// incoming requests to the API to be processed. You can also configure cors to only allow
// requests from certain origins, by passing an options object to the cors function.


app.use(cors({
  origin: 'http://localhost:3000'
}));


// This will only allow requests from "http://localhost:3000" to hit the API.

// Additionally, in the client-side (React App), you can use http-proxy-middleware package
// to proxy your requests to the backend Node.js server.

// It's important to note that it's also possible to handle CORS on the client-side using
// libraries such as axios or fetch by setting the appropriate headers, but it's considered
// best practice to handle CORS on the server-side for better security.