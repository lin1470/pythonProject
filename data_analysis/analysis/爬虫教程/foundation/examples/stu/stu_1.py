# coding:utf-8
import urllib2
import urllib
import re
import requests
import chardet
import sys
# 模拟登录1.1.1.2,并显示流量情况。

class Stu:
    def __init__(self):
        self.url = "http://1.1.1.2/ac_portal/20170602150308/pc.html?template=20170602150308&tabs=pwd&vlanid=0&url="

    def login(self,url):
        session = requests.Session()
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        headers = {'User-Agent':user_agent}
        data = {
        'opr':'pwdLogin',
        'userName':'15zlli2',
        'pwd':'QERtu1014',
        'rememberPwd':'0'
        }
        post_data = urllib.urlencode(data)
        result = session.get(url,data=post_data,headers=headers)
        return result.text

stu = Stu()
html = stu.login(stu.url)
# print html.decode('utf-8')
# htmlEncoding = htmlGuess['encoding']
print sys.getfilesystemencoding()
# html_decoded = html.decode(htmlEncoding)
# sys_encoding = sys.getfilesystemencoding()
# html_encoded = html_decoded.encode(sys_encoding)
# print html_encoded
