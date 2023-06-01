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
    if client == None:
        return None
    else:
            return client.__dict__
    
## Funcion que verifica el estado de BlackList recibiendo el cliente completo
def check_blacklist(client):
    blacklist = client.get("blacklist")
    print(blacklist)
    if blacklist == "True":
        return True
    else:
        return False