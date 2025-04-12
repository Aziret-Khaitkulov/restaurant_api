from datetime import datetime
from pydantic import BaseModel


class ReservationBase(BaseModel):
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int


# Схема для создания бронирования
class ReservationCreate(ReservationBase):
    pass


# Схема для обновления бронирования
class Reservation(ReservationBase):
    id: int

    class Config:
        from_attributes = True
