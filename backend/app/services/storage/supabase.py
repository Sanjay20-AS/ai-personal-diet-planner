from supabase import create_client, Client

from app.core.config import get_settings
from app.services.storage.base import StorageProvider


class SupabaseStorageProvider(StorageProvider):

    def __init__(self):
        settings = get_settings()

        if not settings.supabase_url:
            raise ValueError("SUPABASE_URL is not configured.")

        if not settings.supabase_service_role_key:
            raise ValueError(
                "SUPABASE_SERVICE_ROLE_KEY is not configured."
            )

        self.bucket = settings.supabase_bucket

        self.client: Client = create_client(
            settings.supabase_url,
            settings.supabase_service_role_key,
        )

    def save(
        self,
        user_id: int,
        filename: str,
        content: bytes
    ) -> str:

        # Keep only the filename
        safe_name = filename.replace("\\", "/").split("/")[-1]

        # Store files inside a folder for each user
        storage_path = f"{user_id}/{safe_name}"

        self.client.storage.from_(self.bucket).upload(
            storage_path,
            content,
            {
                "content-type": self._get_content_type(safe_name),
                "upsert": "true",
            },
        )

        return storage_path

    def delete(self, storage_path: str) -> None:

        self.client.storage.from_(self.bucket).remove(
            [storage_path]
        )

    def _get_content_type(self, filename: str) -> str:

        filename = filename.lower()

        if filename.endswith(".pdf"):
            return "application/pdf"

        if filename.endswith(".png"):
            return "image/png"

        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            return "image/jpeg"

        if filename.endswith(".txt"):
            return "text/plain"

        return "application/octet-stream"