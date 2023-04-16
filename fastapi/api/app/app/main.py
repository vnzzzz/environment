# fastapiのインポート
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# モジュールのインポート
from .routers import users
from .routers import items
from .routers import files

# fastapiインスタンスを生成
app = FastAPI(title="Env fastapi", root_path="/env-fastapi")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(items.router)
app.include_router(files.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
