from fastapi import HTTPException
from fastapi.testclient import TestClient
import pytest
from unittest.mock import AsyncMock, patch

from services.http_client import HttpClient
from app_v1.main import app
from app_v1.routers.pokemon import get_pokemon_list

client = TestClient(app)


@pytest.fixture(params=["asyncio"])
def anyio_backend(request):
    return request.param


# SPECIES api tests
def test_get_species_invalid_param_count():
    response = client.get("/species", params={"count": "InvalidType"})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "int_parsing",
                "loc": ["query", "count"],
                "msg": "Input should be a valid integer, unable to parse string as an integer",
                "input": "InvalidType",
            }
        ]
    }


def test_get_species_non_positive_param_count():
    response = client.get("/species", params={"count": 0})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "greater_than",
                "loc": ["query", "count"],
                "msg": "Input should be greater than 0",
                "input": "0",
                "ctx": {"gt": 0},
            }
        ]
    }


def test_get_species_invalid_param_index():
    response = client.get("/species", params={"index": "InvalidType"})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "int_parsing",
                "loc": ["query", "index"],
                "msg": "Input should be a valid integer, unable to parse string as an integer",
                "input": "InvalidType",
            }
        ]
    }


def test_get_species_negative_param_index():
    response = client.get("/species", params={"index": -1})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "greater_than",
                "loc": ["query", "index"],
                "msg": "Input should be greater than 0",
                "input": "-1",
                "ctx": {"gt": 0},
            }
        ]
    }


def test_get_species_post_not_allowed():
    response = client.post("/species")
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}


def test_get_species_put_not_allowed():
    response = client.put("/species")
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}


def test_get_species_delete_not_allowed():
    response = client.delete("/species")
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}


@pytest.mark.anyio
async def test_get_species_data_no_response():
    async def mock_get(url, params=None):
        return None

    with pytest.raises(HTTPException) as exc_info:
        with patch.object(HttpClient, "get", new=AsyncMock(side_effect=mock_get)):
            await get_pokemon_list()
    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "Internal Server Error"


def test_get_species_data_success():
    count = 20
    response = client.get("/species", params={"count": count})
    response_json = response.json()
    assert response.status_code == 200
    assert "species" in response_json
    assert len(response_json["species"]) == count


# POKEMON api tests
def test_get_pokemon_invalid_param_name():
    response = client.post("/pokemon", json={"name": 1000, "max_moves": 0})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "string_type",
                "loc": ["body", "name"],
                "msg": "Input should be a valid string",
                "input": 1000,
            }
        ]
    }


def test_get_pokemon_missing_param_name():
    response = client.post("/pokemon", json={"max_moves": 0})
    assert response.status_code == 422
    print(response.json())
    assert response.json() == {
        "detail": [
            {
                "type": "missing",
                "loc": ["body", "name"],
                "msg": "Field required",
                "input": {"max_moves": 0},
            }
        ]
    }


def test_get_pokemon_invalid_param_max_moves():
    response = client.post(
        "/pokemon", json={"name": "test", "max_moves": "InvalidType"}
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "int_parsing",
                "loc": ["body", "max_moves"],
                "msg": "Input should be a valid integer, unable to parse string as an integer",
                "input": "InvalidType",
            }
        ]
    }


def test_get_pokemon_missing_param_max_moves():
    response = client.post("/pokemon", json={"name": "test"})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "missing",
                "loc": ["body", "max_moves"],
                "msg": "Field required",
                "input": {"name": "test"},
            }
        ]
    }


def test_get_pokemon_get_not_allowed():
    response = client.get("/pokemon", params={"name": "test", "max_moves": 0})
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}


def test_get_pokemon_put_not_allowed():
    response = client.put("/pokemon", json={"name": "test", "max_moves": 0})
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}


def test_get_pokemon_delete_not_allowed():
    response = client.delete("/pokemon")
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}


def test_get_pokemon_name_does_not_exist():
    response = client.post("/pokemon", json={"name": "test", "max_moves": 0})
    assert response.status_code == 404
    print(response.json())
    assert response.json() == {"detail": "Not Found"}


def test_get_pokemon_data_uppercase_name_success():
    max_moves = 5
    response = client.post(
        "/pokemon", json={"name": "BULBASAUR", "max_moves": max_moves}
    )
    response_json = response.json()
    assert response.status_code == 200
    assert len(response_json["moves"]) <= max_moves


def test_get_pokemon_data_success():
    max_moves = 5
    response = client.post(
        "/pokemon", json={"name": "bulbasaur", "max_moves": max_moves}
    )
    response_json = response.json()
    assert response.status_code == 200
    assert len(response_json["moves"]) <= max_moves
