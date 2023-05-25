# -*- coding: utf-8 -*-
from application import app
from common.services.BaseService import BaseService
import os

class FileHelper( BaseService):

    @staticmethod
    def makeSuredirs( path ):
        if not os.path.exists( path ):
            os.makedirs( path )

    @staticmethod
    def getLogPath( path = '' ):
        return "{0}{1}".format( app.config.get( 'LOG_ROOT_PATH' ),path )

    @staticmethod
    def saveContent( path, content):
        with open(path, mode='w+', encoding='utf-8') as f:
            f.write(content)
            f.flush()
            f.close()

    @staticmethod
    def getContent(path,default = ''):
        if os.path.exists( path ):
            with open( path,"r" ) as f:
                return f.read()
        return default
