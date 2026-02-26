import React, { lazy, Suspense, useState } from "react";

const CodeSplit = lazy(() => import("./CodeSplit"));

function App() {

  const [show, setShow] = useState(false);

  return (
    <div>

      <button onClick={() => setShow(true)}>
        Load Component
      </button>

      {show && (
        <Suspense fallback={<div>Loading...</div>}>
          <CodeSplit />
        </Suspense>
      )}

    </div>
  );
}

export default App;


// Advanced Interview Example (Route-based Code Splitting)

import { lazy, Suspense } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

const Home = lazy(() => import("./Home"));
const Dashboard = lazy(() => import("./Dashboard"));

function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<div>Loading page...</div>}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}