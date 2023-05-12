from starlette.config import Config

config = Config(".env")

DB_URL = config("DB_URL", cast=str, default="localhost:5432")
ACCESS_EXPIRATION = config("ACCESS_EXPIRATION", cast=int, default=60)
APP_PORT = config("APP_PORT", cast=int, default=8000)
APP_ADDR = config("APP_ADDR", cast=str, default="localhost")
ALGORITHM = "HS256"
SECRET_KEY = config("SECRET_KEY", cast=str, default="")
SERVICE_URL = config("SERVICE_URL", cast=str, default="https://python.exercise.applifting.cz/api/v1")
SERVICE_REFRESH = config("SERVICE_REFRESH", cast=str, default="")
