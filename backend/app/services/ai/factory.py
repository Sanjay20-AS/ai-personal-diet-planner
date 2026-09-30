from app.core.config import get_settings
from app.services.ai.local import LocalDietProvider

def get_ai_provider():
    settings = get_settings()
    if settings.ai_provider.lower() == "gemini":
        from app.services.ai.gemini import GeminiDietProvider
        return GeminiDietProvider(settings.gemini_api_key)
    return LocalDietProvider()
