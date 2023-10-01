import sqlite3
from gettime import gettime2
from cover_base_64_img import convert_image_to_base64,show_image_from_base64,write_to_text_file

# bảng data địa điểm du lịch để get khi hiển thị 

def create_database_for_tourist_destination_information(tablename):
    
    # Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
    conn = sqlite3.connect('database/tourist_destination_information.db')

    # Tạo một đối tượng cursor để thực thi truy vấn
    cursor = conn.cursor()
    
        # Tạo bảng diseases
    cursor.execute(f'''CREATE TABLE {tablename}
                  (id INTEGER PRIMARY KEY,
                   tourist_destination_name TEXT NOT NULL,
                   img_base64 TEXT NOT NULL,
                   price TEXT NOT NULL,
                   the_right_time_to_go TEXT NOT NULL,
                   createdTime TEXT NOT NULL,
                   tourist_destination_describe TEXT NOT NULL,
                   tourist_destination_location TEXT NOT NULL,
                   number_of_stars TEXT NOT NULL,
                   number_of_travel_days TEXT NOT NULL)''')
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# create_database_for_tourist_destination_information(tablename='tourist_destination_information_basic_for_get_data')

# lưu dữ liệu đăng nhập
def save_data_in_table_tourist_destination_information( tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars ,number_of_travel_days):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/tourist_destination_information.db')
    cursor = conn.cursor()

    # Thêm dữ liệu vào bảng diseases
    cursor.execute(f"INSERT INTO tourist_destination_information_basic_for_get_data (tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars ,number_of_travel_days) VALUES (?,?,?,?,?,?,?,?,?)",
               (tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars,number_of_travel_days ))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()


