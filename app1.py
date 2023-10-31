# phầm import các thư viện dngf trong dự án và import các file , api khác vào file app1.py để sử dụng .

import asyncio
import json
from fastapi import FastAPI, HTTPException # import fastapi để sử dụng trong dự án
from fastapi.middleware.cors import CORSMiddleware # import thư viện cors để bỏ chặn bảo mật giữa frontend và backend
from pydantic import BaseModel

# import các thư viện và api khác tự tạo ở các file khác vào file app1.py này để sử dụng
from login_register_database import query_database_for_login_register_by_name,save_data_for_login_register_in_table,query_database_for_login_register_by_email,update_user_by_email

from base_code.get_code import generate_random_6_digit_number
from catcha_code_for_send_email import delayed_delete_confirm_code_by_email,query_database_for_confirm_code_by_email,save_data_for_confirm_code_in_table,query_data_by_email_with_max_id

from base_code.security_info import emails,passwords,urls
from base_code.string_python_en import responses

from contact_database import query_data_for_contact_in_table_by_email,save_data_for_contact_in_table

from email_with_python.send_emails import send_email_confirm_registration,send_email_forgot_password,send_email_reminder_admin_about_contact_customer

from base_code.gettime import gettime2,check_time_range,gettime3,check_availability,check_time_range2,gettime4
from base_code.get_token import generate_random_token_string

from home_screen_database import query_database_for_tourist_destination_information_by_id,get_all_data_from_table,save_data_in_table_tourist_destination_information,query_database_for_type_file_img_by_id,query_database_for_tourist_destination_information_by_name,query_database_for_tourist_destination_information_all_table

from check_database import get_max_id_from_table,check_table_existence

from base_code.base import random_number,random_3_numbers

from connect_open_weather_api import get_5_datas_from_5_day_weather

from book_hotel_restaurant_database import create_database_for_visual_hotels_and_restaurent_basic1,query_database_for_visual_hotels_and_restaurent_by_tourist_destination_name,save_data_for_visual_hotels_and_restaurent_in_table

from connect_api_travel import get_data_hotel_from_api_rapidapi

from offers_database import query_database_for_offer_by_id_hotel,sort_data_offer_database

from booking_tour_database import delete_data_booking_tour_by_id,update_data_booking_tour_by_id,save_data_for_booking_tour_basic_in_table,query_database_for_booking_tour_by_email,query_database_for_booking_tour_by_id,query_database_for_booking_tour_by_email_all,delete_data_booking_tour_by_email_and_created_time
# from .router_home import 

app = FastAPI() # khởi tạo app fastapi

# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #  chỉ định các nguồn mà bạn muốn chấp nhận yêu cầu từ server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Data(BaseModel):
    username: str
    password:str
    email:str
    islogin:bool

# chức năng login 
@app.post("/api/login_basic") # api login 
async def login_basic(request_data: dict): # hàm xử lý chức năng login
    if request_data:
        name_user = request_data["name"] # nhận các tham số từ frontend
        password = request_data['pass']
        login_check = query_database_for_login_register_by_name(name=name_user) # truy xuất trong database bằng name truyền vào từ frontend
        login_token = generate_random_token_string(length=12) # tạo token cho phiên đăng nhập
        if login_check:
            # id1_,name1 , email1 , password1, createdtime1 = login_check
            password1 = login_check["password"]
            email1 = login_check["email"]
            avata_img1 = login_check["avata_img"]
            if password == password1:
                return {"response":{
                    "message":responses["dang_nhap_thanh_cong"],
                    "status":True,
                    "token":login_token,
                    "email":email1,
                    "avata_img":avata_img1
                }}
            else:
                return {"response":{
                    "message":responses["sai_mat_khau"],
                    "status":False
                }}
        else:
            return {"response":{
                    "message":responses["tai_khoan_chua_duoc_dang_ky"],
                    "status":False
                }}

        


