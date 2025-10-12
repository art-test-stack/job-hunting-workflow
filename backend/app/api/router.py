from fastapi import APIRouter
import os
from app.api.routes import user, job, test

from dotenv import load_dotenv
load_dotenv()

router = APIRouter()
router.include_router(user.router)
router.include_router(job.router)
if os.getenv("ENVIRONMENT") == "dev":
    router.include_router(test.router)

