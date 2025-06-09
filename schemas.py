#  schemas.py
# Schemas con Pydantic.
from pydantic import BaseModel, EmailStr
from datetime import date
from enum import Enum

class RolEnum(str, Enum):
    profesor = "profesor"
    alumno = "alumno"
    administrador = "administrador"

class UsuarioCreate(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    clave: str
    fecha_nacimiento: date
    rol: RolEnum

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    apellido: str
    email: EmailStr
    fecha_nacimiento: date
    rol: RolEnum
    class Config:
        orm_mode = True

# Define esquemas para Tarea y otras entidades según lo necesites.
