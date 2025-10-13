from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.orm.company import Company
from app.orm.role import Role
from app.orm.location import Location
from app.orm.user import User
from app.orm.job import Job

from app.schemas.job import JobInput, JobOutput, UpdateJobDescription, UpdateUserJob

from app.services.industry import _add_job_industry, _get_job_industries

import uuid
from typing import List, Union

def _get_job_by_user_and_id(
        db: Session, 
        job_id: uuid.UUID | None,
        user_id: str | None
    ) -> Union[JobOutput, List[JobOutput], HTTPException]:

    if isinstance(job_id, str):
        job_id = uuid.UUID(job_id)

    db_query = db.query(
            Job.id,
            Role.title,
            Company.name,
            Location.name,
            Job.contract,
            Job.place,
            Job.url,
            Job.status,
            Job.applied_at,
            Job.description
        )
    if not job_id:
        db_query = db_query.filter(Job.user_id == user_id)
    else:
        db_query = db_query.filter(Job.id == job_id, Job.user_id == user_id)
    db_job = (
        db_query
        .join(Company, Company.id == Job.company_id)
        .join(Location, Location.id == Job.location_id, isouter=True)
        .join(Role, Role.id == Job.role_id)
        .all()
    )
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    out_jobs = [
        {
            "id": job[0],
            "title": job[1],
            "company": job[2],
            "location": job[3],
            "contract": job[4],
            "place": job[5],
            "business": ", ".join(_get_job_industries(db, job[0])),
            "url": job[6],
            "status": job[7],
            "applied_at": job[8],
            "description": job[9]
        }
        for job in db_job
        ] 
    return out_jobs[0] if job_id else out_jobs

def _get_jobs_by_user_id(
        db: Session, 
        user_id: uuid.UUID | None
    ) -> list[JobOutput]:
    return _get_job_by_user_and_id(db=db, job_id=None, user_id=user_id)

def _add_job_for_user(db: Session, user_id: str, data: JobInput):
    user = db.query(User).filter(User.id == user_id).first()
    data.user_id = user.id

    role = db.query(Role).filter(Role.title == data.title).first()
    if not role:
        role = Role(**data.dict())
        db.add(role)
        db.commit()
        db.refresh(role)

    company = db.query(Company).filter(
        Company.name == data.company
    ).first()
    if not company:
        company = Company(name=data.company)
        db.add(company)
        db.commit()
        db.refresh(company)

    location = db.query(Location).filter(Location.name == data.location).first()
    if not location:
        location = Location(name=data.location)
        db.add(location)
        db.commit()
        db.refresh(location)
    
    user_job = Job(
        role_id=role.id, 
        company_id=company.id, 
        location_id=location.id,
        **data.dict()
    )
    db.add(user_job)
    db.commit()

    for business in data.business.split(",") if data.business else []:
        _add_job_industry(db, user_job.id, company.id, business)

    db.refresh(user_job)
    return user_job

def _update_job_description(
        db: Session, 
        data: UpdateJobDescription
    ):
    job = db.query(Job).filter(Job.id == data.job_id, Job.user_id == data.user_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    job.description = data.description
    db.commit()
    db.refresh(job)
    return job

def _update_user_job(
        db: Session, 
        data: UpdateUserJob
    ):
    job = db.query(Job).filter(Job.id == data.job_id, Job.user_id == data.user_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    if data.location is not None:
        location = db.query(Location).filter(Location.name == data.location).first()
        if not location:
            location = Location(name=data.location)
            db.add(location)
            db.commit()
            db.refresh(location)
        job.location_id = location.id
    if data.place is not None:
        job.place = data.place
    if data.status is not None:
        job.status = data.status
    if data.applied_at is not None:
        job.applied_at = data.applied_at
    db.commit()
    db.refresh(job)
    return job

def _get_all_jobs(db: Session, limit: int = 100):
    return db.query(Job).limit(limit).all()
