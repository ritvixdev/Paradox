// Interview exapmple for call(), apply(), bind()

// call()

const obj = {
  name: "peter",
};

function sayHello(greet, msg) {
  console.log(`${greet} ${this.name} ! ${msg}`);
}

sayHello.call(obj, "Hello", "Good Morning"); // Hello peter ! Good Morning

// apply()

sayHello.apply(obj, ["Hello", "Good Morning"]); // Hello peter ! Good Morning

// bind()

const obj1 = { name: "peter" };

function sayHello(greet) {
  console.log(`${greet} ${this.name}`);
}

const newFunc1 = sayHello.bind(obj1, "Hello");
newFunc1(); // Hello peter

// bind() another example of calling

const newFunc2 = sayHello.bind(obj1);
newFunc2("Hello"); // Hello peter



// Definition

// ===> call()

// The call method binds the this value to the function and executes the function.
// It takes the this value and a list of arguments as parameters. 
// Then, it returns the value returned by the function, which is called using the call method.

// ===> apply()

// The apply method binds the this value to the function and executes the function.
//  It takes the this value and a single array object as parameters, 
//  and it returns the value returned by the function, which is called using the apply method.

// ===> bind()

// The bind method binds the this value to the function and returns a new function. 
// However, we still need to separately invoke the returned function.
