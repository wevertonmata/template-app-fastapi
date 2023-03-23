from starlette.testclient import TestClient
from v1_api import v1_app


def test_health():
    client = TestClient(v1_app)
    response = client.get("/health")
    data = response.json()
    assert data["api_up"] == True
    assert data["api_version"] == "v1"
    assert response.status_code == 200
    assert response.url == "http://testserver/docs"

