# coding: utf-8
from application import db





class Action(db.Model):
    __tablename__ = 'action'

    id = db.Column(db.Integer, primary_key=True, info='权限ID')
    level1_name = db.Column(db.String(20, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='一级菜单名称')
    level2_name = db.Column(db.String(20, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='二级菜单名称')
    name = db.Column(db.String(20, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='权限名')
    url = db.Column(db.String(255, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='允许访问的链接,用特殊字符分割')
    level1_weight = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='一级菜单权重')
    level2_weight = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='二级菜单权重')
    weight = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='权重 越大排名越前面')
    is_important = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否是重要权限')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1 有效 0无效')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='最后一次更新时间')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='插入时间')
