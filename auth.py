# auth.py (ubicado en C:\americo\API\TaskGenie\auth.py)
# auth.py
# auth.py
from fastapi import (
    APIRouter, Depends, Form, Request, HTTPException, status
)
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import SessionLocal
from services.auth_service import autenticar_usuario, registrar_usuario

router    = APIRouter(tags=["Autenticación"])
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/login", response_class=HTMLResponse)
def login_form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/login_form")
def login_form(
    request: Request,
    email: str = Form(...),
    clave: str = Form(...),
    db: Session = Depends(get_db)
):
    user = autenticar_usuario(db, email, clave)
    if not user:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "error": "Credenciales inválidas."}
        )

    # destino según rol
    if user.rol.value == "administrador":
        destino = "/dashboard_admin"
    elif user.rol.value == "profesor":
        destino = "/dashboard_profesor"
    else:
        destino = "/dashboard_alumno"

    response = RedirectResponse(url=destino, status_code=status.HTTP_302_FOUND)
    response.set_cookie("user_id", str(user.id), httponly=True)
    return response

@router.get("/registro", response_class=HTMLResponse)
def registro_form_get(request: Request):
    return templates.TemplateResponse("registro.html", {"request": request})

@router.post("/registro_form", response_class=HTMLResponse)
def registro_form_post(
    request: Request,
    nombre: str = Form(...),
    apellido: str = Form(...),
    edad: int = Form(...),                   
    fecha_nacimiento: str = Form(...),
    email: str = Form(...),
    rol: str = Form(...),
    clave: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        # registrar_usuario parsea fecha y maneja IntegrityError
        registrar_usuario(
            db,
            nombre=nombre,
            apellido=apellido,
            email=email,
            edad=edad,
            fecha_nacimiento=fecha_nacimiento,
            rol=rol,
            clave=clave
        )
    except ValueError as e:
        # vuelvo a mostrar el formulario con el mensaje de error
        return templates.TemplateResponse(
            "registro.html",
            {"request": request, "error": str(e)}
        )

    # al crear OK, redirijo al login
    return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)
