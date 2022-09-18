# -*- coding: utf-8 -*-
from application import app
import traceback,os,importlib

'''
python manage runjob -m Test  (  jobs/tasks/Test.py )
python manage runjob -m test  (  jobs/tasks/test.py )
python manage runjob -m test/Index (  jobs/tasks/test/Index.py )
'''
class runJob():

    def run(self,*args,**kwargs):
        ret_params = kwargs
        if "name" not in ret_params or not ret_params['name']:
            return self.tips()

        module_name = ret_params['name'].replace( "/","." )
        try:
            # 官方不建议
            # import_string = "from jobs.tasks.%s import JobTask as  job_target" % ( module_name )
            # exec( import_string , globals() )
            # target = job_target()
            # target.run( ret_params )

            # 官方建议这种方式
            import_string = "jobs.tasks.%s"% ( module_name )
            target = importlib.import_module( import_string )
            exit( target.JobTask().run( ret_params ) )

        except Exception as e:
            traceback.print_exc()


    def tips(self):
        tip_msg = '''
            请正确调度Job
            python manage runjob -m Test  (  jobs/tasks/Test.py )
            python manage runjob -m test/Index (  jobs/tasks/test/Index.py )
        '''
        app.logger.info( tip_msg )
        return False


'''
列出所有的Job
'''
class jobList( ):
    def run(self, *args, **kwargs):
        root_path = app.root_path + "/jobs/tasks/"
        job_names = self.iterFiles( root_path )
        cmd_list = [ "本项目的Job列表" ]
        for job_name in job_names:
            job_name = job_name.replace( root_path,"" ).replace(".py","")
            str = "\t{job_name} ： python manage_job.py runjob -m {job_name}".format( job_name = job_name )
            cmd_list.append( str )

        print( "\r\n".join( cmd_list ) )

    # 遍历文件夹
    def iterFiles(self,root_path ):
        job_names = []
        # 遍历根目录
        ignore = ["__pycache__", "__init__.py",".",".."]
        idx = 0
        for root, dirs, files in os.walk( root_path ):
            if "__pycache__" in root:
                continue

            idx += 1
            for file in files:
                if file in ignore:
                    continue
                file_name = os.path.join(root, file)
                job_names.append( file_name )

        return job_names