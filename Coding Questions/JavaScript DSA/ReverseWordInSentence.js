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


// without using build in method split

str = 'there is a man in the world';

const rev1 = (word) => {
  let rev = '';
  for (let i = 0; i <= word.length - 1; i++) {
    rev = word[i] + rev;
  }
  return rev;
};

const splitWord = (str) => {
  words = []
  idx= 0
  temp = ''
  for(let i=0;i<=str.length-1;i++){
    if(str[i] != ' '){
      temp = temp+str[i]
    }else{
      words[idx++] = temp
      temp =''
    }
  }
  return words
}

const operations = (str) => {
  let word = splitWord(str);
  let res = [];
  for (let i = 0; i <= word.length - 1; i++) {
    if (word[i].length > 3) {
      word[i] = rev1(word[i]);
    }
  }
  return word;
};

console.log(operations(str));

