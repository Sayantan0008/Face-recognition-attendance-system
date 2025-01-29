from fastapi import FastAPI
from app.routes.face_routes import router as face_router
from app.models import Base
from app.database import engine  # Assuming a database engine is defined

# Create the FastAPI app
app = FastAPI()

# Include the face recognition routes
app.include_router(face_router)

# Create the database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Face Recognition Attendance System"}
