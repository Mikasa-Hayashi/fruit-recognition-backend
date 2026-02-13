from sqlmodel import Field
from schemas.fruit_nutrient_link import FruitNutrientLinkBase


class FruitNutrientLink(FruitNutrientLinkBase, table=True):
    __tablename__ = 'fruit_nutrient_link'

    fruit_id: int = Field(
        foreign_key='fruits.id',
        primary_key=True
    )

    nutrient_id: int = Field(
        foreign_key='nutrients.id',
        primary_key=True
    )

    value: float
