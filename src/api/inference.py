from fastapi import APIRouter

router = APIRouter()

@router.post('/predictions')
async def create_predictions(image: bytes):
    """
    Run YOLO inference on the provided image and return recognized fruit
    """

    return {
        'fruit': 'orange',
        'confidence': 0.95,
    }