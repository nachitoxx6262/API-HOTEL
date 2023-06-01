from db import SessionLocal
from models import Client

# Función para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

## Funcion que busca cliente por dni
def get_client_by_dni(dni: str):
    db = next(get_db())
    client = db.query(Client).filter(Client.dni == dni).first()
    return client.dni