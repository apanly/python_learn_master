# -*- coding: utf-8 -*-
from common.services.BaseService import BaseService
from flask import make_response
from io import StringIO,BytesIO
import codecs

'''
excel生成类
'''
class ExcelHelper(BaseService):

    @classmethod
    def readExcel(cls,path=""):
        return  cls._err("方法暂未实现")


    '''
    csv 切记不要包含json字符串
    '''
    @classmethod
    def exportCSV(cls,name="",head:list = [],body:list=[]):
        buffer = StringIO()
        csv_str = ""
        if head:
            csv_str = csv_str + ",".join(head) + "\n"

        if body:
            for item in body:
                csv_str = csv_str +','.join(str(x) for x in item) + "\n"

        buffer.write( csv_str )
        ##中文乱码解决办法：https://stackoverflow.com/questions/37013433/proper-rendering-of-flask-produced-csv-files-in-excel
        # forming a Response object with Headers to return from flask
        response = make_response( codecs.BOM_UTF8.decode("utf8") + codecs.BOM_UTF8.decode() + buffer.getvalue() )
        response.headers['Content-Disposition'] = ( f'attachment; filename={name}.csv' ).encode("utf-8")
        response.mimetype = 'text/csv'
        return response

    '''
    csv 切记不要包含json字符串
    '''
    @classmethod
    def exportExcel(cls, name="", head: list = [], body: list = []):
        import xlwt
        # 创建一个excel
        book = xlwt.Workbook(encoding="utf-8")
        # 添加工作区
        sheet = book.add_sheet("sheet1")
        for col, field in enumerate(head):  # 写入excel表头
            sheet.write(0, col, field)

        row = 1
        for data in body:  # 根据数据写入excel，col-单元格行标，field-单元格列标
            for col, field in enumerate(data):
                sheet.write(row, col, field)
            row += 1

        sio = BytesIO()
        book.save(sio)  # 将数据存储为bytes
        sio.seek(0)
        response = make_response( sio.getvalue() )
        response.headers['Content-Disposition'] = (f'attachment; filename={name}.xlsx').encode("utf-8")
        response.headers['Content-type'] = 'application/vnd.ms-excel'  # 响应头告诉浏览器发送的文件类型为excel
        ##response.mimetype = 'application/vnd.ms-excel'
        return response

    @classmethod
    def exportExcelMulSheet(cls, name="", head: list = [], body: list = [],sheet_name:list = []):
        import xlwt
        # 创建一个excel
        book = xlwt.Workbook(encoding="utf-8")

        for idx ,item_body in enumerate( body):
            # 添加工作区
            sheet = book.add_sheet( sheet_name[idx] )
            for col, field in enumerate(head):  # 写入excel表头
                sheet.write(0, col, field)

            row = 1
            for data in item_body:  # 根据数据写入excel，col-单元格行标，field-单元格列标
                for col, field in enumerate(data):
                    sheet.write(row, col, field)
                row += 1

        sio = BytesIO()
        book.save(sio)  # 将数据存储为bytes
        sio.seek(0)
        response = make_response(sio.getvalue())
        response.headers['Content-Disposition'] = (f'attachment; filename={name}.xlsx').encode("utf-8")
        response.headers['Content-type'] = 'application/vnd.ms-excel'  # 响应头告诉浏览器发送的文件类型为excel
        ##response.mimetype = 'application/vnd.ms-excel'
        return response
