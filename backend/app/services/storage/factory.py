from app.core.config import get_settings
from app.services.storage.local import LocalStorageProvider


def get_storage_provider():
    settings = get_settings()

    if settings.storage_provider.lower() == "supabase":
        from app.services.storage.supabase import SupabaseStorageProvider
        return SupabaseStorageProvider()

    return LocalStorageProvider(settings.storage_dir)