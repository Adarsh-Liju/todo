from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime
from enum import Enum

class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(unique=True, index=True)
    hashed_password: str
    is_active: bool = Field(default=True)


class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str | None = None
    is_completed: bool = Field(default=False)
    priority: Priority = Field(default=Priority.medium)
    due_date: datetime | None = None
    completed_at: datetime | None = None
    position: int = Field(default=0)
    owner_id: int = Field(foreign_key="user.id")
    list_id: int | None = Field(default=None, foreign_key="list.id")


class List(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str | None = None
    color: str | None = None
    icon: str | None = None
    position: int = Field(default=0)
    owner_id: int = Field(foreign_key="user.id")
