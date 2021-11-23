var axios = require('axios');
require('dotenv').config()
var uri = 'http://api.twitter.com/2/tweets/search/recent'
var bearer_token = process.env.TWITTER_TOKEN;

async function getTwitterData(keyword){
    const options = {
        headers: {'Authorization':'bearer '+bearer_token},
        params: {
            query: keyword,
            max_results: 50,
            'tweet.fields' : 'created_at',
            expansions : 'author_id'
        },
    }
    
    const result2 = await axios.get(uri,options);
    console.log(result2.data)
  
    return result2.data.data
   
};


exports.getTotalData = async function (keyword){   
    var data,temp=[]
    var res = []
    
    data = await getTwitterData(keyword).catch((err)=>{console.log(err)});

    
    
    for (const i = 0 ; i<Object.keys(data).length;i++){
       
        temp.push(data[i].text.replace('\n',""));
        temp.push('twitter.com/'+data[i].author_id+'/status/'+data[i].id);
        temp.push(data[i].created_at)

        res.push(temp); 
        
        temp = []
    }

    return res;

};



