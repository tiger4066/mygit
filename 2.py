# -*- coding: cp936 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from time import sleep
import time
import os

username=""
password = "" 
brower=webdriver.Firefox()

brower.get("http://vip.jd.com")
time.sleep(2)
brower.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]/a").click()

time.sleep(1)
brower.find_element_by_id('loginname').send_keys(username)
time.sleep(1)
brower.find_element_by_id('nloginpwd').send_keys(password)
time.sleep(1)
brower.find_element_by_id('loginsubmit').click()
time.sleep(5)
brower.find_element_by_xpath("/html/body/div[4]/div[2]/div[3]/div/div/span[1]").click()
brower.quit()



