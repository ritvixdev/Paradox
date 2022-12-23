// iterrate through Javascript objects

const population = {
  male: 4,
  female: 93,
  others: 10,
};

let genders = Object.keys(population);

genders.forEach((gender) => {
  console.log(`There are ${population[gender]} ${gender}`);
});

//====== sum of all population

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

let populationArr = Object.entries(population);

console.log(populationArr);

// return array

for (array of populationArr) {
  console.log(array);
}

// get the keys

for ([key, value] of populationArr) {
  console.log(key);
}

//======== other Example=============

var obj = { first: "John", last: "Doe" };

for (const key of Object.keys(obj)) {
  console.log(key, obj[key]);
}
// ECMAScript 8 adds Object.entries() which avoids having to look up each value in the original object:

Object.entries(obj).forEach(([key, value]) => console.log(key, value));
// You can combine for...of, destructuring, and Object.entries:

for (const [key, value] of Object.entries(obj)) {
  console.log(key, value);
}
// Both Object.keys() and Object.entries() iterate properties-
// in the same order as a for...in loop but ignore the prototype chain.
// Only the object's own enumerable properties are iterated.
