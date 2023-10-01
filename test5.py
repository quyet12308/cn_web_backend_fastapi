def chuyen_doi_chuoi(chuoi):
    # Tách chuỗi thành các thành phần
    parts = chuoi.split(' ')
    
    # Xử lý thành phần đầu tiên
    part1 = parts[0]
    degrees1, minutes1, direction1 = part1.split('°', '′')
    degrees1 = degrees1.strip()
    minutes1 = minutes1.strip()
    direction1 = direction1.strip()
    if direction1 == 'B':
        degrees1 = '-' + degrees1
    
    # Xử lý thành phần thứ hai
    part2 = parts[1]
    degrees2, minutes2, direction2 = part2.split('°', '′')
    degrees2 = degrees2.strip()
    minutes2 = minutes2.strip()
    direction2 = direction2.strip()
    if direction2 == 'Đ':
        degrees2 = '-' + degrees2
    
    # Tạo chuỗi kết quả
    result = degrees1 + '.' + minutes1 + ' ' + degrees2 + '.' + minutes2
    
    return result

# Sử dụng hàm
chuoi = "24°28′B 54°22′Đ"
ket_qua = chuyen_doi_chuoi(chuoi)
print(ket_qua)

