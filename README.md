# TaskGenie

**TaskGenie** es una aplicación de gestión de tareas desarrollada con Python, orientada a objetos y diseñada como proyecto de curso. Está pensada para facilitar la administración de tareas y usuarios a través de una API REST, utilizando un backend basado en FastAPI y una interfaz web renderizada con plantillas Jinja2.

## Características

- **Gestión de Usuarios y Roles**  
  - Tres tipos de usuarios: profesor, administrador y alumno.
  - Permisología y control de acciones basado en roles.
  - Registro, edición y bloqueo de usuarios (administrador).

- **Gestión de Tareas**  
  - Profesores: creación, búsqueda, asignación, cancelación y corrección de tareas.
  - Alumnos: visualización, edición, culminación y entrega de soluciones de tareas.
  - Seguimiento y registro de correcciones y feedback.

- **Autenticación y Seguridad**  
  - Sistema de login con validación de credenciales.
  - Gestión de contraseñas seguras (hashing con bcrypt).
  - Uso de variables de entorno para configuraciones sensibles.
  - Dependencias en FastAPI para proteger endpoints según el rol del usuario.

- **Interfaz Web Dinámica**  
  - Plantillas HTML renderizadas con Jinja2.
  - Formularios para login, registro, gestión de tareas y perfil de usuario.
  - Dashboards específicos para cada rol (profesor, alumno, administrador).

## Tecnologías

- **Backend:**  
  - [FastAPI](https://fastapi.tiangolo.com/)
  - [SQLAlchemy](https://www.sqlalchemy.org/) (con SQLite)
  - [Pydantic](https://pydantic-docs.helpmanual.io/)
  - [python-dotenv](https://pypi.org/project/python-dotenv/)
  - [bcrypt](https://pypi.org/project/bcrypt/)

- **Frontend:**  
  - **Jinja2** para la generación de plantillas HTML

- **Control de Versiones y Automatización:**  
  - Git y GitHub para el control de versiones.
  - (Opcional) GitHub Actions para CI/CD.

## Estructura del Proyecto

La estructura del proyecto es modular y está organizada en el siguiente esquema:

