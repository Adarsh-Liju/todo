from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from crud.user import create_user, get_users, get_user_by_email
from schemas.user import UserCreate, UserRead

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead)
async def register(user_in: UserCreate, session: Session = Depends(get_session)):
    existing = get_user_by_email(session, user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(session, user_in)

@router.get("/", response_model=list[UserRead])
async def list_users(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    return get_users(session, offset=offset, limit=limit)