# -*- coding: utf-8 -*-

from flask import Blueprint,request
from application import db
from common.components.helper.UtilHelper import UtilHelper
from common.components.helper.ValidateHelper import ValidateHelper
from common.components.helper.ModelHelper import ModelHelper
from common.models.rbac.User import ( User )
from common.models.rbac.Role import ( Role )
from common.services.CommonConstant import CommonConstant
from sqlalchemy import or_,and_

from common.services.CurrentUserService import CurrentUserService
from common.services.RBACService import RBACService

route_home_staff = Blueprint('home_staff_page', __name__)

@route_home_staff.route("/")
@route_home_staff.route("/index")
def staff_index():
    req = request.values
    kw = req.get("kw", "").strip()
    page = int(req.get("p", 1))

    query = User.query
    if kw:
        query = query.filter( or_( User.name.ilike( '%{}%'.format(kw) ) ,User.email.ilike( '%{}%'.format(kw) ) ))

    page_params = {
        "total": query.count(),
        "page_size": CommonConstant.PAGE_SIZE,
        "page": page,
        "display": CommonConstant.PAGE_DISPLAY,
    }

    pages = UtilHelper.iPagination(page_params)
    offset = (page - 1) * CommonConstant.PAGE_SIZE
    limit = CommonConstant.PAGE_SIZE * page
    list = query.order_by( User.id.desc() )[offset:limit]

    dept_map = ModelHelper.getDictFilterField( Role )
    sc = {
        'kw': kw
    }

    set_flag = RBACService.checkPageRelatePrivilege("set")
    ops_flag = RBACService.checkPageRelatePrivilege("ops")

    return UtilHelper.renderView( "home/rbac/staff/index.html",   {
        "list": list,
        "pages": pages,
        "dept_map" : dept_map,
        "sc": sc,
        "set_flag": set_flag,
        "ops_flag": ops_flag,
    })


@route_home_staff.route("/set",methods=[ "POST","GET" ])
def staff_set():
    if UtilHelper.isGet() :
        req = request.values
        id = int( req['id'] ) if ( 'id' in req and req['id'] )else 0
        info = None
        if id > 0:
            info = User.query.filter_by( id=id ).first()

        ##部门
        dept_list = Role.query.order_by( Role.pid.asc() ).all()
        dept_data = {}
        if dept_list:
            for item in dept_list:
                if not item.pid  and item.id not in dept_data:
                    dept_data[ item.id ] = {
                        "name": item.name,
                        "sub" : []
                    }

                if item.pid:
                    dept_data[item.pid]['sub'].append( { "id":item.id,"name": item.name } )


        return UtilHelper.renderPopView( "home/rbac/staff/set.html",{ "info":info,"dept_list":dept_data }  )

    req = request.values
    id = int(req['id']) if ('id' in req and req['id']) else 0
    name = req.get("name","").strip()
    email = req.get("email","").strip()
    role_id = int( req.get("role_id",0 ) )


    if not ValidateHelper.validLength( name,1,10 ):
        return UtilHelper.renderErrJSON("请输入符合规范的姓名~~")

    if not ValidateHelper.validEMail( email ):
        return UtilHelper.renderErrJSON("请输入符合规范的邮箱~~")

    if role_id < 1:
        return UtilHelper.renderErrJSON("请选择部门（顶级部门不可选择）~~")

    has_in = User.query.filter(User.email == email, User.id != id).first()
    if has_in:
        return UtilHelper.renderErrJSON("该邮箱已存在，请换一个再试~~")

    info = User.query.filter_by(id=id).first()
    if info:
        model_user = info
    else:
        model_user = User()

    if not model_user.salt:
        model_user.salt = CurrentUserService.geneSalt()

    model_user.name = name
    model_user.email = email
    model_user.role_id = role_id
    db.session.add( model_user )
    db.session.commit()
    return UtilHelper.renderSucJSON()


@route_home_staff.route("/ops",methods=[ "POST" ])
def staff_ops():
    req = request.values
    id = int(req['id']) if ('id' in req and req['id']) else 0
    act = req.get("act","").strip()
    allow_act = [ 'del','recovery' ]
    if not id:
        return UtilHelper.renderErrJSON( CommonConstant.SYSTEM_DEFAULT_ERROR )

    if act not in allow_act:
        return UtilHelper.renderErrJSON(CommonConstant.SYSTEM_DEFAULT_ERROR)

    info = User.query.filter_by(id=id).first()
    if not info:
        return UtilHelper.renderErrJSON( "指定账号不存在" )

    if act == "del":
        info.status = CommonConstant.default_status_false
    elif act == "recovery":
        info.status = CommonConstant.default_status_true

    db.session.add( info )
    db.session.commit()
    return UtilHelper.renderSucJSON()

