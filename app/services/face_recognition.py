import face_recognition
import numpy as np
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.attendance import Attendance
from datetime import datetime

def recognize_face(db: Session, image_path: str):
    # Load the image
    image = face_recognition.load_image_file(image_path)
    # Get the facial embeddings
    unknown_face_encoding = face_recognition.face_encodings(image)[0]

    # Retrieve all users from the database
    users = db.query(User).all()
    for user in users:
        # Convert the stored facial embedding back to a numpy array
        known_face_encoding = np.fromstring(user.facial_embedding[1:-1], sep=',')
        
        # Compare the faces
        results = face_recognition.compare_faces([known_face_encoding], unknown_face_encoding)
        
        if results[0]:
            # Mark attendance if a match is found
            attendance_record = Attendance(user_id=user.id)
            db.add(attendance_record)
            db.commit()
            return user.name  # Return the recognized user's name

    return None  # No match found
