

import datetime
# from datetime import datetime, timedelta
import pytz
# from datetime import timedelta


def gettime2():
    utc_time = datetime.datetime.now(pytz.utc)
    local_time = utc_time.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))
    t = local_time.strftime("%Y-%m-%d %H:%M:%S")
    return t



def check_time_range(created_time, now_time, minute):
    # Chuyển đổi chuỗi thời gian thành đối tượng datetime
    created_datetime = datetime.datetime.strptime(created_time, "%Y-%m-%d %H:%M:%S")
    now_datetime = datetime.datetime.strptime(now_time, "%Y-%m-%d %H:%M:%S")

    # Tính toán khoảng thời gian giữa hai thời điểm
    time_difference = now_datetime - created_datetime

    # Chuyển đổi số phút thành đối tượng timedelta
    minute_delta = datetime.timedelta(minutes=minute)

    # So sánh khoảng thời gian với tham số phút
    if time_difference >= minute_delta:
        return False
    else:
        return True
    
# created_time = "2023-09-14 10:01:00"
# now_time = "2023-09-14 10:04:59"
# minute = 3

# result = check_time_range(created_time, now_time, minute)
# print(result)  # True nếu khoảng thời gian không vượt qua tham số minute, False nếu vượt qua

