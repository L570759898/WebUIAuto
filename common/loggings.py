#! /usr/bin/env python3
# coding=utf-8

# 封装了logging三方库，主要用来进行日志打印

import os
import logging
import datetime
from config import constant


def loggings():
    """新建日志器"""
    global logger, console_handler, file_handler
    now_time = datetime.datetime.now().strftime('%Y%m%d')
    log_file_path = os.path.join(constant.LOG_PATH, now_time)
    logger = logging.getLogger("log")
    logger.setLevel(logging.INFO)
    full_log_path = os.path.join(log_file_path, f"log-{now_time}.txt")
    if not os.path.exists(log_file_path):
        os.system("mkdir %s" % log_file_path)
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(full_log_path, mode='a', encoding="UTF-8")
    console_handler.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    # formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(module)s %(lineno)s: %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    return logger


def debug(msg, *args, **kwargs):
    if not logger.hasHandlers():
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    logger.debug(msg, *args, **kwargs)
    logger.removeHandler(console_handler)
    logger.removeHandler(file_handler)


def info(msg, *args, **kwargs):
    if not logger.hasHandlers():
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    logger.info(msg, *args, **kwargs)
    logger.removeHandler(file_handler)
    logger.removeHandler(console_handler)


def warning(msg, *args, **kwargs):
    if not logger.hasHandlers():
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    logger.warning(msg, *args, **kwargs)
    logger.removeHandler(file_handler)
    logger.removeHandler(console_handler)


def error(msg, *args, **kwargs):
    if not logger.hasHandlers():
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    logger.error(msg, *args, **kwargs)
    logger.removeHandler(file_handler)
    logger.removeHandler(console_handler)


def critical(msg, *args, **kwargs):
    if not logger.hasHandlers():
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    logger.critical(msg, *args, **kwargs)
    logger.removeHandler(file_handler)
    logger.removeHandler(console_handler)


log = loggings()
