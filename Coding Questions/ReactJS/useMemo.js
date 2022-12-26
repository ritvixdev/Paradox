// interview example of useMemo()

// Syantax:
//const chachedValue = useMemo(functionThatReturnsvalue, arrayDependencies)


// Solution with useMemo:

import React, { useState, useMemo } from 'react';

const App = () => {
  const [number, setNumber] = useState(1);
  const [inc, setInc] = useState(0);

  const factorial = useMemo (() => factorialOf(number), [number]);
  const onChange = (event) => {
    setNumber(Number(event.target.value));
  };
  const onClick = () => setInc(inc => inc + 1);

  return (
    <div>
      Factorial of
      <input type="number" value={number} onChange={onChange} />
      is {factorial}
      <button onClick={onClick}>Re-render clicked {inc}</button>
    </div>
  );
};
const factorialOf = (n) => {
  console.log('factorialOf(n) called!');
  return n <= 0 ? 1 : n * factorialOf(n - 1);
}

export default App;

// Explaination of above Code:

// if you click Re-render button, 'factorialOf(n) called!' isn't logged to console because 
// useMemo(() => factorialOf(number), [number]) returns the memoized factorial calculation.


// Problem Example:

import React, { useState } from 'react';

// const App = () => {
  const [number, setNumber] = useState(1);
  const [inc, setInc] = useState(0);

  const factorial = factorialOf(number);
  const onChange = (event) => {
    setNumber(Number(event.target.value));
  };
  const onClick = () => setInc(inc => inc + 1);

  return (
    <div>
      Factorial of
      <input type="number" value={number} onChange={onChange} />
      is {factorial}
      <button onClick={onClick}>Re-render clicked {inc}</button>
    </div>
  );
// };
// const factorialOf = (n) => {
//     console.log('factorialOf(n) called!');
//     return n <= 0 ? 1 : n * factorialOf(n - 1);
//   }

// export default App;

// Explaination of above Code:

// Every time you change the input value, the factorial is calculated 
// factorialOf(n) and 'factorialOf(n) called!' is logged to console.

// On the other side, each time you click Re-render button, inc state value is updated. 
// Updating inc state value triggers <CalculateFactorial /> re-rendering. But, as a 
// secondary effect, during re-rendering the factorial is recalculated again — 'factorialOf(n) called!' 
// is logged to console.


// useMemo Definition:

// the useMemo is a hook used in the functional component of react that react
// that returns a memorized value

// useMemo is a React hook that lets you cached the result of a calculation between re-renders

// the basic purpose of useMemo hook os related to te fact that we try to avaoid the un ncecessary
// re-rendering of components and props in our program
