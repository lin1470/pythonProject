/**
 * Created by bruce on 10/11/17.
 */
var page = require('webpage').create(),
    system = require('system'),
    t,address;

if(system.args.length === 1){
    console.log('Usage: loadSpeed.js <some Url>');
    phantom.exit();
}

t = Date.now();
address = system.args[1];
page.open(address,function(status){
    if(status!== 'success'){
        console.log('FAIL to load the address');
    }else{
        t= Date.now()-t;
        console.log('Loading'+system.args[1]);
        console.log('Loading'+t+'msec');
    }
    phantom.exit();
});