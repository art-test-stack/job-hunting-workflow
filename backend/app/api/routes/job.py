from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.auth import verify_token
from app.core.database import SessionDep
from app.services.user import _get_internal_user_id
from app.services.job import (
    _add_job_for_user, 
    _get_job_by_user_and_id,
    _get_jobs_by_user_id, 
    _update_job_description,
    _update_user_job,
)
from app.schemas.job import (
    JobInput, 
    JobOutput, 
    JobOutputDetails, 
    UpdateJobDescription, 
    UpdateUserJob
)
from fastapi import HTTPException
from typing import List, Union

import uuid
router = APIRouter(prefix="/job", tags=["Job"])

@router.get("/user", response_model=List[JobOutput])
async def get_user_job(
        db: SessionDep, 
        user=Depends(verify_token), 
        user_id: str | None = None,
    ) -> List[JobOutput]:
    if not user["sub"] == user_id:
        raise HTTPException(status_code=403, detail="Unauthorized")
    user_id = _get_internal_user_id(db, user_id)
    jobs = _get_jobs_by_user_id(db=db, user_id=user_id)
    return jobs

@router.get("/details", response_model=JobOutputDetails)
async def get_user_job_by_id(
        db: SessionDep, 
        user=Depends(verify_token), 
        user_id: str | None = None, 
        job_id: uuid.UUID | str | None = None
    ) -> JobOutputDetails:
    if not user["sub"] == user_id:
        raise HTTPException(status_code=403, detail="Unauthorized")
    print("job_id", job_id, "user_id", user_id)
    user_id = _get_internal_user_id(db, user_id)
    job = _get_job_by_user_and_id(db=db, job_id=job_id, user_id=user_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.post("/add", response_model=Union[JobOutput, List[JobOutput]])
async def add_job(
        db: SessionDep, 
        user: dict = Depends(verify_token), 
        data: JobInput = Depends()
    ) -> Union[JobOutput, List[JobOutput]]:
    if not user["sub"] == data.user_id:
        raise HTTPException(status_code=403, detail="Unauthorized")
    user_id = _get_internal_user_id(db, user["sub"])
    user_job_added = _add_job_for_user(db=db, user_id=user_id, data=data)
    return _get_job_by_user_and_id(db=db, job_id=user_job_added.id, user_id=user_id)

@router.put("/add-desc")
async def update_job_description(
        db: SessionDep, 
        user: dict = Depends(verify_token), 
        data: UpdateJobDescription = Depends(),
    ):
    if not user["sub"] == data.user_id:
        raise HTTPException(status_code=403, detail="Unauthorized")
    job = _update_job_description(db=db, data=data)
    job.user_id = user["sub"]
    return job

@router.put("/update")
async def update_job(
        db: SessionDep, 
        user: dict = Depends(verify_token), 
        data: UpdateUserJob = Depends(),
    ):
    if not user["sub"] == data.user_id:
        raise HTTPException(status_code=403, detail="Unauthorized")
    data.user_id = _get_internal_user_id(db, data.user_id)
    job = _update_user_job(db=db, data=data)
    job.user_id = user["sub"]
    return job