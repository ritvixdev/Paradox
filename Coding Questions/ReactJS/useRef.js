// interview example for useRef()
// https://dmitripavlutin.com/react-useref-guide/

// Synatax:
// const ref = useRef(initialValue)


// == Logging Button Clicks ==

import React, { useRef } from 'react';
const App = () => {
  const countRef = useRef(0);

  const handle = () => {
    countRef.current++;
    console.log(`Clicked ${countRef.current} times`);
  };
  console.log('I rendered!');
  return <button onClick={handle}>Click me</button>;
};

export default App;

// const countRef = useRef(0) creates a references countRef initialized with 0.

// When the button is clicked, handle function is invoked and the reference value 
// is incremented: countRef.current++. The reference value is logged to the console.

// Updating the reference value countRef.current++ doesn't trigger component re-rendering.
// This is demonstrated by the fact that 'I rendered!' is logged to the console just once,
// at initial rendering, and no re-rendering happens when the reference is updated.

// == same example by useState: ==

import React, { useState } from 'react';
// const App = () => {
  const [count, setCount] = useState(0);
  
  const handle = () => {
    const updatedCount = count + 1;
    console.log(`Clicked ${updatedCount} times`);
    setCount(updatedCount);
  };
  console.log('I rendered!');
  return <button onClick={handle}>Click me</button>;
//};
//export default App;


// == Accessing DOM Element ==

import React, { useRef, useEffect } from 'react';
// const App = () => {
  const elementRef = useRef();
   useEffect(() => {
    const divElement = elementRef.current;
    console.log(divElement); // logs <div>I'm an element</div>
  }, []);
  return (
    <div ref={elementRef}>
      I'm an element
    </div>
  );
// }
// export default App


// == useCase: focusing an element == 

import React, { useRef, useEffect } from 'react';
// const App = () => {
  const inputRef = useRef();
  useEffect(() => {
    inputRef.current.focus();
  }, []);
  return <input ref={inputRef} type="text" />;
// };
// export default App;


// ===> useRef Definition:

// useRef() is a react hook that let's you reference a value that's not needed for rendering

// changing a reff does not trigger a re-render

// useRef return an object that you can use during the whole lifecycle of the component

// The main use case for the useRef hook is to access a DOM child directly

// useRef is a hook and as such can only be used in functional components!

// create a ref
const exampleRef = useRef()

// set the ref value
exampleRef.current = 'Hello World'

// access teh ref value
// this prints 'Hello world to the console'
console.log(exampleRef.current)

// State VS Ref

// So, the 2 main differences between references and state:

// Updating a reference doesn't trigger re-rendering, while updating the state makes the component re-render

// The reference update is synchronous (the updated reference value is available right away), while the 
// state update is asynchronous (the state variable is updated after re-rendering).

// From a higher point of view, references store infrastructure data of side-effects, while the state 
// stores information that is directly rendered on the screen.
