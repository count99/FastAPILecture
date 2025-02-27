from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()
# 添加 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许的源，根据您的前端URL调整
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有头
)
app.add_middleware(GZipMiddleware, minimum_size=1000)
# 托管静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")

class MessageRequest(BaseModel):
    message: str
# 添加 API 路由（可选）
@app.post("/api/data")
async def process_message(request: MessageRequest):
    # 修正返回值格式问题
    return {"message": f"Hello {request.message} from FastAPI!"}  # 注意使用 request.message

# 处理前端路由回退（关键！）
@app.get("/{full_path:path}")
async def catch_all(full_path: str):
    return FileResponse("static/index.html")
