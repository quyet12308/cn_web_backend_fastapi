# data = ["username",
#                     "avatar_img",
#                     "birthday",
#                     "email",
#                     "password",
#                     "createdTime"]

# for i in data:
#     print(f"{i}2_ = data2['{i}']")


# from connect_open_weather_api import select_data_of_weather_data
data = {'dt': 1696917600, 'main': {'temp': 292.39, 'feels_like': 291.39, 'temp_min': 292.39, 'temp_max': 292.39, 'pressure': 1022, 'sea_level': 1022, 'grnd_level': 928, 'humidity': 39, 'temp_kf': 0}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'mây rải rác', 'icon': '03d'}], 'clouds': {'all': 50}, 'wind': {'speed': 3.47, 'deg': 109, 'gust': 3.71}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2023-10-10 06:00:00'}


# a = select_data_of_weather_data(data)
# print(a)