var express = require('express');
var mongoose = require('mongoose');
const load_naver = require('./controller/loadNaverData.js')
const mongodb = require('./src/mongodb');
const toISO = require('./src/toISO');
var app = express();

// 1. 첫번째 (db 에 아무것도 없는 경우- 가장 마지막 date 에 넣어진 것이 없으면) -> 2021-11-11-11-11 이후것들을 db 에 저장한다
// 2. 두 번째 
//   - db 에 마지막으로 저장된 (date 값이 가장 큰것) 의 date 를 불러온다
//   - 엔드포인트 post /api/twitter/data   그 이후부터 게시물을 크롤링 하고 db 에 저장
//   - 엔드포인트 get /api/twitter/data 프론트엔드에서 받은 날짜 이후 데이터를 조회

//mongoose.connect(mongodb.dbURL);
var db = mongodb.dbsetting()


 app.post('/api/naver/data',function(req,res){
     //첫번째게 키워드로 저장될 것, 두번째게 실제로 검색할 것
    var keywords = [['폭설','폭설'],['산불','산불'],['교통사고','교통사고'],['붕괴','붕괴'],['폭발','폭발'],['화재','화재'],['코로나','코로나 확진'],['홍수','홍수']]

    db.collection('naver_data').findOne({}, {sort:{$natural:-1}})
    .then(async (lastData)=>{
        var cur;
        if(!lastData){
            cur = '2021-11-11T00:00:00.000Z'
        }
        else{
            cur = lastData.date
        }
         
        return cur;
       
    })
    .then(async (lastTime)=>{
        var curTime = new Date().toISOString();
        for(var i = 0 ; i<keywords.length;i++){
            await load_naver.upload(keywords[i][0],keywords[i][1]);
        }
    }).then(()=>{
        res.send('success')
    })
    .catch((err)=>{console.log(err)})
});


app.get('/api/naver/data/1',async function(req,res){
   var response = [];
    var cursor = await db.collection('naver_data').find({date : { $gte:'2021-11-11T00:00:00.000Z'}});
    
    while (await cursor.hasNext()) { // Iterate entire data

        var doc = await cursor.next(); // Get 1 Document
        var dToj = {
            content : doc.content,
            link : doc.link,
            type:doc.type
        }
        await response.push(dToj);
        console.log(dToj);

    }

    res.send(response)


});

app.get('/api/naver/data/',async function(req,res){
    var TimeData = ['2021','11','11','22','05'] //여기에 타임에 관한 정보를 넣어주세요
    var lastTime = toISO.toISO(TimeData);
    var response=[];
    var cursor = await db.collection('naver_data').find({timestamp : { $gte:lastTime}});
    
    while (await cursor.hasNext()) { // Iterate entire data

        var doc = await cursor.next(); // Get 1 Document
        var dToj = {
            content : doc.content,
            link : doc.link,
            type:doc.type
        }
        await response.push(dToj);
        console.log(dToj);

    }

    await res.send(response)


});

app.listen(process.env.NAVER_PORT, function (){
    console.log('app listening on port 3001!');
});
