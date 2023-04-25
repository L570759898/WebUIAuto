#! /usr/bin/env python3
# coding=utf-8

import unittest
from selenium import webdriver
from common.loggings import log
from common.selenium_api import SeleniumApi


class TestcaseGetWeather(unittest.TestCase):
    """获取天气信息"""
    def setUp(self):
        self.driver = webdriver.Edge()
        self.selenium_api = SeleniumApi(self.driver)
        self.country_xpath = '//*[@class="forecastBox"]/dl/dd/a[2]/span/../../../dt/a'
        self.minimum_xpath = '//*[@class="forecastBox"]/dl/dd/a[2]/span'
        self.maximum_xpath = '//*[@class="forecastBox"]/dl/dd/a[3]/b'
        log.info("start testcase_get_weather")

    def testcase_get_weather(self):
        self.selenium_api.get('http://www.weather.com.cn/html/province/hubei.shtml')
        self.selenium_api.maximize_window()
        country = self.selenium_api.find_elements(by="xpath", elements=self.country_xpath)
        minimum_tmp = self.selenium_api.find_elements(by="xpath", elements=self.minimum_xpath)
        maximum_tmp = self.selenium_api.find_elements(by="xpath", elements=self.maximum_xpath)
        for i in range(len(country)):
            log.info(f"{country[i].text}地区最低气温为:{minimum_tmp[i].text}, 最高气温为:{maximum_tmp[i].text}")
        self.selenium_api.get_screenshot()

    def tearDown(self):
        self.selenium_api.quit()
        log.info("testcase_get_weather finsh")


if __name__ == '__main__':
    unittest.main()
