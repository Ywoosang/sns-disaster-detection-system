const twitterService= require('../services/twitter.service');
const twitterData = require('../model/twitter.model')
const mongoose = require('mongoose');
const mongodb = require('../util/mongodb')
const timeutil = require('../util/time');
const db = mongodb.dbsetting(()=>{});

exports.upload = async function(Class,keyword){
    await twitterService.getTotalData(keyword)
    .then(async (res)=>{
        //console.log(res);
        db.collection('twitter_data').createIndex( { link: 1 }, { unique: true } )
        var regExp = /[a-z\@\#\/\:\n0-9\.\|]/gi
        for(let i = 0 ; i<res.length;i++){  
            
            const newData = new twitterData({
                'sns' : res[i][0],
                'content' : res[i][0].replace(regExp,""),
                'link' : res[i][1],
                'date' : timeutil.toArr(res[i][2]),
                'keyword': Class,
                'service': 'twitter'
            });               
            await newData.save().catch(error => {
                // 중복 방지를 위해 link 를 키로 설정했음. 키가 중복되었다면 error 를 발생시키는데, 
                // 키가 중복 관련 에러이면 이를 무시함        
                if(error.message.indexOf('E11000 duplicate key error collection') == -1){
                    console.log(error);
                }                
            });
        }      

    })
    .catch(error => { 
        console.log(error);
    });

    return 0;
}
