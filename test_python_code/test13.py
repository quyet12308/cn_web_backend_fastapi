text = """id INTEGER PRIMARY KEY,
                   username TEXT,
                   fullname TEXT,
                   email TEXT,
                   timeCheckin TEXT,
                   timeCheckout TEXT,
                   booking_tour_name TEXT,
                   booking_tour_id TEXT,
                   number_adults TEXT,
                   number_children TEXT,
                   flight_infor TEXT,
                   hotel_infor TEXT,
                   support_persion TEXT,
                   createdTime TEXT
"""

def get_element_of_table(str_element):
    list_text = str_element.splitlines()
    print(list_text)

    list_text1 = []
    for i in list_text:
        text1 = i.strip()
        print(i.strip())
        # list_text1.append(i.strip())
        text2 = text1.split(" ")
        text3 = text2[0]
        print(text3)
        list_text1.append(text3)

    print(list_text1)
    return list_text1


