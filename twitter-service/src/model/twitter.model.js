const mongoose = require('mongoose')

var twitterDataSchema = new mongoose.Schema({
    'content' : 'string',
    'sns' : 'string',
    'date':'string',
    'link' : 'string',
    'keyword' : 'string',
    'service': 'string'

},{
    collection: 'twitter_data'
});

module.exports = mongoose.model('naver_data',twitterDataSchema);