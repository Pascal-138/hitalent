from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.booking_schema import BookingCreate, BookingResponse
from app.services.booking_logic import create_booking, delete_booking
from app.models.booking import Booking
from app.core.db import get_db

router = APIRouter()


@router.post("/", response_model=BookingResponse, status_code=201)
def create_reservation(data: BookingCreate, db: Session = Depends(get_db)):
    """
    Создание новой брони
    """
    try:
        return create_booking(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[BookingResponse])
def list_reservations(db: Session = Depends(get_db)):
    """
    Получение списка всех броней
    """
    return db.query(Booking).all()


@router.delete("/{booking_id}", status_code=204)
def delete_reservation(booking_id: int, db: Session = Depends(get_db)):
    """
    Удаление брони по ID
    """
    booking = db.query(Booking).get(booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Бронь не найдена")
    delete_booking(db, booking_id)
    return
