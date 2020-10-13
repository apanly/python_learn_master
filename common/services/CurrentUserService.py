# -*- coding: utf-8 -*-
from flask import g
import hashlib,random,string
from common.services.BaseService import BaseService
from common.services.CommonConstant import CommonConstant

class CurrentUserService( BaseService):

    @staticmethod
    def isRoot():
        return CurrentUserService.getField( "is_root" ,0) == CommonConstant.default_status_true

    @staticmethod
    def getRoleId():
        return CurrentUserService.getField( "role_id",0 )

    @staticmethod
    def getUid():
        return CurrentUserService.getField("id", 0)

    @staticmethod
    def getInfo():
        return  g.current_user if hasattr( g,"current_user" ) else None

    @staticmethod
    def getField( f,default = False):
        current_user = g.current_user
        if hasattr( current_user,f ):
            return getattr(current_user, f)
        return default



    '''
        用户信息加密
        可以把多个字段进行加密，还可以把状态放到里面，这样状态变了就会立即退出
    '''
    @staticmethod
    def userAuthToken(user_info):
        m = hashlib.md5()
        str = "%s-%s-%s-%s" % (user_info.id, user_info.email, user_info.salt, user_info.name)
        m.update(str.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def geneSalt( length = 16 ):
        keylist = [random.choice((string.ascii_letters + string.digits)) for i in range(length)]
        return ("".join(keylist))


