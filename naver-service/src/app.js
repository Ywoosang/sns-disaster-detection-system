const express = require('express');
const mongoose = require('mongoose');
const Scheduler = require('./utils/schedule');
require('dotenv').config();

mongoose.connect('mongodb://naver-db:27017/moai');
const db = mongoose.connection;
db.on('error', function () {
    console.log('Connection Failed!');
});
db.once('open', function () {
    console.log('Connected!');
});

class App{
    constructor(port,controllers){
        this.app = express();
        this.port = port;
        this.initializeMiddlewares(controllers);
    }

    initializeMiddlewares(){
        this.app.use((error, req, res, next) => {
            console.log(error);
            res.status(200).json({
                error
            })
        });
    }

    initializeRoutes(controllers){
        controllers.forEach(controller => {
            this.app.use('/api',controller.router);
        });
    }

    listen(){
        this.app.listen(this.port,()=>{
            console.log(`app listening on port ${this.port}`);
        })
    }
}

module.exports = App;
