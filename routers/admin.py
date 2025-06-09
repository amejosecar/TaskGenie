# Endpoints para administración de usuarios.
# routers/admin.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def listar_tareas():
    return {"mensaje": "Listado de tareas"}
