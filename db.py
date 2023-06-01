
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

db_user = os.environ.get("USER")
db_password = os.environ.get("PASSWORD")
db_host  = os.environ.get("HOST")
# Configuración de la base de datos
SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}/hotelpy"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()