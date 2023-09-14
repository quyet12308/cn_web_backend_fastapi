import asyncio
import json
from fastapi import FastAPI, HTTPException 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


from login_register_database import query_database_for_login_register_by_name,save_data_for_login_register_in_table,query_database_for_login_register_by_email
from confirm_email_registration import send_email_confirm_registration
from get_code import generate_random_6_digit_number
from catcha_code_for_send_email import delayed_delete_confirm_code_by_email,query_database_for_confirm_code_by_email,save_data_for_confirm_code_in_table,query_data_by_email_with_max_id

from security_info import emails,passwords,urls
from string_python_en import responses

from gettime import gettime2,check_time_range
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



# @app.post("/api/login_register")
# async def login_register(request_data: dict):
#     # Kiểm tra xem yêu cầu POST có dữ liệu không
#     if request_data:
#         # print(f"data = {request_data} type data = {type(request_data)}")
#         # Truy cập các phần riêng lẻ bằng cách sử dụng khóa
#         name = request_data['name']
#         password = request_data['pass']
#         email = request_data['email']
#         is_login = request_data['islogin']
#         # đăng nhập
#         if is_login:
#             # kiểm tra tài khoản tồn tại chưa . None nếu chưa tồn tại
#             data1 = query_database_for_login_register_by_name(name=name)
#             if data1 :
#                 id1 ,username1 ,  email1,password1,createdtime1 = data1
#                 print(f"user = {username1}, id = {id1} ,email = {email1}, password = {password1} , createdtime = {createdtime1}")
#                 if password == password1:
                    
#                     return {"response":{
#                         "message":"đăng nhập thành công",
#                         "status":True,
#                         "username":username1

#                     }}
#                 else:
#                     return {"response":{
#                         "message":"sai mật khẩu",
#                         "status":False
#                     }}
#             else:
#                 return {"response":{
#                     "message":"chưa có tài khoản",
#                         "status":False
                    
#                 }}
#         # đăng ký
#         else:
#             data1 = query_database_for_login_register_by_name(name=name)
#             if data1 :
#                 return {"response":{
#                     "message":"user đã tồn tại",
#                     "status":False
#                 }}
#             else:
#                 send_email_confirm_registration(code=generate_random_6_digit_number(),password=passwords["outlook"],to_email=email)
#                 # save_data_for_login_register_in_table(username=name,email=email,password=password,createdTime=gettime2())
#                 # return {"response":{
#                 #     "message":"tạo thành công",
#                 #     "status":True
#                 # }}
                

#         return {"response": "OK"}
#     else:
#         return {"response": "Lỗi"}
    
# forgot password
@app.post("/api/forgot_password")
async def login_register(request_data: dict):
    if request_data:
        pass

# async def delete_confirm_code_by_email_after_(email,minute):
#     await delayed_delete_confirm_code_by_email(email=email,delay_minutes=minute)

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
        name = request_data['name']
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
                    save_data_for_login_register_in_table(createdTime=time_now,email=email,password=password,username=name)
                    return {"response":{
                        "message":responses["dang_ky_thanh_cong"],
                        "status":True
                    }}
                else:
                    return {"response":{
                        "message":responses["dang_ky_that_bai"],
                        "status":False
                    }}
            else:
                return {"response":{
                        "message":responses["code_bi_qua_thoi_gian"],
                        "status":False
                    }}


        

        

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app1:app", port=8080, workers=5, reload=True)