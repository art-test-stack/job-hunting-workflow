from sqlmodel import Field, SQLModel, Column, DateTime
from sqlalchemy.sql import func
from datetime import datetime
import uuid

class Profile(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), default=func.now(), nullable=False)
    )
    modified_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), default=func.now(), onupdate=func.now(), nullable=False)
    )
    user_id: str | None = Field(default=None, foreign_key='user.id')
    email: str = Field(unique=True, index=True, nullable=False)
    phone: str = Field(default=None)
    name: str | None = Field(default=None)
    github: str | None = Field(default=None)
    linkedin: str | None = Field(default=None)
    portfolio: str | None = Field(default=None)
    roles: str | None = Field(nullable=True)
    nationalities: str | None = Field(nullable=True)
    specializations: str | None = Field(nullable=True)
    education_sentence: str | None = Field(nullable=True)
    languages: str | None = Field(nullable=True)