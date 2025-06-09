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
python -m venv venv
source venv\Scripts\activate  # En Windows: env\Scripts\activate
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

taskgenie/ │ ├── app/ │ ├── init.py │ ├── main.py # Punto de entrada de la aplicación. │ ├── config.py # Configuración y manejo de variables de entorno. │ ├── database.py # Conexión a la base de datos SQLite y definición de sesión. │ ├── models.py # Modelos de datos usando SQLAlchemy. │ ├── schemas.py # Validación de datos con Pydantic. │ ├── auth.py # Implementación de autenticación, hashing y emisión de tokens. │ └── routers/ │ ├── init.py │ ├── usuarios.py # Endpoints para registro, edición y gestión de usuarios. │ ├── tareas.py # Endpoints para la creación, asignación, edición y corrección de tareas. │ ├── perfil.py # Endpoints para la visualización y edición del perfil. │ └── admin.py # Endpoints dedicados a la administración de usuarios. │ ├── templates/ │ ├── index.html # Página de inicio y formulario de login. │ ├── login.html # Vista de login. │ ├── registro.html # Formulario de registro. │ ├── dashboard_profesor.html # Dashboard y funcionalidades para profesores. │ ├── dashboard_alumno.html # Dashboard y funcionalidades para alumnos. │ ├── dashboard_admin.html # Dashboard para administradores. │ └── ... (otros formularios y vistas) │ ├── .env # Archivo para variables sensibles. ├── requirements.txt # Lista de dependencias del proyecto. ├── README.md # Este archivo. └── tests/ # Pruebas unitarias e integración. └── ...
```

...

## Instalación y Configuración

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu_usuario/TaskGenie.git
cd TaskGenie
2. Configurar el Entorno Virtual
bash
python -m venv venv
source venv/bin/activate  # En Linux/macOS
# ó
venv\Scripts\activate    # En Windows
3. Instalar Dependencias
Asegúrate de tener las versiones recomendadas de Python y luego instala las dependencias:

bash
pip install -r requirements.txt
Contenido sugerido para requirements.txt:

fastapi
uvicorn
sqlalchemy
pydantic
jinja2
python-dotenv
bcrypt
4. Configurar Variables de Entorno
Crea o edita el archivo .env en el directorio raíz y añade las variables necesarias (por ejemplo, la clave secreta para JWT):

dotenv
SECRET_KEY=tu_clave_secreta
DATABASE_URL=sqlite:///./taskgenie.db
Uso y Ejecución
Inicia la aplicación con Uvicorn:

bash
uvicorn app.main:app --reload
Accede a la documentación interactiva de FastAPI en: http://localhost:8000/docs.

Visita la página de inicio para iniciar sesión o registrarte.

Desarrollo y Buenas Prácticas
Modularidad y Separación de Responsabilidades: El proyecto separa claramente la lógica de la base de datos, autenticación, validación y rutas, lo que facilita el mantenimiento y escalabilidad.

Comentarios y Documentación: Se recomienda describir cada función y endpoint con docstrings para facilitar la comprensión del código, y aprovechar la documentación automática de FastAPI.

Control de Versiones y Uso de Git:

Realiza commits frecuentes con mensajes descriptivos.

Utiliza ramas (branches) para el desarrollo de nuevas características y revisa antes de integrar a la rama principal (main).

Integra herramientas de CI/CD (por ejemplo, GitHub Actions) para ejecutar tus tests automáticamente, asegurando la calidad del código.

Pruebas e Integración Continua
Pruebas: Implementa pruebas unitarias e integración en la carpeta tests/ para validar tanto la lógica de negocio como la integridad de los endpoints.

Integración Continua: Configura GitHub Actions para ejecutar tus pruebas con cada push o pull request. Esto mejora la robustez del proyecto y asegura que nuevos cambios no rompan funcionalidades existentes.

Contribución
¡Las contribuciones son bienvenidas!

Haz un fork del proyecto.

Crea una rama para tu nueva funcionalidad (git checkout -b feature/nueva-funcionalidad).

Realiza tus cambios y asegúrate de incluir nuevas pruebas si es necesario.

Envía un pull request explicando tus cambios.

Consulta el archivo CONTRIBUTING.md para más detalles (si decides agregarlo).

Licencia
Este proyecto se distribuye bajo la licencia MIT License.

Contacto
Si tienes alguna duda o comentario, por favor abre un issue en GitHub o envía un correo a tu_email@ejemplo.com.

Más Ideas y Recursos Relacionados
Guías de Buenas Prácticas: Explora la guía de Clean Code para mejorar la calidad de tu código.

Integración con Docker: Considera crear un Dockerfile para facilitar el despliegue y mejorar la portabilidad del proyecto.

Documentación: Integra herramientas como MkDocs para documentar las funcionalidades y arquitectura del proyecto de forma más interactiva.

CI/CD Avanzado: Explora la integración con plataformas de CI/CD, como GitHub Actions o Travis CI, para automatizar pruebas y despliegues.



---

Esta versión de README integra una estructura profesional, detalla las dependencias, guía al usuario en la instalación, y motiva la colaboración, al mismo tiempo que se adhiere a las mejores prácticas de desarrollo web en GitHub. ¿Te gustaría profundizar en algún apartado en particular o agregar nuevas secciones?
```
