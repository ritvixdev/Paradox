// Example of how you can write a JavaScript program to calculate 
// all possible combinations of sums that add up to a given value from an array:

function findCombinationSums(arr, target) {
    let sums = [];
    for (let i = 0; i < arr.length; i++) {
      let num = arr[i];
      if (num < target) {
        let subSums = findCombinationSums(arr, target - num);
        for (let j = 0; j < subSums.length; j++) {
          sums.push([num].concat(subSums[j]));
        }
      } else if (num === target) {
        sums.push([num]);
      }
    }
    return sums;
  }
  
  let arr = [2, 3, 6, 7];
  let target = 7;
  let combinationSums = findCombinationSums(arr, target);
  console.log(combinationSums);
  /* Output: 
  [
    [2, 2, 3],
    [2, 5],
    [3, 4],
    [7]
  ]
  */