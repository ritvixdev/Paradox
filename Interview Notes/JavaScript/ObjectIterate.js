// iterrate through Javascript objects

const population = {
    male: 4,
    female: 93,
    others: 10
  };
  
  let genders = Object.keys(population);

  genders.forEach((gender) => {
    console.log(`There are ${population[gender]} ${gender}`);
  })


//====== sum of all population

//   const population = {
//     male: 4,
//     female: 93,
//     others: 10
//   };
  
  let totalPopulation = 0;
//   let genders = Object.keys(population);
  
  genders.forEach((gender) => {
    totalPopulation += population[gender];
  });
  
  console.log(totalPopulation); // 107


//====== Sum by object.values()

//let totalPopulation = 0;
let numbers = Object.values(population);

numbers.forEach((number) => {
  totalPopulation += number;
});

console.log(totalPopulation); 

//==== Use of Object.entries

// const population = {
//     male: 4,
//     female: 93,
//     others: 10
//   };
  
  let populationArr = Object.entries(population);
  
  console.log(populationArr);

// return array

for (array of populationArr){
    console.log(array);
  }

// get the keys

for ([key, value] of populationArr){
    console.log(key);
  } 