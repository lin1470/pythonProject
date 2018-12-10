# coding:UTF-8
# 这个例子是说明了我们可以模仿登录这个网页的然后就输入了，真的很简单吧哈哈。
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# url = "http://baidu.com"
# driver = webdriver.Chrome()
# driver.get(url)
# print driver.title
# elem = driver.find_element_by_name("wd")
# elem.send_keys("pycon")
# elem.send_keys(Keys.ENTER)
# print driver.page_source

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# class PythonOrgSearch(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#
#     def test_search_in_python_org(self):
#         driver = self.driver
#         driver.get("http://www.python.org")
#         self.assertIn("python",driver.title)
#         elem = driver.find_element_by_name("q")
#         elem.send_keys("pycon")
#         elem.send_keys(Keys.ENTER)
#         assert "No results found." not in driver.page_source
#
#     def tearDown(self):
#         self.driver.close()
#
# if __name__ == "__main__":
#     unittest.main()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS()
driver.get("http://baidu.com")
input_elem = driver.find_element_by_xpath('//*[@id="kw"]')
# print input_elem.get_attribute('type')
soup = BeautifulSoup(driver.page_source,'lxml')