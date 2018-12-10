# coding: UTF-8
# successfully login in the course system.
import urllib2
import urllib
import cookielib

filename = 'cookie_stu.txt'
cookie = cookielib.MozillaCookieJar(filename)  # create a cookie to record the login message
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))  # create a opener
url = 'https://sso.stu.edu.cn/login'  # the login url
course_url = "https://my.stu.edu.cn/discussion/my-courses#%2Fmy-courses"  # the course url
postdata = urllib.urlencode({
"username":"15zlli2",
"password":"QERtu1014",
"lt":"LT-288242-FvEHRzhVb0ZWbdAz9zADm25DlEHmOi",
"execution":"e1s1",
"_eventId":"submit"
})
# the post data is so long

try:
    login_result = opener.open(url,postdata)
except urllib2.HTTPError as e:
    print e.code,e.reason
except urllib2.URLError as e:
    print e.code,e.reason
print "login_result",login_result.url
cookie.save(ignore_expires=True,ignore_discard=True)

# another try the http
try:
    course_result = opener.open(course_url)
except urllib2.HTTPError as e:
    print e.code,e.reason
except urllib2.URLError as e:
    print e.code,e.reason
print course_result.read()