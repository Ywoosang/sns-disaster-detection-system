const twitterData= require('../model/TwitterData.js');
const mongodb = require('../src/mongodb')
var mongoose = require('mongoose');




var db = mongodb.dbsetting(function(){});

exports.upload = function(keyword,Class){
    twitterData.getTotalData(Class)
    .then((res)=>{
        //console.log(res);
        mongodb.data.set('collection', 'twitter_data');
        var DBdata = mongoose.model('twitter_data', mongodb.data);
        
        db.collection('twitter_data').createIndex( { content: 1 }, { unique: true } )
        db.collection('twitter_data').findOne({}, {sort:{$natural:-1}})
        .then(async (lastData)=>{
            console.log(lastData)
            for(var i = 0 ; i<res.length;i++){  
                /*              
                if(lastData != null &&lastData.content == res[i][0]){
                    console.log("break at "+i.toString())
                    break;
                }
                */
                var newData = new DBdata({
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
