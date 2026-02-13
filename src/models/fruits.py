from typing import List
from sqlmodel import Field, Relationship
from datetime import datetime, timezone
from typing import Optional
from .fruit_nutrient_link import FruitNutrientLink
from ..schemas.fruits import FruitBase

class Fruit(FruitBase, table=True):
    __tablename__ = 'fruits'

    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None))

    translations: List['FruitTranslation'] = Relationship(back_populates='fruit')
    nutrients: List['Nutrient'] = Relationship(
        back_populates='fruits',
        link_model=FruitNutrientLink
    )
