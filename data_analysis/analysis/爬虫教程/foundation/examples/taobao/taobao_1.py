# coding:utf-8
import urllib
import urllib2
import re

class Spider:
    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'

    def getPage(self,pageIndex):
        url = self.siteURL+"?page="+str(pageIndex)
        print url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')
    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<a class="lady-name" href="(.*?)".*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        items = re.findall(pattern,page)
        if items:
            for item in items:
                print item[0],item[1],item[2]
            return items
        else:
            print "extract data error"
spider = Spider()
spider.getContents(1)