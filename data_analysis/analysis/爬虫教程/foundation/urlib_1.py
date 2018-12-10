import urllib
import urllib2

values = {"username":"13750429564","password":"qertu1014"}
data= urllib.urlencode(values)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}
url="https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsd"
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)
print response.read()
print response.url
