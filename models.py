# models.py
# Modelos de SQLAlchemy.
# models.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Enum, Boolean, ForeignKey
from sqlalchemy.orm import relationship
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
    clave = Column(String, nullable=False)  # Se recomienda utilizar hash en producción
    fecha_nacimiento = Column(Date, nullable=False)  # Actualizado a Date
    rol = Column(Enum(RolEnum), nullable=False)
    bloqueado = Column(Boolean, default=False)  # Nuevo campo: estado de bloqueo

    # Relaciones con tareas:
    tareas_creadas = relationship("Tarea", back_populates="creador", foreign_keys="Tarea.creador_id")
    tareas_asignadas = relationship("Tarea", back_populates="asignado", foreign_keys="Tarea.asignado_a")

class Tarea(Base):
    __tablename__ = "tareas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String)
    importancia = Column(String)
    fecha_entrega = Column(Date)
    estado = Column(String, default="asignada")
    solucion = Column(String)  # Opcional

    creador_id = Column(Integer, ForeignKey("usuarios.id"))
    asignado_a = Column(Integer, ForeignKey("usuarios.id"))

    creador = relationship("Usuario", back_populates="tareas_creadas", foreign_keys=[creador_id])
    asignado = relationship("Usuario", back_populates="tareas_asignadas", foreign_keys=[asignado_a])
