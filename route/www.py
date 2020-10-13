# -*- coding: utf-8 -*-
'''
专门为web程序准备的初始化入口
'''
from application import app
from common.components.helper.StaticPluginsHelper import StaticPluginsHelper
from common.components.helper.UtilHelper import UtilHelper
from common.services.GlobalUrlService import GlobalUrlService
from common.services.CommonConstant import CommonConstant

'''
toolbar
'''

# from flask_debugtoolbar import DebugToolbarExtension
# toolbar = DebugToolbarExtension(app)

'''
函数模板
'''
app.add_template_global(GlobalUrlService, 'GlobalUrlService')
app.add_template_global(StaticPluginsHelper, 'StaticPluginsHelper')
app.add_template_global(UtilHelper, 'UtilHelper')
app.add_template_global(CommonConstant, 'CommonConstant')

'''
统一拦截处理和统一错误处理
'''

from web.interceptors.AuthHome import  *
from web.interceptors.AuthWWW import  *
from web.interceptors.ErrorHandler import  *

'''
蓝图功能，对所有的url进行蓝图功能配置
'''

from web.controllers.route import *


