from fastapi import FastAPI, Depends
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  Session
from schemas import schema_client
from models import Client
from functions import get_db, get_client_by_dni,check_blacklist
app = FastAPI()


# Ruta para crear un cliente
@app.post("/clients")
def create_client(client: schema_client, db: Session = Depends(get_db)):
    client_existing = get_client_by_dni(client.dni)
    print(client_existing)
    if client_existing == None:
        db_client = Client(
            name=client.name,
            gender=client.gender,
            dni=client.dni,
            birthdate=client.birthdate,
            tel=client.tel,
            address=client.address,
            blacklist=client.blacklist,
            email=client.email,
            description=client.description
        )
        db.add(db_client)
        db.commit()
        db.refresh(db_client)
        return client
    else:
        # verifica si esta en blacklist utilizando la funcion
        if check_blacklist(client_existing):
            client_dni = client_existing.get('dni')
            return {"message":f"El cliente con DNI {client_dni} esta en blacklist ", "type": "false"}
        else:
            client_dni = client_existing.get('dni')
            return {"message":f"El cliente con DNI {client_dni} ya existe ", "type": "false"}

# Ruta para obtener todos los clientes
@app.get("/clients")
def get_client():
    return {"message":"Hola mundo"}