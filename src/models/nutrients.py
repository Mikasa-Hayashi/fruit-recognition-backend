from typing import Optional, List
from datetime import datetime, timezone
from sqlmodel import Field, Relationship

from schemas.nutrients import NutrientBase
from models.fruit_nutrient_link import FruitNutrientLink


class Nutrient(NutrientBase, table=True):
    __tablename__ = 'nutrients'

    id: Optional[int] = Field(default=None, primary_key=True)
    unit_id: int = Field(foreign_key='units.id')

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    translations: List['NutrientTranslation'] = Relationship(back_populates='nutrient')
    fruits: List['Fruit'] = Relationship(
        back_populates='nutrients',
        link_model=FruitNutrientLink
    )
    unit: Optional['Unit'] = Relationship(back_populates='nutrients')
