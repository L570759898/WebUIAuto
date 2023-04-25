#! /usr/bin/env python3
# coding=utf-8

import time
import unittest
from selenium import webdriver
from common.loggings import log
from common.selenium_api import SeleniumApi
from selenium.webdriver.common.keys import Keys


class TestcasePlayCloudmusic(unittest.TestCase):
    """播放网易云音乐"""
    def setUp(self):
        self.driver = webdriver.Edge()
        self.selenium_api = SeleniumApi(self.driver)
        self.web_element1 = 'srch'
        self.web_element2 = '//*[@id="m-search"]/div[2]/div/div/div[1]/div[2]/div/div/a'
        self.web_element3 = '//*[@id="content-operation"]/a[1]'
        log.info("start testcase_play_cloudmusic")

    def testcase_play_cloudmusic(self, music_name="燕归巢-许嵩", duration=30):
        self.selenium_api.get("https://music.163.com/#")
        self.selenium_api.maximize_window()
        log.info(f"搜索{music_name}")
        self.selenium_api.send_keys_to_element(by="id", element=self.web_element1, value=music_name + Keys.ENTER)
        self.selenium_api.switch_to_frame("g_iframe")
        self.selenium_api.click_the_element(by="xpath", element=self.web_element2)
        log.info(f"播放搜索到的第一首音乐")
        self.selenium_api.click_the_element(by="xpath", element=self.web_element3)
        self.selenium_api.get_screenshot()
        time.sleep(duration)

    def tearDown(self):
        self.selenium_api.quit()
        log.info("testcase_play_cloudmusic finsh")


if __name__ == '__main__':
    unittest.main()
