#!/usr/bin/env python3
import os

# create_structure.py
# Lista de rutas de los archivos a incluir, tanto .py como .html,
# usando raw strings (r"") para evitar problemas de secuencias de escape en Windows.
# C:\americo\API\TaskGenie\utilitys\z-crear_lista_app.py

paths_to_process = [
    r"C:\americo\API\TaskGenie\.env",
    r"C:\americo\API\TaskGenie\auth.py",
    r"C:\americo\API\TaskGenie\config.py",
    r"C:\americo\API\TaskGenie\database.py",
    r"C:\americo\API\TaskGenie\main.py",
    r"C:\americo\API\TaskGenie\models.py",
    r"C:\americo\API\TaskGenie\requirements.txt",
    r"C:\americo\API\TaskGenie\schemas.py",
    r"C:\americo\API\TaskGenie\taskgenie.db",
    r"C:\americo\API\TaskGenie\__init__.py",
    r"C:\americo\API\TaskGenie\routers\admin.py",
    r"C:\americo\API\TaskGenie\routers\perfil.py",
    r"C:\americo\API\TaskGenie\routers\tareas.py",
    r"C:\americo\API\TaskGenie\routers\usuarios.py",
    r"C:\americo\API\TaskGenie\routers\__init__.py",
    r"C:\americo\API\TaskGenie\templates\dashboard_admin.html",
    r"C:\americo\API\TaskGenie\templates\dashboard_alumno.html",
    r"C:\americo\API\TaskGenie\templates\dashboard_profesor.html",
    r"C:\americo\API\TaskGenie\templates\errores.html",
    r"C:\americo\API\TaskGenie\templates\dashboard.html",
    r"C:\americo\API\TaskGenie\templates\index.html",
    r"C:\americo\API\TaskGenie\templates\login.html",
    r"C:\americo\API\TaskGenie\templates\registro.html",
    r"C:\americo\API\TaskGenie\services\auth_service.py"

]

def write_files_to_txt(file_paths, output_file):
    """
    Escribe el contenido de cada archivo en 'file_paths' dentro de 'output_file'.
    Antes del contenido de cada archivo se inserta:
      - Una línea divisoria (40 guiones)
      - Una línea con la ruta y nombre del archivo (formateado como comentario)
    """
    with open(output_file, "w", encoding="utf8") as outf:
        for file_path in file_paths:
            # Línea divisoria
            outf.write("-" * 40 + "\n")
            # Encabezado con la ruta y el nombre del archivo
            outf.write(f"# {file_path}\n")
            # Leer y escribir el contenido del archivo
            try:
                with open(file_path, "r", encoding="utf8") as f:
                    outf.write(f.read())
            except Exception as e:
                outf.write(f"# Error al leer este archivo: {e}\n")
            outf.write("\n")
    print(f"Se han copiado {len(file_paths)} archivos a '{output_file}'.")

if __name__ == "__main__":
    output_file = "a-TaskGenie.txt"
    write_files_to_txt(paths_to_process, output_file)
