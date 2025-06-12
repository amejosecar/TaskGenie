# services/auth_service.py
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from models import Usuario

def registrar_usuario(db, *, nombre, apellido, edad, email, fecha_nacimiento, rol, clave):
    # Convertir fecha de string a date
    if isinstance(fecha_nacimiento, str):
        try:
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Fecha debe tener formato YYYY-MM-DD.")

    usuario = Usuario(
        nombre=nombre,
        apellido=apellido,
        edad=edad, 
        email=email,
        clave=clave,  # → en producción usa hashing
        fecha_nacimiento=fecha_nacimiento,
        rol=rol
    )
    db.add(usuario)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("Ya existe un usuario con ese email.")
    db.refresh(usuario)
    return usuario

def autenticar_usuario(db, email: str, clave: str):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if usuario and usuario.clave == clave:
        return usuario
    return None
