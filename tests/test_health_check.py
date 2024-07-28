from fastapi import HTTPException
from fastapi.testclient import TestClient
from unittest import mock

from src.v1.app import app


client = TestClient(app)


def test_health_check_post_not_allowed():
    response = client.post("/healthz")
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}


def test_health_check_put_not_allowed():
    response = client.put("/healthz")
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}


def test_health_check_delete_not_allowed():
    response = client.delete("/healthz")
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}


@mock.patch(
    "src.v1.routers.health_check.health_check",
    return_value=HTTPException(status_code=500),
)
def test_health_check_exception_error(health_check):
    response = health_check()
    assert response.status_code == 500
    assert response.detail == "Internal Server Error"


def test_health_check_success():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"message": "OK", "status": 200}
