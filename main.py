from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_db_and_tables
from routers import user, auth, list


@asynccontextmanager
async def lifespan(_: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(list.router)