#chức năng forgot password 
@app.post("/api/forgot_password_basic") # api đăng nhập
async def forgot_password_basic(request_data: dict): # hàm chức năng đăng nhập
    if request_data:
        email = request_data["email"] # lấy data từ frontend
        password = request_data["pass"]

        time_now = gettime2() # lấy time hiện tại
        check_email = query_database_for_login_register_by_email(email=email) # truy xuất databas bằng email 

        if check_email :
            code = generate_random_6_digit_number() # tạo code để xác nhận cho chức năng quên mật khẩu
            # id_, name_,email_, password_,createdtime_ = check_email
            name_ = check_email["username"]
            save_data_for_confirm_code_in_table(email=email,code=code,createdTime=time_now,username=name_) # lưu code,name và email vào catcha
            send_email_forgot_password(code=code,password=passwords["outlook"],to_email=email,username=name_) # giử email quên mật khẩu
            return {"response":{
                    "message":responses["check_email_to_get_code"],
                    "status":True
                }}
            
        else:
            return {"response":{
                    "message":responses["email_chua_duoc_dang_ky"],
                    "status":False
                }}
        
# xác nhận code khi forgot password
@app.post("/api/forgot_password_confirm_code_email")
async def forgot_password_confirm_code_email(request_data: dict):
    if request_data:
        new_password = request_data['pass']
        email = request_data['email']
        code = request_data['code']

        time_now = gettime2()
        print(f"time now {time_now}")
        print(type(time_now))
        #get code from catcha ( sqlite delete after 3 minutes)
        check_code = query_data_by_email_with_max_id(email=email) 
        id1 , username1,email1,createdTime1 ,code1 = check_code
        print(f"created time = {createdTime1}")
        if check_code:
            check_time = check_time_range(now_time=time_now,created_time=createdTime1,minute=3)#true nếu tạo và truy cập trong khoảng 3 phút
            if check_time:
                if code1 == code:
                    update_user_by_email(column="password",email=email,value=new_password)
                    # update_user_by_email(email=email,new_password=new_password,new_username=username1)
                    return {"response":{
                        "message":responses["cap_nhat_mat_khau_moi_thanh_cong"],
                        "status":True
                    }}
                else:
                    return {"response":{
                        "message":responses["sai_code"],
                        "status":False
                    }}
            else:
                return {"response":{
                        "message":responses["code_bi_qua_thoi_gian"],
                        "status":False
                    }}

# chức năng register
@app.post("/api/register_basic")
async def register_basic(request_data: dict):
    if request_data:
        # print(f"data = {request_data} type data = {type(request_data)}")
        # Truy cập các phần riêng lẻ bằng cách sử dụng khóa
        name = request_data['name']
        password = request_data['pass']
        email = request_data['email']
        
        time_now = gettime2()
        check_email = query_database_for_login_register_by_email(email=email) # truy xuất dữ liệu bằng email cho chức năng đăng ký
        if check_email :
                return {"response":{
                    "message":responses["email_da_duoc_dang_ky"],
                    "status":False
                }}
        else:

            #send confirm email
            code_randum = generate_random_6_digit_number()
            
            send_email_confirm_registration(username=name,code=code_randum,password=passwords["outlook"],to_email=email) # gửi email
            save_data_for_confirm_code_in_table(createdTime=time_now,email=email,username=name,code=code_randum) # lưu data vào catcha
            # asyncio.create_task(delayed_delete_confirm_code_by_email(email=email,delay_minutes=3))# chức năng này tạm thời đóng băng để thực hiện giải pháp khác ( so sánh time tạo và time truy cập)
            
            return {"response":{
                    "message":responses["check_email_to_get_code"],
                    "status":True
                }}
            # return json.dumps(a)
    else:
        return {"response":{
                    "message":responses["co_loi_xay_ra"],
                    "status":False
                }}

