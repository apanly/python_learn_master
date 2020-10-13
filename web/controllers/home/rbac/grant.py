# -*- coding: utf-8 -*-

from flask import Blueprint,request
from application import db
from common.components.helper.UtilHelper import UtilHelper
from common.components.helper.ValidateHelper import ValidateHelper
from common.components.helper.ModelHelper import ModelHelper
from common.models.rbac.Action import ( Action )
from common.models.rbac.RoleAction import ( RoleAction )
from common.models.rbac.Role import ( Role )
from common.models.rbac.User import ( User )
from common.services.CommonConstant import CommonConstant
from common.services.RBACService import RBACService

route_home_grant = Blueprint('home_grant_page', __name__)

@route_home_grant.route("/")
@route_home_grant.route("/index")
def grant_index():
    req = request.values
    page = int(req.get("p", 1))

    query = Action.query
    page_params = {
        "total": query.count(),
        "page_size": CommonConstant.PAGE_SIZE,
        "page": page,
        "display": CommonConstant.PAGE_DISPLAY
    }

    pages = UtilHelper.iPagination(page_params)
    offset = (page - 1) * CommonConstant.PAGE_SIZE
    limit = CommonConstant.PAGE_SIZE * page

    list = query.order_by(Action.id.desc())[offset:limit]
    sc = {}
    set_flag = RBACService.checkPageRelatePrivilege("set")
    ops_flag = RBACService.checkPageRelatePrivilege("ops")
    return UtilHelper.renderView("home/rbac/grant/index.html", {
        "list": list,
        "pages": pages,
        "sc": sc,
        "set_flag": set_flag,
        "ops_flag": ops_flag,
    }  )



@route_home_grant.route("/set",methods=[ "POST","GET" ])
def grant_set():
    if UtilHelper.isGet() :
        req = request.values
        id = int( req['id'] ) if ( 'id' in req and req['id'] )else 0
        act = req.get("act","").strip()
        info = None
        if id > 0:
            info = Action.query.filter_by( id=id ).first()


        weight_list = [1]
        weight_list.extend( range(5,65,5) )

        if act == "copy" and info:
            info.id = 0
        return UtilHelper.renderPopView( "home/rbac/grant/set.html",{ "info":info,"weight_list":weight_list, }  )

    req = request.values
    id = int(req['id']) if ('id' in req and req['id']) else 0
    level1_name = req.get("level1_name","").strip()
    level2_name = req.get("level2_name","").strip()
    name = req.get("name","").strip()
    url = req.get("url","").strip()
    level1_weight = int( req.get("level1_weight","1").strip() )
    level2_weight = int( req.get("level2_weight","1").strip() )
    weight = int( req.get("weight","1").strip() )


    if not ValidateHelper.validLength( level1_name,1,10 ):
        return UtilHelper.renderErrJSON("请输入符合规范的一级菜单名称~~")

    if not ValidateHelper.validLength( level2_name,1,10 ):
        return UtilHelper.renderErrJSON("请输入符合规范的二级菜单名称~~")

    if not ValidateHelper.validLength( name,1,10 ):
        return UtilHelper.renderErrJSON("请输入符合规范的权限名称~~")

    info = Action.query.filter_by(id=id).first()
    if info:
        model_action = info
    else:
        model_action = Action()

    model_action.level1_name = level1_name
    model_action.level2_name = level2_name
    model_action.name = name
    model_action.url = url.replace("\r\n",",")
    model_action.level1_weight = level1_weight
    model_action.level2_weight = level2_weight
    model_action.weight = weight

    db.session.add( model_action )
    db.session.commit()
    return UtilHelper.renderSucJSON()


@route_home_grant.route("/ops",methods=[ "POST" ])
def grant_ops():
    req = request.values
    id = int(req['id']) if ('id' in req and req['id']) else 0
    act = req.get("act","").strip()
    allow_act = [ 'del','recovery' ]
    if not id:
        return UtilHelper.renderErrJSON( CommonConstant.SYSTEM_DEFAULT_ERROR )

    if act not in allow_act:
        return UtilHelper.renderErrJSON(CommonConstant.SYSTEM_DEFAULT_ERROR)

    info = Action.query.filter_by(id=id).first()
    if not info:
        return UtilHelper.renderErrJSON( "指定权限不存在" )

    if act == "del":
        info.status = CommonConstant.default_status_false
    elif act == "recovery":
        info.status = CommonConstant.default_status_true

    db.session.add( info )
    db.session.commit()
    return UtilHelper.renderSucJSON()


