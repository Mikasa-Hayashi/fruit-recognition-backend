from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel import SQLModel
from .constants import DATABASE_URL

engine = create_async_engine(
    DATABASE_URL,
)

AsyncSessionLocal = async_sessionmaker(
    engine, expire_on_commit=False
)

async def get_session():
    async with AsyncSessionLocal() as session:
        yield session