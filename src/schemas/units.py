from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional


class UnitBase(SQLModel):
    slug: str = Field(index=True, unique=True)


class UnitCreate(UnitBase):
    pass


class UnitUpdate(SQLModel):
    slug: Optional[str] = None


class UnitRead(UnitBase):
    id: int
    created_at: datetime
    updated_at: datetime