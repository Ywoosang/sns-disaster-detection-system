var mongoose = require('mongoose');

var dbURL = 'mongodb://localhost:27017/moai'
exports.dbsetting = function(){
    mongoose.connect(dbURL);
    var db = mongoose.connection;
    db.on('error', function(){
    console.log('Connection Failed!');
    });

    db.once('open', function() {
        console.log('Connected!');
    });
    return db;
}



