// BASE SETUP
// =============================================================================

// call the packages we need
var express    = require('express');        // call express
var app        = express();                 // define our app using express
var bodyParser = require('body-parser');


var mongoose   = require('mongoose');
mongoose.connect('mongodb://localhost:27017/local'); // connect

var Order     = require('./models/order'); 
// configure app to use bodyParser()
// this will let us get the data from a POST
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var port = process.env.PORT || 8080;        // set our port

// ROUTES FOR OUR API
// =============================================================================
var router = express.Router();              // get an instance of the express Router

// test route to make sure everything is working (accessed at GET http://localhost:8080/api/PaloAlto)
router.get('/', function(req, res) {
    res.json({ message: 'hooray! welcome to Palo Alto!' });   
});

// more routes for our API will happen here

// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api/PaloAlto
app.use('/api/PaloAlto', router);

// START THE SERVER
// =============================================================================
app.listen(port);
console.log('Magic happens on port ' + port);

var router = express.Router();              // get an instance of the express Router

// middleware to use for all requests
router.use(function(req, res, next) {
    // do logging
    console.log('Something is happening.');
    next(); // make sure we go to the next routes and don't stop here
});

// test route to make sure everything is working (accessed at GET http://localhost:8080/api/PaloAlto)
router.get('/', function(req, res) {
    res.json({ message: 'hooray! welcome to Palo Alto!' });   
});

// more routes for our API will happen here

// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api/PaloAlto
app.use('/api/PaloAlto', router);



// ROUTES FOR OUR API
// =============================================================================

 // <-- route middleware and first route are here

// more routes for our API will happen here

// on routes that end in /orders
// ----------------------------------------------------
router.route('/orders')

    // create a order (accessed at POST http://localhost:8080/api/PaloAlto/orders)
    .post(function(req, res) {
        
        var order = new Order();      // create a new instance of the Order model


        order.location = req.body.location;  // set the ordered qty (comes from the request)



        // save the order and check for errors
        order.save(function(err) {
            if (err)

                res.send(err);
            res.status(200).end('No Errors.');
            res.json({ message: 'Order created!' });
        });
        
    });

// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api
app.use('/api/PaloAlto', router);



// ROUTES FOR OUR API
// =============================================================================

 // <-- route middleware and first route are here

// more routes for our API will happen here

// on routes that end in /orders
// ----------------------------------------------------
router.route('/orders')

    // create a order (accessed at POST http://localhost:8080/api/PaloAlto/orders)
    .post(function(req, res) {
        
        
        
    })

    // get all the orders (accessed at GET http://localhost:8080/api/PaloAlto/orders)
    .get(function(req, res) {
        Order.find(function(err, orders) {
            if (err)
                res.send(err);

            res.json(orders);
        });
    });

// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api/PaloAlto
app.use('/api/PaloAlto', router);

// on routes that end in /bears
// ----------------------------------------------------
router.route('/orders')
 



// ROUTES FOR OUR API
// =============================================================================

 // <-- route middleware and first route are here

// more routes for our API will happen here

// on routes that end in /orders
// ----------------------------------------------------
router.route('/orders')

    // create a order (accessed at POST http://localhost:8080/api/PaloAlto/orders)
    .post(function(req, res) {
        
        
        
    })

    // get all the orders (accessed at GET http://localhost:8080/api/PaloAlto/orders)
    .get(function(req, res) {
        Order.find(function(err, orders) {
            if (err)
                res.send(err);

            res.json(orders);
        });
    });

// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api
app.use('/api/PaloAlto', router);




// on routes that end in /orders
// ----------------------------------------------------
router.route('/orders')
 

// on routes that end in /orders/:order_id
// ----------------------------------------------------
router.route('/orders/:order_id')

    // get the order with that id (accessed at GET http://localhost:8080/api/orders/:order_id)
    .get(function(req, res) {
        Order.findById(req.params.order_id, function(err, orders) {
            if (err)
                res.send(err);
            res.json(orders);
        });
    });

// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api
app.use('/api/PaloAlto', router);

router.route('/orders')


// on routes that end in /orders/:order_id
// ----------------------------------------------------
router.route('/orders/:order_id')

    // get the order with that id (accessed at GET http://localhost:8080/api/orders/:order_id)
    .get(function(req, res) {
   
    })

    // update the order with this id (accessed at PUT http://localhost:8080/api/orders/:order_id)
    .put(function(req, res) {

        // use our order model to find the order we want
        Order.findById(req.params.order_id, function(err, bear) {

            if (err)
                res.send(err);

            order.name = req.body.name;  // update the orders info

            // save the bear
            order.save(function(err) {
                if (err)
                    res.send(err);

                res.json({ message: 'Order updated!' });
            });

        });
    });

// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api
app.use('/api', router);





// on routes that end in /bears/:bear_id
// ----------------------------------------------------
router.route('/orders/:order_id')

    // get the bear with that id (accessed at GET http://localhost:8080/api/bears/:bear_id)
    .get(function(req, res) {
       
    })

    // update the bear with this id (accessed at PUT http://localhost:8080/api/bears/:bear_id)
    .put(function(req, res) {
       
    })

    // delete the order with this id (accessed at DELETE http://localhost:8080/api/PaloAlto/orders:order_id)
    .delete(function(req, res) {
        Order.remove({
            _id: req.params.order_id
        }, function(err, orders) {
            if (err)
                res.send(err);

            res.json({ message: 'Successfully deleted' });
        });
    });

// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api
app.use('/api', router);




