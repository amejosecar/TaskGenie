#!/usr/bin/env python3
import sys
from pathlib import Path

# 1. Calculamos la ruta absoluta de la carpeta raíz (dos niveles arriba)
proyecto_raiz = Path(__file__).parent.parent.resolve()
# 2. La añadimos al path de búsqueda de módulos
sys.path.insert(0, str(proyecto_raiz))

# Ahora sí podemos importar:
from models import Usuario, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

def main():
    try:
        db_file = proyecto_raiz / "taskgenie.db"
        print(f"[+] Conectando a la base de datos en: {db_file}")
        engine = create_engine(f"sqlite:///{db_file}", connect_args={"check_same_thread": False})
        Session = sessionmaker(bind=engine)
        db = Session()

        modificaciones = []
        for u in db.query(Usuario).all():
            original = u.fecha_nacimiento
            if isinstance(original, str) and "/" in original:
                print(f"    – [ANTES] Usuario {u.id}: '{original}'")
                try:
                    nuevo = datetime.strptime(original, "%Y/%m/%d").date()
                except ValueError:
                    print(f"       ¡ERROR! formato inválido, se salta.")
                    continue
                u.fecha_nacimiento = nuevo
                modificaciones.append(u.id)
                print(f"       [DESPUÉS] Usuario {u.id}: '{nuevo}'")

        if modificaciones:
            db.commit()
            print(f"\n[+] Migración OK. Usuarios actualizados: {modificaciones}")
        else:
            print("\n[!] No se hallaron fechas con '/' para migrar.")
        db.close()
        print("[*] Script finalizado correctamente.")
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
