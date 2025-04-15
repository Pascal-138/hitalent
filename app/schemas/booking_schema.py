from pydantic import BaseModel, Field
from datetime import datetime


class BookingBase(BaseModel):
    guest_name: str = Field(..., example="Иван Иванов")
    seating_id: int = Field(..., example=1)
    start_time: datetime = Field(..., example="2025-04-12T19:00:00")
    duration: int = Field(..., example=60)  # в минутах


class BookingCreate(BookingBase):
    pass


class BookingResponse(BookingBase):
    id: int

    class Config:
        orm_mode = True
