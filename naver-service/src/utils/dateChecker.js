module.exports = (dateTime) => {
    const dateArr = dateTime.split('-');
    if(dateArr.length !== 5) return false;
    const [year,month,date,hour,min] = dateArr;
    // 자리수 확인
    const condition = year.length == 4 && month.length == 2 && date.length == 2 && hour.length == 2 && min.length == 2;
    if(!condition) return false;
    // 숫자인지 확인
    for(let item of [year,month,date,hour,min]){
        if(isNaN(item)) return false;
    }
    return true;
}