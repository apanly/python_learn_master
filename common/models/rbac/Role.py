# coding: utf-8
from application import db





class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True, info='角色ID')
    name = db.Column(db.String(255, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='角色名')
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='父级id')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1有效 0无效')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='最后一次更新时间')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='插入时间')
