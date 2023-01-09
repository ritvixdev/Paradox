// Write a function that takes in a string and returns the first non-repeated character in the string.

str = "abbdcdkaceolol"

const firstChar = (str) => {
  let temp = {}
  for(let i=0;i<=str.length-1;i++){
    if(!temp[str[i]]){
      temp[str[i]] = 1
    }else{
      temp[str[i]]++
    }
  }

  for(let i=0;i<=str.length-1;i++){
    if(temp[str[i]] == 1){
      return str[i]
    }
  }

  return null
}

console.log(firstChar(str))