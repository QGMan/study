//使用mock
const Mock = require('mockjs')
// 获取mock.Random对象
const Random = Mock.Random
//mock一组数据
Mock.mock('http://api.com', {
  "user|5-10": [{
    'name': '@cname', //中文名称
    'age|1-100': 100, //100以内随机整数
    'birthday': '@date("yyyy-MM-dd")', //日期
    'city': '@city(true)' //中国城市
  }]
});
