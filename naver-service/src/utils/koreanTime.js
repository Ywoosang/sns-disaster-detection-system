class KoreanTime{
    constructor(){
        const curr = new Date();
        const utc = curr.getTime() +  (curr.getTimezoneOffset() * 60 * 1000);
        const timeDiff = 9 * 60 * 60 * 1000;
        const krDate =  new Date(utc + (timeDiff));
        this.date = krDate;
    }

    getHours(){
        const hours_number = this.date.getHours();
        const hours_string = hours_number.toString();
        return hours_string.lenghth == 1 ? `0${hours_string}` : hours_string   
    }

    getMinutes(){
        const minutes_number = this.date.getMinutes()
        const minutes_string =  minutes_number.toString();
        return minutes_string.lenghth == 1 ? `0${minutes_string}` : minutes_string;
    }
}

module.exports = KoreanTime;