from sqlmodel import Field, SQLModel
from typing import Optional

class NutrientTranslationBase(SQLModel):
    language: str = Field(index=True)
    name: str
    description: str


class NutrientTranslationCreate(NutrientTranslationBase):
    pass


class NutrientTranslationUpdate(SQLModel):
    language: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    

class NutrientTranslationRead(NutrientTranslationBase):
    id: int
    nutrient_id: int
