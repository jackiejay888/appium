# # -*- coding: utf-8 -*-
# '''
# Created on 2020/12/11

# @author: ZL Chen
# @title: Appium
# '''

from appium import webdriver
import appium
import selenium
import unittest
import sys
import time

print(sys.version)


class mobile(unittest.TestCase):

	def test_initial_setting(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '4.2.2'
		desired_caps['deviceName'] = 'Android Emulator'
		desired_caps['appPackage'] = 'com.android.dialer'
		desired_caps['appActivity'] = 'DialtactsActivity'
		driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		driver.find_element_by_id('com.android.dialer:id/search_box_collapsed').click()
		# search_box = driver.find_element_by_id('com.android.dialer:id/search_view')
		# search_box.click()
		# search_box.send_keys('hello toby')
		time.sleep(4)
		driver.close_app()
		print('PASS')
		pass


if __name__ == '__main__':
	unittest.main()
