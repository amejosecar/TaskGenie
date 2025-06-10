# auth_service.py
# este archivo contiene la lógica de negocio relacionada con la autenticación y el registro de usuarios.

# services/auth_service.py
from sqlalchemy.exc import IntegrityError
from database import Usuario
from datetime import datetime

def registrar_usuario(db, nombre, apellido, edad, fecha_nacimiento, email, rol, clave):
    # Convertir fecha de nacimiento a objeto date
    try:
        fecha_obj = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("La fecha de nacimiento debe tener el formato YYYY-MM-DD.")
    
    # Convertir rol a minúsculas para mantener consistencia
    rol = rol.lower()
    
    nuevo_usuario = Usuario(
        nombre=nombre,
        apellido=apellido,
        edad=edad,
        fecha_nacimiento=fecha_obj,  # Se usa el objeto date
        email=email,
        rol=rol,
        clave=clave  # Reemplazar con hash_password(clave) en producción
    )
    db.add(nuevo_usuario)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("Ya existe un usuario con ese email.")
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def autenticar_usuario(db, email, clave):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if usuario and usuario.clave == clave:  # Comparar contra el hash en producción
        return usuario
    return None
