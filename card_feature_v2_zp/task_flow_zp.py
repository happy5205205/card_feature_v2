# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 21:35
# @Author  : zhangpeng
# @Site    : 
# @File    : task_flow_zp.py
# @desc    : 处理征信的流程
import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
import logging

# import warnings
# from card_feature_v2_zp.tools


if __name__ == '__main__':
    os.chdir('E:/04-mySpace/card_feature_v2_zp')
    now_dt = datetime.now().strftime('%Y-%m-d')
    # 定义日志，以及日志级别
    logging.basicConfig(filename=os.getcwd()+'{0}.log'.format(now_dt))
