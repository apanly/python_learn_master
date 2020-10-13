# coding: utf-8
from application import db


class Link(db.Model):
    __tablename__ = 'link'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='类型')
    title = db.Column(db.String(100, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='标题')
    url = db.Column(db.String(300, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='网址')
    weight = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='权重 越大越排前')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态： 1：有效  0：无效')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='最后一次更新时间')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='插入时间')
