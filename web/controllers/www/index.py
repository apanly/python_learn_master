# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,make_response,redirect
from application import app
import math
from common.models.link.Link import Link
from common.services.CommonConstant import CommonConstant
from common.services.GlobalUrlService import GlobalUrlService
from common.components.helper.ConfigHelper import ConfigHelper

route_www_index = Blueprint('www_index_page', __name__)

@route_www_index.route("/")
def index():
    skip_www = ConfigHelper.getEnvConfig("SKIP_WWW", False)
    if skip_www:
        response = make_response(redirect(GlobalUrlService.buildHomeUrl("/user/login")))
        return response
    www_list = Link.query.filter_by( status = CommonConstant.default_status_true )\
        .order_by( Link.weight.desc(),Link.id.desc() ).all()
    tr_count = int(math.ceil(len(www_list) / 2))
    return render_template( "www/index/index.html" ,www_list=www_list,  tr_list=range(1, tr_count + 1 ) )