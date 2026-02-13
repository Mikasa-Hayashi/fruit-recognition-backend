from sqlmodel import Field, SQLModel
from typing import Optional

class UnitTranslationBase(SQLModel):
    language: str = Field(index=True)
    short_form: str
    full_form: str


class UnitTranslationCreate(UnitTranslationBase):
    pass


class UnitTranslationUpdate(SQLModel):
    language: Optional[str] = None
    short_form: Optional[str] = None
    full_form: Optional[str] = None
    

class UnitTranslationRead(UnitTranslationBase):
    id: int
    unit_id: int
