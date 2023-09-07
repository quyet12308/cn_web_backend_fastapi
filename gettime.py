

import datetime

import pytz


def gettime2():
    utc_time = datetime.datetime.now(pytz.utc)
    local_time = utc_time.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))
    t = local_time.strftime("%Y-%m-%d %H:%M:%S")
    return t

