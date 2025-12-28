from fastapi import APIRouter

router = APIRouter()

@router.get('/fruits')
async def get_fruits():
    return {'fruits': ['apple', 'banana', 'cherry']}