from sqlmodel import Session, select
from models.user import User
from schemas.user import UserCreate
from passlib.hash import pbkdf2_sha256
from auth import decode_token

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

def get_user_id_by_session(session: Session, token: str) -> int | None:
    payload = decode_token(token)
    if not payload:
        return None
    email = payload.get("sub")
    if not email:
        return None
    user = get_user_by_email(session, email)
    return user.id if user else None