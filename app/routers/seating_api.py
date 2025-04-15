from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.seating_schema import SeatingCreate, SeatingResponse
from app.models.seating import Seating
from app.core.db import get_db

router = APIRouter()


@router.post("/", response_model=SeatingResponse, status_code=201)
def create_table(seating: SeatingCreate, db: Session = Depends(get_db)):
    """
    Добавление нового столика
    """
    new_seating = Seating(**seating.dict())
    db.add(new_seating)
    db.commit()
    db.refresh(new_seating)
    return new_seating


@router.get("/", response_model=list[SeatingResponse])
def list_tables(db: Session = Depends(get_db)):
    """
    Получение списка всех столиков
    """
    return db.query(Seating).all()


@router.delete("/{seating_id}", status_code=204)
def delete_table(seating_id: int, db: Session = Depends(get_db)):
    """
    Удаление столика по ID
    """
    seating = db.query(Seating).get(seating_id)
    if not seating:
        raise HTTPException(status_code=404, detail="Столик не найден")
    db.delete(seating)
    db.commit()
    return
