from sqlmodel import SQLModel
from enum import Enum
from datetime import datetime


class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class ListView(SQLModel):
    title: str
    description: str
    is_completed: bool
    priority: Priority
    due_date: datetime
    completed_at: datetime
    position: int


class UserCreate(SQLModel):
    name: str
    email: str
    password: str


class UserRead(SQLModel):
    id: int
    name: str
    email: str
    is_active: bool