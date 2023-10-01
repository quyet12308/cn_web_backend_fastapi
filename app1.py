import asyncio
import json
from fastapi import FastAPI, HTTPException 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


from login_register_database import query_database_for_login_register_by_name,save_data_for_login_register_in_table,query_database_for_login_register_by_email,update_user_by_email

from get_code import generate_random_6_digit_number
from catcha_code_for_send_email import delayed_delete_confirm_code_by_email,query_database_for_confirm_code_by_email,save_data_for_confirm_code_in_table,query_data_by_email_with_max_id

from security_info import emails,passwords,urls
from string_python_en import responses

from contact_database import query_data_for_contact_in_table_by_email,save_data_for_contact_in_table

from send_emails import send_email_confirm_registration,send_email_forgot_password,send_email_reminder_admin_about_contact_customer

from gettime import gettime2,check_time_range
from get_token import generate_random_token_string

from home_screen_database import query_database_for_tourist_destination_information_by_id,get_all_data_from_table,save_data_in_table_tourist_destination_information,query_database_for_type_file_img_by_id,query_database_for_tourist_destination_information_by_name

from check_database import get_max_id_from_table

from base import random_number,random_3_numbers

# from .router_home import 

app = FastAPI()

# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Sửa đổi danh sách này để chỉ định các nguồn mà bạn muốn chấp nhận yêu cầu từ
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Data(BaseModel):
    username: str
    password:str
    email:str
    islogin:bool


@app.post("/api/login_basic")
async def login_basic(request_data: dict):
    if request_data:
        name_user = request_data["name"]
        password = request_data['pass']
        login_check = query_database_for_login_register_by_name(name=name_user)
        login_token = generate_random_token_string(length=12)
        if login_check:
            id1_,name1 , email1 , password1, createdtime1 = login_check
            if password == password1:
                return {"response":{
                    "message":responses["dang_nhap_thanh_cong"],
                    "status":True,
                    "token":login_token,
                    "email":email1
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

        


# forgot password
@app.post("/api/forgot_password_basic")
async def forgot_password_basic(request_data: dict):
    if request_data:
        email = request_data["email"]
        password = request_data["pass"]

        time_now = gettime2()
        check_email = query_database_for_login_register_by_email(email=email)

        if check_email :
            code = generate_random_6_digit_number()
            id_, name_,email_, password_,createdtime_ = check_email
            save_data_for_confirm_code_in_table(email=email,code=code,createdTime=time_now,username=name_)
            send_email_forgot_password(code=code,password=passwords["outlook"],to_email=email,username=name_)
            return {"response":{
                    "message":responses["check_email_to_get_code"],
                    "status":True
                }}
            
        else:
            return {"response":{
                    "message":responses["email_chua_duoc_dang_ky"],
                    "status":False
                }}
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
                    update_user_by_email(email=email,new_password=new_password,new_username=username1)
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

# register
@app.post("/api/register_basic")
async def register_basic(request_data: dict):
    if request_data:
        # print(f"data = {request_data} type data = {type(request_data)}")
        # Truy cập các phần riêng lẻ bằng cách sử dụng khóa
        name = request_data['name']
        password = request_data['pass']
        email = request_data['email']
        
        time_now = gettime2()
        check_email = query_database_for_login_register_by_email(email=email)
        if check_email :
                return {"response":{
                    "message":responses["email_da_duoc_dang_ky"],
                    "status":False
                }}
        else:

            #send confirm email
            code_randum = generate_random_6_digit_number()
            
            send_email_confirm_registration(username=name,code=code_randum,password=passwords["outlook"],to_email=email)
            save_data_for_confirm_code_in_table(createdTime=time_now,email=email,username=name,code=code_randum)
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
        check_code = query_data_by_email_with_max_id(email=email)
        id1 , username1,email1,createdTime1 ,code1 = check_code
        print(f"created time = {createdTime1}")
        if check_code:
            check_time = check_time_range(now_time=time_now,created_time=createdTime1,minute=3)#true nếu tạo và truy cập trong khoảng 3 phút
            if check_time:
                if code1 == code:
                    save_data_for_login_register_in_table(createdTime=time_now,email=email,password=password,username=username1)
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

@app.post("/api/contact_basic")
async def contact_basic(request_data: dict):
    if request_data:
        name = request_data['name']
        subject = request_data['subject']
        email = request_data['email']
        message = request_data['message']

        tim_now = gettime2()

        save_data_for_contact_in_table(createdTime=tim_now,email=email,username=name,message=message,subject=subject)
        send_email_reminder_admin_about_contact_customer(username=name,created_time=tim_now,password=passwords["outlook"],to_email=emails["email_admin"])
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

@app.get("/api/get_tourist_destination_information")
async def get_tourist_destination_information():
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
        ttestdata =  query_database_for_tourist_destination_information_by_id(random_num_list[i])
        testdata2 = query_database_for_type_file_img_by_id(random_num_list[i])
        id_ , name_ , type_file_ = testdata2
        id ,tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars ,number_of_travel_days = ttestdata
        
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

@app.post("/api/get_tourist_destination_information_by_name")
async def get_tourist_destination_information_by_name(request_data: dict):
    if request_data:
        name_ = request_data["name_"]
        token = request_data["token_"]
        # get_all_data_from_table()
        data_ = query_database_for_tourist_destination_information_by_name(name=name_)
        id ,tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars ,number_of_travel_days = data_
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
                    "number_of_travel_days":number_of_travel_days
                }
                
            }
        }

        


        

        

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app1:app", port=8080, workers=5, reload=True)