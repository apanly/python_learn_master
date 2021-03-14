# -*- coding: utf-8 -*-
from application import app
from common.services.BaseService import BaseService
from common.services.CommonConstant import CommonConstant


class ConfigHelper(BaseService):
    @staticmethod
    def getEnvConfig( config_name = '',default = None ):
        return app.config.get( config_name, default )

    @staticmethod
    def getConstantConfig( config_name = '',default = None):
        if hasattr( CommonConstant ,config_name ):
            return getattr( CommonConstant ,config_name)
        return default