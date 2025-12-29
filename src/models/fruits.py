from sqlmodel import Field
from datetime import datetime, timezone
from typing import Optional
from src.schemas.fruits import FruitBase

class Fruit(FruitBase, table=True):
    __tablename__ = 'fruits'

    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))