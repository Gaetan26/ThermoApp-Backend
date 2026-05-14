
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import cycle
from routes import coolprop

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from core import handlers, middlewares

app.include_router(cycle.router)
app.include_router(coolprop.router)

@app.get('/')
async def hello_world():
    return {
        "message": "hello world from FastAPI!"
    }
