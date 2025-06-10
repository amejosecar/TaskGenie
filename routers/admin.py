# # Endpoints para administración de usuarios.
# # routers/admin.py
# 
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from database import SessionLocal, Usuario
from schemas import (
    UsuarioResponse,
    UsuarioUpdateRol,
    UsuarioUpdateBloqueo,
    MensajeResponse
)

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint 1: Listar todos los usuarios
@router.get("/usuarios", response_model=List[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return usuarios

# Endpoint 2: Obtener el detalle de un usuario específico
@router.get("/usuarios/{user_id}", response_model=UsuarioResponse)
def obtener_detalle_usuario(user_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    return usuario

# Endpoint 3: Actualizar el rol de un usuario
@router.put("/usuarios/{user_id}/rol", response_model=UsuarioResponse)
def actualizar_rol(user_id: int, update: UsuarioUpdateRol, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    usuario.rol = update.rol
    db.commit()
    db.refresh(usuario)
    return usuario

# Endpoint 4: Actualizar el estado de bloqueo de un usuario
@router.put("/usuarios/{user_id}/bloqueo", response_model=UsuarioResponse)
def actualizar_bloqueo(user_id: int, update: UsuarioUpdateBloqueo, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    usuario.bloqueado = update.bloqueado
    db.commit()
    db.refresh(usuario)
    return usuario

# Endpoint 5 (Opcional): Eliminar un usuario
@router.delete("/usuarios/{user_id}", response_model=MensajeResponse)
def eliminar_usuario(user_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    db.delete(usuario)
    db.commit()
    return {"mensaje": "Usuario eliminado con éxito"}

# (Opcional) Endpoint Extra: Buscar usuarios por filtro
@router.get("/usuarios/search", response_model=List[UsuarioResponse])
def buscar_usuarios(
    rol: Optional[str] = None,
    email: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Usuario)
    if rol:
        query = query.filter(Usuario.rol == rol)
    if email:
        query = query.filter(Usuario.email.ilike(f"%{email}%"))
    usuarios = query.all()
    return usuarios