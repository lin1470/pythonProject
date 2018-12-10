# coding:utf-8
import urllib2
import urllib
import re
from bs4 import BeautifulSoup

class Tool:
    removeImg = re.compile('<img.*?>| {7}')
    removeAddr = re.compile('<a.*?>|</a>')
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    replaceTD = re.compile('<td>')
    replacePara = re.compile('<p.*?>')
    replaceBR = re.compile('<br><br>|<br>')
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,'',x)
        x = re.sub(self.removeAddr,'',x)
        x = re.sub(self.replaceLine,'\n',x)
        x = re.sub(self.replaceTD,'\t',x)
        x = re.sub(self.replacePara,'\n    ',x)
        x = re.sub(self.replaceBR,'\n',x)
        x = re.sub(self.removeExtraTag,'',x)
        return x.strip()


class BDTB:
    # 初始化传入基地址，是否只看楼主的参数
    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)
        self.tool = Tool()

    def getPage(self,pageNum):
        try:
            url = self.baseURL+self.seeLZ+'&pn'+ str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            # print response.read()
            # print response.read()
            return response.read()
        except urllib2.URLError as e:
            if hasattr(e,'reason'):
                print u"连接百度贴吧失败，错误原因：",e.reason
                return None

    # 获取这个贴吧的标题。
    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h3.*?>(.*?)</h3>', re.S)
        result = re.search(pattern, page)
        if result:
            print result.group(1).strip()
            return result.group(1).strip()
        else:
            print "get titile errors"
    # 获取一共有多少页和多少个回复
    def getPageNum(self):
        page = self.getPage(1)
        pattern1 = re.compile('<span class="red" style="margin-right:3px">(.*?)</span>',re.S)
        pattern2 = re.compile('<span class="red">(.*?)</span>')  # <span class="red">5</span>
        result1 = pattern1.search(page)
        result2 = pattern2.search(page)
        if result1 and result2:
            print u"一共有"+result1.group(1)+u"页"
            print u"一共有"+result2.group(1)+u"个回帖"
            return result1.group(1).strip(),result2.group(1).strip()

    def getContent(self,page):
        try:
            pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
            items = re.findall(pattern,page)
            if items:
                floor = 1
                for item in items:
                    print self.tool.replace(item)
                    print floor, u'楼--------------------------------------------------------------------\n'
                    floor +=1
                return items
            else:
                print "extract the context faily"
        except Exception as e:
            print e.message




baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL,1)
page = bdtb.getPage(1)
soup = BeautifulSoup(page,'lxml')
# print page
# print soup.find("h3")
bdtb.getTitle()
bdtb.getPageNum()
bdtb.getContent(page)


