# -*- coding: utf-8 -*-
import requests
from common.components.helper.ConfigHelper import ConfigHelper
from common.services.BaseService import BaseService
class WeChatService(BaseService):
    @staticmethod
    def getAccessToken( code = None ):
        if not code:
            return WeChatService._err( "参数code必须传递" )

        config = ConfigHelper.getEnvConfig( 'WECHAT_OPEN',{} )
        get_params = {
            'appid':config['app_id'],
            'secret':config['sec_key'],
            'grant_type':'authorization_code',
            'code' : code
        }
        url = "https://api.weixin.qq.com/sns/oauth2/access_token"
        resp = requests.get( url ,params = get_params)
        ret = resp.json()
        if not ret or 'errcode' in ret:
            return WeChatService._err("获取token失败：%s"%( ret['errcode'] )  )
        return ret
