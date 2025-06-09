# auth.py (ubicado en C:\americo\API\TaskGenie\auth.py)
# auth.py (ubicado en C:\americo\API\TaskGenie\auth.py)
from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from database import SessionLocal, Usuario
from pydantic import BaseModel

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Schema para registrar un usuario (para solicitudes JSON).
class UsuarioCreate(BaseModel):
    nombre: str
    apellido: str
    edad: int
    fecha_nacimiento: str  # Formato YYYY-MM-DD
    email: str
    clave: str  # Se enviará en texto plano (solo para práctica)

# Endpoint para registrar un usuario usando JSON.
@router.post("/registro/")
def registrar_usuario_json(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    nuevo_usuario = Usuario(nombre=usuario.nombre,  apellido=usuario.apellido, edad=usuario.edad, fecha_nacimiento=usuario.fecha_nacimiento,email=usuario.email, clave=usuario.clave)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return {"mensaje": "Usuario registrado correctamente (JSON)", "id": nuevo_usuario.id}

# Endpoint para registrar un usuario usando datos de formulario.
@router.post("/registro_form")
def registrar_usuario_form(
    nombre: str = Form(...),
    apellido: str = Form(...),
    edad : int = Form(...),
    fecha_nacimiento: str = Form(...),  # Formato YYYY-MM-DD
    email: str = Form(...),
    clave: str = Form(...),
    db: Session = Depends(get_db)
):
    nuevo_usuario = Usuario(nombre=nombre, apellido=apellido, edad=edad, fecha_nacimiento=fecha_nacimiento,email=email, clave=clave)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return {"mensaje": "Usuario registrado correctamente (Form)", "id": nuevo_usuario.id}

# Endpoint para recuperar la contraseña por email.
@router.get("/recuperar/{email}")
def recuperar_clave(email: str, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if usuario:
        return {"mensaje": f"La contraseña para {email} es: {usuario.clave}"}
    return {"error": "Usuario no encontrado"}

# -----------------------------------------------
# Endpoint para login usando JSON (cuerpo de la petición).
class UsuarioLogin(BaseModel):
    email: str
    clave: str

@router.post("/login_json")
def login_json(usuario: UsuarioLogin, db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if not db_usuario:
        return {"error": "Credenciales inválidas"}
    if db_usuario.clave != usuario.clave:
        return {"error": "Credenciales inválidas"}
    return {"mensaje": "Login exitoso (JSON)", "usuario_id": db_usuario.id}

# -----------------------------------------------
# Endpoint para login usando datos de formulario.
@router.post("/login_form")
def login_form(
    email: str = Form(...),
    clave: str = Form(...),
    db: Session = Depends(get_db)
):
    db_usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not db_usuario:
        return {"error": "Credenciales inválidas"}
    if db_usuario.clave != clave:
        return {"error": "Credenciales inválidas"}
    return {"mensaje": "Login exitoso (Form)", "usuario_id": db_usuario.id}
