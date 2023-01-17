// Write a React Program to Print if The number is Prime or not

import React,{useState} from 'react' 

const App = () => {
  const [count, setCount] = useState(0)

  const increment = () => setCount(count + 1)

  const isPrime = (count) => {
    if(count == 0 || count == 1){
      return true
    }
    for(let i=2;i< count;i++){
      if(count % i === 0){
        return false
      }
      
    }
    return true
  }

  return(
    <div >
      <p>Count is: {count}</p>
      <p> Prime Number : {isPrime(count)? "Number is Prime":"number is not a prime"}</p>
      <button onClick={increment}>Click</button>
      </div>
  )

}

// export default App

// Another way

import React, { useState } from 'react';

function App() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  function isPrime(num) {
    for(let i = 2; i < num; i++)
      if(num % i === 0) return false;
    return num !== 1;
  }

  return (
    <div>
      <p>Button has been clicked {count} times.</p>
      <p>{isPrime(count) ? "Number is prime" : "Number is not prime"}</p>
      <button onClick={handleClick}>Click me</button>
    </div>
  );
}

export default App;