# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# # CORS setup
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000", "http://localhost:3000/*"],  # in prod, restrict to frontend URL
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/")
# def root():
#     return {"status": "Backend is running 🚀"}

from fastapi import FastAPI, Security
from fastapi.middleware.cors import CORSMiddleware
from app.api.router import router
from app.core.database import create_db_and_tables

app = FastAPI(
    title="Job-Tracker Backend API",
    # dependencies=[Security(verify)]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables on startup
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the API"}
