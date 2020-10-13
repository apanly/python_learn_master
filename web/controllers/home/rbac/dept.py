# -*- coding: utf-8 -*-

from flask import Blueprint,request
from application import db
from common.components.helper.UtilHelper import UtilHelper
from common.components.helper.ValidateHelper import ValidateHelper
from common.models.rbac.Role import ( Role )
from common.services.CommonConstant import CommonConstant
from common.services.RBACService import RBACService

route_home_dept = Blueprint('home_dept_page', __name__)

@route_home_dept.route("/")
@route_home_dept.route("/index")
def dept_index():
    dept_list = Role.query.order_by(Role.pid.asc()).all()
    list = []
    if dept_list:
        dept_data = {}
        for item in dept_list:
            if not item.pid and item.id not in dept_data:
                dept_data[item.id] = {
                    "self": item,
                    "sub": []
                }

            if item.pid:
                dept_data[item.pid]['sub'].append( item )

        for item in dept_data.values():
            list.append( item['self'] )
            list.extend( item['sub'])

    set_flag = RBACService.checkPageRelatePrivilege("set")
    ops_flag = RBACService.checkPageRelatePrivilege("ops")

    return UtilHelper.renderView("home/rbac/dept/index.html", {
        "list": list,
        "set_flag": set_flag,
        "ops_flag": ops_flag,
    }  )



@route_home_dept.route("/set",methods=[ "POST","GET" ])
def dept_set():
    if UtilHelper.isGet() :
        req = request.values
        id = int( req['id'] ) if ( 'id' in req and req['id'] )else 0
        info = None
        query_role_list = Role.query.filter_by( pid = CommonConstant.default_status_false )
        if id > 0:
            info = Role.query.filter_by( id=id ).first()
            query_role_list = query_role_list.filter( Role.id != id )

        role_list = query_role_list.order_by( Role.id.desc() ).all()

        return UtilHelper.renderPopView( "home/rbac/dept/set.html",{ "info":info ,"role_list": role_list}  )

    req = request.values
    id = int(req['id']) if ('id' in req and req['id']) else 0
    name = req.get("name","").strip()
    pid = int( req.get("pid","0").strip() )


    if not ValidateHelper.validLength( name,1,10 ):
        return UtilHelper.renderErrJSON("请输入符合规范的姓名~~")

    info = Role.query.filter_by(id=id).first()
    if info:
        model_role = info
        #还不能选择自己的子节点

        if id == pid:
            return UtilHelper.renderErrJSON("不能勾选自己为所属部门哦~~")
    else:
        model_role = Role()

    model_role.name = name
    model_role.pid = pid
    db.session.add( model_role )
    db.session.commit()
    return UtilHelper.renderSucJSON()


@route_home_dept.route("/ops",methods=[ "POST" ])
def dept_ops():
    req = request.values
    id = int(req['id']) if ('id' in req and req['id']) else 0
    act = req.get("act","").strip()
    allow_act = [ 'del','recovery' ]
    if not id:
        return UtilHelper.renderErrJSON( CommonConstant.SYSTEM_DEFAULT_ERROR )

    if act not in allow_act:
        return UtilHelper.renderErrJSON(CommonConstant.SYSTEM_DEFAULT_ERROR)

    info = Role.query.filter_by(id=id).first()
    if not info:
        return UtilHelper.renderErrJSON( "指定部门不存在" )

    if act == "del":
        info.status = CommonConstant.default_status_false
    elif act == "recovery":
        info.status = CommonConstant.default_status_true

    db.session.add( info )
    db.session.commit()
    return UtilHelper.renderSucJSON()