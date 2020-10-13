# -*- coding: utf-8 -*-
from common.services.BaseService import BaseService


class CommonConstant(BaseService):
    '''
    这里存放常量，就是不随着环境变的参数
    '''

    # 分页显示最多页数
    PAGE_DISPLAY = 10

    # 分页显示每页大小
    PAGE_SIZE = 30

    ##默认json系统错误
    SYSTEM_DEFAULT_ERROR = "系统繁忙，请稍后再试~~"

    DEFAULT_DATE = "1970-01-01"
    DEFAULT_DATETIME = "1970-01-01 00:00:00"

    ## 如果使用cookie登录，可以用这个作为cookie的name，即学即码
    AUTH_COOKIE_NAME = "learn_master"

    default_status_false = 0
    default_status_true = 1
    default_status_neg_99 = -99

    common_status_map = {
        1 : "正常",
        0 : "已删除"
    }

    common_status_map2 = {
        1: "可用",
        0: "禁用"
    }

    common_status_map3 = {
        1: "已读",
        0: "未读"
    }

    link_type_map = {
        2: {
            "title": "系统",
            "class": "warning"
        },
        3: {
            "title": "工具",
            "class": "warning"
        },
        4: {
            "title": "媒体",
            "class": "primary"
        },
        5: {
            "title": "平台",
            "class": "success"
        },
        1: {
            "title": "其他",
            "class": "info"
        }
    }

