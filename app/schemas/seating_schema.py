from pydantic import BaseModel, Field
from typing import Optional


class SeatingBase(BaseModel):
    label: str = Field(..., example="Table 1")
    capacity: int = Field(..., example=4)
    area: Optional[str] = Field(None, example="терраса")


class SeatingCreate(SeatingBase):
    pass


class SeatingResponse(SeatingBase):
    id: int

    class Config:
        orm_mode = True
