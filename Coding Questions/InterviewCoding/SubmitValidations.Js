// Create a react program using Hooks

// It will add value to the lable from input field
// Conditions and also show input validation if alert value is number
// if red is in capital it will display it in red color
// must not input numbers
// new input display in new line
// clear input after submit click
// also show item numbr left side of added value

// Example output:
// Joy
// Daniel
// George
// RED(only this will be in red color if user type red)


// ===> not complete

import React, { useState, useEffect } from 'react';

const App = () => {

  const [nameList, setNameList] = useState([])
  const [inputName, setInputName] = useState('')
  const [error, setError] = useState('')

  const validateInput = ()=> {
    return true;
  }

  const handleOnSubmitClick = (event)=> {
    if(validateInput()){
      let updateList = [...nameList, inputName]
      setNameList(updateList)

      // clear input box
      setInputName('')
    }else{
      alert('input valid input')
    }
  }

  const handleOnInputChange = (event)=> {
    const {value} = event.target;
    setInputName(value)
  }

  return (
    <div>
      <h1>Welcome to Matrix</h1>
      <h2>Start editing to see Magic!</h2>
      <form submit={handleOnSubmitClick}>
      <input type='text' onChange = {handleOnInputChange}/>
      <button type='submit' onClick={handleOnSubmitClick}>Submit</button>
      <hr/>
      <ul>
        {nameList.map((data, index) => {
          return <ol key={index}>{data}</ol>
        })}
        </ul>
        </form>
    </div>
  );
};

export default App;
