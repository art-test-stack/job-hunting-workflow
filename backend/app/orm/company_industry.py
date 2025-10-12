from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Column, DateTime
from sqlalchemy.sql import func
import uuid

class CompanyIndustry(SQLModel, table=True):
    __tablename__ = "company_industry"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )
    company_id: uuid.UUID | None = Field(default=None, foreign_key="company.id")
    industry_id: uuid.UUID | None = Field(default=None, foreign_key="industry.id")
