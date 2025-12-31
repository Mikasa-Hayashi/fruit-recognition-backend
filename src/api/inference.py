from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
from database import SessionDep
from inference.base import BaseDetector
from inference.loader import get_detector
from models.fruits import Fruit
from sqlmodel import select

router = APIRouter(prefix='/inference', tags=['inference'])

@router.post('/predictions')
async def create_predictions(
    file: UploadFile = File(...), 
    detector: BaseDetector = Depends(get_detector)
):
    image_bytes = await file.read()
    predictions = await detector.predict(image_bytes)
    return predictions


@router.post('/classify')
async def classify_image(
    file: UploadFile = File(...), 
    detector: BaseDetector = Depends(get_detector),
):
    image_bytes = await file.read()
    predictions = await detector.predict(image_bytes)

    if not predictions.detections:
        return {'message': 'No objects detected'}

    main_prediction = max(predictions.detections, key=lambda det: det.confidence)
    return main_prediction


@router.post('/fruit')
async def detect_fruit(
    session: SessionDep,
    file: UploadFile = File(...), 
    detector: BaseDetector = Depends(get_detector)
):
    image_bytes = await file.read()
    predictions = await detector.predict(image_bytes)

    if not predictions.detections:
        return {'message': 'No objects detected'}
    
    main_prediction = max(predictions.detections, key=lambda det: det.confidence)

    result = await session.execute(
        select(Fruit).where(Fruit.name == main_prediction.label)
    )
    fruit = result.scalar_one_or_none()

    if not fruit:
        raise HTTPException(status_code=404, detail=f'Fruit "{main_prediction.label}" not found')

    return {
        'detection': main_prediction,
        'fruit_info': fruit,
    }