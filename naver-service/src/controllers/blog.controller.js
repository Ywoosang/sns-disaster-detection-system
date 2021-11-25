const express = require('express')
const BlogData = require('../model/blogData.model');
const dateChecker = require('../utils/dateChecker');
const SearchDto = require('../dtos/serarch.dto');
const BlogService = require('../services/blog.service');
const Scheduler = require('../utils/schedule');

class BlogController{
    router = express.Router();
    constructor(){
        this.initializeRoutes();
        const scheduler = new Scheduler(this.saveBlogData);
        scheduler.run();
    }

    initializeRoutes(){
        this.router.get('/naver/data',this.getBlogData);
    }

    async getBlogData(req,res,next){
        try{
            // http://localhost:3001/api/naver/data?start=2021-11-24-01-01&end=2021-11-25-03-50 
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
    }
    async saveBlogData(){ 
        try{
            const keywords = ['폭설', '산불', '교통사고', '붕괴', '폭발', '폭발', '화재', '코로나', '홍수']
            for (let keyword of keywords) {
                const searchData = new SearchDto(keyword);
                const blogService = new BlogService(searchData);
                await blogService.saveData();
            };
        } catch(error){
            console.log(error);
        }
     }
}

module.exports = BlogController;