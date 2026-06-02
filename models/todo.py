from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime
from enum import Enum


class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Todo(SQLModel, table=True):
    title: str
    description: str | None = None
    is_completed: bool = Field(default=False)
    priority: Priority = Field(default=Priority.medium)
    due_date: datetime | None = None
    completed_at: datetime | None = None
    position: int = Field(default=0)
    owner_id: int = Field(foreign_key="users.id")
    list_id: int | None = Field(default=None, foreign_key="lists.id")

class List(SQLModel, table=True):
    title: str
    description: str | None = None
    color: str | None = None          # "#ff5733"
    icon: str | None = None           # "🛒" or "work"
    position: int = Field(default=0)
    owner_id: int = Field(foreign_key="users.id")