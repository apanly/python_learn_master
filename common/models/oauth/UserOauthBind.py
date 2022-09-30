# coding: utf-8
from application import db

class UserOauthBind(db.Model):
    __tablename__ = 'user_oauth_bind'
    __table_args__ = (
        db.Index('uk_user_id_openid', 'user_id', 'openid'),
    )
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='用户id')
    openid = db.Column(db.String(80, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='第三方id')
    unionid = db.Column(db.String(100, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='第三方用户统一标识id')
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='绑定类型（1：企业微信，2：公众号）')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态 1：有效 0：无效')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='最后更新时间')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='插入时间')

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])
        