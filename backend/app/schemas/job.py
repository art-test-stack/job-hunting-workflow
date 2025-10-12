from sqlmodel import SQLModel, Field
from sqlalchemy.sql import func
import uuid


class JobInput(SQLModel):
    user_id: str
    title: str
    company: str
    location: str
    contract: str | None = Field(default=None)
    place: str | None = Field(default=None)
    business: str | None = Field(default=None)
    url: str | None = Field(default=None)

class CreateJob(SQLModel):
    title: str

class CreateUserJob(SQLModel):
    user_id: str
    job_id: str
    company_id: str
    location: str
    type: str | None = Field(default=None)
    status: str | None = Field(default=None)
    applied_at: str | None = Field(default=None)

class CreateCompany(SQLModel):
    name: str
    industry: str | None = Field(default=None)
    website: str | None = Field(default=None)

class UpdateUserJob(SQLModel):
    job_id: str
    user_id: str
    location: str | None = Field(default=None)
    place: str | None = Field(default=None)
    status: str | None = Field(default=None)
    applied_at: str | None = Field(default=None)

class UpdateJobDescription(SQLModel):
    job_id: str
    user_id: str
    description: str | None = Field(default=None)

class JobOutput(SQLModel):
    id: uuid.UUID
    title: str | None = Field(default=None)
    company: str | None = Field(default=None)
    location: str | None = Field(default=None)
    contract: str | None = Field(default=None)
    place: str | None = Field(default=None)
    business: str | None = Field(default=None)
    url: str | None = Field(default=None)
    status: str | None = Field(default=None)
    applied_at: str | None = Field(default=None)

class JobOutputDetails(JobOutput):
    description: str | None = Field(default=None)