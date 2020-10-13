# -*- coding: utf-8 -*-
from common.services.BaseService import BaseService
from common.services.GlobalUrlService import GlobalUrlService


class StaticPluginsHelper(BaseService):

    @staticmethod
    def daterangepicker():
        res = [
            GlobalUrlService.buildStaticResUrl("/plugins/daterangepicker/daterangepicker.min.css"),
            GlobalUrlService.buildStaticResUrl("/plugins/daterangepicker/moment.min.js"),
            GlobalUrlService.buildStaticResUrl("/plugins/daterangepicker/jquery.daterangepicker.min.js")
        ]
        return StaticPluginsHelper.groupEcho( res )

    @staticmethod
    def select2():
        res = [
            GlobalUrlService.buildStaticResUrl("/plugins/select2/select2.min.css"),
            GlobalUrlService.buildStaticResUrl("/plugins/select2/select2.pinyin.js"),
            GlobalUrlService.buildStaticResUrl("/plugins/select2/zh-CN.js"),
            GlobalUrlService.buildStaticResUrl("/plugins/select2/pinyin.core.js"),
        ]
        return StaticPluginsHelper.groupEcho(res)

    @staticmethod
    def groupEcho( res ):
        ret = []
        for item in res:

            if ".css" in item:
                tmp_res = "<link rel='stylesheet' href='%s'>"%( item )
            else:
                tmp_res = "<script src='%s'></script>" % (item)

            ret.append( tmp_res )

        return "".join( ret)