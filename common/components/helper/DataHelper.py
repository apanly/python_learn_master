# -*- coding: utf-8 -*-
import  hashlib,json
from common.services.BaseService import BaseService


class DataHelper(BaseService):
    @staticmethod
    def md5( text ):
        md5 = hashlib.md5()
        md5.update(str(text).encode("utf-8"))
        return md5.hexdigest()

    @staticmethod
    def jsonEncode( params = {},ensure_ascii = True ):
        return json.dumps(params,ensure_ascii = ensure_ascii)

    @staticmethod
    def jsonDecode( str = "" ):
        try:
            return json.loads( str )
        except Exception as e:
            return dict()

    @staticmethod
    def md5bytes( text ):
        md5 = hashlib.md5()
        md5.update(str(text).encode('utf-8'))
        return md5.digest()

    @classmethod
    def sha1(cls,txt):
        s = hashlib.sha1()
        # 对创建的hash对象更新需要加密的字符串
        s.update(txt.encode("utf-8"))
        # 加密处理
        return s.hexdigest()
