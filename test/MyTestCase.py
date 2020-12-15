# MyTestCase.py

#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import unittest
import selenium
import time
from appium import webdriver


class MyTestCase(unittest.TestCase):

	@classmethod
	def setUp(self):
		#super().setUp()
		print('selenium version = ', selenium.__version__)
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '4.2.2'
		desired_caps['deviceName'] = '192.168.99.107:5555'
		desired_caps['appPackage'] = 'com.google.android.youtube'
		# desired_caps['app'] = 'F:// debug.apk'
		desired_caps['appActivity'] = 'com.google.android.youtube.HomeActivity'
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

	def test_something(self):
		print('test_something click ------ ')

		# xpath：
		time.sleep(2)
		# self.driver.find_element_by_xpath(
		# 	"//android.widget.ListView/android.widget.TextView[contains(@text,'測試')]").click()

		# uiautomator -UiSelector：
		# name方式在1.5版本後已廢除，能找到介面，不可使用，使用new UiSelector().text替代
		# self.driver.find_element_by_android_uiautomator("newUiSelector().text(\"測試\")").click()

		# class_name - child：
		# items =self.driver.find_elements_by_class_name('android.widget.TextView')
		# items[1].click()

		# id:
		# time.sleep(2)
		# self.driver.find_element_by_id('com.hisense.vod:id/test_video_resize').click()

	@classmethod
	def tearDown(self):
		time.sleep(5)
		print('tearDown ------ ')
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()
