// Javascript programm to split words form sentence

let sentence = 'This is a sample sentence.';

const splitIntoWords = (sentence) => {
  let words = [];
  let word = '';
  for (let i = 0; i < sentence.length; i++) {
    if (sentence[i] === ' ') {
      words.push(word);
      word = '';
    } else {
      word += sentence[i];
    }
  }
  words.push(word);
  return words;
};

console.log(splitIntoWords(sentence));// [ 'This', 'is', 'a', 'sample', 'sentence.' ]
