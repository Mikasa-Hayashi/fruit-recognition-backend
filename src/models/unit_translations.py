from typing import Optional
from sqlmodel import Field, Relationship, UniqueConstraint
from datetime import datetime, timezone

from schemas.unit_translations import UnitTranslationBase

class UnitTranslation(UnitTranslationBase, table=True):
    __tablename__ = 'unit_translations'

    __table_args__ = (
        UniqueConstraint('unit_id', 'language', name='uq_unit_language'),
    )

    id: Optional[int] = Field(default=None, primary_key=True)

    unit_id: int = Field(foreign_key='units.id')

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    unit: Optional['Unit'] = Relationship(back_populates='translations')
