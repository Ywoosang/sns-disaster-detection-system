exports.toISO = function (arr){
    var ti = new Date(arr[0],(Number(arr[1])-1).toString(),arr[2],hours = arr[3],minutes = arr[4])
    var res = new Date(ti.getTime() + 9 * 60 * 60 * 1000)
    console.log(res)
    return res.toISOString()
}