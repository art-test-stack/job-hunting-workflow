from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.auth import verify_token, get_user_info
from app.core.database import get_session
from app.services.user import get_user_by_id, create_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/profile")
async def get_profile(user=Depends(verify_token)):
    print("user", user)
    return {"user_id": user["sub"], "email": user.get("email")}

@router.get("/user-details")
async def user_details(user=Depends(verify_token)):
    user_info = await get_user_info(user["sub"])
    return user_info