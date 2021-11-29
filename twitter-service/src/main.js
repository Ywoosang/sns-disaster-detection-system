const express = require('express');
const load_twitter = require('./controller/loadTwitterData.js')
const get_twitter = require('./controller/getTwitterData.js')
const scheduler = require('./util/scheduler');
const cors = require('cors')
const app = express();
const mongodb = require('./util/mongodb');
const db = mongodb.dbsetting();
const TwitterData = require('./model/twitter.model');
app.use(cors())
require('dotenv').config();


const dateChecker = (dateTime) => {
    const dateArr = dateTime.split('-');
    if(dateArr.length !== 5) return false;
    const [year,month,date,hour,min] = dateArr;
    // 자리수 확인
    const condition = year.length == 4 && month.length == 2 && date.length == 2 && hour.length == 2 && min.length == 2;
    if(!condition) return false;
    // 숫자인지 확인
    for(let item of [year,month,date,hour,min]){
        if(isNaN(item)) return false;
    }
    return true;
}

app.get('/api/twitter/data',async function(req,res){
    try{
        const startDate = req.query.start;
        const endDate = req.query.end;
        console.log('Twitter:Request Received')
        const isDateFormat = dateChecker(startDate) && dateChecker(endDate);
        if(!isDateFormat) return res.status(400).json({
            message : 'Bad Request'
        });
        let response = await get_twitter.download(startDate,endDate);
        if(response.length == 0){
            res.json({"data":[]})
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

app.get('/api/twitter/ping',async function(req,res){
    try{
        const dataset = await TwitterData.find().sort({ "date" : -1 }).limit(20);
        const response = [];
        for(let data of dataset){
            response.push({
                content: data.content,
                keyword: data.keyword,
                date: data.date,
                link: data.link,
                service: data.service
            })
        }
        res.json({
            'data' : response
        });
    }
    catch(err){
        console.log(err);
    }   
});

app.listen(process.env.TWITTER_PORT, function (){
    console.log('app listening on port '+ process.env.TWITTER_PORT.toString()+'!');
    scheduler.scheduler.start();
});




