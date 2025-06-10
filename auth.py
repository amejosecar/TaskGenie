# auth.py (ubicado en C:\americo\API\TaskGenie\auth.py)
# 

from fastapi import APIRouter, Depends, Form, HTTPException, status, Request, Body
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, Usuario
from services.auth_service import registrar_usuario, autenticar_usuario
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Dependencia para obtener la sesión de la base de datos.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =========================== Endpoints JSON ===========================
class UsuarioCreate(BaseModel):
    nombre: str
    apellido: str
    edad: int
    fecha_nacimiento: str  # Formato YYYY-MM-DD
    email: str
    clave: str
    rol: str

class UsuarioLogin(BaseModel):
    email: str
    clave: str

@router.post("/api/registro", response_model=dict)
def registrar_usuario_json(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        nuevo_usuario = registrar_usuario(
            db,
            nombre=usuario.nombre,
            apellido=usuario.apellido,
            edad=usuario.edad,
            fecha_nacimiento=usuario.fecha_nacimiento,
            email=usuario.email,
            rol=usuario.rol,
            clave=usuario.clave
            
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )
    return {"mensaje": "Usuario registrado correctamente (JSON)", "id": nuevo_usuario.id}

@router.post("/api/login", response_model=dict)
def login_json(usuario: UsuarioLogin, db: Session = Depends(get_db)):
    usuario_db = autenticar_usuario(db, email=usuario.email, clave=usuario.clave)
    if not usuario_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas."
        )
    return {"mensaje": "Login exitoso (JSON)", "usuario_id": usuario_db.id}

# ======================== Endpoints para Formularios HTML =======================
@router.get("/registro", response_class=HTMLResponse)
def registro_form_get(request: Request):
    return templates.TemplateResponse("registro.html", {"request": request})


@router.post("/registro_form")
def registrar_usuario_form(
    nombre: str = Form(...),
    apellido: str = Form(...),
    edad: int = Form(...),
    fecha_nacimiento: str = Form(...),  # Formato YYYY-MM-DD
    email: str = Form(...),
    rol: str = Form(...),
    clave: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        nuevo_usuario = registrar_usuario(
            db,
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            fecha_nacimiento=fecha_nacimiento,
            email=email,
            rol=rol,
            clave=clave
        )
    except ValueError as e:
        return templates.TemplateResponse("registro.html", {"request": {}, "error": str(e)})
    return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)


@router.get("/login", response_class=HTMLResponse)
def login_form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/login_form")
def login_form(
    email: str = Form(...),
    clave: str = Form(...),
    db: Session = Depends(get_db)
):
    db_usuario = autenticar_usuario(db, email=email, clave=clave)
    if not db_usuario:
        return templates.TemplateResponse("index.html", {"request": {}, "error": "Credenciales inválidas."})
    
    # Verificar el rol y redireccionar según corresponda:
    if db_usuario.rol == "administrador":
        # Redirigir a la ruta definida, NO a la carpeta de templates.
        return RedirectResponse(url="/dashboard_admin", status_code=status.HTTP_302_FOUND)
    else:
        return RedirectResponse(url="/dashboard", status_code=status.HTTP_302_FOUND)



# ================= Endpoint Alternativo para Pruebas en Swagger =================
# Este endpoint usa Body y un modelo JSON, por lo que Swagger mostrará los parámetros.
class UsuarioForm(BaseModel):
    nombre: str
    apellido: str
    edad: int
    fecha_nacimiento: str  # YYYY-MM-DD
    email: str
    clave: str
    rol: str

@router.post("/registro_form_alt")
def registrar_usuario_form_alt(form: UsuarioForm = Body(...), db: Session = Depends(get_db)):
    try:
        nuevo_usuario = registrar_usuario(
            db,
            nombre=form.nombre,
            apellido=form.apellido,
            edad=form.edad,
            fecha_nacimiento=form.fecha_nacimiento,
            email=form.email,
            rol=form.rol,
            clave=form.clave
            
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    return {"mensaje": "Usuario registrado correctamente (Form Alternative)", "id": nuevo_usuario.id}
