import sqlite3
import time
import asyncio

def create_database_for_confirm_code():
    
    # Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
    conn = sqlite3.connect('database/catchat_code_for_send_email.db')

    # Tạo một đối tượng cursor để thực thi truy vấn
    cursor = conn.cursor()
    
        # Tạo bảng diseases
    cursor.execute(f'''CREATE TABLE catchat_code_for_send_email
                  (id INTEGER PRIMARY KEY,
                   username TEXT,
                   email TEXT,
                   createdTime TEXT,
                   code TEXT)''')
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# create_database_for_confirm_code()

def query_database_for_confirm_code_by_email( email):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/catchat_code_for_send_email.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    cursor.execute(f"SELECT * FROM catchat_code_for_send_email WHERE email=?", (email,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()

    return data

def query_data_by_email_with_max_id(email):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/catchat_code_for_send_email.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn
    cursor.execute("SELECT * FROM catchat_code_for_send_email WHERE email=? ORDER BY id DESC LIMIT 1", (email,))
    result = cursor.fetchone()  # Lấy một dòng dữ liệu

    # Đóng kết nối
    conn.close()

    return result

def query_database_for_confirm_code_by_id( id):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/catchat_code_for_send_email.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    cursor.execute(f"SELECT * FROM catchat_code_for_send_email WHERE id=?", (id,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()

    return data

# lưu dữ liệu 
def save_data_for_confirm_code_in_table( username,email,createdTime ,code):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/catchat_code_for_send_email.db')
    cursor = conn.cursor()

    # Thêm dữ liệu vào bảng diseases
    cursor.execute(f"INSERT INTO catchat_code_for_send_email (username,email ,createdTime,code) VALUES (?,?,?,?)",
               (username,email,createdTime,code))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

#delete data
async def delayed_delete_confirm_code_by_email(email, delay_minutes):
    # Đợi một khoảng thời gian (tính bằng giây) trước khi thực hiện xóa
    # time.sleep(delay_minutes * 60)
    await asyncio.sleep(delay_minutes * 60) 

    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/catchat_code_for_send_email.db')
    cursor = conn.cursor()

    # Xóa dữ liệu từ bảng test dựa trên tên
    cursor.execute("DELETE FROM catchat_code_for_send_email WHERE email=?", (email,))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()
# a = query_database_for_login_register_by_name(name="abc")
# print(a)


# for i in range(1):
#     a = query_database_for_confirm_code_by_id(id=i)
#     id_ , name , email , time_ , code = a
#     print(time_)
#     print(type(time_))

# a = query_database_for_confirm_code_by_id(id=1)
# id_ , name , email , time_ , code = a
# print(time_)
# print(type(time_))

# for i in range(15):
#     c = query_database_for_confirm_code_by_id(i)
#     print(c)