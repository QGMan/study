# y

> A Vue.js project

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

##vue-cli自动生成项目
vue init webpack 项目名

## 引入jquery
一、安装jquery：npm install jquery --save-dev;

二、找到webpack.dev.js 在module.exports》 plugins里面添加两下代码：
var webpack = require("webpack")
new webpack.ProvidePlugin({
  jQuery: "jquery",
  $: "jquery"
}),
三、在App.vue页面引入（放在script标签里面）：
//引入jquery
import $ from 'jquery'