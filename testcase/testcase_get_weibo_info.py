#! /usr/bin/env python3
# coding=utf-8

import unittest
from selenium import webdriver
from common.loggings import log
from common.selenium_api import SeleniumApi


class TestcaseGetWeiboInfo(unittest.TestCase):
    """获取微博热搜信息"""
    def setUp(self):
        self.driver = webdriver.Edge()
        self.selenium_api = SeleniumApi(self.driver)
        self.web_element1 = '//*[@id="app"]/div[1]/div[1]/div[1]/a/aside/label/div'
        self.web_element2 = '//*[@id="app"]/div[1]/div[1]/div[2]/div/div/div[10]/div/div/h4'
        self.web_element3 = '//*[@class="m-link-icon"]/img/../../span[1]'
        self.web_element4 = '//*[@class="m-link-icon"]/img'
        log.info("start testcase_get_weibo_info")

    def testcase_get_weibo_info(self):
        self.selenium_api.get("https://m.weibo.cn/")
        self.selenium_api.maximize_window()
        self.selenium_api.click_the_element(by="xpath", element=self.web_element1)
        self.selenium_api.click_the_element(by="xpath", element=self.web_element2)
        hot_search_list = self.selenium_api.find_elements(by="xpath", elements=self.web_element3)
        type_list = self.selenium_api.find_elements(by="xpath", elements=self.web_element4)
        for i in range(len(hot_search_list)):
            log.info(f"微博热搜榜{i+1}:{hot_search_list[i].text}, link-icon:{type_list[i].get_attribute('src')}")
        self.selenium_api.get_screenshot()

    def tearDown(self):
        self.selenium_api.quit()
        log.info("testcase_get_weibo_info finsh")


if __name__ == '__main__':
    unittest.main()
