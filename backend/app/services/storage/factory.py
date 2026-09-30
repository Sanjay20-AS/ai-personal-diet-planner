from app.core.config import get_settings
from app.services.storage.local import LocalStorageProvider
from app.services.storage.supabase import SupabaseStorageProvider


def get_storage_provider():
    settings = get_settings()

    if settings.storage_provider.lower() == "supabase":
        return SupabaseStorageProvider()

    return LocalStorageProvider(settings.storage_dir)