const express = require('express');
const BlogService = require('./services/blog.service');
const BlogData = require('./model/blogData.model');
const mongoose = require('mongoose');
const SearchDto = require('./dtos/serarch.dto');
const dateChecker = require('./utils/dateChecker');
require('dotenv').config();
// 1. 첫번째 (db 에 아무것도 없는 경우- 가장 마지막 date 에 넣어진 것이 없으면) -> 2021-11-11-11-11 이후것들을 db 에 저장한다
// 2. 두 번째 
//   - db 에 마지막으로 저장된 (date 값이 가장 큰것) 의 date 를 불러온다
//   - 엔드포인트 post /api/twitter/data   그 이후부터 게시물을 크롤링 하고 db 에 저장
//   - 엔드포인트 get /api/twitter/data 프론트엔드에서 받은 날짜 이후 데이터를 조회

//mongoose.connect(mongodb.dbURL);
const app = express();

mongoose.connect('mongodb://naver-db:27017/moai');
const db = mongoose.connection;
db.on('error', function () {
    console.log('Connection Failed!');
});
db.once('open', function () {
    console.log('Connected!');
});


app.post('/api/naver/data', async (req, res, next) => {
    try {
        const keywords = ['폭설', '산불', '교통사고', '붕괴', '폭발', '폭발', '화재', '코로나', '홍수']
        for (let keyword of keywords) {
            const searchData = new SearchDto(keyword);
            const blogService = new BlogService(searchData);
            await blogService.saveData();
        };
        return res.status(201).json({
            msg : '생성'
        });

    } catch (error) {
        next(error);
    }
});

app.get('/api/naver/data', async function (req, res,error) {
    try{
        const startDate = req.query.start;
        const endDate = req.query.end;
        // http://localhost:3001/api/naver/data?start=2021-11-24-01-01&end=2021-11-25-03-50
        const isDateFormat = dateChecker(startDate) && dateChecker(endDate);
        if(!isDateFormat) return res.status(400).json({
            message : 'Bad Request'
        });
        console.log(startDate,endDate);
        const response = await BlogData.find()
        .where('date').gt(startDate)
        .where('date').lte(endDate);
        res.json({
            response
        });
    }catch(error){
         next(error)
    }
});

app.get('/api/naver/test', async function (req, res,error) {
    try{
        const response = await BlogData.find()
        res.json({
            response
        });
    }catch(error){
         next(error)
    }
});

app.use((error, req, res, next) => {
    console.log(error);
    res.status(200).json({
        error
    })
});

console.log('포트 ---------------',process.env)
app.listen(3001, function () {
    console.log(`app listening on port ${process.env.NAVER_PORT}`);
});
