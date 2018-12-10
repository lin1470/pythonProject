# coding: UTF-8
import requests
import json
#有时候需要传送的形式是表单的形式，而是json，因此需要转换形式。
# r = requests.get("http://www.baidu.com")
# print type(r)
# print r.status_code
# print r.encoding
# #print r.text
# print r.cookies
# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# r = requests.get(url, cookies=cookies)
# print r.text

# 注意这种设置cookie的方法
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get("http://httpbin.org/cookies")
# print(r.text)


# 可以利用verify参数来确定证书
# r = requests.get('https://github.com', verify=True)
# print r.text

# 设置代理方法
proxies = {
  "https": "http://41.118.132.69:4433"
}
headers = {"User-Agent":"nmei"}
r = requests.post("http://httpbin.org/post", proxies=proxies,headers=headers)
print r.text