from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Column, DateTime
from sqlalchemy.sql import func
import uuid

class JobCi(SQLModel, table=True):
    __tablename__ = "job_ci"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )
    job_id: uuid.UUID | None = Field(default=None, foreign_key="job.id")
    company_industry_id: uuid.UUID | None = Field(default=None, foreign_key="company_industry.id")
    company_id: uuid.UUID | None = Field(default=None, foreign_key="company.id")
