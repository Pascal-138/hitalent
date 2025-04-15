import pytest_asyncio
from httpx import AsyncClient
from asgi_lifespan import LifespanManager
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.main import app


@pytest_asyncio.fixture(scope="module")
async def test_client():
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as client:
            yield client