# xác nhận code khi register
@app.post("/api/register_confirm_code_email")
async def register_confirm_code_email(request_data: dict):
    if request_data:
        password = request_data['pass']
        email = request_data['email']
        code = request_data['code']


        time_now = gettime2()
        print(f"time now {time_now}")
        print(type(time_now))
        #get code from catcha ( sqlite delete after 3 minutes)
        check_code = query_data_by_email_with_max_id(email=email) # hàm check code catcha
        id1 , username1,email1,createdTime1 ,code1 = check_code
        print(f"created time = {createdTime1}")
        if check_code:
            check_time = check_time_range(now_time=time_now,created_time=createdTime1,minute=3)#true nếu tạo và truy cập trong khoảng 3 phút
            if check_time:
                if code1 == code:
                    save_data_for_login_register_in_table(createdTime=time_now,email=email,password=password,username=username1) # lưu thông tin
                    return {"response":{
                        "message":responses["dang_ky_thanh_cong"],
                        "status":True
                    }}
                else:
                    return {"response":{
                        "message":responses["sai_code"],
                        "status":False
                    }}
            else:
                return {"response":{
                        "message":responses["code_bi_qua_thoi_gian"],
                        "status":False
                    }}

# chức năng contact
@app.post("/api/contact_basic")
async def contact_basic(request_data: dict):
    if request_data:
        name = request_data['name']
        subject = request_data['subject']
        email = request_data['email']
        message = request_data['message']

        tim_now = gettime2()

        save_data_for_contact_in_table(createdTime=tim_now,email=email,username=name,message=message,subject=subject) # lưu thông tin contact
        send_email_reminder_admin_about_contact_customer(username=name,created_time=tim_now,password=passwords["outlook"],to_email=emails["email_admin"]) #gửi email cho admin
        return {"response":{
                        "message":responses["cam_on_dong_gop_cua_ban"],
                        "status":True
                    }}

#test api to get img
@app.get("/api/test_to_get_img")
async def test_get_img():
    max_id = get_max_id_from_table(path_of_database='database\\tourist_destination_information.db',table_name="type_of_file_img")
    randum_num = random_number(end=max_id,start=1)
    ttestdata =  query_database_for_tourist_destination_information_by_id(randum_num)
    testdata2 = query_database_for_type_file_img_by_id(randum_num)
    id_ , name_ , type_file_ = testdata2
    id ,tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars ,number_of_travel_days = ttestdata
    return {
        "response":{
            "url_img":img_base64,
            "name":tourist_destination_name,
            "type_file": type_file_,
            "describe":tourist_destination_describe
        }
    }

# hiển thị tour trên trang chính
@app.get("/api/get_tourist_destination_information")
async def get_tourist_destination_information():
    # update dữ liệu hotel 
    # gettime3 = gettime3()
    # check_data_hotel_is_upadate_for_today = check_table_existence(database_name="database\\visual_hotels_and_restaurent.db",table_name=f"visual_hotels_and_restaurent_{gettime3()}")
    # if check_data_hotel_is_upadate_for_today :
    #     print("data hotel is update")
    # else:
    #     create_database_for_visual_hotels_and_restaurent_basic1(day=gettime3(),tablename="visual_hotels_and_restaurent")
    #     max_id = get_max_id_from_table(path_of_database="database\\tourist_destination_information.db",table_name="tourist_destination_information_basic_for_get_data2")
    #     for i in range(1,max_id + 1):
    #         data6 = query_database_for_tourist_destination_information_by_id(id=i)
    #         data6_tourist_destination_name = data6["tourist_destination_name"]
    #         data6_lat = data6["lat"]
    #         data6_lon = data6["lon"]
    #         result = str(get_data_hotel_from_api_rapidapi(lon=data6_lon,lat=data6_lat))
    #         save_data_for_visual_hotels_and_restaurent_in_table(createdTime=gettime2(),data=result,lat=data6_lat,lon=data6_lon,tourist_destination_name=data6_tourist_destination_name,table_name=f"visual_hotels_and_restaurent_{gettime3()}")




    tourist_destination_name_arr = []
    img_base64_arr = []
    price_arr = []
    the_right_time_to_go_arr = []
    tourist_destination_describe_arr = []
    tourist_destination_location_arr = []
    number_of_stars_arr = []
    number_of_travel_days_arr = []
    type_file_arr = []
    max_id = get_max_id_from_table(path_of_database='database\\tourist_destination_information.db',table_name="type_of_file_img")
    random_num_list = random_3_numbers(end=max_id,start=1)
    for i in range(3):

        # max_id = get_max_id_from_table(path_of_database='database\\tourist_destination_information.db',table_name="type_of_file_img")
        # randum_num = random_number(end=max_id,start=1)
        ttestdata =  query_database_for_tourist_destination_information_by_id(random_num_list[i]) # lấy thông tin các tour du lịch
        testdata2 = query_database_for_type_file_img_by_id(random_num_list[i])
        id_ , name_ , type_file_ = testdata2
        # id ,tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars ,number_of_travel_days = ttestdata
        
        tourist_destination_name = ttestdata["tourist_destination_name"]
        img_base64 = ttestdata["img_base64"]
        price = ttestdata["price"]
        the_right_time_to_go = ttestdata["the_right_time_to_go"]
        tourist_destination_describe = ttestdata["tourist_destination_describe"]
        tourist_destination_location = ttestdata["tourist_destination_location"]
        number_of_stars = ttestdata["number_of_stars"]
        number_of_travel_days = ttestdata["number_of_travel_days"]

        tourist_destination_name_arr.append(tourist_destination_name)
        img_base64_arr.append(img_base64)
        price_arr.append(price)
        the_right_time_to_go_arr.append(the_right_time_to_go)
        tourist_destination_describe_arr.append(tourist_destination_describe)
        tourist_destination_location_arr.append(tourist_destination_location)
        number_of_stars_arr.append(number_of_stars)
        number_of_travel_days_arr.append(number_of_travel_days)
        type_file_arr.append(type_file_)

        
    return {
            "response":{
                "tourist_destination_name_arr":tourist_destination_name_arr,
                "img_base64_arr":img_base64_arr,
                "price_arr": price_arr,
                "the_right_time_to_go_arr":the_right_time_to_go_arr,
                "tourist_destination_describe_arr":tourist_destination_describe_arr,
                "tourist_destination_location_arr":tourist_destination_location_arr,
                "number_of_stars_arr":number_of_stars_arr,
                "number_of_travel_days_arr":number_of_travel_days_arr,
                "type_file_arr":type_file_arr
            }
        }

