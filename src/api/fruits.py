from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from database import SessionDep
from schemas.fruits import FruitCreate, FruitRead, FruitUpdate
from sqlmodel import select
from models.fruits import Fruit
from core.security import verify_token

router = APIRouter(prefix='/fruits')

@router.get('/')
async def read_fruits(session: SessionDep):
    statement = select(Fruit)
    result = await session.execute(statement)
    fruits = result.scalars().all()
    return {'fruits': fruits}


@router.get('/{fruit_name}', response_model=FruitRead)
async def read_fruit(fruit_name: str, session: SessionDep):
    statement = select(Fruit).where(Fruit.name == fruit_name)
    result = await session.execute(statement)
    fruit = result.scalar_one_or_none()

    if not fruit:
        raise HTTPException(status_code=404, detail=f'Fruit "{fruit_name}" not found')

    return fruit


@router.post('/')
async def create_fruit(
    fruit: FruitCreate, 
    session: SessionDep,
    token_verified: str = Depends(verify_token)
):
    fruit_db = Fruit.model_validate(fruit)
    session.add(fruit_db)
    await session.commit()
    await session.refresh(fruit_db)
    return fruit_db


@router.patch('/{fruit_name}')
async def update_fruit(
    fruit_name: str, fruit: 
    FruitUpdate, 
    session: SessionDep,
    token_verified: str = Depends(verify_token)
):
    fruit_db = session.get(Fruit, fruit_name)

    if not fruit_db:
        raise HTTPException(status_code=404, detail=f'Fruit "{fruit_name}" not found')

    for key, value in fruit.model_dump(exclude_unset=True).items():
        setattr(fruit_db, key, value)

    fruit_db.updated_at = datetime.now(timezone.utc)

    session.add(fruit_db)
    await session.commit()
    await session.refresh(fruit_db)
    return fruit_db


@router.delete('/{fruit_name}')
async def delete_fruit(
    fruit_name: str,
    session: SessionDep, 
    token_verified: str = Depends(verify_token)
):
    fruit_db = session.get(Fruit, fruit_name)

    if not fruit_db:
        raise HTTPException(status_code=404, detail=f'Fruit "{fruit_name}" not found')

    await session.delete(fruit_db)
    await session.commit()
    return {'message': f'Fruit "{fruit_name}" deleted successfully'}