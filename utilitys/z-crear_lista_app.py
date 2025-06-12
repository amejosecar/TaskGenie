#!/usr/bin/env python3
import os

# create_structure.py

# Lista de rutas de los archivos a incluir
paths_to_process = [
    r"C:\americo\API\TaskGenie\.env",
    r"C:\americo\API\TaskGenie\auth.py",
    r"C:\americo\API\TaskGenie\config.py",
    r"C:\americo\API\TaskGenie\database.py",
    r"C:\americo\API\TaskGenie\main.py",
    r"C:\americo\API\TaskGenie\models.py",
    r"C:\americo\API\TaskGenie\schemas.py",
    r"C:\americo\API\TaskGenie\routers\admin.py",
    r"C:\americo\API\TaskGenie\routers\perfil.py",
    r"C:\americo\API\TaskGenie\routers\tareas.py",
    r"C:\americo\API\TaskGenie\routers\usuarios.py",
    r"C:\americo\API\TaskGenie\services\auth_service.py",
    r"C:\americo\API\TaskGenie\templates\dashboard_admin.html",
    r"C:\americo\API\TaskGenie\templates\dashboard_alumno.html",
    r"C:\americo\API\TaskGenie\templates\dashboard_profesor.html",
    r"C:\americo\API\TaskGenie\templates\errores.html",
    r"C:\americo\API\TaskGenie\templates\dashboard.html",
    r"C:\americo\API\TaskGenie\templates\index.html",
    r"C:\americo\API\TaskGenie\templates\login.html",
    r"C:\americo\API\TaskGenie\templates\registro.html",
]

def write_files_to_txt(file_paths, output_file):
    """
    Escribe el contenido de cada archivo en 'file_paths' dentro de 'output_file'.
    Antes de cada contenido inserta:
      - 40 guiones
      - comentario con la ruta del archivo
    """
    with open(output_file, "w", encoding="utf8") as outf:
        for file_path in file_paths:
            outf.write("-" * 40 + "\n")
            outf.write(f"# {file_path}\n")
            try:
                with open(file_path, "r", encoding="utf8") as f:
                    outf.write(f.read())
            except Exception as e:
                outf.write(f"# Error al leer este archivo: {e}\n")
            outf.write("\n")
    print(f"Se han copiado {len(file_paths)} archivos a '{output_file}'.")

if __name__ == "__main__":
    # 1) Buscar y eliminar z-crear_lista_app.py
    target = r"C:\americo\API\TaskGenie\utilitys\a-TaskGenie.txt"
    if os.path.exists(target):
        print("Archivo 'a-TaskGenie.txt.py' encontrado, eliminando...")
        try:
            os.remove(target)
            print("Archivo eliminado.")
        except Exception as e:
            print(f"No se pudo eliminar el archivo: {e}")
    else:
        print("Archivo 'a-TaskGenie.txt.py' no encontrado.")

    # 2) Ejecutar la generación del TXT
    output_file = "a-TaskGenie.txt"
    write_files_to_txt(paths_to_process, output_file)

    # 3) Mensaje final
    print("Código ejecutado con éxito.")
