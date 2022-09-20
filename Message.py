from selenium import webdriver
import time
from user import user,password
from messega import x,y,z
from selenium.webdriver.common.keys import Keys
    
class instegram:
    def __init__(self,user,password,x,y,z):
        self.user = user
        self.password = password
        self.x = x
        self.y = y
        self.z = z
        self.browser = webdriver.Chrome()
    def giris(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.user)
        
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        time.sleep(4)
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
        time.sleep(4)
    def messega(self):
    
        self.browser.get("https://www.instagram.com/sefasihlar/")
        time.sleep(5)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div[1]/button/div').click()
        time.sleep(5)

x = instegram(user,password,x,y,z)
x.giris()
x.messega()