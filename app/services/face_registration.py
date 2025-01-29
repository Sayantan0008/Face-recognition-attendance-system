import face_recognition
import numpy as np
from sqlalchemy.orm import Session
from app.models.user import User

def register_face(db: Session, name: str, image_path: str):
    # Load the image
    image = face_recognition.load_image_file(image_path)
    # Get the facial embeddings
    facial_embedding = face_recognition.face_encodings(image)[0]
    # Convert to a list for storage
    facial_embedding_list = np.array(facial_embedding).tolist()
    
    # Create a new user instance
    new_user = User(name=name, facial_embedding=str(facial_embedding_list))
    
    # Add the user to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user
