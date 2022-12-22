//interview forEach exapmple

const arr = ['a', 'b','c','d','e','f','g']

arr.forEach((element, index, array) => {
    console.log(`${element} in index ${index} of array ${array}`)
})

// The forEach method passes a callback function for each element of an array together with the following parameters:

// Current Value (required) - The value of the current array element
// Index (optional) - The current element's index number
// Array (optional) - The array object to which the current element belongs