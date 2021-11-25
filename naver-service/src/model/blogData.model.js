const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const naverDataSchema = new Schema({
    content : 'string',
    date : 'string',
    link : 'string',
    keyword : 'string',
},{
    collection: 'naver_data'
});

//  model은 데이터베이스에서 데이터를 읽고, 생성하고, 수정하는프로그래밍 인터페이스를 정의
//  model 의 첫번째 인자는 은 해당 document가 사용 할 collection의 단수적 표현
//  여기서는 naver_datas 가 collection 이름
// collection 이름을 임의로 정하기 위해 schema 를 만들때 collection 옵션을 추가
module.exports = mongoose.model('naver_data',naverDataSchema);
// 스키마를 정의함에 있어 다음과 같이 옵션을 줄 수 있다.
// new Schema({..}, options);
// or
// const schema = new Schema({..});
// schema.set(option, value);