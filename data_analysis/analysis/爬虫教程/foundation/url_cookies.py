# we can use this way to save a cookie for our logining.
import urllib2
import cookielib

cookie = cookielib.CookieJar()  # assingment a varaible to sava a cookie object
handler = urllib2.HTTPCookieProcessor(cookie)  # creat a cookie processor
opener = urllib2.build_opener(handler)  # create the handler for cookie
response = opener.open("http://www.baidu.com")
for item in cookie:
    print 'name = '+item.name
    print 'Value = '+item.value



