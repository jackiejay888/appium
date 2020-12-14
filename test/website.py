from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import selenium


driver = webdriver.Chrome()
driver.get('https://www.google.com.tw/')

sleep(5)

driver.close()

os.system(selenium.__version__)