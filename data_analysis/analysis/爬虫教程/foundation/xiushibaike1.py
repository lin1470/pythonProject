# coding=utf-8
import urllib2
import re

class QSBK:

    def __init__(self):
        self.pageIndex = 1  # 定义第一页
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'  # 定义代理
        self.headers = {'User-Agent' :self.user_agent}  # 添加代理
        self.stories = []   # 存放段子的变量，每一个元素都是一个故事
        self.enable = False # 存放程序是否继续运行的变量

    # 传入某一页的索引获得页面代码
    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib2.Request(url,headers=self.headers)
            response = urllib2.urlopen(request)
            # 将页面转化为UTF-8编码
            pageCode = response.read().decode('utf-8')
            return pageCode  # 这个就是返回一整个页面的。
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print "error",e.reason
                return None

    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "page load error"
            return None
        pattern = re.compile('h2>(.*?)</h2.*?content">(.*?)</.*?number">(.*?)</',re.S)
        items = re.findall(pattern,pageCode)
        pageStories = []
        for item in items:
            pageStories.append([item[0].strip(),item[1].strip(),item[2].strip()])
        return pageStories

    def loadPage(self):
        if self.enable==True:
            if len(self.stories)<2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex +=1

    def getOneStory(self,pageStories,page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == "Q":

                self.enable = False
                return
            print u"第%d页\t发布人：%s\t 赞：%s\n%s" %(page,story[0],story[2],story[1])

    def start(self):
        print u'正在读取，回车查看，Q退出'
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStories = self.stories[0]
                nowPage +=1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)

spider = QSBK()
spider.start()