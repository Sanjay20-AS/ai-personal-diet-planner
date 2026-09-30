from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "AI Personal Diet Planner"
    environment: str = "development"
    secret_key: str
    access_token_expire_minutes: int = 60
    database_url: str = "sqlite:///./dietplanner.db"
    cors_origins: str = "http://localhost:5173"
    ai_provider: str = "local"
    gemini_api_key: str = ""
    storage_provider: str = "local"
    storage_dir: str = "storage"
    max_upload_mb: int = 5
    supabase_url: str = ""
    supabase_service_role_key: str = ""
    supabase_bucket: str = "diet-files"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def cors_list(self):
        return [x.strip() for x in self.cors_origins.split(",") if x.strip()]

@lru_cache
def get_settings():
    return Settings()
