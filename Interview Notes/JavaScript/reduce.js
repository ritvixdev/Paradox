//Interview example for reduce

//reducers take a callback function and initial value

const numbers = [1,2,3,4,5,6,7]

const sumOfNum = numbers.reduce((acc, cur) => acc + cur, 0)
console.log(sumOfNum) //28


//Summing Values in an Object Array Using Array Reduce JavaScript

let initialValue = 0

let obj = [{n: 5}, {n: 9}, {n: 13}, {n: 25}, {n: 40}]

let sum = obj.reduce((accumulator, curValue) => {

    return accumulator + curValue.n

}, initialValue)

console.log(sum) //92


//Flattening an Array of Arrays With Reduce Method

let mulArray = [[3, 5], [1, 7], [12, 9]]

let newArr = mulArray.reduce((accumulator, curValue) => {

    return accumulator.concat(curValue)

},[])

console.log(newArr)


//Counting Instances in an Object Using Array Reduce in JavaScript

let myCars = [
    'Mercedes-Benz',
    'Jeep',
    'Ferrari',
    'Lamborghini',
    'Mercedes-Benz',
    'BMW',
    'Ferrari',
  ];
  
  let instances = myCars.reduce((allCars, car) => {
    if (car in allCars) {
      allCars[car]++;
    } else {
      allCars[car] = 1;
    }
    
    return allCars;
  }, {});
  
  console.log(instances);
  

//Removing Duplicates With Array Reduce

let array = [2, 5, 7, 5, 12, 9, 7, 5, 4, 3, 5, 2, 4, 15];

let newArray = array.reduce(function (accumulator, curValue) {
  if (accumulator.indexOf(curValue) === -1) {
    accumulator.push(curValue);
  }

//   if (!accumulator.includes(curValue)) {
//     accumulator.push(curValue);
//   }

  return accumulator;
}, []);

console.log(newArray);