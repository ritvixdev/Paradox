//Async/Await way to fetch data

const url = "https://pokeapi.co/api/v2/pokemon?limit=10"

const fetchData = async () => {
  try{
    const response = await fetch(url)
    const data = await response.json()
    console.log(data)
    
  }catch(err){
    console.log(err)
  }
}

fetchData()
