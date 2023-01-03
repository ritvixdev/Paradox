// Example for Fetch API using Async/Await and Displaying the names

import React, { useState, useEffect } from 'react';
import './style.css';

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
    <div>
      <h1>Hello StackBlitz!</h1>
      {user?.map((data, index) => {
        return <p key={index}>{data.firstName} </p>;
      })}
    </div>
  );
};

export default App;
