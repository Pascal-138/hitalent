import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_booking(test_client: AsyncClient):
    data = {
        "table_id": 1,
        "name": "Test User",
        "reservation_time": "2025-04-13T18:00:00"
    }
    response = await test_client.post("/reservations/", json=data)
    assert response.status_code == 201
    assert response.json()["name"] == "Test User"


@pytest.mark.asyncio
async def test_get_all_booking(test_client: AsyncClient):
    response = await test_client.get("/reservations/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
