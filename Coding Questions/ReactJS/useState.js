// interview example of useState

import React, { useState } from 'react';

const App = () => {
  const [count, setCount] = useState(0);

  const increment = () => setCount(count + 1);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={increment}>Click Me!</button>
    </div>
  );
};

export default App;
