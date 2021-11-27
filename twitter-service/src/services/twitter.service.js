const axios = require('axios');
const uri = 'http://api.twitter.com/2/tweets/search/recent'
require('dotenv').config()
const bearer_token = process.env.TWITTER_TOKEN;

exports.getTotalData = async function (keyword) {
    try{
        //var data = await getTwitterData(keyword);
        const options = {
            headers: { 'Authorization': 'bearer ' + bearer_token },
            params: {
                query: keyword,
                max_results: 50,
                'tweet.fields': 'created_at',
                expansions: 'author_id'
            },
        }
        const response = await axios.get(uri, options);
        var data = response.data.data
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