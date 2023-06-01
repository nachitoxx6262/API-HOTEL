from pydantic import BaseModel
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
