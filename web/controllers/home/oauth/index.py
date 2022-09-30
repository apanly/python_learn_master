# -*- coding: utf-8 -*-
import json
from flask import Blueprint,request
from flask import request,redirect,g,make_response
from application import db,app

from common.models.oauth.UserOauthBind import UserOauthBind
from common.models.rbac.User import User
from common.services.CurrentUserService import CurrentUserService
from common.services.GlobalUrlService import GlobalUrlService
from common.services.wechat.WeChatService import WeChatService
from common.components.helper.ConfigHelper import ConfigHelper
from common.components.helper.DateHelper import DateHelper

route_home_oauth_index = Blueprint('home_oauth_index', __name__)

@route_home_oauth_index.route("/open-login")
def oauth_login():
    req = request.values
    code = req.get("code", "").strip()
    state = req.get("state", "").strip()
    redirect_url = GlobalUrlService.buildHomeUrl("/user/login")
    if not code:
        return redirect(redirect_url)

    ret = WeChatService.getAccessToken(code)
    if not ret:
        return redirect(redirect_url)

    openid = ret.get("openid", "")
    unionid = ret.get("unionid", "")
    if not openid:
        return redirect(redirect_url)

    bind_info = UserOauthBind.query.filter_by(openid=openid, status=ConfigHelper.getConstantConfig('default_status_true')
    , type=ConfigHelper.getConstantConfig('LOGIN_TYPE_WECHAT_OPEN')).first()
    if not bind_info:
        return redirect(redirect_url)

    user_info = User.query.filter_by( id= bind_info.user_id, status= ConfigHelper.getConstantConfig('default_status_true') ).first()
    if not user_info:
        return redirect(redirect_url)

    next_url = GlobalUrlService.buildHomeUrl("/")
    response = make_response(redirect( next_url ) )
    # 确保隔日凌晨一点cookie必须失效
    today_last_timestamp = DateHelper.getTimestamps(DateHelper.getCurrentTime('%Y-%m-%d 23:59:59'))
    today_now_timestamp = DateHelper.getTimestamps(DateHelper.getCurrentTime())
    expired_time = today_last_timestamp - today_now_timestamp + 3600

    response.set_cookie(ConfigHelper.getConstantConfig('AUTH_COOKIE_NAME'),
                        '%s#%s' % (CurrentUserService.userAuthToken(user_info), user_info.id),
                        expired_time, httponly=True)  # 保存120天
    return response


@route_home_oauth_index.route("/open-bind")
def oauth_bind():
    req = request.values
    code = req.get("code","").strip()
    state = req.get("state","").strip()
    redirect_url = GlobalUrlService.buildHomeUrl("/profile/index")
    if not code:
        return redirect( redirect_url )

    ret = WeChatService.getAccessToken( code )
    if not ret:
        return redirect(redirect_url)

    openid = ret.get("openid","")
    unionid = ret.get("unionid","")
    if not openid:
        return redirect(redirect_url)

    if not CurrentUserService.getUid():
        return redirect(redirect_url)

    bind_info = UserOauthBind.query.filter_by( openid = openid,user_id= CurrentUserService.getUid()
                                   ,type = ConfigHelper.getConstantConfig( 'LOGIN_TYPE_WECHAT_OPEN') ).first()
    if bind_info and bind_info.status == ConfigHelper.getConstantConfig( 'default_status_true'):
        return redirect(redirect_url)

    ##如果存在但是状态是解绑状态那就重新更新为已绑定
    if bind_info and bind_info.status == ConfigHelper.getConstantConfig( 'default_status_false'):
        bind_info.status = ConfigHelper.getConstantConfig( 'default_status_true')
        db.session.add( bind_info )
        db.session.commit()
        return redirect(redirect_url)

    params = {
        "user_id":CurrentUserService.getUid(),
        "openid":openid,
        "unionid":unionid,
        "type":ConfigHelper.getConstantConfig( 'LOGIN_TYPE_WECHAT_OPEN')
    }
    model_user_oauth = UserOauthBind( **params )
    db.session.add(model_user_oauth)
    db.session.commit()
    return redirect(redirect_url)


