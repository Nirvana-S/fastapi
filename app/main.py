from fastapi import FastAPI
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine, get_db
from .routers import post, user, auth, vote
from .config import settings

# uvicorn main:app --reload
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(vote.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hello World"}

