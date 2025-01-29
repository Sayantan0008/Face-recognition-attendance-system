from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.services.face_registration import register_face
from app.services.face_recognition import recognize_face
from app.models import User
from app.database import get_db  # Assuming a database session dependency is defined

router = APIRouter()

@router.post("/register")
async def register(name: str, file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Save the uploaded file temporarily
    with open(file.filename, "wb") as buffer:
        buffer.write(await file.read())
    
    # Register the face
    user = register_face(db, name, file.filename)
    return {"message": "User registered successfully", "user_id": user.id}

@router.post("/recognize")
async def recognize(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Save the uploaded file temporarily
    with open(file.filename, "wb") as buffer:
        buffer.write(await file.read())
    
    # Recognize the face
    user_name = recognize_face(db, file.filename)
    if user_name:
        return {"message": f"Welcome back, {user_name}!"}
    return {"message": "Face not recognized."}
