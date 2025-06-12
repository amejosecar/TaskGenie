# database.py
# app/database.py
import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings

# Convertimos a string
raw_url = str(settings.database_url)

# Solo para SQLite local: garantizamos carpeta 'instance'
if raw_url.startswith("sqlite:///"):
    # extraemos la parte después de sqlite:///
    relative_path = raw_url.replace("sqlite:///", "")
    db_file = Path(relative_path)
    instance_dir = db_file.parent

    # Si la carpeta no existe, la creamos
    if not instance_dir.exists():
        instance_dir.mkdir(parents=True, exist_ok=True)

    db_url = f"sqlite:///{relative_path}"
    connect_args = {"check_same_thread": False}
else:
    db_url = raw_url
    connect_args = {}

engine = create_engine(db_url, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

