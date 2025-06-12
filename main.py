# main.py - Punto de arranque de la aplicación.

# main.py
from fastapi import FastAPI, Request, HTTPException, Depends, Cookie
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import engine, SessionLocal
from models import Base, Usuario
from auth import router as auth_router
from routers import admin, tareas, perfil, usuarios

# Creamos tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskGenie")
templates = Jinja2Templates(directory="templates")

# Montamos routers
app.include_router(auth_router)
app.include_router(admin.router)
app.include_router(tareas.router, prefix="/tareas", tags=["Tareas"])
app.include_router(perfil.router, prefix="/perfil", tags=["Perfil"])
app.include_router(usuarios.router, prefix="/u", tags=["Usuarios"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(
    user_id: str | None = Cookie(None),
    db: Session = Depends(get_db)
) -> Usuario | None:
    if user_id:
        return db.get(Usuario, int(user_id))
    return None

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(
    request: Request,
    user: Usuario | None = Depends(get_current_user)
):
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "user": user}
    )

@app.get("/dashboard_admin", response_class=HTMLResponse)
async def dashboard_admin(
    request: Request,
    user: Usuario | None = Depends(get_current_user)
):
    if not user or user.rol.value != "administrador":
        # Si no es admin, prohibimos el acceso
        raise HTTPException(status_code=403, detail="Acceso denegado")
    return templates.TemplateResponse(
        "dashboard_admin.html",
        {"request": request, "user": user}
    )

@app.exception_handler(404)
async def not_found(request: Request, exc: HTTPException):
    if "text/html" in request.headers.get("accept", ""):
        return templates.TemplateResponse(
            "errores.html",
            {"request": request, "mensaje": "Página no encontrada."},
            status_code=404
        )
    return JSONResponse(status_code=404, content={"detail": "Not found"})
