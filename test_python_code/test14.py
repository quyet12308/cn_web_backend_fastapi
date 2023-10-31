import json
# from base_code.cover_base_64_img import convert_image_to_base64
# from home_screen_database import update_data_tourist_destination_information_by_id

data = (
    ("0","name0","20","23-03-2002","email0"),
    ("1","name1","21","23-03-2012","email1"),
    ("2","name2","22","23-03-2022","email2"),
    ("3","name3","23","23-03-2032","email3"),
    ("4","name4","24","23-03-2042","email4"),
    ("5","name5","25","23-03-2052","email5"),
    ("6","name6","26","23-03-2062","email6"),
    ("7","name7","27","23-03-2072","email7"),
    ("8","name8","28","23-03-2082","email8"),
    ("9","name9","29","23-03-2092","email9")
)

# columns = ['id', 'name', 'age', 'birth_day','email']

# data_dict = dict(zip(columns, zip(*data)))

# print(data_dict)
# text1 = ""

# input1 = input("nhap 1 = ")
# input2 = input("nhap 2 = ")
# input3 = input("nhap 3 = ")
# input4 = input("nhap 4 = ")

# arr = []
# if input1 == "0":
#     arr.append("input1")
# elif input1 == "1":
#     pass
# if input2 == "0":
#     arr.append("input2")
# elif input2 == "1":
#     pass
# if input3 == "0":
#     arr.append("input3")
# elif input3 == "1":
#     pass
# if input4 == "0":
#     arr.append("input4")
# elif input4 == "1":
#     pass
# if len(arr) > 0:
#         text1 = ", ".join(arr)
# print(text1)

a = """Hồ bơi ngoài trời
Chỗ đỗ xe miễn phí
WiFi miễn phí
Phòng gia đình
Phòng không hút thuốc
Tiện nghi cho khách khuyết tật
Quầy bar
Bữa sáng tốt
"""

arr = a.splitlines()
print(arr)