
from fastapi import APIRouter, Depends

from core.security import verify_token
from core.seeder import seed_database
from database import SessionDep


router = APIRouter(prefix='/seed')

@router.post('/')
async def run_seed(
    session: SessionDep, 
    token_verified: str = Depends(verify_token)
):
    return await seed_database(session)
