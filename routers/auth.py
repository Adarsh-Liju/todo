from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from database import get_session
from crud.user import get_user_by_email
from auth import create_access_token
from passlib.hash import pbkdf2_sha256

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    user = get_user_by_email(session, form_data.username)
    if not user or not pbkdf2_sha256.verify(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(user.email)
    return {"access_token": token, "token_type": "bearer"}
