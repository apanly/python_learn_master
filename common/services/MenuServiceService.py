# -*- coding: utf-8 -*-
from common.services.BaseService import BaseService
from application import app
from common.services.RBACService import RBACService


class MenuServiceService( BaseService):
    @staticmethod
    def getMenu():
        menus = MenuServiceService.definedMenu()
        prefix = '/home'
        for _key, _item in menus.items():
            #如果强制设置了不显示，那就不要在判断
            if hasattr( _item ,"hidden") and _item['hidden']:
                continue

            tmp_counter = len( _item['sub'] )
            for _sub_key, _sub_item in enumerate( _item['sub'] ):
                if hasattr(_sub_item, "hidden") and _sub_item['hidden']:
                    tmp_counter -= 1
                    continue
                if not RBACService.checkPrivilege( prefix + _sub_item['url'] ):
                    menus[ _key ]['sub'][_sub_key]['hidden'] = True
                    tmp_counter -= 1

            if tmp_counter <= 0 :
                menus[ _key ]['hidden'] = True
        return menus
    @staticmethod
    def definedMenu():
        menus = {
            "dashboard" :{
                "title" :"仪表盘",
                "icon" : "dashboard",
                "sub" : [
                    { "title" : "首页","url":"/" }
                ]
            },
            "link": {
                "title": "网址之家",
                "icon": "link",
                "sub": [
                    {"title": "网址管理", "url": "/link/index"}
                ]
            },
            "rbac": {
                "title": "员工管理",
                "icon": "user",
                "sub": [
                    {"title": "员工列表", "url": "/rbac/staff/index"},
                    {"title": "部门列表", "url": "/rbac/dept/index"},
                    {"title": "权限分配", "url": "/rbac/grant/assign"},
                    {"title": "权限管理", "url": "/rbac/grant/index"},
                ]
            },
            "log": {
                "title": "系统日志",
                "icon": "info",
                "sub": [
                    {"title": "访问日志", "url": "/log/access"},
                    {"title": "错误日志", "url": "/log/error"}
                ]
            }
        }

        ## 判断环境，如果环境在local，dev这些可以显示gii工具
        if app.config.get("jxjm_env","") in [ "local","dev" ]:
            menus['tools'] = {
                "title": "系统工具",
                "icon": "th-large",
                "sub": [
                    {"title": "Gii", "url": "/tools/gii"}
                ]
            }

        return menus



