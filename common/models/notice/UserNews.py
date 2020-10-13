# coding: utf-8
from application import db

class UserNews(db.Model):
    __tablename__ = 'user_news'
    id = db.Column(db.Integer, primary_key=True, info='消息id')
    uid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='用户id')
    title = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue(), info='标题')
    content = db.Column(db.String(1500), nullable=False, server_default=db.FetchedValue(), info='内容')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态 0：未读 1：已读')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])
        