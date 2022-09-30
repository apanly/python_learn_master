# -*- coding: utf-8 -*-
from flask import Flask
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
            '''
            \033[显示方式;前景色;背景色m + 结尾部分：\033[0m
            数值表示的参数含义：
            显示方式: 0（默认\）、1（高亮）、22（非粗体）、4（下划线）、24（非下划线）、 5（闪烁）、25（非闪烁）、7（反显）、27（非反显）
            前景色:   30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋 红）、36（青色）、37（白色）
            背景色:   40（黑色）、41（红色）、42（绿色）、 43（黄色）、44（蓝色）、45（洋 红）、46（青色）、47（白色）
            '''
            print( f"\033[1;31m * -----------------------------------------\033[0m" )
            print( f"\033[1;31m * 【jixuejima.com】 loading environment[{ops_config}] config，path：{config_path}\033[0m" )
            print( f"\033[1;31m * -----------------------------------------\033[0m")
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
