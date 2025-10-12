from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Column, DateTime
from sqlalchemy.sql import func
import uuid

class Location(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    created_at: datetime = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )
    name: str = Field(unique=True, index=True)
    country: str | None = Field(default=None)
    city: str | None = Field(default=None)
    