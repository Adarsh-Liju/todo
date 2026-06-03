from sqlmodel import SQLModel
from enum import Enum
from datetime import datetime


class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class ListView(SQLModel):
    title: str
    description: str | None = None
    color: str | None = None
    icon: str | None = None
    position: int = 0


class UserCreate(SQLModel):
    name: str
    email: str
    password: str


class UserRead(SQLModel):
    id: int
    name: str
    email: str
    is_active: bool
