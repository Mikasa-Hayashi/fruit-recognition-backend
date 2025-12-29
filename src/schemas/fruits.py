from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional


class FruitBase(SQLModel):
    name: str = Field(index=True, unique=True)
    display_name: str
    description: str
    calories: int
    sugar_content: float
    image_url: str = Field(
        default='assets/default_fruit_image.png'
    )


class FruitCreate(FruitBase):
    pass


class FruitUpdate(SQLModel):
    name: Optional[str] = None
    display_name: Optional[str] = None
    description: Optional[str] = None
    calories: Optional[int] = None
    sugar_content: Optional[float] = None
    image_url: Optional[str] = None


class FruitRead(FruitBase):
    id: int
    created_at: datetime
    updated_at: datetime