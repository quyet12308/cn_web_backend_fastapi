import random

def random_number(start, end):
    return random.randint(start, end)


def random_3_numbers(start, end):
    # Tạo một danh sách các số từ start đến end
    number_list = list(range(start, end + 1))
    
    # Kiểm tra nếu danh sách không đủ 3 số thì trả về danh sách đó
    if len(number_list) < 3:
        return number_list

    # Lấy ngẫu nhiên 3 số không trùng nhau từ danh sách
    random_numbers = random.sample(number_list, 3)

    return random_numbers

def cover_kelvin_to_c(kelvin):
    c = kelvin - 273.15
    return c