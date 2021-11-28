const toDateFormat = (date) => {
    const utc = date.getTime() + (date.getTimezoneOffset() * 60 * 1000);
    const timeDiff = 9 * 60 * 60 * 1000;
    const currentTime = new Date(utc + (timeDiff));
    const year = currentTime.getFullYear();
    const month = currentTime.getMonth() + 1;
    const day = currentTime.getDate();
    const hours = currentTime.getHours();
    const minutes = currentTime.getMinutes();
    const timeArray = [month.toString(),day.toString(),hours.toString(),minutes.toString()].map(elem => elem.length == 1 ? `0${elem}` : elem);
    const dateFormat = [year.toString(),...timeArray].join('-');
    return dateFormat;
}

export default toDateFormat;