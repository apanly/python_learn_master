# -*- coding: utf-8 -*-

'''
基础Job类
'''
class BaseJob():
    def exitOK(self):
        return 0

    def exitFail(self,exit_code = 1):
        return exit_code