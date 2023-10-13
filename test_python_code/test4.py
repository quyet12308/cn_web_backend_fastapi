# from home_screen_database import query_database_for_tourist_destination_information_by_id

data_for_location_openweather = {
"Đại thánh đường Sheikh Zayed, Abu Dhabi,  Abu Dhabi, thủ đô Các Tiểu vương quốc Ả Rập Thống nhất":"24.28 54.22",
"Đông Xuyên, Trung Quốc,  Tây Nam Côn Minh, thủ phủ tỉnh Vân Nam , Trung Quốc":"35.04 109.05",
"Ốc đảo sa mạc Huacachina, cạnh thủ đô Lima của Peru":"-12.2 -77.2",
"Cửu Trại Câu, châu tự trị dân tộc Khương, dân tộc Tạng A Bá, ở miền Bắc tỉnh Tứ Xuyên, Trung Quốc":"33.12 103.54",
"Isola Bella, Một trong những Quần đảo Borromean của Lago Maggiore ở Bắc Ý ":"45.53 8.31",
"Nhà thờ Las Lajas, Nằm trên một hẻm núi thuộc biên giới Colombia và Ecuador ":"0.48 -77.35",
"LonDon, Thủ đô của Anh":"51.30 -0.7",
"Mauritius, Một phần của quần đảo Mascarene, Ấn Độ Dương":"-20.12 57.30",
"Lệ giang cổ trấn , Vân Nam, Trung Quốc":"26.52 100.14",
"Phúc Kiến Thổ Lâu, Đông nam tỉnh Phúc Kiến, Trung Quốc.":"25.1 117.41",
"Phượng Hoàng Cổ Trấn, Phía tây tỉnh Hồ Nam, bên cạnh dòng Đà Giang":"27.56 109.36",
"Popeye, Malta, Thuộc Vịnh Anchor trên vùng biển Địa Trung Hải, phía Tây Bắc Malta":"35.58 14.20",
"Santorini Greece, Phía nam biển Aegean , Hy Lạp":"36.24 25.25",
"Scotland, Phía bắc Vương quốc Anh":"57 -4",
"Setenil de las Bodegas, Setenil de las Bodegas, Tây Ban Nha":"36.51 -5.10",
"Thung lũng Shangrila, Tây Bắc tỉnh Vân Nam ,Trung Quốc":"27.50 99.42",
"Thác Havasu, Arizona, Grand Canyon, Arizona, Hoa Kỳ":"36.15 -112.41"
}

arr_test = []
for key, value in data_for_location_openweather.items():
    print(value)
    arr_test.append(value)
print(arr_test)


