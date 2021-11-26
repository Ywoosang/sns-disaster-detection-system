const cron = require('node-cron')
const load_twitter = require('../controller/loadTwitterData.js')

exports.scheduler = cron.schedule('*/5 * * * *', async function () {
    var keywords = [['폭설','폭설 내려'],['산불','산불 발생'],['교통사고','교통사고 발생'],['붕괴','붕괴 사고'],['폭발','폭발 발생'],['화재','화재 발생'],['코로나','코로나 확진'],['홍수','홍수 발생']]
    console.log('start!');
    // const curTime = new Date().toISOString();
    for(var i = 0 ; i<keywords.length;i++){
        await load_twitter.upload(keywords[i][0],keywords[i][1]);
    }    
    console.log('last data uploaded :', new Date().toString());
  });