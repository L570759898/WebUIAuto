#! /usr/bin/env python3
# coding=utf-8

import os
import time
import unittest
import HTMLTestRunner
from config import constant


# 指定扫描指定的文件目录，将符合命名规则的py文件加入测试套件
# 参数一：被执行文件的路径  参数二：被执行文件的名字
suite = unittest.defaultTestLoader.discover(constant.TESTCASE_PATH, pattern='testcase*.py')
# 生成报告的路径, rb wb ab  二进制的读写和追加
current_time = time.strftime("%Y%m%d%H%M%S")
file = open(os.path.join(constant.LOG_PATH, current_time[:-6], f"report-{current_time}.html"), 'wb')
# 设置报告文件
runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='自动化测试报告', description=time.strftime("%Y%m%d_%H%M%S"))
# 执行testcase
runner.run(suite)
file.close()
