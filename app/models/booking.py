from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.core.db import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    guest_name = Column(String, nullable=False)
    seating_id = Column(Integer, ForeignKey("seatings.id"))
    start_time = Column(DateTime, nullable=False)
    duration = Column(Integer, nullable=False)

    seating = relationship("Seating", backref="bookings")
