import sqlite3

from base_code.gettime import gettime3,gettime2

def create_database_for_visual_hotels_and_restaurent_basic1(tablename,day):
    
    # Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
    conn = sqlite3.connect('database/visual_hotels_and_restaurent.db')

    # Tạo một đối tượng cursor để thực thi truy vấn
    cursor = conn.cursor()
    
        # Tạo bảng diseases
    cursor.execute(f'''CREATE TABLE {tablename}_{day}
                  (id INTEGER PRIMARY KEY,
                   tourist_destination_name TEXT,
                   lat TEXT,
                   lon TEXT,
                   data TEXT,
                   createdTime TEXT)''')
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()


# create_database_for_visual_hotels_and_restaurent_basic1(day=gettime3(),tablename="visual_hotels_and_restaurent")

def query_database_for_visual_hotels_and_restaurent_by_tourist_destination_name(tourist_destination_name,table_name):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/visual_hotels_and_restaurent.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    cursor.execute(f"SELECT * FROM {table_name} WHERE tourist_destination_name=?", (tourist_destination_name,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()

    if data:
        columns = ['id', 'tourist_destination_name', 'lat', 'lon','data' , 'createdTime']
        data_dict = dict(zip(columns, data))
        return data_dict
    else:
        return None
    
# lưu dữ liệu 
def save_data_for_visual_hotels_and_restaurent_in_table(table_name,lat,lon,data,tourist_destination_name,createdTime ):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/visual_hotels_and_restaurent.db')
    cursor = conn.cursor()

    # Thêm dữ liệu vào bảng diseases
    # chuyển dữ liệu qua bảng mới basic_login_register2
    # if birthday is None and avata_img is None:
    #     birthday = avata_img == ""
    cursor.execute(f"INSERT INTO {table_name} (tourist_destination_name, lat,lon,data,createdTime) VALUES (?,?,?,?,?)",
               (tourist_destination_name, lat,lon,data,createdTime))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# data = query_database_for_visual_hotels_and_restaurent_by_tourist_destination_name(tourist_destination_name=f"Thung lũng Shangrila",table_name=f"visual_hotels_and_restaurent_{gettime3()}")
# print(data)



