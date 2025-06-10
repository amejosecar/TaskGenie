# main.py - Punto de arranque de la aplicación.

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from auth import router as auth_router
from routers import tareas, perfil, admin  # Asegúrate de que admin se importe
# resto de importaciones...

app = FastAPI(title="TaskGenie")
templates = Jinja2Templates(directory="templates")

app.include_router(auth_router, tags=["Autenticación"])
app.include_router(tareas.router, prefix="/tareas", tags=["Tareas"])
app.include_router(perfil.router, prefix="/perfil", tags=["Perfil"])
app.include_router(admin.router, prefix="/admin", tags=["Administración"])  # Nuevo router admin

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    accept = request.headers.get("accept", "")
    if "text/html" in accept:
        return templates.TemplateResponse(
            "errores.html",
            {"request": request, "mensaje": "La página que buscas no fue encontrada. Por favor, revisa la URL o regresa al inicio."},
            status_code=404
        )
    return JSONResponse(status_code=404, content={"detail": "La página no fue encontrada."})

@app.get("/dashboard_admin", response_class=HTMLResponse)
async def dashboard_admin(request: Request):
    return templates.TemplateResponse("dashboard_admin.html", {"request": request})

