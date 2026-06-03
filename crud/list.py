from sqlmodel import Session, select
from schemas import ListView
from database import engine
from models import List


def get_lists_based_on_user_id(user_id:int):
    with Session(engine) as session:
        statement = select(List).where(List.owner_id == user_id)
        return session.exec(statement).all()


def create_new_list(user_id:int, listdata: ListView):
    with Session(engine) as session:
        new_list = List(owner_id=user_id, **listdata.model_dump(exclude={'id'}))
        session.add(new_list)
        session.commit()
        session.refresh(new_list)
        return new_list


def update_list(list_id: int, user_id: int, listdata: ListView) -> List | None:
    with Session(engine) as session:
        lst = session.exec(
            select(List).where(List.id == list_id, List.owner_id == user_id)
        ).first()
        if not lst:
            return None
        for key, value in listdata.model_dump(exclude_unset=True).items():
            setattr(lst, key, value)
        session.add(lst)
        session.commit()
        session.refresh(lst)
        return lst


def delete_list(list_id: int, user_id: int) -> bool:
    with Session(engine) as session:
        lst = session.exec(
            select(List).where(List.id == list_id, List.owner_id == user_id)
        ).first()
        if not lst:
            return False
        session.delete(lst)
        session.commit()
        return True