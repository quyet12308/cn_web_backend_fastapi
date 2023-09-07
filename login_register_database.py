import sqlite3

def create_database_for_login_register_basic():
    
    # Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
    conn = sqlite3.connect('database/login_register.db')

    # Tạo một đối tượng cursor để thực thi truy vấn
    cursor = conn.cursor()
    
        # Tạo bảng diseases
    cursor.execute(f'''CREATE TABLE basic_login_register
                  (id INTEGER PRIMARY KEY,
                   username TEXT,
                   email TEXT,
                   password TEXT,
                   createdTime TEXT)''')
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# create_database_for_login_register_basic()

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

# a = query_database_for_login_register_by_name(name="abc")
# print(a)

