// Products API Medium

// example of a trade data JSON Object:
[
  {
    id: 1,
    name: "premium R coffee",
    price: 1.19,
    mrp: 1.19,
    stock: 1,
    isPublished: false,
  },
];

// The task is to impliment the REST service that exposes the /product endpoint, which allows for managing
// the collectioon of product

// Folder: routes, File: product.js

const router = requie('express').Router()
const controller = require('../controllers/products')

// creating Router; api end point is /product; inside controller we define method - createProduct 
router.post('/products', controller.createProduct);
router.get('/products', controller.getAllProducts);
router.get('/products/:id', controller.getProductById);
router.patch('/products/:id', controller.patchProductById);
router.put('/products/:id', controller.createProduct);
router.delete('/products/:id', controller.updateProductById); // :id - path parameter


module.exports = router

// Folder: controllers; File: product.js

const ProductModel = require('../model/products')
const {Op} = require("sequelize");

class ProductController {

    async createProduct(req, res){
        try{
            const {body} = req;
            // get existing length of the data presem=nt in database
            const data = await ProductModel.findAll({})// finding all empty object
            body.id = data.length + 1; // if item is empty we will asign the ID - 1
            body.isPublished = false; // mentioned in Q
            const response =  await ProductModel.create(body);
            res.status(201).json(response)
        }catch(err){
            throw new Error(err.message)
        }
    }

    updateProductById(req, res) {
        res.status(405).json({ message: "Not allowed" })
    }

    async getAllProducts(req, res){
        try{
            
            // get existing length of the data presem=nt in database
            const data = await ProductModel.findAll({})// finding all empty object
            // we are just returning the data
            res.status(201).json(data)
        }catch(err){
            throw new Error(err.message)
        }
    }

    async patchProductById(){
        // validation criteria
        const {id} = req.params;
        const {body} = req;
        //validate the id reallr exists in the database or not
        const data = await ProductModel.findOne({where: {id}});
        if(!data) {
            res.status(404).send()
            return
        }
        // if we have a data
        const {price, mrp, stock} = data;
        if(mrp < price && stock == 0){
            res.status(422).send([])
        }else if(mrp < price){
            res.status(422).send([])
        }else if(stock === 0){
            res.status(422).send([])
        }else{
            await ProductModel.update({isPublished: true}, {where:{id}})
        }
    }
}

module.export = new ProductController()


