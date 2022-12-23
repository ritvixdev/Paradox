//interview map example

//Syantax
//arr.map(function(element, index, array){  }, this);

let arr = [3, 4, 5, 6];

let modifiedArr = arr.map((element) => {
    return element *3;
});

console.log(modifiedArr); // [9, 12, 15, 18]

//Map over an array of objects

let users = [
    {firstName : "Susan", lastName: "Steward"},
    {firstName : "Daniel", lastName: "Longbottom"},
    {firstName : "Jacob", lastName: "Black"}
  ];
  
  let userFullnames = users.map((element) => {
      return `${element.firstName} ${element.lastName}`;
  })
  
  console.log(userFullnames); // ["Susan Steward", "Daniel Longbottom", "Jacob Black"]

//Map example with this

let array = [2, 3, 5, 7]

array.map(function(element, index, array){
	console.log(this) // 80
}, 80);

//


