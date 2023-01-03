// React example to Call API by Fetch and use Effect

import React, { useState, useEffect } from 'react';

const App = () => {
  const [user, setUser] = useState([]);

  useEffect(() => {
    fetch('https://hub.dummyapis.com/employee?noofRecords=10&idStarts=1001')
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setUser(data);
      })
      .catch((err) => console.log(err.message));
  }, []);

  return (
    <ul>
      {user.map((data, index) => {
        return <li key={index}>{data.firstName}</li>;
      })}
    </ul>
  );
};

export default App;