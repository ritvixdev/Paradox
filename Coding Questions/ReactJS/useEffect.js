// Interview Example for useEffect()

// Syntax
// useEffect (callback, [dependencies])

import React, { useState, useEffect } from "react";

const App = () => {
  const [count1, setCount1] = useState(0);
  const [count2, setCount2] = useState(0);
  const [count3, setCount3] = useState(0);

  const increment1 = () => setCount1(count1 + 1);
  const increment2 = () => setCount2(count2 + 1);
  const increment3 = () => setCount3(count3 + 1);

  useEffect(() => {
    console.log("count1 changed!");
  }, [count1]);

  return (
    <div>
      <p>You clicked {count1} {count2} {count3} times</p>
      <br />
      <button onClick={increment1}>Increment count1</button>
      <button onClick={increment2}>Increment count2</button>
      <button onClick={increment3}>Increment count3</button>
    </div>
  );
};

export default App;


// useEffect example with cleanup

import React, { useState, useEffect } from 'react';
import './style.css';

// const App = () => {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setSeconds((seconds) => seconds + 1);
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <header>{seconds} seconds have elapsed since mounting.</header>
    </div>
  );
// };

// export default App;


// ===> cleanup usecase:
// example of component being unmount is going to a new page or a new route in our
// application where the component is no longer used.


//===> useEffect Definition:

// It allows us to impliment all the lifecycle hooks from withing a single functional API.

// It is basically a hook replcament for the 'old-school' lifecylce methods componentDidmount, componrntDidUpdate,
//  and componentWillUnmount

// It allows to execute lifecycle tasks without a needs for a class component
