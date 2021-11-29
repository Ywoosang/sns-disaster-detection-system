const mongodb = require('../util/mongodb');
const toISO = require('../util/toISO');
const db = mongodb.dbsetting();

exports.download = async function(start,end){
    const StartTime = start.split('-') //여기에 타임에 관한 정보를 넣어주세요
    const EndTime =  end.split('-') 
    const firstTime = toISO.toISO(StartTime);
    const lastTime = toISO.toISO(EndTime);
    const response = []
    const cursor = db.collection('twitter_data').find({date : { $gte:firstTime,$lte:lastTime}});
    while (await cursor.hasNext()) { // Iterate entire data
        const doc = await cursor.next(); // Get 1 Document
        const dToj = {
             sns: doc.sns,
             content : doc.content,
             link : doc.link,
             keyword :doc.keyword,
             date : toISO.toArr(doc.date),
             service : doc.service
        }
        response.push(dToj);
    }
    return response;
}