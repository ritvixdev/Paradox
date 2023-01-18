// Example for Fetch API using Async/Await and Displaying the names in React

import React, { useState, useEffect } from 'react';

const App = () => {
  const [user, setUser] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(
          'https://hub.dummyapis.com/employee?noofRecords=10&idStarts=1001'
        );
        const data = await response.json();
        console.log(data);
        setUser(data);
      } catch (err) {
        console.log(err);
      }
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

