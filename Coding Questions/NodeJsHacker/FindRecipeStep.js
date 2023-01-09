// file app.js

app.use('/', indexRouter);
app.use('/recipes/step/', recipeRouter)

// Given Info:

// recipe/step/:id?elapsedTime
// Example:
// /recipe/step/4?elapsedTime=11
// output - {index: 0}

// file routes

var recipes = require('../recipe.json')
var router = require('express').Router();


function getIndex(timers, elapsedTime){
    for(let i=0;i<=timers.length-1; i++){
        if(timers[i] >= elapsedTime){
            return i;
        }
    }
}

router.get('/:id', (req,res) => {
    const id = req.params.id;
    const elapsedTime = req.query.elapsedTime || 0; // if query parameter is not present default would be 0

    if(isNaN(id)){ // if Id passed is URL is mssing or not a Valid Number
        res.status(400).send('NOT_FOUND'); // response with code 400 and sting NOT_FOUND 
    }

    const selectedRecipe = recipes.filter(i => {
        return i.id === Number(id)
    })[0];

    if(selectedRecipe) {
        const {timers} = selectedRecipe
        const index  = getIndex(timers, elapsedTime);
        res.status(200).send({index})
    }else{
        res.status(404).send('NOT_FOUND')
    }
})

module.exports = router;


// Extra information:


// ==> request.params:

// Suppose you have defined your route name like this:
// https://localhost:3000/user/:userId

// which will become:
//https://localhost:3000/user/5896544


// Here, if you will print: request.params

// {
// userId : 5896544
// }

// request.params.userId = 5896544
// so request.params is an object containing properties to the named route

// ==> request.query

// The request.query comes from query parameters in the URL eg:

// https://localhost:3000/user?userId=5896544 

// request.query 

// {
// userId: 5896544
// }

// request.query.userId = 5896544