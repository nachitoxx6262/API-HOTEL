from pydantic import BaseModel

# Schema de clientes
class schema_client(BaseModel):
    name: str
    gender: str
    dni: str
    birthdate: str
    tel: str
    address: str
    blacklist: str
    email: str
    description: str
