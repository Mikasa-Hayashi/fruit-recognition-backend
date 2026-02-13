from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional


class FruitBase(SQLModel):
    slug: str = Field(index=True, unique=True)
    scientific_name: str    
    image_url: str = Field(
        default='assets/default_fruit_image.png'
    )


class FruitCreate(FruitBase):
    pass


class FruitUpdate(SQLModel):
    slug: Optional[str] = None
    scientific_name: Optional[str] = None
    image_url: Optional[str] = None


class FruitRead(FruitBase):
    id: int
    created_at: datetime
    updated_at: datetime