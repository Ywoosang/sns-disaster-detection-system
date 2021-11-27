const express = require('express');
const load_twitter = require('./controller/loadTwitterData.js')
const get_twitter = require('./controller/getTwitterData.js')
const scheduler = require('./util/scheduler');
const app = express();
require('dotenv').config();


function checkdate(req,res,next){
    var date_pattern = /^(19|20)\d{2}-([1-9]|0[1-9]|1[012])-([1-9]|0[1-9]|[12][0-9]|3[0-1])-([0-9]|0[0-9]|1[0-9]|2[0-3])-([0-9]|0[0-9]|[12345][0-9])$/; 

    if (date_pattern.test(req.query.start) && date_pattern.test(req.query.end)) {
        next();
    } else {
        res.status(301).send({"msg":"잘못된 접근입니다.","start":req.query.start,"end":req.query.end})
    }
}

app.get('/api/twitter/data',checkdate,async function(req,res){
    try{
        var response = await get_twitter.download(req.query.start,req.query.end);
        if(response.length == 0){
            res.status(400).json({"msg":"no data"})
        }
        else{
            res.json({
                'data': response
            })
        }
        
    }
    catch(err){
        console.log(err);
    }
   
});

app.listen(process.env.TWITTER_PORT, function (){
    console.log('app listening on port '+ process.env.TWITTER_PORT.toString()+'!');
    scheduler.scheduler.start();
});




