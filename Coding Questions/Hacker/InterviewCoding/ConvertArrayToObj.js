// Way to convert arrray to object

console.log(Object.assign({}, ["a", "b", "c"])); // {0:"a", 1:"b", 2:"c"}

// Second way

console.log({ ...["a", "b", "c"] }); // {0:"a", 1:"b", 2:"c"}

// Third way

console.log(["a", "b", "c"].reduce((a, v) => ({ ...a, [v]: v }), {}));
// { a: "a", b: "b", c: "c" }

// Fourth way

const arr = ["a", "b", "c"].reduce(function (result, item, index, array) {
  result[index] = item; //a, b, c
  return result;
}, {}); //watch out the empty {}, which is passed as "result"

console.log(arr);
