// Interview Example for Higher Order Functions

//Pass function as an argument to another function

//array of names to be used in the function
const names= ['John', 'Tina','Kale','Max']

//Function using function fn as a parameter
function useFunction(arr,fn){
  for(let i=0; i<arr.length; i++){
    fn(arr[i]);
  }
}                                

//Function that is being used as a parameter
function argFn (name){
  console.log("Hello " + name );
}

//calling useFunction() with argFn() as a parameter
useFunction(names,argFn);

/*Result printed:
   Hello John
   Hello Tina
   Hello Kale
   Hello Max
*/

// HOF Definition:

// Basically, a function which takes another function as an argument or returns 
// a function is known as a higher order function.

// The functions that use other functions as arguments or return functions are named higher-order functions.