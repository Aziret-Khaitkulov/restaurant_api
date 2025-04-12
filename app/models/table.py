from sqlalchemy import Column, Integer, String
from app.database import Base


class Table(Base):
    __tablename__ = "tables"  # Имя таблицы в базе данных

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    seats = Column(Integer)
    location = Column(String)
