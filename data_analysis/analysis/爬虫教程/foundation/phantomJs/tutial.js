/**
 * Created by bruce on 10/11/17.
 */
// webpage模块是PhantomJS的核心模块，用于网页操作。
var webpage = require('webpage');
// 上面代码表示加载PhantomJS的webpage模块，并创建一个实例。
var page = webpage.create();
// open方法用于打开具体的网页。
// page.open('http://www.baidu.com',function(s){
//     console.log(s);
//     phantom.exit();
// });
// 上面代码中，open()方法，用于打开具体的网页。它接受两个参数。第一个参数是网页的网址，这里打开的是著名新闻网站Slashdot，第二个参数是回调函数，网页打开后该函数将会运行，它的参数是一个表示状态的字符串，如果打开成功就是success，否则就是fail。
url = "http://www.baidu.com";
// page.open(url,function(status){
//     var title = page.evalute(function(){
//         return document.title;
//     });
//     console.log("the page title is"+ title);
//     phantom.exit();
// });

// 最为简单的截图功能
// page.onConsoleMessage = function(msg){
//     console.log(msg);
// }
// page.open(url,function(status){
//     console.log("status: "+ status);
//     if(status== "success"){
//         page.render("baidu1.png");
//     }
//     phantom.exit();
// });

// 当接受到请求时，可以通过改写onResourceRequested和onResourceReceived回调函数来实现接收到资源请求和资源接受完毕的监听
// page.onResourceRequested = function(request){
//     console.log('Request'+JSON.stringify(request,undefined,4));
// };
// page.onResourceReceived = function(response){
//     console.log('receive'+JSON.stringify(response,underfined,4));
// };
// page.open(url);

// 脚本都是像在浏览器中运行的，所以标准的 JavaScript 的 DOM 操作和 CSS 选择器也是生效的。
// 例如下面的例子就修改了 User-Agent，然后还返回了页面中某元素的内容。

// console.log('the default user agent is '+page.settings.userAgent);
// page.settings.userAgent = 'SpecialAgent';  // change the userAgent manually
// page.open(url,funtion(status){
//     if(status!== 'success'){
//         console.log('Unable to access network');
//     } else{
//         var ua = page.evaluate(function(){
//             return document.getElementById('myagent').textContent;
//         });
//         console.log(ua);
//     }
//     phantom.exit();
// });

console.log('The default user agent is ' + page.settings.userAgent);
page.settings.userAgent = 'SpecialAgent';
page.open(url, function(status) {
  if (status !== 'success') {
    console.log('Unable to access network');
  } else {
    var ua = page.evaluate(function() {
      return document.getElementById('myagent').textContent;
    });
    console.log(ua);
  }
  phantom.exit();
});