//  find all the anagrams within a series of words

// Object.values

const arr = ['monk', 'konm', 'nkom', 'bbc', 'cbb', 'dell', 'ledl', 'llde'];
let anagram = {};

for (let i = 0; i < arr.length; i++) {
  const word = arr[i];
  const sortedWord = word.split('').sort().join('');
  let tempArray = [];
  if (anagram[sortedWord]) {
    tempArray =
      anagram[sortedWord].length == 1
        ? anagram[sortedWord]
        : [...anagram[sortedWord]];
    tempArray.push(word);
    anagram[sortedWord] = tempArray;
  } else {
    anagram[sortedWord] = [word];
  }
}
console.log(Object.values(anagram));

  

// reduce

arr = ['kmno', 'okmn', 'omkn', 'dell', 'ledl', 'ok', 'ko']

const group_anagrams = (arr) => {
    let   sortedArr = arr.map(item => item.split('').sort().join(''));
    let setArr = new Set(sortedArr);
    let reducedObj = {};
    for (let setItem of setArr) {
      let indexArr = sortedArr.reduce((acc, cur, index) => {
        if (setItem === cur) {
          acc.push(index);
        }
        return acc;
      }, []);
      reducedObj[setItem] = indexArr;
    }
    let finalArr = [];
    for (let reduceItem in reducedObj) {
      finalArr.push(reducedObj[reduceItem].map(item => arr[item]));
    }
    return finalArr;
  }
  console.log(group_anagrams(arr));
  


// hasOwnProperty

arr = ['kmno', 'okmn', 'omkn', 'dell', 'ledl', 'ok', 'ko']

function anagram (array) {
  var organized = {};
  for (var i = 0; i < array.length; i++) {
      var word = array[i].split('').sort().join('');
      if (!organized.hasOwnProperty(word)) {
          organized[word] = [];
      }
      organized[word].push(array[i]);
  }    
  return organized;
}


console.log(anagram(arr))