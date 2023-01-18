// Prototype in javascript

// Every object in JavaScript has a built-in property, which is called its prototype. 
// The prototype is itself an object, so the prototype will have its own prototype, 
// making what's called a prototype chain. The chain ends when we reach a prototype 
// that has null for its own prototype.


// JavaScript is a prototype based language, so, whenever we create a function using JavaScript,
// JavaScript engine adds a prototype property inside a function, Prototype property is basically
// an object (also known as Prototype object), where we can attach methods and properties in a
// prototype object, which enables all the other objects to inherit these methods and properties.

// Createing new object

const obj = new Object ({
    name: 'Ash'
})

const obj2 = new obj2();

const obj3 = {
    name: 'Ash'
}

// Array and fucntion are using Prototype

// object itself provides some properties thats call prototype

// Example:

const obj4={
    name:'Ash',
    getName: function(){
        return this.name
    }
}
console.log(obj4)

const obj5={
    roll: 1,
    __proto__:obj4 // obj4 is send as a prototype in obj5
}
console.log(obj4.name) // Ash
console.log(obj4.getName()) // Ash
console.log(obj4)