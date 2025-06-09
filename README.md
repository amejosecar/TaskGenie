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
