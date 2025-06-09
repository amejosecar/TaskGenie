# models.py
# Modelos de SQLAlchemy.
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Enum
import enum

Base = declarative_base()

class RolEnum(enum.Enum):
    profesor = "profesor"
    alumno = "alumno"
    administrador = "administrador"

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    clave = Column(String, nullable=False)  # Almacenada como hash
    fecha_nacimiento = Column(Date)
    rol = Column(Enum(RolEnum), nullable=False)

class Tarea(Base):
    __tablename__ = "tareas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String)
    importancia = Column(String)
    fecha_entrega = Column(Date)
    estado = Column(String, default="asignada")
    asignado_a = Column(Integer)  # Referencia al id del alumno
    # Agrega otros campos como solución o correcciones
