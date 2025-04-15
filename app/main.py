from fastapi import FastAPI
from app.routers import seating_api, booking_api

app = FastAPI(
    title="Restaurant Table Booking API",
    description="Сервис для бронирования столиков в ресторане",
    version="1.0.0",
)

app.include_router(seating_api.router, prefix="/seating", tags=["Seating"])
app.include_router(booking_api.router,
                   prefix="/reservations", tags=["Booking"])
