from sqlmodel import Field , SQLModel, Column, DateTime
from sqlalchemy.sql import func
from datetime import datetime
from typing import Optional
import uuid

class CVGenerated(SQLModel, table=True):  
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), default=func.now(), nullable=False)
    )
    modified_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), default=func.now(), onupdate=func.now(), nullable=False)
    )
    user_id: uuid.UUID | None = Field(default=None, foreign_key="user.id")
    user_job_id: uuid.UUID | None = Field(default=None, foreign_key="user_job.id")
    location: str = Field(nullable=False)
    
