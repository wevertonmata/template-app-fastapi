from starlette.testclient import TestClient
from src.api_main import app

def test_health():
    client = TestClient(app)
    response = client.get("/health")
    data = response.json()
    assert data["api_up"] == True
    assert data["api_version"] == "v1"
    assert response.status_code == 200
    assert response.url == "http://testserver/docs"