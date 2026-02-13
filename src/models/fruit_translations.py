from typing import Optional
from sqlmodel import Field, Relationship, UniqueConstraint
from datetime import datetime, timezone

from schemas.fruit_translations import FruitTranslationBase

class FruitTranslation(FruitTranslationBase, table=True):
    __tablename__ = 'fruit_translations'

    __table_args__ = (
        UniqueConstraint('fruit_id', 'language', name='uq_fruit_language'),
    )

    id: Optional[int] = Field(default=None, primary_key=True)

    fruit_id: int = Field(foreign_key='fruits.id')

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    fruit: Optional['Fruit'] = Relationship(back_populates='translations')
