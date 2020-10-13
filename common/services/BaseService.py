# -*- coding: utf-8 -*-

class BaseService(object):
    #私有类变量
    __error_msg = None
    __error_code = None

    @staticmethod
    def _err( msg = None,code = -1):
        BaseService.__error_msg = msg if msg is not None else "操作失败"
        BaseService.__error_code = code
        return False

    @staticmethod
    def getLastErrorMsg():
        return BaseService.__error_msg if BaseService.__error_msg else ""