@route_home_grant.route("/assign",methods=[ "POST","GET" ])
def grant_assign():
    if UtilHelper.isGet() :
        req = request.values
        role_id = int( req.get("role_id", 0) )
        role_pid = int( req.get("role_pid", 0) )
        '''
        取出来所有的一级部门
        '''
        p_role_list = Role.query.filter_by(pid=CommonConstant.default_status_false)\
            .order_by( Role.id.asc() ).all()

        if not role_pid and p_role_list :#如果没有父部门，那就选择一个
            role_pid = p_role_list[0].id

        sub_role_list = Role.query.filter_by( pid = role_pid)\
            .order_by( Role.id.asc() ).all()

        if not role_id and sub_role_list:
            role_id = sub_role_list[0].id

        user_list = User.query.filter_by( status = CommonConstant.default_status_true, role_id = role_id).all()

        action_list = Action.query.filter_by( status = CommonConstant.default_status_true )\
            .order_by( Action.level1_weight.desc(),Action.level2_weight.desc(),Action.weight.desc() ).all()

        action_data = {}
        if action_list:
            for item in action_list:
                tmp_level1_key = item.level1_name
                tmp_level2_key = item.level2_name
                if tmp_level1_key not in action_data:
                    action_data[ tmp_level1_key ] = {
                        "name" : tmp_level1_key,
                        "counter" : 0,
                        "sub" : {}
                    }

                if tmp_level2_key not in action_data[ tmp_level1_key ]['sub']:
                    action_data[tmp_level1_key]['sub'][ tmp_level2_key ] = {
                        "name": tmp_level2_key,
                        "counter": 0,
                        "act_list": []
                    }


                action_data[tmp_level1_key]['counter'] += 1
                action_data[tmp_level1_key]['sub'][tmp_level2_key]['counter'] += 1

                tmp_data = {
                    "id" : item.id,
                    "name" : item.name,
                    "is_important": item.is_important
                }
                action_data[tmp_level1_key]['sub'][tmp_level2_key]['act_list'].append( tmp_data )


        owned_act = RoleAction.query.filter_by(role_id=role_id,status = CommonConstant.default_status_true).all()
        owned_act_ids = ModelHelper.getFieldList(owned_act, 'action_id')

        sc = {
            "role_id" : role_id,
            "role_pid" : role_pid,
        }

        return UtilHelper.renderView("home/rbac/grant/assign.html", {
            "list": action_data,
            "p_role_list":p_role_list,
            "sub_role_list":sub_role_list,
            "user_list":user_list,
            "owned_act_ids":owned_act_ids,
            "sc" : sc
        })

    req = request.values
    role_id = int( req.get("role_id",0) )
    action_ids = request.form.getlist("action_ids[]")
    action_ids = list(map(int, action_ids))
    if not role_id or role_id < 1 :
        return UtilHelper.renderErrJSON( "请选择部门在分配权限~~" )

    info = Role.query.filter_by( id = role_id).first()
    if not info:
        return UtilHelper.renderErrJSON("请选择部门在分配权限 -2~~")
    ###分配权限逻辑还是挺复杂的
    ## 已有的权限
    owned_act = RoleAction.query.filter_by( role_id = role_id ).all()
    owned_act_ids = ModelHelper.getFieldList(owned_act,'action_id')
    '''
    找出删除的权限（生产环境数据库没有删除权限）
    假如已有的权限集合是A，界面传递过得权限集合是B
    权限集合A当中的某个权限不在权限集合B当中，就应该删除
    计算差集
    '''
    delete_act_ids = list(set( owned_act_ids ) - set( action_ids ) )
    if delete_act_ids:
        RoleAction.query.filter( RoleAction.role_id == role_id,RoleAction.action_id.in_( delete_act_ids ) )\
            .update({ "status":CommonConstant.default_status_false },synchronize_session = False)
        db.session.commit()
    '''
    找出添加的权限
    假如已有的权限集合是A，界面传递过得权限集合是B
    权限集合B当中的某个权限不在权限集合A当中，就应该添加
    计算差集
    '''
    add_act_ids = list(set( action_ids ) - set( owned_act_ids ) )
    if add_act_ids:
        for _action_id in add_act_ids:
            _model_role_action = RoleAction()
            _model_role_action.role_id = role_id
            _model_role_action.action_id = _action_id
            db.session.add( _model_role_action )
        db.session.commit()
    '''
    找出需要更新的权限（生产环境数据库没有删除权限）
    假如已有的权限集合是A，界面传递过得权限集合是B
    权限集合B当中的某个权限也在在权限集合A当中，就应该更新
    计算补集
    '''
    update_act_ids = list(set(owned_act_ids).intersection( set( action_ids ) ))
    if update_act_ids:
        RoleAction.query.filter(RoleAction.role_id == role_id, RoleAction.action_id.in_(update_act_ids)) \
            .update({"status": CommonConstant.default_status_true}, synchronize_session=False)
        db.session.commit()

    return UtilHelper.renderSucJSON({},"权限分配成功~~")
