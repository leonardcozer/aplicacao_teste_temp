import os
from typing import List
from pydantic_settings import BaseSettings


class CORSConfig(BaseSettings):
    allow_origins: List[str] = os.getenv(
        "CORS_ORIGINS",
        "http://localhost:3000,http://localhost:8080"
    ).split(",") if os.getenv("CORS_ORIGINS") else [
        "http://localhost:3000",
        "http://localhost:8080"
    ]
    allow_credentials: bool = os.getenv("CORS_CREDENTIALS", "True").lower() == "true"
    allow_methods: List[str] = ["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"]
    allow_headers: List[str] = [
        "Content-Type",
        "Authorization",
        "Accept",
        "Origin",
        "X-Requested-With",
        "X-Request-ID"
    ]


class ServerConfig(BaseSettings):
    host: str = os.getenv("SERVER_HOST", "0.0.0.0")
    port: int = int(os.getenv("SERVER_PORT", "8000"))
    reload: bool = os.getenv("ENVIRONMENT") == "development"
    log_level: str = os.getenv("LOG_LEVEL", "INFO")


class LokiConfig(BaseSettings):
    url: str = os.getenv("LOKI_URL", "http://localhost:3100")
    job: str = os.getenv("LOKI_JOB", "MONITORAMENTO_PRODUTO")
    enabled: bool = os.getenv("LOKI_ENABLED", "True").lower() == "true"


class TempoConfig(BaseSettings):
    endpoint: str = os.getenv("TEMPO_ENDPOINT", "http://172.30.0.45:4317")
    enabled: bool = os.getenv("TEMPO_ENABLED", "True").lower() == "true"


class Settings(BaseSettings):
    server: ServerConfig = ServerConfig()
    cors: CORSConfig = CORSConfig()
    loki: LokiConfig = LokiConfig()
    tempo: TempoConfig = TempoConfig()
    environment: str = os.getenv("ENVIRONMENT", "development")
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"

    class Config:
        extra = "allow"
        env_file = ".env"


settings = Settings()

