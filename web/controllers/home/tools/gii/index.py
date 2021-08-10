# -*- coding: utf-8 -*-
import os,re
from flask import Blueprint,request
from application import app,db
from common.components.helper.UtilHelper import UtilHelper

route_home_gii = Blueprint('home_gii_page', __name__)

@route_home_gii.route("/")
@route_home_gii.route("/index")
def gii_index():
    return UtilHelper.renderView( "/home/tools/gii/index.html"  )


@route_home_gii.route("/model",methods=[ "POST","GET" ])
def gii_model():
    default_path_prefix = "/common/models/"
    if UtilHelper.isGet():
        db.reflect()
        #dict_keys 转 list
        table_list = list( db.metadata.tables.keys() )
        table_list.sort()
        return UtilHelper.renderView( "/home/tools/gii/model.html",{
            "default_path_prefix":default_path_prefix,
            "table_list" : table_list
        })

    req = request.values

    table = req.get("table", "").strip()
    path = req.get("path", "").strip()

    ##后面这里的数据库做成选择的，因为有多数据库的可能
    engine_uri = app.config.get( 'SQLALCHEMY_DATABASE_URI','' )
    folder_path = app.root_path + default_path_prefix + path
    #不存在就新建
    if not os.path.exists( folder_path ):
        os.makedirs( folder_path )

    model_name = ( table.replace( "-"," " ).replace( "_"," " ).title() ).replace(" ","")
    model_path = folder_path + "/" + model_name + ".py"

    #2>&1 标准错误重定向到标准输出, --noinflect 不把复数处理成单数 例如 user_news 会变成 UserNew
    cmd = 'flask-sqlacodegen "{0}" --noinflect --tables {1} --outfile "{2}"  --flask 2>&1'.format( engine_uri ,table,model_path)
    print( cmd )
    p = os.popen( cmd )
    out_list = p.readlines()
    p.close()
    if  out_list and len( out_list ) > 0:
        return UtilHelper.renderErrJSON( "失败原因：" + "<br/>".join( out_list) )

    ##为了不破坏扩展，实现正则替换，读文件，按行替换
    if not os.path.exists( model_path ):
        return UtilHelper.renderErrJSON("model文件不存在，无法执行替换~~")
    try:
        f = open( model_path )
        ret = []
        ret.append( "# coding: utf-8\n" )
        ret.append( "from application import db\n\n" )
        ignore_kws = [ "from flask_sqlalchemy","from sqlalchemy","SQLAlchemy","coding: utf-8" ]
        line_break_kws = [ "\n","\r\n" ]
        for line in f.readlines():
            tmp_break_flag = False
            for _ignore_kw in ignore_kws:
                if _ignore_kw in line:
                    tmp_break_flag = True
                    break

            if tmp_break_flag:
                continue

            if line in line_break_kws:
                continue
            ret.append( line )
        f.close()

        ##最后加一些常用方法
        common_funcs = '''
    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])
        '''
        f = open( model_path , "w", encoding="utf-8")
        f.write( "".join(ret) + common_funcs )
        f.flush()
        f.close()
    except Exception as e:
        pass

    return UtilHelper.renderSucJSON()


@route_home_gii.route("/job",methods=[ "POST","GET" ])
def gii_job():
    default_path_prefix = "/jobs/tasks/"
    if UtilHelper.isGet():

        return UtilHelper.renderView( "/home/tools/gii/job.html",{
            "default_path_prefix":default_path_prefix
        })

    req = request.values

    filename = req.get("filename", "").strip()
    path = req.get("path", "").strip()
    note = req.get("note", "").strip()

    ##后面这里的数据库做成选择的，因为有多数据库的可能
    folder_path = app.root_path + default_path_prefix + path
    #不存在就新建
    if not os.path.exists( folder_path ):
        os.makedirs( folder_path )

    task_path = folder_path + "/" + filename + ".py"

    module_task = ( ( path + "/" ) if path else '' ) + filename
    tips = 'python {0}/manage_job.py runjob -m {1}'.format( app.root_path,module_task )

    try:
        content = '''
# -*- coding: utf-8 -*-
import logging
from flask.logging import default_handler
from jobs.BaseJob import BaseJob
from application import app

\'\'\'
{0}
{1}
\'\'\'
class JobTask( BaseJob ):
    def __init__(self):
        ## 设置Job使用debug模式
        app.config['DEBUG'] = True
        logging_format = logging.Formatter(
            '%(levelname)s %(asctime)s %(filename)s:%(funcName)s L%(lineno)s %(message)s')
        default_handler.setFormatter(logging_format)

    def run(self, params):
        app.logger.info( "执行命令是：{0}" )
        app.logger.info( "这是自动生成的job" )
        return self.exitOK()        
        '''.format( note,tips )


        f = open( task_path , "w", encoding="utf-8")
        f.write( content )
        f.flush()
        f.close()
    except Exception as e:
        pass

    return UtilHelper.renderSucJSON()