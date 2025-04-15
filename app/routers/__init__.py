from fastapi import APIRouter

router = APIRouter()


# Импортируем локально, чтобы избежать циклических импортов
def include_routers():
    from app.routers import seating_api, booking_api

    router.include_router(seating_api.router,
                          prefix="/tables", tags=["Tables"])
    router.include_router(booking_api.router,
                          prefix="/reservations", tags=["Reservations"])


include_routers()
