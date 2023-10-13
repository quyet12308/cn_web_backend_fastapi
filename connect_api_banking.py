import requests

def get_list_data_from_banks(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Nếu có lỗi, raise exception
        data = response.json()  # Chuyển đổi dữ liệu nhận được thành đối tượng JSON
        return data
    except requests.exceptions.RequestException as e:
        print("Lỗi trong quá trình gửi yêu cầu:", e)
        return None

# Sử dụng hàm để lấy dữ liệu từ một URL cụ thể
# url = "https://api.vietqr.io/v2/banks"
# data = get_list_data_from_banks(url)
# print(data)

