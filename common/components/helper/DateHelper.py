# -*- coding: utf-8 -*-
from __future__ import division
import datetime
from common.services.BaseService import BaseService


class DateHelper(BaseService):
    @staticmethod
    def getCurrentTime( fmt="%Y-%m-%d %H:%M:%S", date=None ):
        return DateHelper.getFormatDate(date=date, format=fmt)

    '''
    获取格式化的时间
    '''
    @staticmethod
    def getFormatDate(date=None, format="%Y-%m-%d %H:%M:%S"):
        if date is None:
            date = datetime.datetime.now()

        return date.strftime(format)

    @staticmethod
    def getDateBefore(day=1, date=None):
        if date is None:
            date = datetime.date.today()
        return date - datetime.timedelta(days=day)

    @staticmethod
    def getDateAfter(day=1, date=None):
        if date is None:
            date = datetime.date.today()
        return date + datetime.timedelta(days=day)

    @staticmethod
    def getCurrentWeekRange():
        now = datetime.datetime.now()
        return DateHelper.getWeekRange( now )

    @staticmethod
    def getWeekRange(date=None, fmt=None):
        now = datetime.datetime.now()
        if date is not None:
            now = date
        week_start = now - datetime.timedelta(days = now.weekday() )
        week_end = now + datetime.timedelta(days =6 - now.weekday() )
        if fmt is not None:
            week_start = DateHelper.getFormatDate(date =week_start,format = fmt)
            week_end = DateHelper.getFormatDate(date = week_end,format = fmt )
        return [week_start, week_end]

    @staticmethod
    def getMonthRange(date=None, fmt=None):
        now = datetime.datetime.now()
        if date is not None:
            now = date
        month_start = datetime.datetime(now.year, now.month, 1)
        month_end = month_start + datetime.timedelta(days=30) - datetime.timedelta(days=1)
        if fmt is not None:
            month_start = DateHelper.getFormatDate(date=month_start,format = fmt )
            month_end = DateHelper.getFormatDate(date=month_end,format = fmt)
        return [month_start, month_end]

    @staticmethod
    def str2Date(date=None, format = "%Y-%m-%d %H:%M:%S", is_datetime=True):
        ret = datetime.datetime.strptime(str(date), format)
        if not is_datetime:
            ret = ret.date()
        return ret

    @staticmethod
    def diffDays(d1, d2):
        return (d1 - d2).days

    @staticmethod
    def weekNumOfYear(date=None):
        now = datetime.datetime.now()
        if date is not None:
            now = date
        return now.isocalendar()[1]