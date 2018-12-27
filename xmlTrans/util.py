from bs4 import BeautifulSoup
import requests

def is_chinese(words):
    for ch in words:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def chinese2html(words):
    transword = list()
    retstring = ''
    for word in words:
        # print(word)
        word = word.encode('unicode_escape').decode().upper().replace('\\U','&#x')
        word = word+';'
        # print(word)
        transword.append(word)
    for word in transword:
        retstring += word
    return retstring


def scrach_data(link):
    htmllink = "http://app.lib.stu.edu.cn/ljs/" + link
    details = dict()
    request = requests.get(htmllink)
    # print(request.status_code)
    if 200 != request.status_code:
        print('scrach details error,the status code is:',request.status_code)
        return None
    # print(request.text)
    htmltext = request.text
    soup = BeautifulSoup(htmltext,"html.parser")
    abstract = soup.find(id='lbl_abstract')
    subject = soup.find(id="lbl_subject")
    desc = soup.find(id="lbl_desc")
    details['abstract'] = abstract.text
    details['subject'] = subject.text
    details['desc'] = desc.text
    return details

def getImg(link):
    htmllink = "http://app.lib.stu.edu.cn/ljs/" + link
    img = requests.get(htmllink)
    if 200 != img.status_code:
        print('get image error, the status code is:',img.status_code)
        return None
    return img.content

# getImg("a/2013-1-21/s_zhongsjnt001_JPG.JPG")
# details = scrach_data("imgDetails.aspx?id=1645")
# print(details)
