import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, engine
from app.models import Base

# Create the database tables for testing
Base.metadata.create_all(bind=engine)

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

def test_register_face(client):
    # Test face registration
    response = client.post("/register", data={"name": "Test User"}, files={"file": open("test_image.jpg", "rb")})
    assert response.status_code == 200
    assert response.json()["message"] == "User registered successfully"
