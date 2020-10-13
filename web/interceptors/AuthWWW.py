# -*- coding: utf-8 -*-

from application import app
from flask import request,redirect,g,make_response
import re

from common.components.helper.UtilHelper import UtilHelper
from common.services.AppLogService import AppLogService
from common.services.CommonConstant import CommonConstant
from common.services.GlobalUrlService import GlobalUrlService

'''
前端拦截器，一般不做强制登录要求
'''
@app.before_request
def before_request():
    method = request.method.lower()
    path = request.path
    if "/home" in path:
        return
    return


@app.after_request
def after_request( response ):

    return response
