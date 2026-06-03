from sqlmodel import SQLModel
from datetime import datetime
from models import Priority


class ListView(SQLModel):
    id: int
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
