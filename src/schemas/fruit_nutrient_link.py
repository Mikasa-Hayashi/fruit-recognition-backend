from sqlmodel import SQLModel
from typing import Optional

class FruitNutrientLinkBase(SQLModel):
    value: float


class FruitNutrientLinkCreate(FruitNutrientLinkBase):
    pass


class FruitNutrientLinkUpdate(SQLModel):
    value: Optional[float] = None
    

class FruitNutrientLinkRead(FruitNutrientLinkBase):
    fruit_id: int
    nutrient_id: int
    value: float
