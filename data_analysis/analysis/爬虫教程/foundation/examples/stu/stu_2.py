from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class Stu():
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.url = "http://1.1.1.2/ac_portal/20170602150308/pc.html?template=20170602150308&tabs=pwd&vlanid=0&url="
        self.account = '15ltlong'
        self.password = 'ZZliting123'
    def login(self):
        self.driver.get(self.url)
        try:
            if self.driver.current_url == self.url:
                print "logining "+self.driver.current_url
                account_elem = self.driver.find_element_by_xpath('//*[@id="password_name"]')
                password_elem = self.driver.find_element_by_xpath('//*[@id="password_pwd"]')
                account_elem.send_keys(self.account)
                password_elem.send_keys(self.password)
                password_elem.send_keys(Keys.ENTER)
                time.sleep(5)
                return True
            else:
                self.logout()
            return False
        except Exception as e:
            print e.message
            self.logout()
    def logout(self):
        print "logout website "+self.driver.current_url
        logout = self.driver.find_element_by_xpath('//*[@id="logout_submitBtn"]')
        logout.click()
        time.sleep(5)

    def display_flow(self,state):
        if not state:
            self.login()
        try:
            block = self.driver.find_element_by_xpath('//*[@id="mode_logout"]')
            table = self.driver.find_element_by_xpath('//*[@id="mode_flux_info"]/div/dl/dd/table')
        except Exception as e:
            print e.message
            self.login()
        print table.text
stu = Stu()
state = stu.login()
stu.display_flow(state)
