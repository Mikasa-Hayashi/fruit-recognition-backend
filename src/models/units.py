from typing import Optional, List
from datetime import datetime, timezone
from sqlmodel import Field, Relationship

from schemas.units import UnitBase

class Unit(UnitBase, table=True):
    __tablename__ = 'units'

    id: Optional[int] = Field(default=None, primary_key=True)

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None))

    translations: List['UnitTranslation'] = Relationship(back_populates='unit')
    nutrients: List['Nutrient'] = Relationship(back_populates='unit')
