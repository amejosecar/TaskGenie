# database.py
# Configuración de la conexión a SQLite.
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Conectar a SQLite
DATABASE_URL = "sqlite:///./taskgenie.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base de datos
Base = declarative_base()

# Modelo de Usuario
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    edad = Column(Integer, nullable=False)
    fecha_nacimiento = Column(String, nullable=False)  # Formato YYYY-MM-DD
    email = Column(String, unique=True, nullable=False)
    clave = Column(String, nullable=False)  # Aquí se guarda la contraseña en texto plano (No recomendado en producción)

# Crear tablas en la BD
Base.metadata.create_all(bind=engine)

