import sqlite3

list_element = ['id', 'username', 'fullname', 'email', 'timeCheckin', 'days', 'booking_tour_name', 'booking_tour_id', 'number_adults', 'number_children', 'flight_infor', 'hotel_infor', 'support_persion', 'createdTime']

def create_database_for_booking_tour_basic(tablename):
    
    # Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
    conn = sqlite3.connect('database/booking_tour.db')

    # Tạo một đối tượng cursor để thực thi truy vấn
    cursor = conn.cursor()
    
        # Tạo bảng diseases
    cursor.execute(f'''CREATE TABLE {tablename}
                  (id INTEGER PRIMARY KEY,
                   username TEXT,
                   fullname TEXT,
                   email TEXT,
                   timeCheckin TEXT,
                   days TEXT,
                   booking_tour_name TEXT,
                   booking_tour_id TEXT,
                   number_adults TEXT,
                   number_children TEXT,
                   flight_infor TEXT,
                   hotel_infor TEXT,
                   support_persion TEXT,
                   createdTime TEXT)''')
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# create_database_for_booking_tour_basic(tablename="booking_tour_basic")


# lưu dữ liệu 
def save_data_for_booking_tour_basic_in_table( username,fullname,email,timeCheckin,days,booking_tour_name,booking_tour_id,number_adults,number_children,flight_infor,hotel_infor,support_persion,createdTime):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/booking_tour.db')
    cursor = conn.cursor()

    # Thêm dữ liệu vào bảng diseases
    # chuyển dữ liệu qua bảng mới basic_login_register2
    # if birthday is None and avata_img is None:
    #     birthday = avata_img == ""
    cursor.execute(f"INSERT INTO booking_tour_basic (username,fullname,email,timeCheckin,days,booking_tour_name,booking_tour_id,number_adults,number_children,flight_infor,hotel_infor,support_persion,createdTime) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
               (username,fullname,email,timeCheckin,days,booking_tour_name,booking_tour_id,number_adults,number_children,flight_infor,hotel_infor,support_persion,createdTime))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

#delete
# def delete_data_for_booking_tour_basic_by_name(name):
#     # Đợi một khoảng thời gian (tính bằng giây) trước khi thực hiện xóa
#     # time.sleep(delay_minutes * 60)

#     # Kết nối tới cơ sở dữ liệu
#     conn = sqlite3.connect('database/login_register.db')
#     cursor = conn.cursor()

#     # Xóa dữ liệu từ bảng test dựa trên tên
#     # chuyển dữ liệu qua bảng mới basic_login_register2
#     cursor.execute("DELETE FROM basic_login_register2 WHERE username=?", (name,))

#     # Lưu thay đổi và đóng kết nối
#     conn.commit()
#     conn.close()