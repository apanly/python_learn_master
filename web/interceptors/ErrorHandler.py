# -*- coding: utf-8 -*-
from application import app
from common.components.helper.UtilHelper import UtilHelper
from common.services.AppLogService import AppLogService


@app.errorhandler(404) #捕获应用的异常
def error_404(e):
    err_msg = getErrMsg()
    AppLogService.addErrLog(err_msg)
    return UtilHelper.renderView( "home/error/error.html",{ "status":404,"msg":"很抱歉！,您访问的页面不存在 ~~" } )

@app.errorhandler(500) #捕获应用的异常
def error_500(e):
    err_msg = getErrMsg()
    AppLogService.addErrLog(err_msg)
    return UtilHelper.renderView("home/error/error.html",{ "status":500,"msg":"服务器错误" })

@app.errorhandler(502) #捕获应用的异常
def error_502(e):
    err_msg = getErrMsg()
    AppLogService.addErrLog(err_msg)
    return UtilHelper.renderView("home/error/error.html")


@app.errorhandler(Exception)
def error_exception( e ):
    err_msg = getErrMsg()
    AppLogService.addErrLog( err_msg )
    if UtilHelper.isAjax():
        return UtilHelper.renderErrJSON( "系统错误，错误原因:%s<br/>%s"%( str( e.__class__).replace("<",""),str( e ) ) )

    return UtilHelper.renderView("home/error/error.html", {"status": 500, "msg": err_msg })


def getErrMsg():
    import traceback, sys
    exc_type, exc_value, exc_obj = sys.exc_info()
    err_msg = "exception_type: \t%s,\nexception_value: \t%s,\nexception_object: \t%s,\n" % (
        exc_type, exc_value, traceback.format_exc())
    return err_msg

