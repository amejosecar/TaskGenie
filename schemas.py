#  schemas.py
# Schemas con Pydantic.
# schemas.py
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
    fecha_nacimiento: date  # Ahora date
    rol: RolEnum

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    apellido: str
    email: EmailStr
    fecha_nacimiento: date
    rol: RolEnum

    class Config:
        # Si estás usando Pydantic V1, deja: orm_mode = True
        # Para Pydantic V2:
        from_attributes = True

class UsuarioUpdateRol(BaseModel):
    rol: RolEnum

class UsuarioUpdateBloqueo(BaseModel):
    bloqueado: bool

class MensajeResponse(BaseModel):
    mensaje: str

