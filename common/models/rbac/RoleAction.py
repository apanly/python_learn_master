# coding: utf-8
from application import db





class RoleAction(db.Model):
    __tablename__ = 'role_action'
    __table_args__ = (
        db.Index('uk_role_action_id', 'role_id', 'action_id'),
    )

    id = db.Column(db.Integer, primary_key=True, info='角色权限ID')
    role_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='角色ID')
    action_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='权限ID')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1有效 0无效')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='最后一次更新时间')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='插入时间')
