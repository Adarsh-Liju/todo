from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session
from database import get_session
from crud.user import get_user_id_by_session
from models import List
from database import get_lists_based_on_user_id

router = APIRouter(prefix="/lists", tags=["lists"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")  # point to your login endpoint

@router.get("/")
async def lists_view(
    session: Session = Depends(get_session),
    token: str = Depends(oauth2_scheme)
):
    user_id = get_user_id_by_session(session, token)
    lists = get_lists_based_on_user_id(user_id)
    return lists
