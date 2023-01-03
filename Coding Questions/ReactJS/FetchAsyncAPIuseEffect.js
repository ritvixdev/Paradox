// React example to Call API by Asysnc/Await Fetch and use Effect

import React, { useState, useEffect } from 'react';

const App = () => {
  const [user, setUser] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(
        'https://hub.dummyapis.com/employee?noofRecords=10&idStarts=1001'
      );
      const data = await response.json();
      console.log(data);
      setUser(data);
    };

    fetchData();
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
