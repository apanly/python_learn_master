# -*- coding: utf-8 -*-
from application import  app
import re,validators

from common.services.BaseService import BaseService


class ValidateHelper(BaseService):

    @staticmethod
    def validDate( str_date = '',fmt = r'^\d{4}-\d{2}-\d{2}$' ):
        return (  str_date is not None and len( str_date ) > 0  and  re.match( fmt,str_date ) != None )

    @staticmethod
    def validLength( text = '',min = 1,max = None ):
        str_len = len(text)
        if max is None:
            return True if str_len >= min else False
        return True if str_len >= min and str_len <= max else False

    @staticmethod
    def validUrl( url ):
        return validators.url( url )

    @staticmethod
    def validEMail( email ):
        return validators.email( email )



