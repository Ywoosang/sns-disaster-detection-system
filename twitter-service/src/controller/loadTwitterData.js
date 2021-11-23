const twitterData= require('../model/twitterData.js');
const mongodb = require('../mongodb')
const mongoose = require('mongoose');
const db = mongodb.dbsetting(()=>{});

exports.upload = function(keyword,Class){
    twitterData.getTotalData(Class)
    .then((res)=>{
        //console.log(res);
        mongodb.data.set('collection', 'twitter_data');
        const DBdata = mongoose.model('twitter_data', mongodb.data);
        db.collection('twitter_data').createIndex( { content: 1 }, { unique: true } )
        db.collection('twitter_data').findOne({}, {sort:{$natural:-1}})
        .then(async (lastData)=>{
            console.log(lastData)
            for(let i = 0 ; i<res.length;i++){  
                /*              
                if(lastData != null &&lastData.content == res[i][0]){
                    console.log("break at "+i.toString())
                    break;
                }
                */
                const newData = new DBdata({
                    content : res[i][0],
                    link : res[i][1],
                    date : res[i][2],
                    type: keyword
            
                });               
                await newData.save().catch(error => { 
                    console.log(error);
                });
            }
        })
        .then(()=>{    
            mongoose.disconnect();
        })
        .then(()=>{
            console.log("전송 완료")
        })
    })
    .catch(error => { 
        console.log(error);
    });
    return 0;
}
