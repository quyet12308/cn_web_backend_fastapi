# import requests

# url = "https://hotels4.p.rapidapi.com/reviews/v3/list"

# payload = {
# 	"currency": "USD",
# 	"eapid": 1,
# 	"locale": "en_US",
# 	"siteId": 300000001,
# 	"propertyId": "9209612",
# 	"size": 10,
# 	"startingIndex": 0
# }
# headers = {
# 	"content-type": "application/json",
# 	"X-RapidAPI-Key": "93d691634emsh06aece34ef9f62ap168b08jsn94ecdbe3a334",
# 	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
# }

# response = requests.post(url, json=payload, headers=headers)

# print(response.json())


# import requests

# def get_nearby_hotels(latitude, longitude):
#     url = "https://hotels-com-free.p.rapidapi.com/srle/listing/v1/brands/hotels.com"
#     querystring = {
#         "lat": str(latitude),
#         "lon": str(longitude),
#         "currency": "USD",
#         "locale": "en_US",
#         "sortOrder": "PRICE",
#         "pageNumber": "1",
#         "checkIn": "2023-10-01",
#         "checkOut": "2023-10-02",
#         "pageSize": "10"
#     }
#     headers = {
#         "X-RapidAPI-Key": "93d691634emsh06aece34ef9f62ap168b08jsn94ecdbe3a334",
#         "X-RapidAPI-Host": "hotels-com-free.p.rapidapi.com"
#     }

#     response = requests.get(url, headers=headers, params=querystring)
#     data = response.json()

#     # Xử lý dữ liệu phản hồi
#     if response.status_code == 200:
#         # Trích xuất thông tin khách sạn từ data
#         hotels = data["sr"]["properties"]
#         for hotel in hotels:
#             # Xử lý thông tin khách sạn theo nhu cầu của bạn
#             hotel_name = hotel["name"]
#             hotel_address = hotel["address"]["streetAddress"]
#             hotel_price = hotel["ratePlan"]["price"]["current"]
#             # In thông tin khách sạn
#             print(f"Name: {hotel_name}")
#             print(f"Address: {hotel_address}")
#             print(f"Price: {hotel_price}")
#             print("----------------------")
#     else:
#         print("Error:", data)  # Xử lý lỗi nếu có

# # Gọi hàm và truyền vào tọa độ mong muốn
# latitude = 10.1234
# longitude = 20.5678
# get_nearby_hotels(latitude, longitude)



import requests
from base_code.security_info import api_key

url = "https://travel-advisor.p.rapidapi.com/restaurants/list-by-latlng"

querystring = {"latitude":"12.91285","longitude":"100.87808","limit":"30","currency":"USD","distance":"2","open_now":"false","lunit":"km","lang":"en_US"}

headers = {
	"X-RapidAPI-Key": f"{api_key['X-RapidAPI-Key']}",
	"X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())



