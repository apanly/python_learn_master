# -*- coding: utf-8 -*-
from application import app
from jobs.launcher import runJob,jobList
from flask.cli import FlaskGroup
import sys,click

def createApp():
    return app

cli = FlaskGroup( create_app = createApp )

@cli.command("jobList")
def getJobList():

    jobList().run()

'''
–或-：参数前缀
default: 设置命令行参数的默认值
help: 参数说明
type: 参数类型，可以是 str, int, float ,也可以是选择参数
prompt: 当在命令行中没有输入相应的参数时，会根据 prompt 提示用户输入
hide_input: 隐藏输入的参数
confirmation_prompt：对输入的命令参数检查两次是否一致
nargs: 指定命令行参数接收的值的个数, -1 表示可以接收多个参数
python manage_job.py runjob -m test -a aaa  -p 1 -p 2 -p 3
'''
@cli.command("runjob")
@click.option("-m","--name",help="指定job名",required=True)
@click.option("-a","--act",help="Job动作",required=False)
@click.option("-p","--param",help="业务参数",default = (),required=False, multiple=True)
def handleJob(*args,**kwargs):
    runJob().run( **kwargs )


if __name__ == '__main__':
    try:
        with app.app_context():
            #sys.exit( cli.main() )
            sys.exit( cli() )
    except Exception as e:
        app.logger.info( e )