#! /usr/bin/env python3
# coding=utf-8

# 封装了logging三方库对日志打印、保存到本地的方法

import os
import logging
import datetime
from config import constant


now_time = datetime.datetime.now().strftime('%Y%m%d')
log_path = os.path.join(constant.LOG_PATH, now_time)
log_file_path = os.path.join(log_path, f"log-{now_time}.txt")
if not os.path.exists(log_path):
    os.makedirs(log_path)

log = logging.getLogger("log")
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(module)s %(lineno)s: %(message)s')

# 日志打印到文件
file_handler = logging.FileHandler(log_file_path, mode='a', encoding="UTF-8")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
# 日志打印到屏幕
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

log.setLevel(logging.INFO)
log.addHandler(console_handler)
log.addHandler(file_handler)
