# coding: utf-8
from application import db


class AppAccessLog(db.Model):
    __tablename__ = 'app_access_log'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue(), info='用户表id')
    uname = db.Column(db.String(20, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='用户表姓名')
    referer_url = db.Column(db.String(1000, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='当前访问的refer')
    target_url = db.Column(db.String(1000, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='访问的url')
    query_params = db.Column(db.String(1000, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='get和post参数')
    ua = db.Column(db.String(1000, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='访问ua')
    ip = db.Column(db.String(32, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='访问ip')
    note = db.Column(db.String(1000, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='json格式备注字段')
    created_time = db.Column(db.DateTime, nullable=False, index=True, server_default=db.FetchedValue(), info='插入日期')
