from sqlalchemy.orm import Session
from sqlalchemy.sql import func, and_
from datetime import timedelta

from app.models.reservation import Reservation
from app.schemas.reservation import ReservationCreate


def is_time_conflict(db: Session, table_id: int, new_start, new_duration: int):
    """
    Проверяет, занят ли столик в заданный временной интервал.
    new_start: время начала новой брони
    new_duration: длительность брони (в минутах)
    """
    new_end = new_start + timedelta(minutes=new_duration)

    # Проверяем пересечение временных интервалов
    conflict = (
        db.query(Reservation)
        .filter(
            Reservation.table_id == table_id,
            and_(
                Reservation.reservation_time < new_end,
                (Reservation.reservation_time + func.make_interval(0, 0,
                 0, 0, 0, 0, Reservation.duration_minutes)) > new_start
            )
        )
        .first()
    )
    return conflict is not None


def get_reservations(db: Session, skip: int = 0, limit: int = 100):
    # Получает список всех бронирований
    return db.query(Reservation).offset(skip).limit(limit).all()


def create_reservation(db: Session, reservation: ReservationCreate):
    # Проверяет, существует ли столик с таким id
    if is_time_conflict(db, reservation.table_id, reservation.reservation_time, reservation.duration_minutes):
        return None
    # Создает новое бронирование
    db_reservation = Reservation(**reservation.model_dump())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation


def delete_reservation(db: Session, reservation_id: int):
    # Удаляет бронирование по id
    db_reservation = db.query(Reservation).filter(
        Reservation.id == reservation_id).first()
    if not db_reservation:
        return None
    db.delete(db_reservation)
    db.commit()
    return db_reservation
