// Way to convert Javacript Object to array

// Best Way
var obj = {"1":5,"2":7,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0}
var result = Object.entries(obj);

console.log(result);

// Second way

var obj = {"1":5,"2":7,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0}
var result = Object.keys(obj).map((key) => [Number(key), obj[key]]);

console.log(result);

