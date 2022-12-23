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


// by Async/Await

const myPromises = () => {
  return new Promise((resolve, reject) => {
  const condition = true
  if(condition){
    setTimeout(() => {
      resolve("promise is resolved")
    },1000)
  }else{
    reject("promise is rejected")
  }
})
}

const demoPromise = async () => {
  try{
    const msg = await myPromises();
    console.log(msg)
  }catch(err){
    console.log(err)
  }
}

demoPromise()

