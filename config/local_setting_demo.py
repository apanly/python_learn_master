# -*- coding: utf-8 -*-
'''
修改文件名为local_setting.py，然后作为本地开发配置
'''
from config.base_setting import *
DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS=False
#mysql://user:password@127.0.0.1/database?charset=utf8mb4
SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1/learn_master?charset=utf8mb4'
SQLALCHEMY_ENCODING = "utf8mb4"

## 域名配置
DOMAIN = {
    "www": "http://127.0.0.1:" + str( SERVER_PORT ),
    "api": "http://127.0.0.1:" + str( API_SERVER_PORT ),
    "resource" : "http://127.0.0.1:" + str( SERVER_PORT ) + "/static/cdn"
}


##登录方式配置项
LOGIN_TYPE_MAP = {
    "open_wechat":True,
    "mp_wechat": False,
    "email" : True
}

##开发平台登录配置项 这里申请：https://open.weixin.qq.com/
WECHAT_OPEN = {
    "app_id" : "xxxxxxx",
    "sec_key" : "xxxxx"
}

