from db import Base
from sqlalchemy import Column, Integer, String

# Modelo de Cliente
class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String)
    dni = Column(String)
    birthdate = Column(String)
    tel = Column(String)
    address = Column(String)
    blacklist = Column(String)
    email = Column(String)
    description = Column(String)

