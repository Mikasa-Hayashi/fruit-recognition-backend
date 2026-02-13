from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional


class NutrientBase(SQLModel):
    slug: str = Field(index=True, unique=True)
    category: str


class NutrientCreate(NutrientBase):
    pass


class NutrientUpdate(SQLModel):
    slug: Optional[str] = None
    category: Optional[str] = None


class NutrientRead(NutrientBase):
    id: int
    unit_id: int
    created_at: datetime
    updated_at: datetime