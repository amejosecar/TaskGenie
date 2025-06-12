#  schemas.py
# Schemas con Pydantic.
# schemas.py
from pydantic import BaseModel, EmailStr
from datetime import date
from enum import Enum

class RolEnum(str, Enum):
    profesor      = "profesor"
    alumno        = "alumno"
    administrador = "administrador"

class UsuarioCreate(BaseModel):
    nombre: str
    apellido: str
    edad: int
    email: EmailStr
    clave: str
    fecha_nacimiento: date
    rol: RolEnum

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    apellido: str
    email: EmailStr
    edad: int
    fecha_nacimiento: date
    rol: RolEnum
    bloqueado: bool

    class Config:
        from_attributes = True  # Pydantic V2

class UsuarioUpdateRol(BaseModel):
    rol: RolEnum

class UsuarioUpdateBloqueo(BaseModel):
    bloqueado: bool

class MensajeResponse(BaseModel):
    mensaje: str

class Tarea(BaseModel):
    id: int
    titulo: str
    descripcion: str
    importancia: str
    fecha_entrega: date
    estado: str
    solucion: str   
    creador_id: int
    asignado_a: int 
    