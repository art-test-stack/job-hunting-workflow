from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.auth import verify_token, get_user_info
from app.core.database import SessionDep
from app.services.user import _get_user_by_id, _create_user, _user_in_db

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/profile")
async def get_profile(db: SessionDep, user: str =Depends(verify_token)):
    print("user", user)
    return {"user_id": user["sub"], "email": user.get("email")}

@router.get("/user-details")
async def user_details(db: SessionDep, user: str =Depends(verify_token)):
    user_info = await get_user_info(user["sub"])
    return user_info

@router.get("/auth")
async def post_user(db: SessionDep, user: str =Depends(verify_token)):
    user = await get_user_info(user["sub"])
    if _user_in_db(db=db, user_id=user["user_id"]):
        user_db = _get_user_by_id(db=db, user_id=user["user_id"])
        return user_db
    if "created_at" in user:
        del user["created_at"]
    if "updated_at" in user:
        del user["updated_at"]
    user_db = _create_user(db=db, user_data=user)
    return user_db 

@router.get("/user_in_db")
async def get_user(db: SessionDep, user: str =Depends(verify_token)):
    user_exists = _user_in_db(db=db, user_id=user["sub"])
    return {"user_in_db": user_exists}