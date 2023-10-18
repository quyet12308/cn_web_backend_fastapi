import sqlite3

from base_code.cover_base_64_img import convert_image_to_base64
from base_code.base import doc_du_lieu,tach_doan_text,random_decimal,random_number_price,random_number_rivew
from base_code.gettime import gettime2


def create_database_for_offer_basic(tablename):
    
    # Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
    conn = sqlite3.connect('database/offer.db')

    # Tạo một đối tượng cursor để thực thi truy vấn
    cursor = conn.cursor()
    
        # Tạo bảng diseases
    cursor.execute(f'''CREATE TABLE {tablename}
                  (id INTEGER PRIMARY KEY,
                   id_hotel TEXT,
                   hotel_name TEXT,
                   stars TEXT,
                   price TEXT,
                   num_reviews TEXT,
                   avata_img TEXT,
                   describe_hotel TEXT,
                   createdTime TEXT)''')
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# create_database_for_offer_basic(tablename="offer_basic")

def query_database_for_offer_by_id_hotel( id_hotel):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/offer.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    # chuyển dữ liệu qua bảng mới basic_login_register2
    cursor.execute(f"SELECT * FROM offer_basic WHERE id_hotel=?", (id_hotel,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()
    if data:
        columns = ['id', 'id_hotel', 'hotel_name', 'stars','price','num_reviews' ,'avata_img','describe_hotel', 'createdTime']
        data_dict = dict(zip(columns, data))
        return data_dict
    else:
        return None
    
def query_database_for_offer_by_id_hotel_order_by( ):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/offer.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    # chuyển dữ liệu qua bảng mới basic_login_register2
    
    # cursor.execute(f"SELECT * FROM offer_basic order by CAST(num_reviews AS INTEGER) DESC ", (id_hotel,))
    cursor.execute(f"SELECT * FROM offer_basic ORDER BY CAST(num_reviews AS INTEGER) DESC ")
    data = cursor.fetchall()

    # Đóng kết nối
    # conn.close()
    # if data:
    #     for i in data:
    #         columns = ['id', 'id_hotel', 'hotel_name', 'stars','price','num_reviews' ,'avata_img','describe_hotel', 'createdTime']
    #         data_dict = dict(zip(columns, data))
    #     return data_dict
    # else:
    #     return None
    
    # return data

    

# lưu dữ liệu 
def save_data_for_offer_in_table( id_hotel, hotel_name,stars,price,num_reviews,avata_img,describe_hotel,createdTime ):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/offer.db')
    cursor = conn.cursor()

    # Thêm dữ liệu vào bảng diseases
    # chuyển dữ liệu qua bảng mới basic_login_register2
    # if birthday is None and avata_img is None:
    #     birthday = avata_img == ""
    cursor.execute(f"INSERT INTO offer_basic ( id_hotel, hotel_name,stars,price,num_reviews,avata_img,describe_hotel,createdTime) VALUES (?,?,?,?,?,?,?,?)",
               ( id_hotel, hotel_name,stars,price,num_reviews,avata_img,describe_hotel,createdTime))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# def sort_data_offer_database(table_name,price_offer=None,location_offer=None,star_offer=None,distance_offer=None,review_offer=None):
#     conn = sqlite3.connect('database/offer.db')
#     cursor = conn.cursor()
#     query_text1 = ""
#     query_text2 = ""
#     query_string_text = f"SELECT * FROM {table_name}"
#     where_query_string = f"WHERE {query_text1}"
#     orfer_by_query_string = f"ORDER BY {query_text2}"
#     if price_offer is not None:
#         if price_offer == "ascending_price":


            
    
#     decrease_price

#     default_location
#     a_to_z_location

#     show_all_star
#     ascending_star
#     decrease_star
#     three_star
#     four_star
#     five_star

#     default_distance

#     default_review
#     ascending_review
#     decrease_review

#     data = cursor.fetchone()
#     if data:
#         columns = ['id', 'id_hotel', 'hotel_name', 'stars','price','num_reviews' ,'avata_img','describe_hotel', 'createdTime']
#         data_dict = dict(zip(columns, data))
#         return data_dict
#     else:
#         return None

# a = doc_du_lieu(file_path="test3.txt")
# # print(a)
# ket_qua = tach_doan_text(a)

# for i, (ten_khach_san, mo_ta) in enumerate(ket_qua):
#     # print(f"Đoạn {i+1}:")
#     star = random_decimal(end=5,start=3)
#     price = random_number_price(start=6,end=20)
#     number_review = random_number_rivew(start=2,end=20)
#     id_hotel = 1000 + i
#     print(id_hotel)
#     print(star)
#     print(i)
#     img_base64_str = convert_image_to_base64(image_path=f"img\\img_hotels\\anh{i+2}.jpeg")
#     print("Tên khách sạn:", ten_khach_san)
#     print("Mô tả:", mo_ta)
#     print()
#     save_data_for_offer_in_table(describe_hotel=mo_ta,avata_img=img_base64_str,createdTime=gettime2(),hotel_name=ten_khach_san,id_hotel=id_hotel,num_reviews=number_review,price=price,stars=star)

# d = query_database_for_offer_by_id_hotel(id_hotel=f"1001")
# print(f'id = {d["id"]}')
# print(f'id_hotel = {d["id_hotel"]}')
# print(f'hotel_name = {d["hotel_name"]}')
# print(f'stars = {d["stars"]}')
# print(f'price = {d["price"]}')
# print(f'num_reviews = {d["num_reviews"]}')
# print(f'createdTime = {d["createdTime"]}')

a = query_database_for_offer_by_id_hotel_order_by()
print(len(a))
print(type(a[1]))


