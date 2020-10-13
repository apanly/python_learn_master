# -*- coding: utf-8 -*-

from common.services.BaseService import BaseService
from flask import render_template,g,jsonify,request
from common.components.helper.UAHelper import UAHelper

class UtilHelper( BaseService):

    @staticmethod
    def isAjax():
        '''
        request.is_xhr有bug ，因为Werkzeug版本问题
        需要Werkzeug==0.16.1，等后面官方修复了这个bug再用，自己学再判断算了
        '''
        if  hasattr(request,"is_xhr") and request.is_xhr:
            return True

        head_ajax = request.headers.get("X-Requested-With","")
        if head_ajax == "XMLHttpRequest":
            return True

        return False

    @staticmethod
    def isGet():
        return request.method == "GET"

    @staticmethod
    def renderView(template, context={}):
        if 'current_user' in g:
            context['current_user'] = g.current_user

        if 'menus' in g:
            context['menus'] = g.menus
        return render_template(template, **context)

    @staticmethod
    def renderPopView(template, context={}):
        content =  render_template(template, **context)
        return UtilHelper.renderSucJSON( data = { "content":content } )


    @staticmethod
    def renderSucJSON(data = {},msg="操作成功~~",code = 200 ):
        resp = {'code': code, 'msg': msg, 'data': data}
        return jsonify(resp)

    @staticmethod
    def renderErrJSON(msg="操作失败~~", data={},code = -1):
        return UtilHelper.renderSucJSON( data = data,msg = msg,  code = code )


    @staticmethod
    def isPC():
        return UAHelper.isPC()




    '''
    自定义分页类
    '''

    @staticmethod
    def iPagination(params):
        import math

        ret = {
            "is_prev": 1,
            "is_next": 1,
            "from": 0,
            "end": 0,
            "current": 0,
            "total_pages": 0,
            "page_size": 0,
            "total": 0,
            "url": params['url'] if hasattr( params,'url' ) else request.path
        }

        total = int(params['total'])
        page_size = int(params['page_size'])
        page = int(params['page'])
        display = int(params['display'])
        total_pages = int(math.ceil(total / page_size))
        total_pages = total_pages if total_pages > 0 else 1
        if page <= 1:
            ret['is_prev'] = 0

        if page >= total_pages:
            ret['is_next'] = 0

        semi = int(math.ceil(display / 2))

        if page - semi > 0:
            ret['from'] = page - semi
        else:
            ret['from'] = 1

        if page + semi <= total_pages:
            ret['end'] = page + semi
        else:
            ret['end'] = total_pages

        ret['current'] = page
        ret['total_pages'] = total_pages
        ret['page_size'] = page_size
        ret['total'] = total
        ret['range'] = range(ret['from'], ret['end'] + 1)
        return ret