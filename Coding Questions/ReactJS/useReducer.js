// Interview example of useReducer

// Syntax:
// const [state, dispatch] = useReducer (reducer, initialArg, init?)

import React, { useReducer } from "react";

const initialState = { count: 0 };

const reducer = (state, action) => {
  switch (action.type) {
    case "increment":
      return { count: state.count + 1 };
    case "decrement":
      return { count: state.count - 1 };
    case "reset":
      return { count: 0 };
    default:
      throw new Error(" unexpected action");
  }
};

const App = () => {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <div>
      count: {state.count}
      <br />
      <button onClick={() => dispatch({ type: "increment" })}>+</button>
      <button onClick={() => dispatch({ type: "decrement" })}>-</button>
      <button onClick={() => dispatch({ type: "reset" })}>0</button>
    </div>
  );
};

export default App;

// useState vs UseReducer:

// useState is the most simplest and most convinent option
// where useReducer really shines is when you start having state that is using a lot of different useState

// Example:

// useState:

const [firstName, setFirstName] = useState('')
const [lastName, setLastName] = useState('')
const [password, setPasssword] = useState('')
const [repeatPassword, setrepeatPassword] = useState('')
const [email, setEmail] = useState('')

// useReducer:
// useReducer allows you to bring all of the state into one object which is centrally managed

const initialState1 = {
    firstName: '',
    lastname: '',
    password: '',
    repeatPassword: '',
    email: '',
  };
  
  const reducer1 = () => {
    switch (action.type) {
      case 'changeValue':
        return { ...state, [action.field]: action.value };
      case 'reset':
        return initialState;
      default:
        throw new Error();
    }
  };
  

// ===> useReducer Definition:

// useReducer is a React hook that lets you add a reducer to your component

// it is prefered over useState hook  when we have complex state-building logic

// Also used when next state value depends upon its previous values or when the component
// are need to be optimised

// call useReducer at the top level of your component to manage state with a reducer

// React will pass the current state and the action to your reducer function.
// Your Reducer will calculate and return the next state

// React will store the next state, render your component with it and update the UI
