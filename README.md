# TaskGenie

TaskGenie es una aplicación de gestión de tareas desarrollada en Python, orientada a objetos y diseñada como proyecto de curso. La aplicación gestiona usuarios y tareas con tres roles definidos: profesor, administrador y alumno. TaskGenie utiliza un backend basado en FastAPI, SQLAlchemy con SQLite para la base de datos, Pydantic para la validación de datos, y Jinja2 para renderizar plantillas HTML. Además, incluye mecanismos de autenticación, seguridad y gestión de roles, y está diseñada para ser replicada en GitHub.

---

## 1. Definición y Planificación Inicial

### Requerimientos Funcionales
- **Roles de Usuario:**  
  - Profesor  
  - Administrador  
  - Alumno

- **Permisología por Rol:**  
  Cada rol tiene acciones específicas dentro del sistema.

- **Gestión de Tareas:**  
  - Creación, asignación, edición, culminación y corrección de tareas.  
  - Bloqueo y administración de usuarios (por el administrador).

- **Módulos:**  
  - Login/Registro  
  - Mi perfil  
  - Administración de usuarios

### Requerimientos Tecnológicos
- **Backend:**  
  - FastAPI  
  - SQLAlchemy (SQLite)  
  - Pydantic  
  - Jinja2 (plantillas)  
  - python-dotenv (variables de entorno)  
  - bcrypt (hashing de contraseñas)

- **Autenticación y Seguridad:**  
  - Gestión de roles y permisos (usando JWT o dependencias para validar roles)  
  - Hashing y verificación de contraseñas

- **Frontend:**  
  - Plantillas HTML generadas con Jinja2

---

## 2. Configuración del Entorno y Estructura del Proyecto

### 2.1. Crear el Proyecto y Configurar el Entorno Virtual

