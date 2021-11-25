const mongoose = require('mongoose');

exports.db = () => {
    mongoose.connect('mongodb://naver-db:27017/moai');
    const db = mongoose.connection;
    db.on('error', function(){
    console.log('Connection Failed!');
    });
    db.once('open', function() {
        console.log('Connected!');
    });
    return db;
}

