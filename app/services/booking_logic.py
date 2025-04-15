from sqlalchemy.orm import Session
from datetime import timedelta

from app.models.booking import Booking
from app.schemas.booking_schema import BookingCreate


def has_conflict(db, seating_id, start_time, duration):
    bookings = db.query(Booking).filter(Booking.seating_id == seating_id).all()

    requested_end = start_time + timedelta(minutes=duration)

    for booking in bookings:
        existing_start = booking.start_time
        existing_end = booking.start_time + timedelta(minutes=booking.duration)

        if start_time < existing_end and requested_end > existing_start:
            return True

    return False


def create_booking(db: Session, data: BookingCreate) -> Booking:
    if has_conflict(db, data.seating_id, data.start_time, data.duration):
        raise ValueError("Выбранный столик уже забронирован на это время.")

    new_booking = Booking(**data.dict())
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking


def delete_booking(db: Session, booking_id: int) -> None:
    booking = db.query(Booking).get(booking_id)
    if booking:
        db.delete(booking)
        db.commit()
