# # Endpoints para administración de usuarios.
# # routers/admin.py
# 
# routers/admin.py
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from database import SessionLocal
from models import Usuario
from schemas import UsuarioResponse, UsuarioUpdateRol, UsuarioUpdateBloqueo, MensajeResponse

router = APIRouter(prefix="/admin", tags=["Administración"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/usuarios", response_model=List[UsuarioResponse], summary="Listar todos los usuarios")
def listar_usuarios(db: Session = Depends(get_db)):
    """Obtiene una lista de todos los usuarios almacenados en la base de datos."""
    return db.query(Usuario).all()

@router.get("/usuarios/search", response_model=List[UsuarioResponse], summary="Buscar usuarios por email y/o rol")
def buscar_usuarios(
    rol: Optional[str] = Query(None, description="Filtrar por rol"),
    email: Optional[str] = Query(None, description="Buscar por email"),
    db: Session = Depends(get_db)
):
    """Busca usuarios filtrando por rol y/o email."""
    query = db.query(Usuario)
    if rol:
        query = query.filter(Usuario.rol == rol)
    if email:
        query = query.filter(Usuario.email.ilike(f"%{email}%"))
    
    usuarios = query.all()
    
    if not usuarios:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron usuarios con los criterios dados")
    
    return usuarios

@router.get("/usuarios/{user_id}", response_model=UsuarioResponse, summary="Obtener detalle de un usuario por ID")
def detalle_usuario(user_id: int, db: Session = Depends(get_db)):
    """Obtiene detalles de un usuario por su ID."""
    usuario = db.get(Usuario, user_id)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario

@router.put("/usuarios/{user_id}/rol", response_model=UsuarioResponse, summary="Actualizar rol de un usuario")
def cambiar_rol(user_id: int, upd: UsuarioUpdateRol, db: Session = Depends(get_db)):
    """Cambia el rol de un usuario con el ID proporcionado."""
    usuario = db.get(Usuario, user_id)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    usuario.rol = upd.rol
    db.commit()
    db.refresh(usuario)
    return usuario

@router.put("/usuarios/{user_id}/bloqueo", response_model=UsuarioResponse, summary="Actualizar estado de bloqueo de un usuario")
def cambiar_bloqueo(user_id: int, upd: UsuarioUpdateBloqueo, db: Session = Depends(get_db)):
    """Actualiza el estado de bloqueo de un usuario con el ID proporcionado."""
    usuario = db.get(Usuario, user_id)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    usuario.bloqueado = upd.bloqueado
    db.commit()
    db.refresh(usuario)
    return usuario

@router.delete("/usuarios/{user_id}", response_model=MensajeResponse, summary="Eliminar un usuario")
def eliminar_usuario(user_id: int, db: Session = Depends(get_db)):
    """Elimina un usuario por su ID."""
    usuario = db.get(Usuario, user_id)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    db.delete(usuario)
    db.commit()
    return MensajeResponse(mensaje="Usuario eliminado con éxito")
