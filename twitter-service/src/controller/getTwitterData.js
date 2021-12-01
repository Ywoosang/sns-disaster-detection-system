const mongodb = require('../util/mongodb');
const timeutil = require('../util/time');
const db = mongodb.dbsetting();

exports.download = async function(start,end){
    const StartTime = start.split('-') //여기에 타임에 관한 정보를 넣어주세요
    const EndTime =  end.split('-') 
    const firstTime = timeutil.ArrtoStr(StartTime);
    const lastTime = timeutil.ArrtoStr(EndTime);
    const response = []
    const cursor = db.collection('twitter_data').find({date : { $gte:firstTime,$lte:lastTime}});
    while (await cursor.hasNext()) { // Iterate entire data
        const doc = await cursor.next(); // Get 1 Document
        const dToj = {
             sns: doc.sns,
             content : doc.content,
             link : doc.link,
             keyword :doc.keyword,
             date : doc.date,
             service : doc.service
        }
        response.push(dToj);
    }
    return response;
}