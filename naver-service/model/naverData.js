
const axios = require('axios');
require('dotenv').config()
const uri =  'https://openapi.naver.com/v1/search/blog';
const client_id =process.env.NAVER_CLIENT;
const client_secret = process.env.NAVER_CLIENT_SECRET;

//var recent = ""

async function getNaverData(keyword){
    const options = {
        headers: {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret': client_secret},
        params: {
            query: keyword,
            display: 50,
            sort : 'date'
        },
      }
    

    const result2 = await axios.get(uri,options);
    
    //console.log("콜백함수 밖: " ) 
    //console.log(result2.data.items)
  
    return result2.data.items
   
};

async function getNaverDataDetail(url){
    var detail= await axios.get(url);
    console.log(detail.data)
};

exports.getTotalData =async function (keyword){   
    var data,temp=[]
    var res = []
    
    data = await getNaverData(keyword);


    
    for (const i = 0 ; i<Object.keys(data).length;i++){
        //console.log(data[i].title.replace("<b>","").replace("</b>",""))
        //console.log(data[i].description.replace("<b>","").replace("</b>",""))
        temp.push(data[i].title.replace("<b>","").replace("</b>","")+data[i].description.replace("<b>","").replace("</b>",""));
        temp.push(data[i].link);
        temp.push(data[i].postdate)

        res.push(temp);
        temp = []
    }

    console.log(temp[0])
    return res;

};