const express = require('express');
const load_twitter = require('./controller/loadTwitterData.js')
const mongodb = require('./util/mongodb');
const toISO = require('./util/toISO');
const scheduler = require('./util/scheduler');
const app = express();
require('dotenv').config();
const db = mongodb.dbsetting();

function checkdate(req,res,next){
    var date_pattern = /^(19|20)\d{2}-([1-9]|0[1-9]|1[012])-([1-9]|0[1-9]|[12][0-9]|3[0-1])-([0-9]|0[0-9]|1[0-9]|2[0-3])-([0-9]|0[0-9]|[12345][0-9])$/; 

    if (date_pattern.test(req.query.start) && date_pattern.test(req.query.end)) {
        next();
    } else {
        res.status(301).send({"msg":"잘못된 접근입니다.","start":req.query.start,"end":req.query.end})
    }
}

app.get('/api/twitter/data/',checkdate,async function(req,res){
    try{
        const StartTime = req.query.start.split('-') //여기에 타임에 관한 정보를 넣어주세요
        const EndTime = req.query.end.split('-') 
        const firstTime = toISO.toISO(StartTime);
        const lastTime = toISO.toISO(EndTime);
        const response = []
        const cursor = db.collection('twitter_data').find({date : { $gte:firstTime,$lte:lastTime}});
        while (await cursor.hasNext()) { // Iterate entire data
            const doc = await cursor.next(); // Get 1 Document
            const dToj = {
                 sns: doc.sns,
                 content : doc.content,
                 link : doc.link,
                 keyword :doc.class,
                 date : toISO.toArr(doc.date),
                 service : doc.service
    
            }
            response.push(dToj);
            console.log(dToj);
        }
        if(response.length == 0){
            res.status(400).json({"msg":"no data"})
        }
        else{
            res.send(response)
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

/*
app.post('/api/twitter/data',async function(req,res){

    var keywords = [['폭설','폭설 내려'],['산불','산불 발생'],['교통사고','교통사고 발생'],['붕괴','붕괴 사고'],['폭발','폭발 발생'],['화재','화재 발생'],['코로나','코로나 확진'],['홍수','홍수 발생']]
    
    for(var i = 0 ; i<keywords.length;i++){
        await load_twitter.upload(keywords[i][0],keywords[i][1]);
    }
    
    res.send('success')
});

*/
