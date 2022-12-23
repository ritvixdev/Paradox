// Interview Example for useEffect()

import React, { useState, useEffect } from "react";

const App = () => {
  const [count1, setCount1] = useState(0);
  const [count2, setCount2] = useState(0);
  const [count3, setCount3] = useState(0);

  const increment1 = () => setCount1(count1 + 1);
  const increment2 = () => setCount2(count2 + 1);
  const increment3 = () => setCount3(count3 + 1);

  useEffect(() => {
    console.log("count1 changed!");
  }, [count1]);

  return (
    <div>
      {count1} {count2} {count3}
      <br />
      <button onClick={increment1}>Increment count1</button>
      <button onClick={increment2}>Increment count2</button>
      <button onClick={increment3}>Increment count3</button>
    </div>
  );
};

export default App;