# truy vấn token bằng email
def query_database_for_tourist_destination_information_by_id( id):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/tourist_destination_information.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    cursor.execute(f"SELECT * FROM tourist_destination_information_basic_for_get_data WHERE id=?", (id,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()

    return data

def query_database_for_tourist_destination_information_by_name( name):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/tourist_destination_information.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    cursor.execute(f"SELECT * FROM tourist_destination_information_basic_for_get_data WHERE tourist_destination_name=?", (name,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()

    return data

# loại file database
def create_database_for_type_file_img(tablename):
    
    # Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
    conn = sqlite3.connect('database/tourist_destination_information.db')

    # Tạo một đối tượng cursor để thực thi truy vấn
    cursor = conn.cursor()
    
        # Tạo bảng diseases
    cursor.execute(f'''CREATE TABLE {tablename}
                  (id INTEGER PRIMARY KEY,
                   tourist_destination_name TEXT NOT NULL,
                   type_of_file_img TEXT NOT NULL)''')
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# create_database_for_type_file_img(tablename='type_of_file_img')

# lưu dữ liệu đăng nhập
def save_data_in_table_type_file_img(type_of_file_img,tourist_destination_name):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/tourist_destination_information.db')
    cursor = conn.cursor()

    # Thêm dữ liệu vào bảng diseases
    cursor.execute(f"INSERT INTO type_of_file_img (type_of_file_img,tourist_destination_name) VALUES (?,?)",
               (type_of_file_img ,tourist_destination_name))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()



def query_database_for_type_file_img_by_id( id):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/tourist_destination_information.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    cursor.execute(f"SELECT * FROM type_of_file_img WHERE id=?", (id,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()

    return data



# def query_database_for_type_file_img_and_tourist_destination_information_by_id( id):
#     # Kết nối tới cơ sở dữ liệu
#     conn = sqlite3.connect('database/tourist_destination_information.db')
#     cursor = conn.cursor()

#     # Thực hiện truy vấn dữ liệu từ bảng
#     cursor.execute(f"""SELECT *
#                         FROM type_of_file_img
#                         INNER JOIN tourist_destination_information_basic_for_get_data ON type_of_file_img.tourist_destination_name = tourist_destination_information_basic_for_get_data.tourist_destination_name;
#                         WHERE id=?""", (id,))
#     data = cursor.fetchone()

#     # Đóng kết nối
#     conn.close()

#     return data

def get_all_data_from_table(table_name,database_path):
    # Kết nối tới cơ sở dữ liệu SQLite
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Truy vấn lấy tất cả dữ liệu từ bảng
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)

    # Lấy tất cả các hàng dữ liệu
    rows = cursor.fetchall()

    # Đóng kết nối và trả về kết quả
    conn.close()
    return rows



# Sử dụng hàm để lấy dữ liệu từ bảng "my_table"
# database_path = 'database\\tourist_destination_information.db'
# table_name = "type_of_file_img"
# data = get_all_data_from_table(database_path=database_path,table_name=table_name)
# print(data)
# print(type(data))
# print(data[1])
# print(data[1][1])

# save_data_in_table_tourist_destination_information(
#     createdTime=gettime2(),
#     img_base64=convert_image_to_base64("img\\thac_havasu_arizona.jpg"),
#     number_of_stars="4.2",
#     price="1150",
#     number_of_travel_days="8",
#     the_right_time_to_go="every day of the year",
#     # the_right_time_to_go="from May to September",
#     tourist_destination_describe="Thác Havasu là một thác nước nằm trên nhánh Havasu Creek, thuộc Grand Canyon, Arizona, Hoa Kỳ. Thác nước nằm trong vùng đất của bộ lạc Havasupai. Đây là thác nước nổi tiếng nhất trong số các thác dọc theo Havasu Creek. Thác nước hùng vĩ này có độ cao 27 mét, nước chảy xuống từ một vách đá thẳng đứng cao 30 mét xuống một hồ bơi lớn. Do hàm lượng khoáng chất cao trong nước, hình dạng của thác nước luôn luôn thay đổi, đôi khi tạo thành hai máng nước riêng biệt rất đặc sắc. Nhờ lượng Canxi Carbonat và Magiê khá lớn, hồ nước tự nhiên phía dưới thác có màu ngọc lam đẹp mắt. Bạn sẽ phải cuốc bộ cả chục dặm trước khi có thể hòa mình vào dòng nước xanh mát gần công viên quốc gia Grand Canyon này, nhưng đây cũng là dịp lý tưởng để ngắm cảnh dọc đường.",
#     tourist_destination_location="Grand Canyon, Arizona, Hoa Kỳ",
#     tourist_destination_name="Thác Havasu, Arizona"
# )

for i in range(20):
    a = query_database_for_tourist_destination_information_by_id(i)
    if a:
        id ,tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars ,number_of_travel_days = a
        print(f"{tourist_destination_name}, {tourist_destination_location}")


    else:
        print(f"id {i} chưa có data")


#test show img by load data from sqlite
# b = query_database_for_tourist_destination_information_by_id(3)
# id ,tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars ,number_of_travel_days = b
# show_image_from_base64(base64_string=img_base64)

# data_dict = {
# 'Đại thánh đường Sheikh Zayed, Abu Dhabi':'jpg',
# 'Đông Xuyên, Trung Quốc':'jpg',
# 'Ốc đảo sa mạc Huacachina':'jpg',
# 'Cửu Trại Câu':'webp',
# 'Isola Bella':'jpg',
# 'Nhà thờ Las Lajas':'jpg',
# 'LonDon':'jpg',
# 'Mauritius':'webp',
# 'Lệ giang cổ trấn':'webp',
# 'Phúc Kiến Thổ Lâu':'webp',
# 'Phượng Hoàng Cổ Trấn':'webp',
# 'Popeye, Malta':'jpg',
# 'Santorini Greece':'jpg',
# 'Scotland':'jpg',
# 'Setenil de las Bodegas':'jpg',
# 'Thung lũng Shangrila':'webp',
# 'Thác Havasu, Arizona':'jpg'
# }

# for destination, file_type in data_dict.items():
#     save_data_in_table_type_file_img(type_of_file_img=file_type, tourist_destination_name=destination)

# for i in range(20):
#     print(query_database_for_type_file_img_by_id(i))

# d = query_database_for_type_file_img_and_tourist_destination_information_by_id(id=2)
# write_to_text_file(data=d,file_path="test_data2.txt")
