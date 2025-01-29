from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Attendance(Base):
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)  # Foreign key to User
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Attendance(id={self.id}, user_id={self.user_id}, timestamp={self.timestamp})>"
