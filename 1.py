# -*- coding: cp936 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from time import sleep
import time
import os

username=u"林文彪"
password = "3874" 
brower=webdriver.Firefox()
brower.get("http://www.lkzx.net")
#brower.get("http://vip.jd.com")
#time.sleep(2)
#brower.find_element_by_link_text('账户登录').click()
time.sleep(2)
#brower.find_element_by_id('_ctl2_Txt_UserName').click() 

brower.find_element_by_id('_ctl2_Txt_UserName').send_keys(username)
time.sleep(1)
brower.find_element_by_id('_ctl2_Txt_Password').send_keys(password)
time.sleep(1)
brower.find_element_by_id('_ctl2_Btn_Login').click() 


