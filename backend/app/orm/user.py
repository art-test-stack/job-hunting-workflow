from sqlmodel import Field, SQLModel
from datetime import datetime

class User(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    user_id: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True, nullable=False)
    name: str | None = Field(default=None)
    nickname: str | None = Field(nullable=True)
    last_ip: str = Field(nullable=True)
    last_login: str = Field(nullable=True)
    # created_at: datetime = Field(default=)
