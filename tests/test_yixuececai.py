#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os  # 系统命令
import sys  # python设置
import shutil  # 高级文件操作
import timeit  # 计时相关
import datetime
import time  # 时间相关
import random
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 基地址是本项目根目录
sys.path.append(BASE_DIR)
from yxf_yixue.app_yixuececai.jichufenxi import Pr,P,Cr,C
from yxf_yixue.app_yixuececai.datax import *
from yxf_yixue.app_yixuececai.yuce import *


def work1():
    # 展示理论概率用于对照
    print('理论组六概率：')
    print(str(P(10, 3))+'/'+str(Pr(10, 3))+'='+str(P(10, 3) / Pr(10, 3)))
    print('理论组六包7中奖概率：')
    print(str(C(7, 3) * P(3, 3))+'/'+str(Pr(10, 3))+'='+str(C(7, 3) * P(3, 3) / Pr(10, 3)))
    print('理论组六包4中奖概率：')
    print(str(C(4, 3) * P(3, 3))+'/'+str(Pr(10, 3))+'='+str(C(4, 3) * P(3, 3) / Pr(10, 3)))


def work2():
    # 测试奇门测彩的命中率
    yuce = Yuce()
    yuce.test_qimen()


def work3():
    # 测试八字喜用五行的命中率
    yuce = Yuce()
    yuce.test_bazi()


if __name__ == '__main__':
    print("基础路径：", BASE_DIR)
    # gen_db()  # 生成数据库，只需要在最初执行一次
    work1()
    work2()
