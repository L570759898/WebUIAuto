#! /usr/bin/env python3
# coding=utf-8

import unittest
from selenium import webdriver
from common.loggings import log
from common.selenium_api import SeleniumApi


class TestcaseJdSearch(unittest.TestCase):
    """获取京东秒杀信息"""
    def setUp(self):
        self.driver = webdriver.Edge()
        self.selenium_api = SeleniumApi(self.driver)
        self.web_element1 = '//*[@id="navitems-group1"]/li/a'
        self.web_element2 = '//*[@class="seckill_mod_goodslist clearfix"]/li/a/h4'
        self.web_element3 = '//*[@id="super_seckill"]/div/ul/li/div/span/span[1]/i'
        log.info("start testcase_jd_search")

    def testcase_jd_search(self):
        self.selenium_api.get('https://www.jd.com/')
        self.selenium_api.maximize_window()
        for element in self.selenium_api.find_elements(by="xpath", elements=self.web_element1):
            element.click()
        for handle in self.selenium_api.get_window_handles():
            self.selenium_api.switch_to_window(handle)
            if self.selenium_api.get_title() == "京东秒杀-正品保证、天天低价、限时限量":
                break
            else:
                self.selenium_api.close()
        ms_list = self.selenium_api.find_elements(by="xpath", elements=self.web_element2)
        ms_price = self.selenium_api.find_elements(by="xpath", elements=self.web_element3)
        for product in range(len(ms_list)):
            log.info(f"京东秒杀-正品保证、天天低价、限时限量商品:{ms_list[product].text}, 价格:{ms_price[product].text}")
        self.selenium_api.get_screenshot()

    def tearDown(self):
        self.selenium_api.quit()
        log.info("testcase_jd_search finsh")


if __name__ == '__main__':
    unittest.main()
