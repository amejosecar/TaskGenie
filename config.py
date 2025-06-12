# congig.py
# # Manejo de variables de entorno.
# config.py
from pydantic_settings import BaseSettings  # ← Corrección
from pydantic import AnyUrl

class Settings(BaseSettings):
    database_url: AnyUrl
    secret_key: str
    debug_mode: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
