
Date.prototype.Format = function (fmt) {
    var o = {
        "M+": this.getMonth() + 1, //月份
        "d+": this.getDate(), //日
        "h+": this.getHours(), //小时
        "m+": this.getMinutes(), //分
        "s+": this.getSeconds(), //秒
        "q+": Math.floor((this.getMonth() + 3) / 3), //季度
        "S": this.getMilliseconds() //毫秒
    };
    if (/(y+)/.test(fmt)) fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
    for (var k in o)
        if (new RegExp("(" + k + ")").test(fmt)) fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
    return fmt;
}

/**
 * 获取当前月份的第一天和最后一天
 * @returns {Date[]}  例如 2019-09-01~2019-09-30
 */
function getMonthFirstLastDay(date, current_day) {
    let myDate
    if (current_day){
        myDate = new Date()
    }else {
        myDate = new Date(date.replace(/-/, "/"));
    }

    let currentMonth = myDate.getMonth();
    let firstDay = new Date(myDate.getFullYear(), currentMonth, 1)
    let lastDay = new Date(firstDay.getFullYear(), currentMonth + 1, 0);
    firstDay = firstDay.Format("yyyy-MM-dd");
    lastDay = lastDay.Format("yyyy-MM-dd");
    return [firstDay, lastDay]
}

// let [month_first_day, month_last_day] = getMonthFirstLastDay('2020-04-07', 1)


function getYearFirstLastDay(date, current_day) {
  let firstDay, lastDay
  if(current_day){
    firstDay = new Date()
    lastDay = new Date()
  }
  else{
    firstDay = new Date(date.replace(/-/, "/"));
    lastDay = new Date(date.replace(/-/, "/"));
  };
  firstDay.setDate(1);
  firstDay.setMonth(0);
  lastDay.setFullYear(lastDay.getFullYear() + 1);
  lastDay.setDate(31);
  lastDay.setMonth(-2.5);
  firstDay = firstDay.toLocaleDateString().split('/').join('-');
  lastDay = lastDay.toLocaleDateString().split('/').join('-');
  return [firstDay, lastDay]
}

let [year_first_day, year_last_day] = getYearFirstLastDay('2021-01-09', 1)


// console.log(month_first_day, month_last_day)
console.log(year_first_day, year_last_day)

//  let firstDay = new Date();  // 这里会获取当天的时间
// //
// // console.log('当天日期的数据类型是：' + typeof firstDay + '  数值是：' + firstDay)
// firstDay = firstDay.Format("yyyy-MM-dd")
//  console.log(firstDay, typeof firstDay)
// //     // firstDay.setDate(1);
// //
// console.log(firstDay)



