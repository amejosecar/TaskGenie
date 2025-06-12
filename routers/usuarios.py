# C:\americo\API\TaskGenie\routers\usuarios.py
# routers/usuarios.py
from fastapi import APIRouter, Depends, Form, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import SessionLocal
from models import Usuario

router = APIRouter(tags=["Usuarios"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UsuarioCreateForm(BaseModel):
    nombre: str
    apellido: str
    edad: int
    fecha_nacimiento: str
    email: str
    clave: str

@router.post("/registro-json")
def registrar_json(u: UsuarioCreateForm, db: Session = Depends(get_db)):
    existing = db.query(Usuario).filter(Usuario.email == u.email).first()
    if existing:
        raise HTTPException(409, "Email ya registrado")
    nuevo = Usuario(
        nombre=u.nombre,
        apellido=u.apellido,
        email=u.email,
        clave=u.clave,
        fecha_nacimiento=u.fecha_nacimiento,  # se parsea en auth_service
        rol="alumno"  # o lo que definas
    )
    db.add(nuevo)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(409, "Email ya registrado")
    db.refresh(nuevo)
    return {"mensaje": "Usuario creado", "id": nuevo.id}
