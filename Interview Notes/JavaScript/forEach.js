//interview forEach exapmple

const array = ['a', 'b','c','d','e','f','g']

array.forEach((item, index, array) => {
    console.log(`${item} in index ${index} of array ${array}`)
})


const arr = ['John', 'Sara', 'Jack', 'Andy', 'Paty'];

arr.forEach((item, index, array) => {
  array[index] = 'Hello ' + item;
})

console.log(arr)

// The forEach method passes a callback function for each element of an array together with the following parameters:

// Current Value (required) - The value of the current array element
// Index (optional) - The current element's index number
// Array (optional) - The array object to which the current element belongs