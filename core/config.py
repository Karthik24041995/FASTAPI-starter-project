import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    env: str = os.environ.get("APP_ENV", "dev")
    app_name: str = "Intermediate FastAPI"
    admin_email: str = "admin@example.com"

settings = Settings()
