// Explain Spread an Rest Operator

// ==> Rest Parameters:

// The rest operator, also represented by three dots "...", is used to gather
// remaining elements in a function call or destructuring assignment. 

// When using rest arguments, you are collapsing all the remaining arguments
// of a function into one array

const sum = (first, ...rest) => { // rest parameter
    for (let i =0; i < rest.length; i++ )
        first += rest[i]
    
    return first
}
console.log(sum(1,2,3,4)) // output -> 10

// Rest parameters have to be at the last argument. 
// This is because it collects all remaining/excess arguments into an array

let [c,... rest] = [1,2,3,4,5,6,7] // rest -> [2,3,4,5]

// Here ...rest is a collector, it collects the rest of the parameters


// ==> Spread Operator

// The spread operator in JavaScript allows an iterable (such as an array or string)
// to be expanded into multiple elements

// When using spread we are expanding a single variable into more

var abc = ['a','b','c'];
var def = ['d','e','f'];
var alpha = [...abc, ...def]
console.log(alpha) // output -> ['a','b','c','d','e','f']


// We have been using arrays to demonstrate the spread operator, but any iterable also works.
// So if we had a string const str = 'testing', [...str] translate to ['t','e','s','t','i','n','g']



// Better Explained:

// The spread operator in JavaScript allows an iterable (such as an array or string) 
// to be expanded into multiple elements. For example, if you have an array called "fruits" 
// and you want to add another element to it, you can use the spread operator to add the new
//  element to a new array that includes all of the elements from the original array:


let fruits = ["apple", "banana"];
let newFruits = ["orange", ...fruits];
console.log(newFruits); // Output: ["orange", "apple", "banana"]



// The rest operator (also represented by three dots "...") is used to gather remaining elements
// in a function call. It allows you to represent an indefinite number of arguments as an array.
// For example:


function myFunction(first, second, ...others) {
  console.log(first); // Output: "apple"
  console.log(second); // Output: "banana"
  console.log(others); // Output: ["orange", "lemon"]
}

myFunction("apple", "banana", "orange", "lemon");


// The rest operator is used to gather all the remaining elements in the arguments list 
// and assign them to the variable "others" in this case.