# -*- coding: utf-8 -*-
from common.services.BaseService import BaseService
from flask import render_template, jsonify,g

'''
统一封装response简易方法
'''
class ResponseHelper(BaseService):

    @staticmethod
    def renderView(template, context={}):
        if 'current_user' in g:
            context['current_user'] = g.current_user

        if 'merchant_info' in g:
            context['merchant_info'] = g.merchant_info

        if 'menus' in g:
            context['menus'] = g.menus
        return render_template(template, **context)

    @classmethod
    def renderPopView(cls,template, context={}):
        content = render_template(template, **context)
        return cls.renderSucJSON(data = { "content": content} )

    @classmethod
    def renderSucJSON(cls,data={}, msg="操作成功~~", code=200):
        resp = {'code': code, 'msg': msg, 'data': data}
        return jsonify(resp)

    @classmethod
    def renderErrJSON(cls,msg="操作失败~~", data={}, code=-1):
        return cls.renderSucJSON(data=data, msg=msg, code=code)

