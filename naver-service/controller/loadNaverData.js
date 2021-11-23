const naverData= require('../model/naverData.js');
const mongodb = require('../src/mongodb')
const mongoose = require('mongoose');

var db = mongodb.dbsetting(function(){});

exports.upload = function(keyword,Class){
    naverData.getTotalData(Class)
    .then((res)=>{
        //console.log(res);
        mongodb.data.set('collection', 'naver_data');
        var DBdata = mongoose.model("naver_data", mongodb.data);
        
        db.collection('naver_data').createIndex( { content: 1 }, { unique: true } )
        db.collection('naver_data').findOne({}, {sort:{$natural:-1}})
        .then(async (lastData)=>{
            console.log(lastData)
            for(var i = 0 ; i<res.length;i++){  
                /*              
                if(lastData != null &&lastData.content == res[i][0]){
                    console.log("break at "+i.toString())
                    break;
                }
                */
                var Dte = new Date()
                var korDte = new Date(Dte.getTime()+ 9 * 60 * 60 * 1000)
                var newData = new DBdata({
                    content : res[i][0],
                    link : res[i][1],
                    date : res[i][2],
                    type: keyword,
                    timestamp: korDte.toISOString()
            
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

//upload("교통사고 발생","교통사고")
