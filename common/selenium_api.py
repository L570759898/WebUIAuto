#! /usr/bin/env python3
# coding=utf-8

import os
import time
from selenium import webdriver
from datetime import datetime
from common.loggings import log
from config import constant
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class SeleniumApi(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=10, poll_frequency=0.5)

    def get(self, url, time_to_wait=10):
        # 在当前浏览器会话中打开网页, 10s未加载完则停止加载
        self.driver.get(url)
        self.driver.set_page_load_timeout(time_to_wait)

    def get_title(self):
        # 返回当前页面的标题
        return self.driver.title

    def get_window_handles(self):
        # 返回当前会话中所有窗口的句柄，需要切换到新打开的窗口时新窗口句柄为：window_handles[-1]
        return self.driver.window_handles

    def get_current_window_handle(self):
        # 返回当前窗口的句柄
        return self.driver.current_window_handle

    def close(self):
        # 关闭当前浏览器窗口
        self.driver.close()

    def quit(self):
        # 退出webdriver正在使用的当前窗口
        self.driver.quit()

    def maximize_window(self):
        # 最大化webdriver正在使用的当前窗口
        self.driver.maximize_window()

    def find_element(self, by, element):
        # 采用显示等待方式，在15s内每间隔0.5s扫描一次是否找到对应element控件
        try:
            if by == By.ID:
                # 1、find_element_by_id                  example: //*[@id="query_ticket"]
                self.wait.until(expected_conditions.presence_of_element_located((By.ID, element)))
            elif by == By.XPATH:
                # 2、find_element_by_xpath               example: //*[@id="sear-sel-bd"]/div[2]
                self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, element)))
            elif by == By.NAME:
                # 3、find_element_by_name                example: //*[@name="leftTicketDTO.from_station_name"]
                self.wait.until(expected_conditions.presence_of_element_located((By.NAME, element)))
            elif by == By.TAG_NAME:
                # 4、find_element_by_tag_name            example: find_element_by_tag_name('div')
                self.wait.until(expected_conditions.presence_of_element_located((By.TAG_NAME, element)))
            elif by == By.CLASS_NAME:
                # 5、find_element_by_class_name          example: //*[@class="sear-box quick-sear-box sear-box-lg"]
                self.wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, element)))
            elif by == By.LINK_TEXT:
                # 6、find_element_by_link_text           example: find_element_by_link_text('车次类型：')
                self.wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, element)))
            elif by == By.PARTIAL_LINK_TEXT:
                # 7、find_element_by_partial_link_text   example: find_element_by_partial_link_text('车次')
                self.wait.until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, element)))
            elif by == By.CSS_SELECTOR:
                # 8、find_element_by_css_selector        example: find_element_by_css_selector('div.class')
                self.wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, element)))
            get_element = self.driver.find_element(by=by, value=element)
            self.driver.execute_script('arguments[0].style.border="2px solid red";', get_element)
            time.sleep(0.2)
            return get_element
        except TimeoutException:
            log.warning(f"找不到定位元素：{element}")
            return None

    def find_elements(self, by, elements):
        # 查找给定策略和定位器的所有元素，返回一个列表
        try:
            self.wait.until(expected_conditions.presence_of_all_elements_located((by, elements)))
            return self.driver.find_elements(by=by, value=elements)
        except TimeoutException:
            log.warning(f"找不到定位元素：{elements}")
            return None

    def get_element_text(self, by, element):
        # 获取element控件text
        web_element = self.find_element(by, element)
        if web_element is not None:
            return web_element.text
        else:
            log.warning(f"找不到定位元素：{element}")

    def send_keys_to_element(self, by, element, value):
        # 将键发送到当前聚焦的元素
        web_element = self.find_element(by, element)
        if web_element is not None:
            web_element.clear()
            time.sleep(0.5)
            web_element.send_keys(value)
        else:
            log.warning(f"找不到定位元素：{element}")

    def up_load_file_to_element(self, by, element, file_path):
        # 适用于元素为input且type="file"的文件上传
        web_element = self.find_element(by, element)
        if web_element is not None:
            web_element.send_keys(os.path.abspath(file_path))
        else:
            log.warning(f"找不到定位元素：{element}")

    def click_the_element(self, by, element, sleep_time=1):
        # 鼠标左键单击元素
        web_element = self.find_element(by, element)
        if web_element is not None:
            web_element.click()
            time.sleep(sleep_time)
        else:
            log.warning(f"找不到定位元素：{element}")

    def move_to_element(self, by, element, sleep_time=1):
        # 将鼠标移动到对应元素上
        ActionChains(self.driver).move_to_element(self.find_element(by=by, element=element)).perform()
        time.sleep(sleep_time)

    def scroll_to_element(self, by=None, element=None, sleep_time=1):
        # 如果元素在当前页面视口之外，则将元素的底部滚动到当前页面的底部
        ActionChains(self.driver).scroll_to_element(self.find_element(by=by, element=element)).perform()
        time.sleep(sleep_time)

    def get_screenshot(self, path=None):
        # 将当前窗口的截图保存为PNG图像文件
        if path is None:
            image_path = os.path.join(constant.LOG_PATH, datetime.now().strftime('%Y%m%d'))
            if not os.path.exists(image_path):
                os.makedirs(image_path)
            self.driver.get_screenshot_as_file(image_path + "//" + f"{datetime.now().strftime('%Y%m%d%H%M%S')}.PNG")
        else:
            self.driver.get_screenshot_as_file(path)

    def switch_to_window(self, window_name, sleep_time=1):
        # 将焦点切换到指定的窗口
        self.driver.switch_to.window(window_name)
        time.sleep(sleep_time)

    def switch_to_frame(self, frame_name, sleep_time=1):
        # 将焦点切换到指定frame, by index, name, or web_element
        self.driver.switch_to.frame(frame_name)
        time.sleep(sleep_time)

    def select_the_element(self, by, element, select_type="index", text=None):
        # Select the option at the given index
        # Select all options that have a value matching the argument
        # Select all options that display text matching the argument
        if select_type == "index":
            Select(self.find_element(by, element)).select_by_index(text)
        elif select_type == "value":
            Select(self.find_element(by, element)).select_by_value(text)
        elif select_type == "visible_text":
            Select(self.find_element(by, element)).select_by_visible_text(text)

    def execute_script(self, script):
        # 同步执行当前窗口/frame中的JavaScript
        return self.driver.execute_script(script)

    def scroll_to_focus_element(self, by, element):
        # 聚焦元素
        target = self.find_element(by=by, element=element)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
