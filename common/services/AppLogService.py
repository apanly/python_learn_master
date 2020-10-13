# -*- coding: utf-8 -*-
import json,re
from common.models.applogs.AppAccessLog import AppAccessLog
from common.models.applogs.AppErrLog import AppErrLog
from common.services.BaseService import BaseService
from application import db,app
from flask import request

class AppLogService(BaseService):
    @staticmethod
    def addErrLog( msg = None ):
        if not msg:
            return AppLogService._err( "错误消息没有~~" )

        try:
            url = request.url
            referrer = request.referrer
            ip = request.remote_addr
            ua = request.user_agent.string
            max_len = 3000
            model_err_log = AppErrLog()
            model_err_log.request_uri = url
            model_err_log.referer = referrer
            model_err_log.content = msg[0:max_len ] if len( msg ) > max_len else msg
            model_err_log.ip = ip
            model_err_log.ua = ua
            db.session.add( model_err_log )
            db.session.commit()
        except Exception as e:
            return AppLogService._err( e )
        return True

    @staticmethod
    def addAccessLog( user_info ):
        try:
            path = request.path
            ignore_urls = [
                "/home/log",
                "/favicon.ico",
                "/home/error"
            ]

            pattern = re.compile('%s' % "|".join(ignore_urls))
            if pattern.match( path ):
                return

            target_url = request.url
            referrer = request.referrer
            ip = request.remote_addr
            ua = request.user_agent.string

            params = request.values.to_dict()
            model_access_log = AppAccessLog()
            model_access_log.uid = user_info.id if hasattr(user_info,"id" ) else 0
            model_access_log.uname = user_info.name if  hasattr(user_info,"name" ) else ''
            model_access_log.referer_url = referrer
            model_access_log.target_url = target_url
            model_access_log.query_params = json.dumps( params )
            model_access_log.ua = ua
            model_access_log.ip = ip
            db.session.add(model_access_log)
            db.session.commit()
        except Exception as e:
            app.logger.info( e )
            return AppLogService._err( e )
        return True