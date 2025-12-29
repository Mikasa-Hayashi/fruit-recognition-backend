from fastapi import APIRouter

router = APIRouter(prefix='/fruits')

@router.get('/')
async def get_fruits():
    return {'fruits': ['apple', 'banana', 'cherry']}