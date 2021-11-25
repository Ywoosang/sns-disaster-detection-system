const axios = require('axios');
const keywordFiler = require('../utils/keywordFilter');
const toDateFormat = require('../utils/toDateFomat');
const BlogDao = require('../daos/blog.dao');
const BlogDataDto = require('../dtos/blog.dto');
const BlogData = require('../model/blogData.model');
const KoreanTime = require('../utils/koreanTime');
require('dotenv').config()

class BlogService{
    constructor(serarchDto){
        this.keyword = keywordFiler(serarchDto.getKeyword());
    }
    // NaverAPI 에서 받은 블로그 게시글들 반환
    async getKeywordData(){
        // date  기준으로 sort 해서 50개씩 가져온다.

        const options = {
            headers: {
                'X-Naver-Client-Id':process.env.NAVER_CLIENT, 
                'X-Naver-Client-Secret': process.env.NAVER_CLIENT_SECRET
            },
            // 키워드 기준 데이터 50개 끊어서 가져온다.
            params: {
                query: this.keyword,
                display: 20,
                sort : 'date'
            }
        }
        // openAPI 결과
        const result = await axios.get('https://openapi.naver.com/v1/search/blog',options);
        const items =  result.data.items;
        return items.map(item => {
            const content = item.title.replace("<b>","").replace("</b>","") + item.description.replace("<b>","").replace("</b>","")
            const link = item.link;
            // 포맷 변경
            const koreanTime = new KoreanTime();
            console.log(koreanTime.getHours(),koreanTime.getMinutes())
            const date = `${toDateFormat(item.postdate)}-${koreanTime.getHours()}-${koreanTime.getMinutes()}`;
            return new BlogDataDto(content,link,date,this.keyword);
        });
    }
    // 
    async saveData() {
        const recentData = await BlogData.findOne({},{}, { sort: { 'date': -1 }})
        if(recentData){
            const recentDate = recentData.date;
            console.log('최근',recentDate); 
        }
        //
        const keywordDataSet = await this.getKeywordData();
        for(const blogData of keywordDataSet){
            const blogDao = new BlogDao();
            await blogDao.create(blogData) 
        }
    }
}

module.exports = BlogService;

// async function getNaverDataDetail(url){
//     var detail= await axios.get(url);
//     console.log(detail.data)
// };
