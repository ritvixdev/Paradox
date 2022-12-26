// interview exaple for useCallback

// Syantax
// const cachedFn = useCallback(fn, dependencies)

import React, { useState, useCallback } from 'react';
var funccount = new Set();
const App = () => {
  const [count, setCount] = useState(0);
  const [number, setNumber] = useState(0);

  const incrementCounter = useCallback(() => {
    setCount(count + 1);
  }, [count]);
  const decrementCounter = useCallback(() => {
    setCount(count - 1);
  }, [count]);
  const incrementNumber = useCallback(() => {
    setNumber(number + 1);
  }, [number]);

  funccount.add(incrementCounter);
  funccount.add(decrementCounter);
  funccount.add(incrementNumber);
  console.log(funccount.size);

  return (
    <div>
      Count: {count}
      <button onClick={incrementCounter}>Increase counter</button>
      <button onClick={decrementCounter}>Decrease Counter</button>
      <button onClick={incrementNumber}>increase number</button>
    </div>
  );
};

export default App;

// Above code Explained:

// As we can see from the below output when we change the state ‘count’ 
// then two functions will re-instantiated so the set size will increase 
// by 2 and when we update the state ‘number’ then only one function will 
// re-instantiated and the size of the set will increase by only one.


// ===> useCallback Definition:

// Problem:  When a component re-renders, every function inside of the component 
// is recreated and therefore these functions’ references change between renders.

// useCallback: The useCallback hook is used when you have a component in which the 
// child rendering again and again whithout need.

// it can help us to prevent same unnecessary renders and therefore gain a performance boost.

// useCallback (callback, dependencies) will return a memorized instance of the call back 
// only change if one of the dependencies has changed.

// useCallback chaches a funcn between re-render untill dependencies change.

// in Javascript a function (){} or () => {} always create a different function, similiar to how the {}
// object literal always creates a new object