# hiện thông tin tour chi tiết 
@app.post("/api/get_tourist_destination_information_by_name")
async def tourist_destination_information_by_name(request_data: dict):
    if request_data:
        name_ = request_data["name"]
        token = request_data["token"]
        # print(name_)
        # get_all_data_from_table()
        
        data_ = query_database_for_tourist_destination_information_by_name(name=name_) # lấy thông tin các tour du lịch
        # print(data_)
        tourist_destination_name = data_["tourist_destination_name"]
        img_base64 = data_["img_base64"]
        price = data_["price"]
        the_right_time_to_go = data_["the_right_time_to_go"]
        tourist_destination_describe = data_["tourist_destination_describe"]
        tourist_destination_location = data_["tourist_destination_location"]
        number_of_stars = data_["number_of_stars"]
        number_of_travel_days = data_["number_of_travel_days"]
        lat = data_["lat"]
        lon = data_["lon"]
        hotel_info = data_["hotel_info"]
        five_day_weather_datas = get_5_datas_from_5_day_weather(lang="vi",lat=lat,lon=lon) # lấy thông tin thời tiết
        # id_ ,tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars ,number_of_travel_days = data_
        return {
            "response":{
                "status":True,
                'message':{
                    "tourist_destination_name":tourist_destination_name,
                    "img_base64":img_base64,
                    "price": price,
                    "the_right_time_to_go":the_right_time_to_go,
                    "tourist_destination_describe":tourist_destination_describe,
                    "tourist_destination_location":tourist_destination_location,
                    "number_of_stars":number_of_stars,
                    "number_of_travel_days":number_of_travel_days,
                    "five_day_weather_datas":five_day_weather_datas,
                    "hotel_info":hotel_info
                }
                
            }
        }

