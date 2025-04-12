from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.database import Base


class Reservation(Base):
    __tablename__ = "reservations"  # Имя таблицы в базе данных

    id = Column(Integer, primary_key=True, index=True)     # Идентификатор бронирования
    customer_name = Column(String, nullable=False)         # Имя клиента 
    table_id = Column(Integer, ForeignKey("tables.id"))    # Внешний ключ на таблицу столов
    reservation_time = Column(DateTime, nullable=False)    # Время бронирования                                                         
    duration_minutes = Column(Integer, nullable=False)     # Продолжительность в минутах
