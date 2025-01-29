from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    facial_embedding = Column(String)  # Store facial embeddings as a string

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name})>"
