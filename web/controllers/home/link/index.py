# -*- coding: utf-8 -*-
from flask import Blueprint,request
from application import db
from common.components.helper.UtilHelper import UtilHelper
from common.components.helper.ValidateHelper import ValidateHelper
from common.models.link.Link import Link
from common.services.CommonConstant import CommonConstant
from common.services.RBACService import RBACService

route_home_link = Blueprint('home_link_page', __name__)

@route_home_link.route("/")
@route_home_link.route("/index")
def link_index():
    req = request.values
    kw = req.get("kw","").strip()
    page = int(req.get("p", 1))

    query = Link.query
    if kw:
        query = query.filter( Link.title.ilike( '%{}%'.format(kw) ) )

    page_params = {
        "total": query.count(),
        "page_size": CommonConstant.PAGE_SIZE,
        "page": page,
        "display": CommonConstant.PAGE_DISPLAY
    }

    pages = UtilHelper.iPagination(page_params)
    offset = (page - 1) * CommonConstant.PAGE_SIZE
    limit = CommonConstant.PAGE_SIZE * page
    list = query.order_by( Link.id.desc() )[offset:limit]

    sc = {
        'kw': kw
    }

    set_flag = RBACService.checkPageRelatePrivilege("set")
    ops_flag = RBACService.checkPageRelatePrivilege("ops")
    return UtilHelper.renderView("home/link/index.html",{
        "list": list,
        "pages":pages,
        "type_map":CommonConstant.link_type_map,
        "sc":sc ,
        "set_flag" : set_flag,
        "ops_flag" : ops_flag,
    })

@route_home_link.route("/set",methods=[ "POST","GET" ])
def link_set():
    if UtilHelper.isGet() :
        req = request.values
        id = int( req['id'] ) if ( 'id' in req and req['id'] )else 0
        info = None
        if id > 0:
            info = Link.query.filter_by( id=id ).first()
        return UtilHelper.renderPopView( "home/link/set.html",{ "info":info,"type_map":CommonConstant.link_type_map }  )

    req = request.values
    id = int(req['id']) if ('id' in req and req['id']) else 0
    type = int( req.get("type",0).strip() )
    title = req.get("title","").strip()
    url = req.get("url","").strip()
    weight = int(req.get("weight", 1).strip())

    if  type < 1 :
        return UtilHelper.renderErrJSON( "请选择分类~~" )

    if not ValidateHelper.validLength( title,1,30 ):
        return UtilHelper.renderErrJSON("请输入符合规范的标题~~")

    if not ValidateHelper.validUrl( url ):
        return UtilHelper.renderErrJSON("请输入符合规范的网址~~")

    info = Link.query.filter_by(id=id).first()
    if info:
        model_link = info
    else:
        model_link = Link()

    model_link.type = type
    model_link.title = title
    model_link.url = url
    model_link.weight = weight
    db.session.add( model_link )
    db.session.commit()
    return UtilHelper.renderSucJSON()


@route_home_link.route("/ops",methods=[ "POST" ])
def link_ops():
    req = request.values
    id = int(req['id']) if ('id' in req and req['id']) else 0
    act = req.get("act","").strip()
    allow_act = [ 'del','recovery' ]
    if not id:
        return UtilHelper.renderErrJSON( CommonConstant.SYSTEM_DEFAULT_ERROR )

    if act not in allow_act:
        return UtilHelper.renderErrJSON(CommonConstant.SYSTEM_DEFAULT_ERROR)

    info = Link.query.filter_by(id=id).first()
    if not info:
        return UtilHelper.renderErrJSON( "指定链接不存在" )

    if act == "del":
        info.status = CommonConstant.default_status_false
    elif act == "recovery":
        info.status = CommonConstant.default_status_true

    db.session.add( info )
    db.session.commit()
    return UtilHelper.renderSucJSON()

