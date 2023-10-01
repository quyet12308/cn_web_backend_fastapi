import requests
from security_info import api_key

api_key = api_key["openweather"]  # Thay YOUR_API_KEY bằng API key bạn đã lấy từ OpenWeather
city = "hanoi"  # Thay Hanoi bằng tên thành phố bạn muốn lấy thông tin thời tiết

# vd 24°28′B 54°22′Đ thì bắc nam là vĩ độ , đông tây là kinh độ
# lat = 33.12 # vĩ độ 
# lon = 103.54# kinh độ
# -12.2 -77.2
lat = -12.2
lon = -77.2
lang = "vi"

# Gửi yêu cầu GET đến API OpenWeather để lấy thông tin dự báo thời tiết
# response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}")
response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&lang={lang}")

# Kiểm tra mã trạng thái của yêu cầu
if response.status_code == 200:
    # Yêu cầu thành công, lấy thông tin dự báo thời tiết từ phản hồi
    forecast_data = response.json()
    print(forecast_data)
    
    # Xử lý thông tin dự báo thời tiết ở đây
    # Ví dụ:
    for forecast in forecast_data['list']:
        date = forecast['dt_txt']
        temperature = forecast['main']['temp']
        humidity = forecast['main']['humidity']
        print(f"Date: {date}")
        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")
        print('---')
else:
    # Yêu cầu không thành công, in ra lỗi
    print("Failed to retrieve weather forecast data.")