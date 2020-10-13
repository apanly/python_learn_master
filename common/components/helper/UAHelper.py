# -*- coding: utf-8 -*-
import hashlib
import re

from common.services.BaseService import BaseService
from flask import render_template,g,jsonify,request

class UAHelper( BaseService):


    @staticmethod
    def isPC():
        ua = request.user_agent.string.lower()

        mobile_feature = ['nokia','sony','ericsson','mot','samsung','htc','sgh','lg','sharp','sie-','philips',
                          'panasonic','alcatel','lenovo','iphone','ipod','blackberry','meizu','android','netfront',
                          'symbian','ucweb','windowsce','palm','operamini','operamobi','opera mobi','openwave',
                          'nexusone','cldc','midp','wap','mobile'
        ]

        pattern = re.compile('%s' % "|".join( mobile_feature) )
        if pattern.search( ua ) != None or "ipad" not in ua:
            return False
        return True

    @staticmethod
    def isWechat():
        ua = request.user_agent.string.lower()
        return "micromessenger" in ua