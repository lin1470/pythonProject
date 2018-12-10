# coding: UTF-8
import urllib
import urllib2
from bs4 import BeautifulSoup
import re
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent ="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36 OPR/45.0.2552.812"
headers = {"User-Agent":user_agent}
try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('UTF-8')
    pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?' +
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>', re.S)
    items = re.findall(pattern,content)
    for item in items:
        haveImg = re.search('img',item[3])
        if not haveImg:
            print item[0],item[1],item[2],item[4]
    soup = BeautifulSoup(response.read(),"lxml")
    print soup
except urllib2.URLError as e:
    if hasattr(e,'code'):
        print e.code,
    if hasattr(e,'reason'):
        print e.reason