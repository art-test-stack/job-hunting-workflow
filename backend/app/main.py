from fastapi import FastAPI, Security
from fastapi.middleware.cors import CORSMiddleware
from app.api.router import router
from app.core.database import create_db_and_tables
from fastapi.requests import Request
from app.core.database import Session
from app.orm.log import Log
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title="Job-Tracker Backend API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    # allow_origins=["http://localhost:3000", "http://localhost:3000/*"],  # in prod, restrict to frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# @app.middleware("http")
# async def log_requests(request: Request, call_next):
#     response = await call_next(request)
#     db = Session(bind=create_db_and_tables())
#     log_entry = Log(
#         method=request.method,
#         url=str(request.url),
#         status_code=response.status_code,
#         timestamp=datetime.now()
#     )
#     db.add(log_entry)
#     db.commit()
#     db.close()
#     return response

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the API"}
