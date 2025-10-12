from sqlmodel import SQLModel, Field
from sqlalchemy.sql import func
from sqlmodel import Column, DateTime
from datetime import datetime
from typing import Optional
import uuid

class Log(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    created_at: datetime = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )
    user_id: uuid.UUID | None = Field(default=None, foreign_key="user.id")
    action: str | None = Field(default=None)
    details: str | None = Field(default=None)