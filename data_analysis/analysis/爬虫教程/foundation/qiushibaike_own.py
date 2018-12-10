# coding: utf-8
import urllib2
import re

class QSBK:

    def __init__(self):
        self.pageIndex = 1 # define the page number
        self.user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        self.headers = {'User-Agent':self.user_agent}
        self.stories = []  # store the stories of the page
        self.enable = False  # indicate if continue to run

    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page'+ str(pageIndex)
            request = urllib2.Request(url,headers=self.headers)
            response = urllib2.urlopen(request)

            pageCode = response.read().decode("utf-8")
            return pageCode
        except urllib2.URLError as e:
            if hasattr(e,'reason'):
                print "error",e.reason
                return None
    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "page load error"
            return None
        pattern = re.compile('h2>(.*?)</h2.*?content">(.*?)</.*?number">(.*?)</',re.S)  # regex expression
        items = re.findall(pattern,pageCode)    # we can find many stories in this page
        pageStories = []
        for item in items:
            pageStories.append([item[0].strip(),item[1].strip(),item[2].strip()]) # add these stories into the pageStories
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
            if input == 'Q':
                self.enable =False
                return
            print u"第%d页\t发布人：%s\t 赞:%s\n%s"%(page,story[0],story[2],story[1])

    def start(self):
        print u'正在读取，回车查看，Q退出'
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)
spider = QSBK()
spider.start()