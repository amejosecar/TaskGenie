import os

# Determinar el directorio base del proyecto.
# Este script se encuentra en: C:\americo\API\TaskGenie\utilitys\create_structure.py
# Por lo tanto, el directorio base será el directorio padre de "utilitys", es decir:
# C:\americo\API\TaskGenie
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Estructura de carpetas y archivos a crear, directamente en la raíz del proyecto TaskGenie.
estructura = {
    "__init__.py": "",
    "main.py": "# Punto de arranque de la aplicación.\n",
    "config.py": "# Manejo de variables de entorno.\n",
    "database.py": "# Configuración de la conexión a SQLite.\n",
    "models.py": "# Modelos de SQLAlchemy.\n",
    "schemas.py": "# Schemas con Pydantic.\n",
    "auth.py": "# Funciones de autenticación y manejo de roles.\n",
    "routers": {
        "__init__.py": "",
        "usuarios.py": "# Endpoints para registro, edición, búsqueda y bloqueo de usuarios.\n",
        "tareas.py": "# Endpoints para la gestión de tareas.\n",
        "perfil.py": "# Endpoints para ver y editar la información del perfil.\n",
        "admin.py": "# Endpoints para administración de usuarios.\n"
    },
    "templates": {
        "index.html": "<!-- Página de inicio con formulario de login -->\n",
        "login.html": "<!-- Vista de login -->\n",
        "registro.html": "<!-- Formulario de registro -->\n",
        "dashboard_profesor.html": "<!-- Dashboard para profesores -->\n",
        "dashboard_alumno.html": "<!-- Dashboard para alumnos -->\n",
        "dashboard_admin.html": "<!-- Dashboard para administradores -->\n"
        # Se pueden agregar más archivos según se requiera.
    },
    ".env": "# Archivo de configuración de variables sensibles.\n"
}

def crear_estructura(root, estructura_dict):
    """
    Crea recursivamente carpetas y archivos según la estructura definida en el diccionario.
    """
    for nombre, contenido in estructura_dict.items():
        ruta = os.path.join(root, nombre)
        if isinstance(contenido, dict):
            # Es una carpeta: se crea (si no existe) y se procesa recursivamente su contenido.
            if not os.path.exists(ruta):
                print(f"Creando carpeta: {ruta}")
                os.makedirs(ruta)
            crear_estructura(ruta, contenido)
        else:
            # Es un archivo: se crea (si no existe) y se escribe el contenido.
            if not os.path.exists(ruta):
                print(f"Creando archivo: {ruta}")
                with open(ruta, "w", encoding="utf-8") as f:
                    f.write(contenido)
            else:
                print(f"El archivo ya existe: {ruta}")

if __name__ == "__main__":
    crear_estructura(base_dir, estructura)
    print("Estructura de proyecto creada con éxito.")
