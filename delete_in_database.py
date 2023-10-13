

import sqlite3
from base_code.gettime import gettime3

def delete_table_in_database(database_name,table_name,enforcement_rights):
    if enforcement_rights == "admin":
        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect(f'database\{database_name}.db')

        # Tạo đối tượng cursor
        cursor = conn.cursor()

        # Tên của bảng bạn muốn xóa
        # table_name_to_delete = 'login_session'

        # Sử dụng lệnh SQL để xóa bảng
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

        # Lưu các thay đổi vào cơ sở dữ liệu
        conn.commit()

        # Đóng kết nối
        conn.close()
    else:
        print("you dont have a enforcement rights")

# delete_table_in_database(database_name="booking_tour",enforcement_rights="admin",table_name="booking_tour_basic")
# delete_table_in_database(database_name="visual_hotels_and_restaurent",enforcement_rights="admin",table_name=f"visual_hotels_and_restaurent_{gettime3()}")
# delete_table_in_database(database_name="offer",enforcement_rights="admin",table_name=f"offer_basic")
