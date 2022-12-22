// interview Promise example

const myPromise = new Promise((resolve, reject) => {
  const condition = true
  if(condition){
    setTimeout(() => {
      resolve("promise is resolved")
    },5000)
  }else{
    reject("promise is rejected")
  }
})

myPromise
.then((msg) => console.log(msg))
.catch((err) => console.log(err))