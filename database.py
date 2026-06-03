from sqlmodel import Session, SQLModel, create_engine, select

from models import List, Todo

DATABASE_URL = "mysql+pymysql://adarsh:ala@localhost/todo"


engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
