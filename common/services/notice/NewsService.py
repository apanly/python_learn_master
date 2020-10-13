# -*- coding: utf-8 -*-
from common.models.notice.UserNews import UserNews
from common.services.BaseService import BaseService
from application import db

class NewsService( BaseService ):
    @staticmethod
    def addNews( params ):
        model_user_news = UserNews( **params )
        db.session.add( model_user_news )
        db.session.commit()
