# coding: UTF-8
# successfully login in the course system.
import urllib2
import urllib
import cookielib

filename = 'cookie_stu.txt'
cookie = cookielib.MozillaCookieJar(filename)  # create a cookie to record the login message
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))  # create a opener
url = 'http://1.1.1.2/ac_portal/20170602150308/pc.html?template=20170602150308&tabs=pwd&vlanid=0&url='  # the login url
course_url = "http://1.1.1.2/ac_portal/20170602150308/pc.html?template=20170602150308&tabs=pwd&vlanid=0&url="  # the course url
# the post data is so long

postdata = urllib.urlencode({
    "opr":"pwdLogin",
    "userName":"15ltlong",
    "pwd":"ZZliting123",
    "ipv4or6":"",
    "rememberPwd":"0"
})
try:
    login_result = opener.open(url,postdata)
except urllib2.HTTPError as e:
    print e.code,e.reason
except urllib2.URLError as e:
    print e.code,e.reason
cookie.save(ignore_expires=True,ignore_discard=True)

# another try the http
try:
    course_result = opener.open(course_url)
except urllib2.HTTPError as e:
    print e.code,e.reason
except urllib2.URLError as e:
    print e.code,e.reason
print course_result.read()