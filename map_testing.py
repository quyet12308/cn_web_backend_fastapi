from geopy.geocoders import Nominatim

def chuyen_doi_toa_do(latitude, longitude):
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.reverse((latitude, longitude))
    return location.address

# Sử dụng hàm
# latitude = -12.040434294404621
# longitude = -77.04524794331445
# dia_diem = chuyen_doi_toa_do(latitude, longitude)
# print(dia_diem)

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import geocoder

def get_current_location():
    # Lấy vị trí hiện tại dựa trên địa chỉ IP
    g = geocoder.ip('me')
    latitude = g.latlng[0]
    longitude = g.latlng[1]

    # Lấy thông tin địa điểm từ vị trí hiện tại
    geolocator = Nominatim(user_agent="my_app")
    try:
        location = geolocator.reverse(f'{latitude}, {longitude}')
        return location.address, latitude, longitude
    except GeocoderTimedOut:
        return get_current_location()

# Lấy vị trí hiện tại
# current_location, latitude, longitude = get_current_location()
# print("Vị trí hiện tại:", current_location)
# print("Vĩ độ:", latitude)
# print("Kinh độ:", longitude)