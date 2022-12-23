// interview filter example

//Syntax:
//arr.filter(callback(element), thisArg)

//filter items out of an array

let people = [
    { name: 'aaron', age: 65 },
    { name: 'beth', age: 2 },
    { name: 'cara', age: 13 },
    { name: 'daniel', age: 3 },
    { name: 'ella', age: 25 },
    { name: 'fin', age: 1 },
    { name: 'george', age: 43 },
  ];
  
  let toddlers = people.filter((person) => person.age <= 3);
  
  console.log(toddlers);

//filter out items based on a particular property

let team = [
    {
      name: 'aaron',
      position: 'developer',
    },
    {
      name: 'beth',
      position: 'ui designer',
    },
    {
      name: 'cara',
      position: 'developer',
    },
    {
      name: 'daniel',
      position: 'content manager',
    },
    {
      name: 'ella',
      position: 'cto',
    },
    {
      name: 'fin',
      position: 'backend engineer',
    },
    {
      name: 'george',
      position: 'developer',
    },
  ];
  
  let developers = team.filter((member) => member.position == 'developer');
  
  console.log(developers);

  
//access the index property

let winners = ["Anna", "Beth", "Cara"]

let gold = winners.filter((winner, index) => index == 0)
let silver = winners.filter((winner, index) => index == 1)
let bronze = winners.filter((winner, index) => index == 2)

console.log(`Gold winner: ${gold}, Silver Winner: ${silver}, Bronze Winner: ${bronze}`)

// "Gold winner: Anna, Silver Winner: Beth, Bronze Winner: Cara"