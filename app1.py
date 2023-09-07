from fastapi import FastAPI, HTTPException 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from login_register_database import query_database_for_login_register_by_name,save_data_for_login_register_in_table


from gettime import gettime2
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



@app.post("/api/test")
async def validate_request(request_data: dict):
    # Kiểm tra xem yêu cầu POST có dữ liệu không
    if request_data:
        # print(f"data = {request_data} type data = {type(request_data)}")
        # Truy cập các phần riêng lẻ bằng cách sử dụng khóa
        name = request_data['name']
        password = request_data['pass']
        email = request_data['email']
        is_login = request_data['islogin']
        # đăng nhập
        if is_login:
            # kiểm tra tài khoản tồn tại chưa . None nếu chưa tồn tại
            data1 = query_database_for_login_register_by_name(name=name)
            if data1 :
                id1 ,username1 ,  email1,password1,createdtime1 = data1
                print(f"user = {username1}, id = {id1} ,email = {email1}, password = {password1} , createdtime = {createdtime1}")
                if password == password1:
                    
                    return {"response":{
                        "message":"đăng nhập thành công",
                        "status":True,
                        "username":username1

                    }}
                else:
                    return {"response":{
                        "message":"sai mật khẩu",
                        "status":False
                    }}
            else:
                return {"response":{
                    "message":"chưa có tài khoản",
                        "status":False
                    
                }}
        # đăng ký
        else:
            data1 = query_database_for_login_register_by_name(name=name)
            if data1 :
                return {"response":{
                    "message":"user đã tồn tại",
                    "status":False
                }}
            else:
                save_data_for_login_register_in_table(username=name,email=email,password=password,createdTime=gettime2())
                return {"response":{
                    "message":"tạo thành công",
                    "status":True
                }}
                


        return {"response": "OK"}
    else:
        return {"response": "Lỗi"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app1:app", port=8080, workers=5, reload=True)