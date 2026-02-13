from sqlmodel import Field, SQLModel
from typing import Optional

class FruitTranslationBase(SQLModel):
    language: str = Field(index=True)
    name: str
    description: str


class FruitTranslationCreate(FruitTranslationBase):
    pass


class FruitTranslationUpdate(SQLModel):
    language: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    

class FruitTranslationRead(FruitTranslationBase):
    id: int
    fruit_id: int
