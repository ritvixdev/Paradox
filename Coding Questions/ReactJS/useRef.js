// interview example for useRef()

// Synatax:
// const ref = useRef(initialValue)



import React, { useEffect, useRef } from "react";

const App = () => {
  // create a ref
  const divElement = useRef();

  // trigger on the first render of the component 
  useEffect(() => {
    // get the height of the div element
    console.log(
      "The height of the div is: ", divElement.current.offsetHeight
    );
  }, []);

  return (
    <div ref={divElement}>
      <h1>Learn about useRef!</h1>
    </div>
  );

}
export default App


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