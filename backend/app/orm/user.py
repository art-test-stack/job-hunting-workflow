from sqlmodel import Field, SQLModel, Column, DateTime
from sqlalchemy.sql import func
from datetime import datetime
from typing import Optional
import uuid

class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    created_at: datetime = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    user_id: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True, nullable=False)
    name: str | None = Field(default=None)
    nickname: str | None = Field(nullable=True)
    family_name: str | None = Field(nullable=True)
    given_name: str | None = Field(nullable=True)
    last_ip: str = Field(nullable=True)
    last_login: str = Field(nullable=True)
    

    # id: int = Field(primary_key=True, index=True)
    # created_at: datetime = Field(
    #     sa_column=Column(DateTime(timezone=True), default=func.now(), nullable=False)
    # )
    # modified_at: datetime = Field(
    #     sa_column=Column(DateTime(timezone=True), default=func.now(), onupdate=func.now(), nullable=False)
    # )