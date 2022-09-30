# -*- coding: utf-8 -*-
APP_NAME = "即学即码实验室"
APP_VERSION = "V1.0"
SERVER_PORT = 8889
API_SERVER_PORT = 8888

'''
有可能你使用浏览器看到的一串字符串(ascii编码)不是那么容易看懂的，
这是因为python底层使用unicode编码。
通过设置下面的参数可以解决这个问题。
'''
JSON_AS_ASCII = False


DEBUG = True
DEBUG_TB_INTERCEPT_REDIRECTS = True
SQLALCHEMY_ECHO = False
SECRET_KEY = 'ZoDWffA2deeVOzii'

## 域名配置
DOMAIN = {
    "www": "http://192.168.33.10:" + str( SERVER_PORT ),
    "api": "http://192.168.33.10:" + str( API_SERVER_PORT ),
    "resource" : "http://static.cdn.jixuejima.cn"
}


##过滤url
IGNORE_URLS_HOME = [
    "^/home/user/login",
    "^/home/user/logout",
    "^/home/oauth/",
]

## 权限过滤的
IGNORE_URLS_HOME_RRIVILEGE = [
    "^/home/error",
    "^/home/profile",
]


IGNORE_URLS_WWW = [
]

##登录忽略url
IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

##HTTP请求超时时间
HTTP_TIMEOUT = 5

##日志存放位置 一定不能放在tmp目录 tmp有自己的回收机制了
LOG_ROOT_PATH = "/data/www/logs/learn_master"
##版本号文件
RELEASE_PATH = "/data/www/release_version/learn_master"