# hiện thông tin người dùng 
@app.post("/api/get_user_infor")
async def get_user_infor(request_data: dict):
    if request_data:
        name = request_data["name"]
        email = request_data["email"]

        data2 = query_database_for_login_register_by_email(email=email) # lây thông tin người dùng
        # print(data2)
        # id2_ ,username2_, email2_,password2_,createdTime2_ = data2
        username2_ = data2['username'] 
        avatar_img2_ = data2['avata_img']
        # avatar_img2_ = data2.get("avatar_img")
        birthday2_ = data2['birthday']
        email2_ = data2['email']
        password2_ = data2['password']
        createdTime2_ = data2['createdTime']

        # if avatar_img2_ is None :
        #     avatar_img2_ = ""
        # if birthday2_ is None:
        #     birthday2_ = ""
        # print(avatar_img2_)
        return {
            "response":{
                "status":True,
                'message':{
                    "username":username2_,
                    "avatar_img":avatar_img2_,
                    "birthday": birthday2_,
                    "email":email2_,
                    "password":password2_,
                    "createdTime":createdTime2_
                }
                
            }
        }
# sửa thông tin người dùng
@app.post("/api/edit_user_infor")
async def edit_user_infor(request_data: dict):
    if request_data:
        # print(request_data)
        email_ = request_data["email"]
        username_ = request_data["username"]
        password_ = request_data["password"]
        birthday_ = request_data["birthday"]
        avatar_img_ = request_data["avatar_img"]

        # print(username_)
        # print(password_)
        # print(birthday_)
        # print(avatar_img_)

        if email_:
            check_email = query_database_for_login_register_by_email(email=email_)
            if check_email :
                check_username = query_database_for_login_register_by_name(name=username_) # lấy thông tin người dùng
                update_user_by_email(column="birthday",email=email_,value=birthday_) # update các thông tin mới 
                update_user_by_email(column="password",email=email_,value=password_)
                update_user_by_email(column="avata_img",email=email_,value=avatar_img_)
                if check_username:
                    return {"response":{
                    "message":responses["user_da_ton_tai"],
                    "status":False
                    }}
                else:
                    update_user_by_email(column="username",email=email_,value=username_)
                    
                    return {"response":{
                        "message":responses["sua_thong_tin_thanh_cong"],
                        "status":True
                    }}
            else:
                return {"response":{
                    "message":responses["email_chua_duoc_dang_ky"],
                    "status":False
                }}

# chức năng offer hotel đăng hoàn thiện       
@app.post("/api/get_offer_data")
        
   
async def get_offer_data(request_data: dict):
    if request_data:

        price_offer = request_data["price_offer"]
        name_hotel_offer = request_data["name_hotel_offer"]
        star_offer = request_data["star_offer"]
        distance_offer = request_data["distance_offer"]
        review_offer = request_data["review_offer"]

        print(f"{price_offer} , {name_hotel_offer} , {star_offer} , {distance_offer} , {review_offer}")

        data = sort_data_offer_database(
            table_name="offer_basic",
            distance_offer=distance_offer,
            name_hotel_offer=name_hotel_offer,
            price_offer=price_offer,
            star_offer=star_offer,
            review_offer=review_offer
            )
        
        return {
            "response":{
                "status":True,
                'message':{
                    "id_hotel":data["id_hotel"],
                    "hotel_name":data["hotel_name"],
                    "stars": data["stars"],
                    "price":data["price"],
                    "num_reviews":data["num_reviews"],
                    "avata_img":data["avata_img"],
                    "describe_hotel":data["describe_hotel"]
                }
                
            }
        }  

@app.post("/api/the_blog")
async def the_blog(request_data: dict):
    if request_data:
        pass

@app.post("/api/booking_tour")
async def booking_tour(request_data: dict):
    if request_data:
        # print(request_data)
        full_name = request_data["full_name"]
        email = request_data["email"]
        num_adults = request_data["num_adults"]
        num_children = request_data["num_children"]
        time = request_data["time"]
        price = request_data["price"]
        name_tour = request_data["name_tour"]
        days = request_data["days"]
        name_hotel = request_data["name_hotel"]

        # check data
        data = query_database_for_booking_tour_by_email(email=email)
        if data == None:
            # save data
            t = gettime2()
            save_data_for_booking_tour_basic_in_table(
                booking_tour_name=name_tour,
                createdTime=t,
                days=days,
                email=email,
                fullname=full_name,
                hotel_infor=name_hotel,
                number_adults=num_adults,
                number_children=num_children,
                price=price,
                timeCheckin=time
            )
            return  {
                "response":{
                    "status":True,
                    'message': responses["booking_tour_thanh_cong"]
                    
                }
            } 
        else:
            # print(data["days"])
            # print(data["timeCheckin"])
            # print(time)
            check_time = check_availability(days=int(data["days"]),time1=data["timeCheckin"],time2=time)
            if check_time:
                t = gettime2()
                save_data_for_booking_tour_basic_in_table(
                booking_tour_name=name_tour,
                createdTime=t,
                days=days,
                email=email,
                fullname=full_name,
                hotel_infor=name_hotel,
                number_adults=num_adults,
                number_children=num_children,
                price=price,
                timeCheckin=time
            )
                return  {
                "response":{
                    "status":True,
                    'message': responses["booking_tour_thanh_cong"]
                    
                }
            }
            else:
                return  {
                "response":{
                    "status":False,
                    'message': responses["thoi_gian_nay_ban_dang_lua_chon_tour_du_lich_khac_roi"]
                    
                }
            } 

