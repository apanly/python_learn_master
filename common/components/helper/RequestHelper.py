# -*- coding: utf-8 -*-
from common.services.BaseService import BaseService
from flask import request

'''
统一封装获取参数
'''
class RequestHelper(BaseService):
    @staticmethod
    def isAjax():
        '''
        request.is_xhr有bug ，因为Werkzeug版本问题
        需要Werkzeug==0.16.1，等后面官方修复了这个bug再用，自己学再判断算了
        '''
        if hasattr(request, "is_xhr") and request.is_xhr:
            return True

        head_ajax = request.headers.get("X-Requested-With", "")
        if head_ajax == "XMLHttpRequest":
            return True

        return False

    @staticmethod
    def isGet():
        return request.method == "GET"

    @staticmethod
    def getInt( name = "",default = 0 ):
        if not name:
            return default
        req = request.values.to_dict()
        if name not in req:
            return default

        val = req.get(name).strip()
        try:
            val = int( val )
        except:
            val = default
        return val

    @staticmethod
    def getString(name="", default=""):
        if not name:
            return default
        req = request.values.to_dict()
        if name not in req:
            return default

        val = req.get(name).strip()
        try:
            val = str(val)
        except:
            val = default
        return val

    # 获取文件
    @staticmethod
    def getFile(name="", default=None):
        if not name:
            return default
        try:
            var = request.files[name]
        except Exception:
            var = default
        return var
    @staticmethod
    def getRemoteIp():
        return request.remote_addr
