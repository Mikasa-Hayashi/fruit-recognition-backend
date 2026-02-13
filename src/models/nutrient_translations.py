from typing import Optional
from sqlmodel import Field, Relationship, UniqueConstraint
from datetime import datetime, timezone

from schemas.nutrient_translations import NutrientTranslationBase

class NutrientTranslation(NutrientTranslationBase, table=True):
    __tablename__ = 'nutrient_translations'

    __table_args__ = (
        UniqueConstraint('nutrient_id', 'language', name='uq_nutrient_language'),
    )

    id: Optional[int] = Field(default=None, primary_key=True)

    nutrient_id: int = Field(foreign_key='nutrients.id')

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    nutrient: Optional['Nutrient'] = Relationship(back_populates='translations')
