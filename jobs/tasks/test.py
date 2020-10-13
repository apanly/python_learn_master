# -*- coding: utf-8 -*-
import logging
from flask.logging import default_handler
from jobs.BaseJob import BaseJob
from common.services.notice.NewsService import NewsService
from application import app

class JobTask( BaseJob ):
    def __init__(self):
        ## 设置Job使用debug模式
        app.config['DEBUG'] = True
        logging_format = logging.Formatter(
            '%(levelname)s %(asctime)s %(filename)s:%(funcName)s L%(lineno)s %(message)s')
        default_handler.setFormatter(logging_format)

    def run(self, params):
        news_params = {
            "uid" : 1,
            "title" : "定制化 Flask 框架 V2.0",
            "content" : "新功能更多~~"
        }

        NewsService.addNews( news_params )
        app.logger.info( "这是测试job,会写入一条站内信" )
        return True