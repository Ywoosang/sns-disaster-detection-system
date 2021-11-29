const axios = require('axios');
const keywordFiler = require('../utils/keywordFilter');
const toDateFormat = require('../utils/toDateFomat');
const BlogDao = require('../daos/blog.dao');
const BlogDataDto = require('../dtos/blog.dto');
// const KoreanTime = require('../utils/koreanTime');
const contentUtil = require('../utils/contentUtil');
require('dotenv').config()

class BlogService{
    constructor(serarchDto){
        this.keyword = serarchDto.getKeyword();
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
                query: keywordFiler(this.keyword),
                display: 10,
                sort : 'date'
            }
        }
        // openAPI 결과
        const result = await axios.get('https://openapi.naver.com/v1/search/blog',options);
        const items =  result.data.items;
        return items.map(item => {
            const content =  contentUtil(item.title,item.description)
            const sns = item.title.replace('</b>','').replace('<b>','') +  item.description.replace('</b>','').replace('<b>','')
            const link = item.link;
            // 포맷 변경
            // const koreanTime = new KoreanTime();
            const curr = new Date();
            const utc = curr.getTime() +  (curr.getTimezoneOffset() * 60 * 1000);
            const timeDiff = 9 * 60 * 60 * 1000;
            const krDate =  new Date(utc + (timeDiff));
            const hours = krDate.getHours().toString().length == 1 ? `0${krDate.getHours().toString()}` : krDate.getHours().toString();
            const minutes = krDate.getMinutes().toString().length == 1 ? `0${krDate.getMinutes().toString()}` : krDate.getMinutes().toString();
            const date = `${toDateFormat(item.postdate)}-${hours}-${minutes}`;
            return new BlogDataDto(content,link,date,this.keyword,sns);
        });
    }
    // 
    async saveData() {
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
