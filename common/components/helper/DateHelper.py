# -*- coding: utf-8 -*-
from __future__ import division
import datetime,time
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
    def getTimestamps(date_str = None, format="%Y-%m-%d %H:%M:%S"):
        time_array = time.strptime(date_str, format)
        return int(time.mktime(time_array) )

    @staticmethod
    def getDateOnTimestamps( timestamps = 0, format="%Y-%m-%d %H:%M:%S"):
        return time.strftime( format , time.localtime( timestamps ) )

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
    
    
    @staticmethod
    def formatBeautyTime( diff_time ):
        retval = ''
        day = hour = min = sec =  0
        if diff_time < 60:
            sec = '%d' % diff_time
        elif diff_time >= 60 and diff_time < 3600:
            min = int(diff_time / 60)
            sec = diff_time % 60
        elif diff_time >= 3600 and diff_time < 86400:
            hour = int(diff_time / 3600)
            min = int((diff_time - hour * 3600) / 60)
            sec = int((diff_time - hour * 3600 - min * 60) % 60)
        elif diff_time >= 86400:
            day = int(diff_time / 86400)
            hour = int((diff_time - day * 86400) / 3600)
            min = int((diff_time - day * 86400 - hour * 3600) / 60)
            sec = (diff_time - day * 86400 - hour * 3600 - min * 60) % 60

        if day:
            retval += "%s天"%( day )

        if hour:
            retval += "%s小时"%( hour )

        if min:
            retval += "%s分"%( min )

        if sec:
            retval += "%s秒"%( int(sec) )
        return retval
        