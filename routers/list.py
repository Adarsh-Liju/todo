from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session

from crud.list import get_lists_based_on_user_id, create_new_list, update_list, delete_list
from crud.user import get_user_id_by_session
from database import get_session
from models import List
from schemas import ListView

router = APIRouter(prefix="/lists", tags=["lists"])
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)  # point to your login endpoint


@router.get("/", response_model=list[ListView])
async def get_lists(
    session: Session = Depends(get_session), token: str = Depends(oauth2_scheme)
):
    user_id = get_user_id_by_session(session, token)
    return get_lists_based_on_user_id(user_id)

@router.post("/", response_model=ListView, status_code=201)
async def create_list(formdata: ListView, session: Session = Depends(get_session), token: str = Depends(oauth2_scheme)):
    user_id = get_user_id_by_session(session, token)
    result = create_new_list(user_id, formdata)
    if not result:
        raise HTTPException(status_code=400, detail="Failed to create list")
    return result

@router.put("/{list_id}", response_model=ListView, status_code=200)
async def update_list_route(list_id: int, formdata: ListView, session: Session = Depends(get_session), token: str = Depends(oauth2_scheme)):
    user_id = get_user_id_by_session(session, token)
    result = update_list(list_id, user_id, formdata)
    if not result:
        raise HTTPException(status_code=404, detail="List not found")
    return result


@router.delete("/{list_id}", status_code=204)
async def delete_list_route(list_id: int, session: Session = Depends(get_session), token: str = Depends(oauth2_scheme)):
    user_id = get_user_id_by_session(session, token)
    if not delete_list(list_id, user_id):
        raise HTTPException(status_code=404, detail="List not found")


