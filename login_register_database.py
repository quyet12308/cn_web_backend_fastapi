import sqlite3

def create_database_for_login_register_basic(tablename):
    
    # Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
    conn = sqlite3.connect('database/login_register.db')

    # Tạo một đối tượng cursor để thực thi truy vấn
    cursor = conn.cursor()
    
        # Tạo bảng diseases
    cursor.execute(f'''CREATE TABLE {tablename}
                  (id INTEGER PRIMARY KEY,
                   username TEXT,
                   email TEXT,
                   password TEXT,
                   createdTime TEXT)''')
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# create_database_for_login_register_basic(tablename='basic_login_register')

def query_database_for_login_register_by_name( name):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/login_register.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    cursor.execute(f"SELECT * FROM basic_login_register WHERE username=?", (name,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()

    return data

def query_database_for_login_register_by_id( id):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/login_register.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    cursor.execute(f"SELECT * FROM basic_login_register WHERE id=?", (id,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()

    return data

def query_database_for_login_register_by_email( email):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/login_register.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    cursor.execute(f"SELECT * FROM basic_login_register WHERE email=?", (email,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()

    return data

# lưu dữ liệu 
def save_data_for_login_register_in_table( username, password,email,createdTime ):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/login_register.db')
    cursor = conn.cursor()

    # Thêm dữ liệu vào bảng diseases
    cursor.execute(f"INSERT INTO basic_login_register (username, password,email ,createdTime) VALUES (?,?,?,?)",
               (username, password,email,createdTime))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

#delete
def delete_data_for_login_and_register_by_name(name):
    # Đợi một khoảng thời gian (tính bằng giây) trước khi thực hiện xóa
    # time.sleep(delay_minutes * 60)

    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/login_register.db')
    cursor = conn.cursor()

    # Xóa dữ liệu từ bảng test dựa trên tên
    cursor.execute("DELETE FROM basic_login_register WHERE username=?", (name,))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

def update_user_by_email(email, new_username, new_password):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/login_register.db')
    cursor = conn.cursor()
    
    # Xây dựng truy vấn SQL để cập nhật dòng dựa trên email
    update_query = f'''UPDATE basic_login_register
                      SET username = ?,
                          password = ?
                      WHERE email = ?'''
    
    # Thực thi truy vấn với các giá trị thay thế
    cursor.execute(update_query, (new_username, new_password, email))
    
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# a = query_database_for_login_register_by_name(name="abc")
# print(a)
# delete_data_for_login_and_register_by_name(name="quyet12306")
# for i in range(10):
#     a = query_database_for_login_register_by_id(i)
#     print(a)



###############################################
# phiên đăng nhập
###############################################

# tạo bảng phiên đăng nhập
def create_database_for_login_session(tablename):
    
    # Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
    conn = sqlite3.connect('database/login_register.db')

    # Tạo một đối tượng cursor để thực thi truy vấn
    cursor = conn.cursor()
    
        # Tạo bảng diseases
    cursor.execute(f'''CREATE TABLE {tablename}
                  (id INTEGER PRIMARY KEY,
                   username TEXT,
                   email TEXT,
                   token TEXT,
                   createdTime TEXT)''')
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# create_database_for_login_session(tablename='login_session')

# lưu dữ liệu đăng nhập
def save_data_in_table_login_session( username, token,email,createdTime ):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/login_register.db')
    cursor = conn.cursor()

    # Thêm dữ liệu vào bảng diseases
    cursor.execute(f"INSERT INTO login_session (username, token,email ,createdTime) VALUES (?,?,?,?)",
               (username, token,email,createdTime))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()


# truy vấn token bằng email
def query_database_for_login_session_by_email( email):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/login_register.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    cursor.execute(f"SELECT * FROM login_session WHERE email=?", (email,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()

    return data


# for i in range(15):
#     c = query_database_for_login_session_by_email(email='1@gmail.com')
#     print(c)
