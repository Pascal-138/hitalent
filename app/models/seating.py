from sqlalchemy import Column, Integer, String
from app.core.db import Base


class Seating(Base):
    __tablename__ = "seatings"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, unique=True, index=True)
    capacity = Column(Integer, nullable=False)
    area = Column(String, nullable=True)
