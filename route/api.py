# -*- coding: utf-8 -*-
'''
专门为wapi程序准备的初始化入口
'''

'''
统一拦截处理和统一错误处理
'''
from api.interceptors.Auth import  *
from api.interceptors.ErrorHandler import  *


'''
蓝图功能，对所有的url进行蓝图功能配置
'''
from api.controllers.route import *

