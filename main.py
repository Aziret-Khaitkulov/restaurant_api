from fastapi import FastAPI
from app.routers import tables, reservations
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Подключаем маршруты
app.include_router(tables.router)
app.include_router(reservations.router)
