// React example to Call API by Asysnc/Await Fetch and use Effect

import React, { useState, useEffect } from 'react';

const App = () => {
  const [pokemons, setPokemons] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(
        'https://pokeapi.co/api/v2/pokemon?limit=10'
      );
      const data = await response.json();
      console.log(data);
      setPokemons(data.results)
    };

    fetchData();
  }, []);

  return (
    <ul>
      {pokemons.map(({ name, url }) => (
        <li key={url}>{name}</li>
      ))}
    </ul>
  );
};

export default App;
