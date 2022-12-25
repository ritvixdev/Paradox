// interview example of useContext()

// Extra detailed infromation: https://upmostly.com/tutorials/how-to-use-the-usecontext-hook-in-react

// Basics Examle for interview: https://dmitripavlutin.com/react-context-and-usecontext/

import React, { createContext } from "react";

export const UserContext = createContext();

// const App = () => {
  return (
    <UserContext.Provider value="Reed">
      <User />
    </UserContext.Provider>
  );
//};

const User = () => {
  return (
    <UserContext.Consumer>
      {(value) => <h1>{value}</h1>}
      {/* prints: Reed */}
    </UserContext.Consumer>
  );
};

// export default App;

// Detailed example for interview and understanding:

// Example with prop:

function Application() {
  const userName = "John Smith";
  return <Layout userName={userName}>Main content</Layout>;
}
function Layout({ children, userName }) {
  return (
    <div>
      <Header userName={userName} />
      <main>{children}</main>
    </div>
  );
}
function Header({ userName }) {
  return (
    <header>
      <UserInfo userName={userName} />
    </header>
  );
}
function UserInfo({ userName }) {
  return <span>{userName}</span>;
}

// Same example with useContext:

import React, { useContext, createContext } from 'react';

const UserContext = createContext('Unknown');

const App = () => {
  const userName = "John Smith";
  return (
    <UserContext.Provider value={userName}>
      <Layout>
        Main content
      </Layout>
    </UserContext.Provider>
  );
}

const Layout = ({ children }) => {
  return (
    <div>
      <Header />
      <main>
        {children}
      </main>
    </div>
  );
}
const Header = () => {
  return (
    <header>
      <UserInfo />
    </header>
  );
}
const UserInfo = () => {
  const userName = useContext(UserContext);
  return <span>{userName}</span>;
}

export default App


// First, const UserContext = createContext('Unknown') creates the context that's going to 
// hold the user name information.

// Second, inside the <Application /> component, the application's child components are 
// wrapped inside the user context provider: <UserContext.Provider value={userName}>. 
// Note that the value prop of the provider component is important: this is how you set 
// the value of the context.

// Finally, <UserInfo /> becomes the consumer of the context by using the built-in 
// useContext(UserContext) hook. The hook is called with the context as an argument 
// and returns the user name value.

// <Layout /> and <Header /> intermediate components don't have to pass down the userName 
// prop. That is the great benefit of the context: it removes the burden of passing down 
//data through the intermediate components.



// =========== Updating the context =========

// The React Context API is stateless by default and doesn't provide a dedicated method 
// to update the context value from consumer components.

// But this can be easily implemented by integrating a state management mechanism 
// (like useState() or useReducer() hooks), and providing an update function right 
// in the context next to the value itself.

// In the following example, <Application /> component uses useState() hook to 
// manage the context value.

// code Example:

import React, { createContext, useState, useContext, useMemo } from 'react';

// const UserContext = createContext({
//   userName: '',
//   setUserName: () => {},
// });

// const App = () => {
  const [userName, setUserName] = useState('John Smith');
  const value = useMemo(
    () => ({ userName, setUserName }), 
    [userName]
  );
  
  return (
    <UserContext.Provider value={value}>
      <UserNameInput />
      <UserInfo />
    </UserContext.Provider>
  );
// }
const UserNameInput = () => {
  const { userName, setUserName } = useContext(UserContext);
  const changeHandler = event => setUserName(event.target.value);
  return (
    <input
      type="text"
      value={userName}
      onChange={changeHandler}
    />
  );
}
const UserInfo = () => {
  const { userName } = useContext(UserContext);
  return <span>{userName}</span>;
}

// export default App

// explain:

// <UserNameInput /> consumer reads the context value, from where userName and setUserName are extracted.
// The consumer then can update the context value by invoking the update function setUserName(newContextValue).

// <UserInfo /> is another consumer of the context. When <UserNameInput /> updates the context, 
// this component is updated too.

// Note that <Application /> memoizes the context value. Memoization keeps the context value object 
// the same as long as userName is the same, preventing re-rendering of consumers every time the 
// <Application /> re-renders.

// Otherwise, without memoization, const value = { userName, setUserName } would create different 
// object instances during re-rendering of <Application />, triggering re-rendering in context consumers. 


// ===> useContext Definition:

// This hooks allows us to work with React's context API which itself a mechanism to allow us to share data
// within it's component tree without passing through props. It bascally removes prop-drilling

// -> You can hold inside the context:

// -global state
// -theme
// -application configuration
// -authenticated user name
// -user settings
// -preferred language
// -a collection of services
