import requests
from base_code.security_info import api_key

def get_data_hotel_from_api_rapidapi(lon,lat):
    url = "https://travel-advisor.p.rapidapi.com/restaurants/list-by-latlng"

    querystring = {"latitude":f"{lat}","longitude":f"{lon}","limit":"30","currency":"USD","distance":"2","open_now":"false","lunit":"km","lang":"en_US"}

    headers = {
        "X-RapidAPI-Key": f"{api_key['X-RapidAPI-Key']}",
        "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    # print(response.json())
    result = response.json()
    return result



