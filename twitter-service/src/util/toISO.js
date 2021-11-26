var arr= ['2020','10','12','20','13']
var iso = '2021-11-22T22:16:00.000Z'
var t = '2020-11-12-20-13'
var str = "";


exports.toISO = function (arr){
    var ti = new Date(arr[0],(Number(arr[1])-1).toString(),arr[2],hours = arr[3],minutes = arr[4])
    var res = new Date(ti.getTime() + 9 * 60 * 60 * 1000)
    console.log(res)
    return res.toISOString()
}

exports.toArr = function(iso){
    var res = [];
    
    var ti = new Date(iso)
    res.push(ti.getFullYear().toString())
    res.push((ti.getUTCMonth()+1).toString())
    res.push(ti.getUTCDate().toString())
    res.push(ti.getUTCHours().toString())
    res.push(ti.getMinutes().toString())
    var res_str=res[0]+"-"+res[1]+"-"+res[2]+"-"+res[3]+"-"+res[4]
    return res_str;

}

