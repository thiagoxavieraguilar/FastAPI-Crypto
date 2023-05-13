
from fastapi.testclient import TestClient
from routes.hello import app

Client = TestClient(app)


def test_read_main():
    with Client as client:
        response = client.get("/")
        assert response.status_code == 200
        
