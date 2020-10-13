# -*- coding: utf-8 -*-
from flask import Blueprint,request
from common.components.helper.DateHelper import DateHelper
from common.components.helper.UtilHelper import UtilHelper
from common.models.notice.UserNews import UserNews
from common.services.CommonConstant import CommonConstant
from common.services.CurrentUserService import CurrentUserService

route_home_index = Blueprint('home_index_page', __name__)

@route_home_index.route("/")
@route_home_index.route("/index")
def home_index():
    return UtilHelper.renderView( "home/index/index.html"  )


@route_home_index.route("/news")
def home_news():
    query = UserNews.query.filter_by( uid =  CurrentUserService.getUid(),status =  CommonConstant.default_status_false )
    total = query.count()
    list = query.order_by( UserNews.id.desc() ).all()
    data = []
    if list:
        for item in list:
            tmp_content = "<h5 class='text-danger'>标题：%s</h5><br/>%s<br/>时间：%s"%( item.title,item.content,item.created_time )
            tmp_data = {
                "id" : item.id,
                "title" : item.title,
                "content" : tmp_content,
                "created_time" : DateHelper.getFormatDate( DateHelper.str2Date( item.created_time ),format="%m-%d %H:%M" ),
            }
            data.append( tmp_data )
    content = UtilHelper.renderView( "home/index/news.html",{ "list":data ,"total" : total}  )
    return UtilHelper.renderSucJSON( { "total" : total,"content" :content } )



