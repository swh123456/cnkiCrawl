#-*-coding:gbk-*-
__author__ = 'Administrator'
filename=""
# class ReadTxt:
#     def __init__(self,filename):
#         self.filename=filename
#         file=open(filename)
#         for line in file:
#             return line
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox() # Get local session of firefox
browser.get("http://www.yahoo.com") # Load page
# assert "Yahoo!" in browser.title
elem = browser.find_element_by_name("p") # Find the query box
elem.send_keys(u'北京邮电大学' + Keys.RETURN)
time.sleep(0.2) # Let the page load, will be added to the API
try:
    browser.find_element_by_link_text(u'北京邮电大学').click()
except NoSuchElementException:
    assert 0, "can't find seleniumhq"
browser.close()




