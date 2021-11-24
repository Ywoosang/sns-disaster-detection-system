const twitterData= require('../model/twitterData.js');
const mongodb = require('../mongodb')
const mongoose = require('mongoose');
const db = mongodb.dbsetting(()=>{});

exports.upload = async function(Class,keyword){
    await twitterData.getTotalData(keyword)
    .then(async (res)=>{
        //console.log(res);
        mongodb.data.set('collection', 'twitter_data');
        const DBdata = mongoose.model('twitter_data', mongodb.data);
        db.collection('twitter_data').createIndex( { content: 1 }, { unique: true } )
        var regExp = /[a-z\@\#\/\:\n0-9\.\|]/gi
        console.log(res)
        for(let i = 0 ; i<res.length;i++){  
                /*              
                if(lastData != null &&lastData.content == res[i][0]){
                    console.log("break at "+i.toString())
                    break;
                }
                */
            const newData = new DBdata({
                'content' : res[i][0].replace(regExp,""),
                'link' : res[i][1],
                'date' : res[i][2],
                'class': Class
            
            });               
            await newData.save().catch(error => { 
                console.log(error);
            });
        }
        
        
        
    }).then(()=>{
        console.log("전송 완료")
        
    }) 
    .catch(error => { 
        console.log(error);
    });

    
    return 0;
}
