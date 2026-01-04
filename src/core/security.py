from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader
from typing import Annotated
from core.config import settings

api_key_header = APIKeyHeader(name='Authorization', auto_error=False)

async def verify_token(
    auth_header: str = Security(api_key_header)
):
    if auth_header is None or not auth_header.startswith('Bearer '):
        raise HTTPException(status_code=401, detail='Unauthorized')

    token = auth_header.replace('Bearer ', '')

    if token != settings.TRUSTED_TOKEN:
        raise HTTPException(status_code=403, detail='Forbidden')

    return token