// React example to Call API by Fetch

import React, { useState, useEffect } from 'react';

const App = () => {
  const [pokemons, setPokemons] = useState([]);

  useEffect(() => {
    fetch('https://pokeapi.co/api/v2/pokemon?limit=10')
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setPokemons(data.results);
      })
      .catch((err) => console.log(err.message));
  }, []);

  return (
    <ul>
      {pokemons.map(({name, url}) => (
        <li key={url}>{name}</li>
      ))}
    </ul>
  );
};