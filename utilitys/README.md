# 🚀 TaskGenie

La aplicación **TaskGenie** es un sistema desarrollado en **FastAPI**, una potente y moderna biblioteca de Python para la creación de aplicaciones web y APIs rápidas y eficientes.  
Su objetivo principal es la gestión de **tareas** y **usuarios**, organizándolos según distintos roles: **administrador**, **profesor** y **alumno**.

---

> En pocas palabras, **TaskGenie** es un sistema completo para manejar usuarios y tareas en un ambiente académico o administrativo, asegurando organización y eficiencia.

---

## 📋 Análisis Global

### 🏗️ Arquitectura

- **Backend**  
  – Desarrollado en FastAPI, con estructura modular mediante _routers_ especializadas.
- **Base de datos**  
  – SQLite, gestionada a través de SQLAlchemy.
- **Plantillas**  
  – Jinja2 para renderizar páginas HTML dinámicas.
- **Autenticación**  
  – Dependencias de FastAPI y login basado en formularios.

---

## 📦 Paquetes Utilizados

| 📦 Paquete            | 🛠️ Uso                                                            |
| --------------------- | ----------------------------------------------------------------- |
| 🚀 **FastAPI**        | Creación de endpoints y API REST.                                 |
| 🐍 **SQLAlchemy**     | ORM para manejar la base de datos SQLite.                         |
| ⚙️ **Pydantic**       | Validación de datos y esquemas con `BaseModel`.                   |
| 🎨 **Jinja2**         | Motor de plantillas HTML.                                         |
| 📂 **Pathlib**        | Manejo de rutas y archivos.                                       |
| ⏰ **datetime**       | Manipulación de fechas, especialmente en el registro de usuarios. |
| 📑 **Enum**           | Definición de roles (`RolEnum`).                                  |
| ❗ **IntegrityError** | Detección y manejo de errores de integridad en la base de datos.  |

---

## 🛠️ Funcionalidad de la Aplicación

- 🔒 **Autenticación de usuarios**  
  Login mediante formularios y cookies HTTP-only.
- 📝 **Registro de usuarios**  
  Formulario con validación de campos y control de errores.
- ✅ **Gestión de tareas**  
  Creación, asignación y cambio de estado de tareas.
- 👥 **Administración de usuarios**  
  Listar, buscar, actualizar roles y gestionar bloqueos.
- 📊 **Dashboards personalizados**  
  Vistas adaptadas a cada rol: administrador, profesor y alumno.

---

TaskGenie/
├── .env # 🔒 Variables de entorno
├── .gitignore # 🚫 Archivos ignorados
├── requirements.txt # 📦 Dependencias del proyecto
├── **init**.py # 🧩 Inicializador de módulo
├── auth.py # 🔑 Autenticación de usuarios
├── config.py # ⚙️ Configuración de entorno
├── database.py # 🗄️ Conexión y gestión de BD
├── main.py # 🚀 Punto de entrada de la aplicación
├── models.py # 📜 Modelos SQLAlchemy
├── schemas.py # 📊 Esquemas Pydantic
├── README.md # 📖 Documentación del proyecto
├── routers/ # 📌 Endpoints organizados por funcionalidad
│----├── **init**.py # 🧩 Inicializador de rutas
│----├── admin.md # 📄 Documentación de administración
│----├── admin.py # 👥 Administración de usuarios
│----├── perfil.py # 🧑‍💼 Información del perfil
│----├── tareas.py # ✅ Gestión de tareas
│----└── usuarios.py # 🔍 Registro y búsqueda de usuarios
├── services/ # 🔧 Lógica de negocio y servicios
│----└── auth_service.py # 🛠️ Servicio de autenticación
└── templates/ # 🎨 Vistas HTML con Jinja2
----├── dashboard.html # 🏠 Dashboard general
----├── dashboard_admin.html # 👑 Panel de administrador
----├── dashboard_profesor.html # 🧑‍🏫 Panel de profesor
----├── dashboard_alumno.html # 👨‍🎓 Panel de alumno
----├── errores.html # ❌ Página de errores
----├── index.html # 🔑 Formulario de login
----├── login.html # 🎫 Vista de login
----└── registro.html # 📝 Formulario de registro
