from app.core.config import get_settings
from app.services.storage.factory import get_storage_provider
from app.services.storage.local import LocalStorageProvider


def test_storage_factory_uses_local_provider_by_default(monkeypatch):
    monkeypatch.setenv("STORAGE_PROVIDER", "local")
    get_settings.cache_clear()
    try:
        provider = get_storage_provider()
        assert isinstance(provider, LocalStorageProvider)
    finally:
        get_settings.cache_clear()
