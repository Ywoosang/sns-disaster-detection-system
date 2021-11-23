var mongoose = require('mongoose');

exports.dbsetting = function(){
    mongoose.connect('mongodb://twitter-db:27017/moai', {useUnifiedTopology : true, useNewUrlParser: true});
    var db = mongoose.connection;
    db.on('error', function(){
    console.log('Connection Failed!');
    });

    db.once('open', function() {
        console.log('Connected!');
    });
    return db;
}

exports.data = new mongoose.Schema({
    content : 'string',
    date : 'string',
    link : 'string',
    type : 'string'

});

