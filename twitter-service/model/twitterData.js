var axios = require('axios');
var uri = 'http://api.twitter.com/2/tweets/search/recent'
var bearer_token = 'AAAAAAAAAAAAAAAAAAAAAMbAVgEAAAAA0Ifyo8%2FQiol4LQZGJJMSCfOfXno%3D0dYaH0EposblJXmk5Rsui4jiid8BIYHW6HasILJED9BgpOyoX1';

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

    
    
    for (var i = 0 ; i<Object.keys(data).length;i++){
       
        temp.push(data[i].text.replace('\n',""));
        temp.push('twitter.com/'+data[i].author_id+'/status/'+data[i].id);
        temp.push(data[i].created_at)

        res.push(temp); 
        
        temp = []
    }

    return res;

};



