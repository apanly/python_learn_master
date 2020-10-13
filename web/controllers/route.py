# -*- coding: utf-8 -*-
from application import  app
'''
蓝图功能，对所有的url进行蓝图功能配置
'''

from web.controllers.www.index import route_www_index
from web.controllers.static import route_static
from web.controllers.home.tools.gii.index import route_home_gii
from web.controllers.home.error.index import route_home_error
from web.controllers.home.index import route_home_index
from web.controllers.home.user.User import route_home_user
from web.controllers.home.user.Profile import route_home_profile
from web.controllers.home.rbac.staff import route_home_staff
from web.controllers.home.rbac.dept import route_home_dept
from web.controllers.home.rbac.grant import route_home_grant
from web.controllers.home.log.log import route_home_log
from web.controllers.home.link.index import route_home_link


MODULES = (
    ( route_www_index, '/' ),
    ( route_static, '/static' ),
    ( route_home_index, '/home' ),
    ( route_home_gii, '/home/tools/gii' ),
    ( route_home_error, '/home/error' ),
    ( route_home_log, '/home/log' ),
    ( route_home_staff, '/home/rbac/staff' ),
    ( route_home_dept, '/home/rbac/dept' ),
    ( route_home_grant, '/home/rbac/grant' ),
    ( route_home_link, '/home/link' ),
    ( route_home_user, '/home/user' ),
    ( route_home_profile, '/home/profile' ),
)


def setting_modules(app, modules):
    """ 注册Blueprint模块 """
    for module, url_prefix in modules:
        app.register_blueprint(module, url_prefix=url_prefix)

setting_modules(app, MODULES)