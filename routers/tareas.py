# Endpoints para la gestión de tareas.
# routers/tareas.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def listar_tareas():
    return {"mensaje": "Listado de tareas"}
