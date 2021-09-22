from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
type(browser)
browser.get("https://play2048.co/")
htmlElem = browser.find_element_by_tag_name('html')
for i in range(100):
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)
time.sleep(30)
browser.quit()
