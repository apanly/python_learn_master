# -*- coding: utf-8 -*-
import re
from common.services.BaseService import BaseService
from common.services.CommonConstant import CommonConstant
from common.services.CurrentUserService import CurrentUserService
from common.models.rbac.RoleAction import ( RoleAction )
from common.models.rbac.Action import ( Action )
from common.components.helper.ModelHelper import ModelHelper
from flask import  g,request
from application import app

# g只和每一次请求有关系，请求完了就没有了

class RBACService( BaseService):
    @staticmethod
    def checkPrivilege( url = "",ignore_root = False ):
        ignore_privilege_urls = app.config['IGNORE_URLS_HOME_RRIVILEGE']

        if not ignore_root and CurrentUserService.isRoot():
            return True

        pattern = re.compile('%s' % "|".join( ignore_privilege_urls ))
        if pattern.match( url ) :
            return True
        return url in RBACService.getRolePrivilege()

    '''
    返回页面相关链接权限判断
    例如 当前页面是 link/index
    你想判断 link/set 权限，直接传递 set 参数就行了
    '''
    @staticmethod
    def checkPageRelatePrivilege( uri = '' ,ignore_root = False):
        path = request.path
        page_url_arr = path.split("/")
        page_url_arr[ len(page_url_arr) - 1 ] = uri
        check_url = "/".join(page_url_arr)
        return RBACService.checkPrivilege( check_url ,ignore_root)

    '''
    判断当前人是否有当前url的个人my | 下属sub | 全部的权限all
    当然type是其他的也可以的
    '''

    @staticmethod
    def checkDataPrivilege( type = 'all',ignore_root = False ):
        path = request.path
        check_url = path + "_" + type;
        return RBACService.checkPrivilege( check_url,ignore_root )

    @staticmethod
    def getRolePrivilege( role_id = 0 ):
        role_id = role_id if role_id else CurrentUserService.getRoleId()
        #所属角色拥有的权限
        if 'privilege_url' not in g or not g.privilege_url or len( g.privilege_url ) < 1 :
            g.privilege_url = []
            owned_act = RoleAction.query.filter_by(role_id=role_id, status=CommonConstant.default_status_true).all()
            owned_act_ids = ModelHelper.getFieldList(owned_act, 'action_id')
            if not owned_act_ids:
                return g.privilege_url

            owned_act_ids = list(map(int, owned_act_ids))
            act_list = Action.query.filter( Action.status == CommonConstant.default_status_true ,Action.id.in_( owned_act_ids ) ).all()
            if not act_list:
                return g.privilege_url


            for item in act_list:
                tmp_urls = str( item.url ).split(",")
                g.privilege_url.extend( tmp_urls )

        return g.privilege_url



