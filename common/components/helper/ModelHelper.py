# -*- coding: utf-8 -*-
from common.services.BaseService import BaseService

class ModelHelper(BaseService):

    '''
    根据id字段获取一个dict出来
    '''
    @staticmethod
    def getDictFilterField( db_model,select_field = '',key_field = "id",id_list = None ):
        ret = {}
        query = db_model.query
        if id_list and len( id_list ) > 0:
            query = query.filter( select_field.in_( id_list ) )

        list = query.all()
        if not list:
            return ret
        for item in list:
            if not hasattr( item,key_field ):
                break

            ret[ getattr( item,key_field ) ] = item
        return ret

    @staticmethod
    def getDictListFilterField( db_model,select_filed = '',key_field = "id",id_list = None ):
        ret = {}
        query = db_model.query
        if id_list and len( id_list ) > 0:
            query = query.filter( select_filed.in_( id_list ) )

        list = query.all()
        if not list:
            return ret
        for item in list:
            if not hasattr( item,key_field ):
                break
            if getattr( item,key_field ) not in ret:
                ret[getattr(item, key_field)] = []

            ret[ getattr( item,key_field ) ].append(item )
        return ret

    '''
    从model列表中取出某个字段，相当于php array_column
    '''
    @staticmethod
    def getFieldList( model_list,key_field ):
        ret = []
        from application import db
        if isinstance( model_list, db.Model ):
            model_list = [ model_list ]

        for item in model_list:
            if not hasattr( item,key_field ):
                break
            ret.append( getattr(item, key_field) )
        return ret