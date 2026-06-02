from sqlmodel import create_engine, SQLModel, Session, select
from models.todo import List, Todo

DATABASE_URL = "sqlite:///./app.db"


engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

def get_lists_based_on_user_id(user_id):
    with Session(engine) as session:
        statement = select(List).where(List.owner_id==user_id)
        results = session.exec(statement)
        return results