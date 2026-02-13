from typing import Optional, List
from datetime import datetime, timezone
from sqlmodel import Field, Relationship

# from models.nutrients import Nutrient
# from models.unit_translations import UnitTranslation
from ..schemas.units import UnitBase

class Unit(UnitBase, table=True):
    __tablename__ = 'units'

    id: Optional[int] = Field(default=None, primary_key=True)

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    translations: List['UnitTranslation'] = Relationship(back_populates='unit')
    nutrients: List['Nutrient'] = Relationship(back_populates='unit')
