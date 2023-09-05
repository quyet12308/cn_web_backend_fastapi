from fastapi import FastAPI
import uvicorn
import sqlite3
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Sửa đổi danh sách này để chỉ định các nguồn mà bạn muốn chấp nhận yêu cầu từ
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/test")
def test_endpoint():
    return {"message": "Hello from FastAPI!"}

if __name__ == "__main__":
    
    uvicorn.run("app1:app",port=8080,workers=5,reload=True)