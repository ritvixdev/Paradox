// Interview example for Higher Order Components or HOC

// Synatax:
const newComponent = higherFunction(WrappedComponent);

// newComponent — will be the enhanced component
// higherFunction — as the name suggests, this function will enhance WrappedComponent
// WrappedComponent — The component whose functionality we want to extend.

// React Syntax:

import React from 'react';
// Take in a component as argument WrappedComponent
const higherOrderComponent = (WrappedComponent) => {
  // And return another component
  class HOC extends React.Component {
    render() {
      return <WrappedComponent />;
    }
  }
  return HOC;
};


// CODE:

// https://blog.logrocket.com/understanding-react-higher-order-components/


// ===> HOC Definition:

// In React, HOC is an advanced technique for reusing component logic. 
// It is a function that takes a component and returns a new component. 

// higher-order components allow developers to reuse code logic in their project. 
// As a result, this means less repetition and more optimized, readable code.