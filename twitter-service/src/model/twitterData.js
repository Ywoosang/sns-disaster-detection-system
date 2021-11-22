const axios = require('axios');
const uri = 'http://api.twitter.com/2/tweets/search/recent'
const bearer_token = process.env.TWITTER_TOKEN;
require('dotenv').config()

async function getTwitterData(keyword) {
    const options = {
        headers: { 'Authorization': 'bearer ' + bearer_token },
        params: {
            query: keyword,
            max_results: 50,
            'tweet.fields': 'created_at',
            expansions: 'author_id'
        },
    }
    // 에러를 상위 블록으로 위임
    const response = await axios.get(uri, options);
    // console.log(result2.data)
    return response.data.data
};

exports.getTotalData = async function (keyword) {
    try{
        const data = await getTwitterData(keyword);
        const res = []
        for (let i = 0; i < Object.keys(data).length; i++) {
            const temp = []
            temp.push(data[i].text.replace('\n', ""));
            temp.push('twitter.com/' + data[i].author_id + '/status/' + data[i].id);
            temp.push(data[i].created_at)
            res.push(temp);
        };
        return res;
    }catch(error){
        console.log(error);
    }
};