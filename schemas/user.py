from sqlmodel import SQLModel

class UserCreate(SQLModel):
    name: str
    email: str
    password: str

class UserRead(SQLModel):
    id: int
    name: str
    email: str
    is_active: bool