import random

def get_random_elements(lst):
    result = []
    for _ in range(5):
        start = random.randint(0, 4) * 8
        end = start + 7
        element = random.randint(start, end)
        result.append(lst[element])
    return result


def get_random_elements2(lst):
    result = []
    for i in range(5):
        start2 = i * 8
        end2 = start2 + 7
        element2 = random.randint(start2,end2)
        # start = random.randint(0, 4) * 8
        # end = start + 7
        # element = random.randint(start, end)
        result.append(element2)
    return result
# Ví dụ sử dụng
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
# random_elements = get_random_elements2(my_list)
# print(random_elements)

# print(random.randint(1,10))