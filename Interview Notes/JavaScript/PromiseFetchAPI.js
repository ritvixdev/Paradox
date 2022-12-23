// Promise way to Fetch API

const url = "https://pokeapi.co/api/v2/pokemon?limit=10"

fetch(url)
.then((response) => response.json())
.then((data) => console.log(data))
.catch((err) => console.log(err))