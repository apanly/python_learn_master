# -*- coding: utf-8 -*-
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import sys,os


class Application(Flask):
    def __init__(self, import_name,template_folder = None,static_folder = None,root_path = None):
        super(Application, self).__init__(import_name,template_folder = template_folder,static_folder = static_folder,root_path = root_path)
        self.config.from_pyfile('config/base_setting.py')

        ##获取环境变量决定使用哪个配置文件覆盖
        ops_config = os.environ.get("ops_config","local")
        config_path = '%s/config/%s_setting.py'%( root_path,ops_config.strip() )
        if os.path.exists( config_path  ):
            self.config.from_pyfile( config_path )

        ##设置环境
        self.config['jxjm_env'] = ops_config

        db.init_app(self)

    def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
        if endpoint is None:
            endpoint = rule

        super(Application, self).add_url_rule(   rule,   endpoint=endpoint, view_func=view_func,  **options )


##获取根目录路径
os.chdir( sys.path[0] )
root_path = os.path.abspath( os.path.join(os.getcwd(), ".") )

db = SQLAlchemy()
app = Application( __name__ ,template_folder = None ,static_folder = None,root_path = root_path )
manager = Manager( app )



