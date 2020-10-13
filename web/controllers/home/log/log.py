# -*- coding: utf-8 -*-
from flask import Blueprint,request

from common.components.helper.DateHelper import DateHelper
from common.components.helper.UtilHelper import UtilHelper
from common.models.applogs.AppAccessLog import AppAccessLog
from common.models.applogs.AppErrLog import AppErrLog
from common.services.CommonConstant import CommonConstant

route_home_log = Blueprint('home_log_page', __name__)

@route_home_log.route("/access")
def log_access():
    req = request.values
    page = int( req.get("p",1) )
    date_from = req.get("date_from",DateHelper.getCurrentTime(  fmt = "%Y-%m-%d" ))
    date_to = req.get("date_to",DateHelper.getCurrentTime(  fmt = "%Y-%m-%d" ))
    query = AppAccessLog.query.filter( AppAccessLog.created_time.between( date_from,date_to + " 23:59:59" ) )

    page_params = {
        "total": query.count(),
        "page_size": CommonConstant.PAGE_SIZE,
        "page": page,
        "display": CommonConstant.PAGE_DISPLAY,
    }

    pages = UtilHelper.iPagination(page_params)
    offset = (page - 1) * CommonConstant.PAGE_SIZE
    limit = CommonConstant.PAGE_SIZE * page
    list = query.order_by( AppAccessLog.id.desc())[offset:limit]

    sc = {
        'date_from': date_from,
        'date_to': date_to
    }
    return UtilHelper.renderView( "home/log/access.html",{"list": list,"pages":pages,"sc":sc }  )

@route_home_log.route("/error")
def log_error():
    req = request.values
    page = int(req.get("p", 1))
    date_from = req.get("date_from", DateHelper.getCurrentTime(fmt="%Y-%m-%d"))
    date_to = req.get("date_to", DateHelper.getCurrentTime(fmt="%Y-%m-%d"))
    query = AppErrLog.query.filter(AppErrLog.created_time.between(date_from, date_to + " 23:59:59" ))

    page_params = {
        "total": query.count(),
        "page_size": CommonConstant.PAGE_SIZE,
        "page": page,
        "display": CommonConstant.PAGE_DISPLAY,
    }

    pages = UtilHelper.iPagination(page_params)
    offset = (page - 1) * CommonConstant.PAGE_SIZE
    limit = CommonConstant.PAGE_SIZE * page
    list = query.order_by(AppErrLog.id.desc())[offset:limit]

    sc = {
        'date_from': date_from,
        'date_to': date_to
    }
    return UtilHelper.renderView("home/log/error.html", {"list": list, "pages": pages, "sc": sc})


