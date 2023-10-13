# from catcha_code_for_send_email import delayed_delete_confirm_code_by_email,query_database_for_confirm_code_by_email,save_data_for_confirm_code_in_table

# for i in range(10):
#     print(query_database_for_confirm_code_by_email)

# import re

# sql_query = """
#     CREATE TABLE IF NOT EXISTS tourist_destinations
#     (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         tourist_destination_name TEXT NOT NULL,
#         img_base64 TEXT NOT NULL,
#         price TEXT NOT NULL,
#         the_right_time_to_go TEXT NOT NULL,
#         createdTime TEXT NOT NULL,
#         tourist_destination_describe TEXT NOT NULL,
#         tourist_destination_location TEXT NOT NULL,
#         number_of_stars TEXT NOT NULL
#     );
# """

# def extract_column_names(sql_query):
#     pattern = r"([a-zA-Z_]+) TEXT NOT NULL"
#     column_names = re.findall(pattern, sql_query)
#     return column_names

# column_names = extract_column_names(sql_query)
# print(column_names)

# # In tên các thuộc tính
# for column_name in column_names:
#     print(column_name)

# import re

# sql_query = """
#     CREATE TABLE IF NOT EXISTS tourist_destinations
#     (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         tourist_destination_name TEXT NOT NULL,
#         img_base64 TEXT NOT NULL,
#         price TEXT NOT NULL,
#         the_right_time_to_go TEXT NOT NULL,
#         createdTime TEXT NOT NULL,
#         tourist_destination_describe TEXT NOT NULL,
#         tourist_destination_location TEXT NOT NULL,
#         number_of_stars TEXT NOT NULL
#     );
# """

# def extract_column_names(sql_query):
#     pattern = r"([a-zA-Z_]+)\sTEXT NOT NULL,"
#     column_names = re.findall(pattern, sql_query)
#     return column_names

# column_names = extract_column_names(sql_query)
# print(column_names)

# # In tên các thuộc tính
# for column_name in column_names:
#     print(column_name)