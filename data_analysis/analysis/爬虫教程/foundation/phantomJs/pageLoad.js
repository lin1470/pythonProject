/**
 * Created by bruce on 10/11/17.
 */
var page = require('webpage').create();
page.open('http://cuiqincai.com',function(status){
    console.log("status:"+status);
    if (status === "success"){
        page.render("example.png");
    }
    phantom.exit()
});