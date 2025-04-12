from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.reservation import ReservationCreate, Reservation as ReservationSchema
from app.services.reservations import get_reservations, create_reservation, delete_reservation
from app.database import SessionLocal


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/reservations/", response_model=list[ReservationSchema])
def read_reservations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Получаем список всех бронирований
    reservations = get_reservations(db, skip=skip, limit=limit)
    return reservations


@router.post("/reservations/", response_model=ReservationSchema)
def add_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    # Создаем новое бронирование
    db_reservation = create_reservation(db, reservation)
    if db_reservation is None:
        raise HTTPException(
            status_code=400, detail="Временной слот этого столика уже занят")
    return db_reservation


@router.delete("/reservations/{reservation_id}", response_model=ReservationSchema)
def remove_reservation(reservation_id: int, db: Session = Depends(get_db)):
    # Удаляем бронирование по ID
    db_reservation = delete_reservation(db, reservation_id)
    if db_reservation is None:
        raise HTTPException(status_code=404, detail="Бронирование не найдено")
    return db_reservation
