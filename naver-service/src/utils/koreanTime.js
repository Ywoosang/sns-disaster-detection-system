class KoreanTime{
    constructor(){
        const curr = new Date();
        const utc = curr.getTime() +  (curr.getTimezoneOffset() * 60 * 1000);
        const timeDiff = 9 * 60 * 60 * 1000;
        const krDate =  new Date(utc + (timeDiff));
        this.date = krDate;
    }

    getHours(){
        const hours = this.date.getHours().toString();
        return hours.lenghth == 1 ? `0${hours}` : hours   
    }

    getMinutes(){
        const minutes = this.date.getMinutes().toString();
        return minutes.lenghth == 1 ? `0${minutes}` : minutes;
    }
}

module.exports = KoreanTime;