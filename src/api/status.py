from fastapi import APIRouter

router = APIRouter(prefix='/status')

@router.get('/')
async def get_status():
    return {'status': 'ok'}

@router.get('/health')
async def get_health():
    return {'health': 'healthy'}