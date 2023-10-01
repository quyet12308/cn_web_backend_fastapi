from geopy.geocoders import Nominatim

def chuyen_doi_toa_do(latitude, longitude):
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.reverse((latitude, longitude))
    return location.address

# Sử dụng hàm
latitude = -12.040434294404621
longitude = -77.04524794331445
dia_diem = chuyen_doi_toa_do(latitude, longitude)
print(dia_diem)