# -*- coding: utf-8 -*-
from flask import Blueprint,request
from application import  db
from common.components.helper.UtilHelper import UtilHelper
from common.components.helper.ValidateHelper import ValidateHelper
from common.models.notice.UserNews import UserNews
from common.services.CommonConstant import CommonConstant
from common.services.CurrentUserService import CurrentUserService
from common.models.rbac.User import ( User )

route_home_profile = Blueprint('home_profile_page', __name__)

@route_home_profile.route("/")
@route_home_profile.route("/index")
def home_index():
    return UtilHelper.renderView( "home/user/profile/index.html",{ "info":CurrentUserService.getInfo() }  )

@route_home_profile.route("/set_info",methods=[ "GET","POST" ])
def set_info():
    if UtilHelper.isGet():
        return UtilHelper.renderPopView("home/user/profile/set_info.html", {"info": CurrentUserService.getInfo() })
    req = request.values
    name = req.get("name", "").strip()
    email = req.get("email", "").strip()
    if not ValidateHelper.validLength(name, 1, 10):
        return UtilHelper.renderErrJSON("请输入符合规范的姓名~~")

    if not ValidateHelper.validEMail(email):
        return UtilHelper.renderErrJSON("请输入符合规范的邮箱~~")

    info = CurrentUserService.getInfo()
    if not info:
        return UtilHelper.renderErrJSON( CommonConstant.SYSTEM_DEFAULT_ERROR )

    has_in = User.query.filter(User.email == email, User.id != info.id ).first()
    if has_in:
        return UtilHelper.renderErrJSON("该邮箱已存在，请换一个再试~~")

    info.name = name
    info.email = email
    db.session.add(info)
    db.session.commit()
    return UtilHelper.renderSucJSON()


@route_home_profile.route("/news")
def home_news():
    req = request.values
    kw = req.get("kw", "").strip()
    status = int( req.get("status",CommonConstant.default_status_neg_99) )
    page = int(req.get("p", 1))

    query = UserNews.query.filter_by( uid = CurrentUserService.getUid() )
    if kw:
        query = query.filter(UserNews.title.ilike('%{}%'.format(kw)))

    if status > CommonConstant.default_status_neg_99:
        query = query.filter_by( status = status )
    page_params = {
        "total": query.count(),
        "page_size": CommonConstant.PAGE_SIZE,
        "page": page,
        "display": CommonConstant.PAGE_DISPLAY
    }

    pages = UtilHelper.iPagination(page_params)
    offset = (page - 1) * CommonConstant.PAGE_SIZE
    limit = CommonConstant.PAGE_SIZE * page
    list = query.order_by(UserNews.id.desc())[offset:limit]

    sc = {
        'kw': kw,
        'status': status
    }
    return UtilHelper.renderView("home/user/profile/news.html",{"list": list,"pages":pages,"sc":sc })


@route_home_profile.route("/news/ops",methods=[ "POST" ])
def news_ops():
    req = request.values
    id = int(req['id']) if ('id' in req and req['id']) else 0
    if not id:
        return UtilHelper.renderErrJSON( CommonConstant.SYSTEM_DEFAULT_ERROR )


    info = UserNews.query.filter_by( id = id,uid = CurrentUserService.getUid() ).first()
    if not info:
        return UtilHelper.renderErrJSON( "指定站内信不存在" )

    info.status = CommonConstant.default_status_true
    db.session.add( info )
    db.session.commit()
    return UtilHelper.renderSucJSON()


@route_home_profile.route("/news/batch_ops",methods=[ "POST" ])
def news_batch_ops():
    UserNews.query.filter_by( uid = CurrentUserService.getUid() ).update({"status": CommonConstant.default_status_true })
    db.session.commit()
    return UtilHelper.renderSucJSON()