@app.post("/api/my_booking_tour")
async def my_booking_tour(request_data: dict):
    if request_data:
        email = request_data["email"]
        print(request_data)
        data_list = query_database_for_booking_tour_by_email_all(email=email)
        if data_list:
            img_tours = []
            for i in range(len(data_list)):
                name_tour = data_list[i]["booking_tour_name"]
                print(name_tour)
                data4 = query_database_for_tourist_destination_information_by_name(name=name_tour)
                img_tour = data4["img_base64"]
                img_tours.append(img_tour)
            return  {
                "response":{
                    "status":True,
                    'message': {
                        "data_list":data_list,
                        "img_tours_list":img_tours
                    }
                    
                }
            } 
        else:
            return  {
                "response":{
                    "status":False,
                    'message': responses["ban_chua_dang_ky_tour_du_lich_nao"]
                    
                }
            } 
@app.post("/api/delete_my_booking_tour")
async def delete_my_booking_tour(request_data: dict):
    if request_data:
        email = request_data["email"]
        created_time = request_data["created_time"]
        timeCheckin = request_data["timeCheckin"]
        # print(request_data)
        # print(timeCheckin)
        # print(created_time)

        time_now = gettime4()
        print(time_now)
        check_time = check_time_range2(date2=str(timeCheckin),date1=time_now,days=3)
        print(f"check time = {check_time}")
        if check_time:
            delete_data_booking_tour_by_email_and_created_time(createdTime=str(created_time),email=email)

            return  {
                "response":{
                    "status":True,
                    'message': responses["tour_du_lich_da_duoc_xoa_thanh_cong"]
                }
            }
        else:
            return  {
                "response":{
                    "status":False,
                    'message': responses["tour_da_het_thoi_gian_de_xoa"]
                }
            }

@app.get("/api/show_all_tour")
async def show_all_tour():
    data = query_database_for_tourist_destination_information_all_table()
    id_list = data['id']
    tourist_destination_name_list = data['tourist_destination_name']
    img_base64_list = data["img_base64"]
    price_list = data["price"]
    the_right_time_to_go_list = data["the_right_time_to_go"]
    number_of_stars_list = data["number_of_stars"]
    tourist_destination_describe_list = data["tourist_destination_describe"]
    tourist_destination_location_list = data["tourist_destination_location"]
    number_of_travel_days_list = data["number_of_travel_days"]
    hotel_info_list = data["hotel_info"]

    return  {
                "response":{
                    "status":True,
                    'message': {
                        "id_list":id_list,
                        "tourist_destination_name_list":tourist_destination_name_list,
                        "img_base64_list":img_base64_list,
                        "price_list":price_list,
                        "the_right_time_to_go_list":the_right_time_to_go_list,
                        "number_of_stars_list":number_of_stars_list,
                        "tourist_destination_describe_list":tourist_destination_describe_list,
                        "tourist_destination_location_list":tourist_destination_location_list,
                        "number_of_travel_days_list":number_of_travel_days_list,
                        "hotel_info_list":hotel_info_list
                    }
                }
            } 
    
        

        

        
# nơi khởi chạy
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app1:app", port=8080, workers=5, reload=True) # chạy trên cổng 8080 , worker = 5 và có reload để mỗi khi dự án thay đổi thì tự động cập nhật