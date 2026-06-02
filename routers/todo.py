from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from crud.user import create_user, get_users, get_user_by_email

router = APIRouter(prefix="/lists", tags=["lists"])

@router.get("/")
async def lists_view():
    