# -*- coding: utf-8 -*-
from application import app
from route.www import *
import click

##设置模板路径
app.template_folder = app.root_path + "/web/templates/"
'''
https://medium.datadriveninvestor.com/migrating-flask-script-to-flask-2-0-cli-4a5eee269139
'''
def main():
    app.run( host='0.0.0.0', port=app.config.get('SERVER_PORT'), debug=True )

if __name__ == '__main__':
    try:
        import sys
        sys.exit( main() )
    except Exception as e:
        app.logger.info( e )