// Reverse words in a sentense whose word length is more than 3 letters

str = 'there is a man in the world';

const rev = (word) => {
  let rev = '';
  for (let i = 0; i <= word.length - 1; i++) {
    rev = word[i] + rev;
  }
  return rev;
};

const operation = (str) => {
  let word = str.split(' ');
  let res = [];
  for (let i = 0; i <= word.length - 1; i++) {
    if (word[i].length > 3) {
      word[i] = rev(word[i]);
    }
  }
  return word;
};

console.log(operation(str)); // [ 'ereht', 'is', 'a', 'man', 'in', 'the', 'dlrow' ]

