from sqlalchemy import Column, Integer, String, Text
from app.db.base_class import Base

class Contact(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    email = Column(String(100), index=True)
    interest = Column(String(100))
    phone = Column(String(20))
    message = Column(Text)
