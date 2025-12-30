from fastapi import APIRouter, UploadFile, File, Depends

from inference.base import BaseDetector
from inference.loader import get_detector

router = APIRouter()

@router.post('/predictions')
async def create_predictions(
    file: UploadFile = File(...), 
    detector: BaseDetector = Depends(get_detector)
):
    image_bytes = await file.read()
    result = await detector.predict(image_bytes)
    return result
    