# -*- coding: utf-8 -*-

from application import app
from flask import request,redirect,g,make_response
import re

from common.components.helper.UtilHelper import UtilHelper
from common.models.rbac.User import ( User )
from common.services.AppLogService import AppLogService
from common.services.CommonConstant import CommonConstant
from common.services.CurrentUserService import CurrentUserService
from common.services.GlobalUrlService import GlobalUrlService
from common.services.RBACService import RBACService
from common.services.MenuServiceService import MenuServiceService

'''
Home后台授权拦截器，一般做用户登录判断
'''
@app.before_request
def before_request():
    ignore_urls  = app.config['IGNORE_URLS_HOME']
    ignore_check_login_urls  = app.config['IGNORE_CHECK_LOGIN_URLS']
    path = request.path
    #如果是静态文件就不要查询用户信息了
    pattern = re.compile('%s' % "|".join( ignore_check_login_urls ) )
    if pattern.match( path ) or "/home" not in path:
        return

    # 多查询一次数据也没有什么问题
    user_info = check_login()
    g.current_user = None
    if user_info:
        g.current_user = user_info

    #将忽略数组换成字符串
    pattern = re.compile('%s' % "|".join( ignore_urls ) )
    if pattern.match( path ):
        return

    if not user_info :
        response = make_response( redirect(GlobalUrlService.buildHomeUrl("/user/logout")))
        return response

    #判断RBAC的权限
    if not RBACService.checkPrivilege( path ):
        if UtilHelper.isAjax():
            return UtilHelper.renderErrJSON("无权限，请联系管理员" )
        response = make_response(redirect( GlobalUrlService.buildHomeUrl("/error/ban",{ "msg" : path }) ))
        return response

    g.menus = MenuServiceService.getMenu()
    AppLogService.addAccessLog( user_info )
    return


@app.after_request
def after_request( response ):
    #清理收尾工作
    return response

def check_login():
    cookies = request.cookies
    cookie_name = CommonConstant.AUTH_COOKIE_NAME
    auth_cookie = cookies[ cookie_name ] if cookie_name in cookies else None
    if auth_cookie is None:
        return False

    auth_info = auth_cookie.split("#")
    if len(auth_info) != 2:
        return False

    try:
        user_info = User.query.filter_by( id= auth_info[1] ).first()
    except Exception:
        return False

    if user_info is None or not user_info.status:
        return False

    if CurrentUserService.userAuthToken(user_info) != auth_info[0]:
        return False

    return user_info
