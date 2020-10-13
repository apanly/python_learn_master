# -*- coding: utf-8 -*-
from common.components.helper.DateHelper import DateHelper
from common.services.BaseService import BaseService
from application import app
import os,urllib

class GlobalUrlService( BaseService):
    @staticmethod
    def buildWWWUrl(path,params = {}):
        if  params and len( params ) > 0 :
            path = path + "?" + urllib.parse.urlencode( params )
        config_domain = app.config['DOMAIN']
        return "%s%s" % (config_domain['www'], path)

    @staticmethod
    def buildHomeUrl(path,params = {}):
        if  params and len( params ) > 0 :
            path = path + "?" + urllib.parse.urlencode( params )
        config_domain = app.config['DOMAIN']
        return "%s/home%s" % (config_domain['www'], path)

    @staticmethod
    def buildWWWStaticUrl(path):
        ver = GlobalUrlService.getReleaseVersion()
        path = "/static" + path + "?ver=" + ver
        return GlobalUrlService.buildWWWUrl(path)

    @staticmethod
    def buildStaticResUrl(path):
        config_domain = app.config['DOMAIN']
        return "%s%s" % (config_domain['resource'], path)

    @staticmethod
    def buildNull():
        return "javascript:void(0);"

    @staticmethod
    def getReleaseVersion():
        ver = "%s" % (DateHelper.getCurrentTime("%Y%m%d%H%M%S%f"))
        release_path = app.config.get('RELEASE_PATH')
        if release_path and os.path.exists(release_path):
            with open(release_path, 'r') as f:
                ver = f.readline()

        return ver