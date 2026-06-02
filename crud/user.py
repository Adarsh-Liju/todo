from sqlmodel import Session, select
from models.user import User
from schemas.user import UserCreate
from passlib.hash import pbkdf2_sha256

def create_user(session: Session, user_in: UserCreate) -> User:
    hashed = pbkdf2_sha256.hash(user_in.password)  # use passlib in real code
    user = User(name=user_in.name, email=user_in.email, hashed_password=hashed)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_user_by_email(session: Session, email: str) -> User | None:
    return session.exec(select(User).where(User.email == email)).first()

def get_users(session: Session, offset: int = 0, limit: int = 100) -> list[User]:
    return list(session.exec(select(User).offset(offset).limit(limit)).all())