from login_register_database import save_data_for_login_register_in_table,query_database_for_login_register_by_id

from delete_in_database import delete_table_in_database



data = [
    (1, '000000', '1@gmail.com', '123456a', '2023-09-07 17:17:34'),
None,
(3, 'nhom13', 'quyet12308@gmail.com', '123456a', '2023-09-14 14:59:17'),
(4, 'Cuong Nguuyen', 'cuong.fithau@gmail.com', 'abc123', '2023-09-15 09:59:01'),
(5, 'lam123', 'quyet12306@gmail.com', '000000a', '2023-09-16 08:51:15'),
(6, 'tung123', 'tngthanh62@gmail.com', '123456a', '2023-10-04 10:34:59'),
(7, 'test123', 'nguyenviet212002@gmail.com', '123456a', '2023-10-06 10:11:42'),
]

# for i in data:
#     # print(i)
#     if i is None:
#         print(None)
#     else:
#         a = list(i)
#         print(a)

data2 = [
    [1, '000000', '1@gmail.com', '123456a', '2023-09-07 17:17:34'],
    # None,
    [3, 'nhom13', 'quyet12308@gmail.com', '123456a', '2023-09-14 14:59:17'],
    [4, 'Cuong Nguuyen', 'cuong.fithau@gmail.com', 'abc123', '2023-09-15 09:59:01'],
    [5, 'lam123', 'quyet12306@gmail.com', '000000a', '2023-09-16 08:51:15'],
    [6, 'tung123', 'tngthanh62@gmail.com', '123456a', '2023-10-04 10:34:59'],
    [7, 'test123', 'nguyenviet212002@gmail.com', '123456a', '2023-10-06 10:11:42']
]

# for i in range(len(data2)):
#     if i is None:
#         pass
#     save_data_for_login_register_in_table(createdTime=data2[i][4],email=data2[i][2],password=data2[i][3],username=data2[i][1])

# for i in range(10):
#     a = query_database_for_login_register_by_id(i)
#     print(a)

# delete_table_in_database(database_name="login_register",table_name="basic_login_register2")