# Endpoints para ver y editar la información del perfil.
# routers/perfil.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def listar_tareas():
    return {"mensaje": "Listado de tareas"}
