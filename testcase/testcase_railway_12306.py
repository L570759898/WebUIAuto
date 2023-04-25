#! /usr/bin/env python3
# coding=utf-8

import unittest
from selenium import webdriver
from common.loggings import log
from common.selenium_api import SeleniumApi


class TestcaseRailway12306(unittest.TestCase):
    """获取12306车票信息"""
    def setUp(self):
        self.driver = webdriver.Edge()
        self.selenium_api = SeleniumApi(self.driver)
        self.place_element = '//*[@id="place_area"]/ul/li[4]/div'
        self.date_element = '//*[@id="toolbar_Div"]/div[38]/div[1]/div[2]/div/div'
        log.info("start testcase_railway_12306")

    def testcase_railway_12306(self, start="武汉", destination="深圳", date="27", times="00002400"):
        self.selenium_api.get('https://kyfw.12306.cn/otn/leftTicket/init')
        self.selenium_api.maximize_window()
        log.info(f"点击出发地选项框, 选择{start}")
        self.selenium_api.click_the_element(by="id", element='fromStationText')
        self.selenium_api.click_the_element(by="xpath", element=f'//*[@title="{start}"]')
        log.info(f"点击目的地选项框, 选择{destination}")
        self.selenium_api.click_the_element(by="id", element='toStationText')
        self.selenium_api.click_the_element(by="xpath", element=f'//*[@title="{destination}"]')
        self.selenium_api.click_the_element(by="xpath", element=self.place_element)
        elements1 = self.selenium_api.find_elements(by="xpath", elements=self.date_element)
        log.info(f"点击出发日选项框, 选择{date}号")
        [day.click() for day in elements1 if date in day.text]
        self.selenium_api.click_the_element(by="id", element="train_type_btn_all")
        log.info(f"选择发车时间{times}, 并点击查询按钮")
        self.selenium_api.select_the_element(by="id", element='cc_start_time', select_type="value", text=times)
        self.selenium_api.click_the_element(by="xpath", element='//*[@id="query_ticket"]')
        log.info(self.selenium_api.get_element_text(by="xpath", element='//*[@id="sear-result"]/p[1]'))
        elements2 = self.selenium_api.find_elements(by="xpath", elements='//*[@id="queryLeftTable"]/tr/td[1]/div')
        if elements2 is not None:
            for element in elements2:
                train_number = element.find_element(by="xpath", value='./div/div/a').text
                start_time = element.find_element(by="xpath", value='./div[3]/strong[1]').text
                arrive_time = element.find_element(by="xpath", value='./div[3]/strong[2]').text
                start_station = element.find_element(by="xpath", value='./div[2]/strong[1]').text
                arrival_station = element.find_element(by="xpath", value='./div[2]/strong[2]').text
                total_duration = element.find_element(by="xpath", value='./div[4]/strong').text
                arrive_day = element.find_element(by="xpath", value='./div[4]/span').text
                log.info("车次:{}, 出发站:{}, 出发时间:{}, 到达站:{}, 到达时间:{}, {}, 历时:{}".format(train_number,
                          start_station, start_time, arrival_station, arrive_time, arrive_day, total_duration))
        else:
            log.info("未找到{}号从{}到{}的车次信息".format(date, start, destination))
        self.selenium_api.get_screenshot()

    def tearDown(self):
        self.selenium_api.quit()
        log.info("testcase_railway_12306 finsh")

if __name__ == '__main__':
    unittest.main()
