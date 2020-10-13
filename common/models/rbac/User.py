# coding: utf-8
from application import db





class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='用户名')
    email = db.Column(db.String(50, 'utf8mb4_general_ci'), nullable=False, unique=True, server_default=db.FetchedValue(), info='邮箱地址也是登录用户名')
    role_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='人员所属部门')
    salt = db.Column(db.String(64, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='随机码')
    is_root = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否是管理员 1：是 0：不是')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态 1：有效 0：无效')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='最后一次更新时间')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='插入时间')
