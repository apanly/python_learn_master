# coding: utf-8
from application import db


class AppErrLog(db.Model):
    __tablename__ = 'app_err_log'

    id = db.Column(db.Integer, primary_key=True)
    request_uri = db.Column(db.String(255, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='请求uri')
    referer = db.Column(db.String(500, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='来源url')
    content = db.Column(db.String(3000, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='日志内容')
    ip = db.Column(db.String(100, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='ip')
    ua = db.Column(db.String(1000, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='ua信息')
    created_time = db.Column(db.DateTime, nullable=False, index=True, server_default=db.FetchedValue(), info='插入时间')
