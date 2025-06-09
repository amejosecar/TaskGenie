# main.py - Punto de arranque de la aplicación.
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

# Importa el router de autenticación y otros routers.
from auth import router as auth_router
from routers import usuarios, tareas, perfil, admin
from routers import usuarios  # Asegúrate de que la ruta sea la correcta



app = FastAPI(title="TaskGenie")
templates = Jinja2Templates(directory="templates")

app.include_router(auth_router, tags=["Autenticación"])
app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(tareas.router, prefix="/tareas", tags=["Tareas"])
app.include_router(perfil.router, prefix="/perfil", tags=["Perfil"])
app.include_router(admin.router, prefix="/admin", tags=["Administración"])
app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Endpoint para mostrar la página de registro (HTML) 
@app.get("/registro")
async def registro(request: Request):
    return templates.TemplateResponse("registro.html", {"request": request})

@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    accept = request.headers.get("accept", "")
    if "text/html" in accept:
        return templates.TemplateResponse("errores.html", {"request": request, "mensaje": "La página que buscas no fue encontrada. Por favor, revisa la URL o regresa al inicio."}, status_code=404)
    return JSONResponse(status_code=404, content={"detail": "La página que buscas no fue encontrada. Por favor, revisa la URL o regresa al inicio."})
