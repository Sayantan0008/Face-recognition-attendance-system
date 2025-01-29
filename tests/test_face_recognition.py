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

def test_recognize_face(client):
    # Test face recognition
    response = client.post("/recognize", files={"file": open("test_image.jpg", "rb")})
    assert response.status_code == 200
    assert "message" in response.json()
