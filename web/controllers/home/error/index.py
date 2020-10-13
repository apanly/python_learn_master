# -*- coding: utf-8 -*-
from flask import Blueprint,request

from common.components.helper.UtilHelper import UtilHelper

route_home_error = Blueprint('home_error_page', __name__)

@route_home_error.route("/ban")
def error_ban():
    req = request.values
    msg = req.get("msg", "").strip()
    return UtilHelper.renderView( "/home/error/ban.html",{ "msg":msg }  )