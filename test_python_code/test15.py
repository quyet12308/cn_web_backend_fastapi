a = """Giặt ủi
Tiện nghi BBQ
Khu vực xem TV/sảnh chung
Sân gôn (trong vòng 3km)
Đi bộ đường dài
Hệ thống sưởi
Hồ bơi ngoài trời
Bãi đỗ xe miễn phí
Ghế/ghế dài tắm nắng
Phòng không hút thuốc
"""

# a_arr = ['3 hồ bơi', 'WiFi miễn phí', 'Giáp biển', 'Chỗ đỗ xe miễn phí', 'Phòng gia đình', 'Xe đưa đón sân bay', 'Trung tâm thể dục', 'Quầy bar', 'Khu vực bãi tắm riêng', 'Bữa sáng tuyệt hảo']

# arr = a.splitlines()
# print(arr)

text_block = "fullname TEXT, email TEXT, timeCheckin TEXT, days TEXT, booking_tour_name TEXT, price TEXT, number_adults TEXT, number_children TEXT, hotel_infor TEXT, createdTime TEXT"

# Tách khối văn bản thành danh sách các cặp tên và kiểu dữ liệu
pairs = text_block.split(", ")

# Tạo một từ điển để lưu trữ tên và kiểu dữ liệu
data_dict = {}

# Lặp qua các cặp tên và kiểu dữ liệu
for pair in pairs:
    # Tách tên và kiểu dữ liệu
    name, data_type = pair.split(" ")
    # Xóa khoảng trắng thừa
    name = name.strip()
    # Lưu trữ tên và kiểu dữ liệu vào từ điển
    data_dict[name] = data_type

# Tạo đoạn văn bản mới
new_text = ", ".join(data_dict.keys())

print(new_text)