```bash
mkdir taskgenie
cd taskgenie
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
2.2. Instalar Dependencias
bash
pip install fastapi uvicorn sqlalchemy pydantic jinja2 python-dotenv bcrypt
2.3. Configurar la Estructura de Directorios
La siguiente es una estructura sugerida del proyecto:

taskgenie/
│-- app/
│   │-- __init__.py
│   │-- main.py         # Punto de arranque de la aplicación.
│   │-- config.py       # Manejo de variables de entorno.
│   │-- database.py     # Configuración de la conexión a SQLite.
│   │-- models.py       # Modelos de SQLAlchemy.
│   │-- schemas.py      # Schemas con Pydantic.
│   │-- auth.py         # Funciones de autenticación y manejo de roles.
│   │-- routers/
│   │   │-- __init__.py
│   │   │-- usuarios.py   # Endpoints para registro, edición, búsqueda y bloqueo de usuarios.
│   │   │-- tareas.py     # Endpoints para la gestión de tareas.
│   │   │-- perfil.py     # Endpoints para ver y editar la información del perfil.
│   │   │-- admin.py      # Endpoints para administración de usuarios.
│   │-- templates/
│       │-- index.html               # Página de inicio con formulario de login.
│       │-- login.html               # Vista de login.
│       │-- registro.html            # Formulario de registro.
│       │-- dashboard_profesor.html  # Dashboard para profesores.
│       │-- dashboard_alumno.html    # Dashboard para alumnos.
│       │-- dashboard_admin.html     # Dashboard para administradores.
│       └-- ... (otros formularios y vistas)
└-- .env                           # Archivo de variables sensibles.
2.4. Inicializar un Repositorio Git
bash
git init
git add .
git commit -m "Proyecto TaskGenie: inicialización de la aplicación"
3. Desarrollo del Backend
3.1. Configuración de Base de Datos y Modelado
database.py: Configura la conexión a SQLite y crea la sesión con SQLAlchemy.

models.py: Define las siguientes clases:

Usuario:

Campos: id, nombre, apellido, email, clave (hash), fecha_nacimiento, edad (calculada) y rol.

Tarea:

Campos: id, título, descripción, importancia, fecha de entrega, estado, asignado_a, solución del alumno, etc.

Se pueden definir relaciones, por ejemplo: un profesor crea tareas, y cada tarea está asignada a un alumno.

3.2. Definición de Schemas con Pydantic (schemas.py)
Crear los esquemas para:

Usuario: UsuarioCreate, UsuarioResponse, UsuarioEdit

Tarea: TareaCreate, TareaResponse, TareaEdit, TareaCorreccion

3.3. Autenticación y Manejo de Roles (auth.py)
Implementa:

Funciones para el hashing y verificación de contraseñas (usando bcrypt).

Emisión y verificación de tokens (por ejemplo, con JWT o usando dependencias de FastAPI).

Dependencias para proteger endpoints según el rol del usuario (por ejemplo, funciones como get_current_user que verifiquen que el usuario tenga el rol adecuado).

3.4. Endpoints y Routers (routers/)
Usuarios (usuarios.py): Endpoints para registro, edición, búsqueda y bloqueo de usuarios (este último para el administrador).

Tareas (tareas.py): Acciones según rol:

Profesor: Crear, buscar, asignar, cancelar y corregir tareas.

Alumno: Visualizar, editar, culminar tareas, cargar solución y fecha de entrega.

Perfil (perfil.py): Endpoints para ver y editar el perfil del usuario.

Administración (admin.py): Endpoints para la administración de los usuarios, como editar roles o bloquear usuarios.

Integración en main.py: Importa y registra los routers con app.include_router(...).

4. Desarrollo del Frontend con Jinja2
4.1. Configuración de Templates
Configura Jinja2Templates en un archivo (por ejemplo, templates.py o directamente en main.py) para renderizar las vistas HTML.

4.2. Diseño de las Plantillas HTML
Index/Login:

index.html contendrá un formulario de login con campos para usuario y clave, y enlaces a registro y recuperación de cuenta.

Registro:

registro.html tendrá el formulario para capturar nombre, apellido, email, clave, fecha de nacimiento (realizando el cálculo de edad en el backend).

Dashboards y Formularios de Gestión:

dashboard_profesor.html: Funcionalidades para que el profesor cree, busque, asigne, cancele y corrija tareas.

dashboard_alumno.html: Funcionalidades para que el alumno visualice, edite y culmine las tareas asignadas.

dashboard_admin.html: Funcionalidades para que el administrador gestione usuarios (bloqueo, edición de permisos).

4.3. Enlaces y Navegación
Incluir enlaces o botones en las plantillas para facilitar la navegación entre vistas, por ejemplo, enlaces a "Mi Perfil" o a "Administración de Usuarios".

5. Integración, Pruebas y Documentación
5.1. Pruebas Unitarias e Integración
Desarrollar tests para:

Endpoints críticos (autenticación, registro, gestión de tareas y usuarios).

Validación de datos en los esquemas.

5.2. Pruebas de Interfaz
Utilizar herramientas como Postman o cURL para verificar los endpoints y asegurar que las plantillas HTML se rendericen correctamente.

5.3. Documentación y Comentarios
Aprovechar la documentación automática de FastAPI (Swagger UI) e incluir comentarios en el código para una mejor comprensión.

5.4. Ajustes de Seguridad y Variables de Entorno
Verificar que todas las variables sensibles estén definidas en el archivo .env y sean utilizadas adecuadamente dentro de la aplicación.

6. Replicación en GitHub
6.1. Creación del Repositorio en GitHub
Ingresa a GitHub y crea un nuevo repositorio, por ejemplo, TaskGenie.

Añade una descripción adecuada, como: "Aplicación de gestión de tareas con FastAPI, SQLAlchemy y Jinja2".

6.2. Conectar el Repositorio Local con GitHub
Desde la línea de comandos, en el directorio raíz del proyecto:

bash
git remote add origin https://github.com/tu_usuario/TaskGenie.git
git branch -M main
git push -u origin main
6.3. Buenas Prácticas en Git
Realiza commits frecuentes y descriptivos conforme avances en cada paso.

Utiliza ramas (branches) para el desarrollo de nuevas funcionalidades o correcciones.

Actualiza este README.md con instrucciones de instalación, configuración de variables de entorno y ejemplos de uso.

6.4. Automatización y CI/CD (Opcional)
Considera la integración de GitHub Actions para ejecutar tests automáticamente al hacer push, garantizando la calidad y robustez del código.

Resumen Final
TaskGenie se desarrollará de manera modular, integrando el backend (FastAPI, SQLAlchemy, Pydantic y Jinja2) y replicado en GitHub para facilitar el control de versiones y colaboraciones. Este plan abarca desde la configuración inicial del entorno, la estructura de directorios, la definición de modelos y endpoints, hasta la documentación y despliegue.

TaskGenie es tu punto de partida para aprender y desarrollar una aplicación real de gestión de tareas utilizando tecnologías modernas en Python.
