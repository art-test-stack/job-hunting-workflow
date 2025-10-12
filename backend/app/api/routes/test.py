from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.auth import verify_token, get_user_info
from app.core.database import SessionDep
from app.orm.company import Company
from app.orm.user import User
from app.orm.job import Job
from app.orm.role import Role

router = APIRouter(prefix="/test", tags=["Test"])


@router.get("/company")
async def get_companies(db: SessionDep):
    companies = db.query(Company).all()
    return companies

@router.get("/auth")
async def test_auth(db: SessionDep, user=Depends(verify_token)):
    return {"user_id": user["sub"], "email": user.get("email")}

@router.get("/user-in-db")
async def test_user_in_db(db: SessionDep):
    users = db.query(User).all()
    return users

@router.get("/jobs")
async def test_jobs(db: SessionDep):
    jobs = db.query(Job).all()
    return jobs

@router.get("/roles")
async def test_roles(db: SessionDep):
    roles = db.query(Role).all()
    return roles