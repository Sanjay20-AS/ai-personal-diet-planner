from pathlib import Path
from app.services.storage.base import StorageProvider

class LocalStorageProvider(StorageProvider):
    def __init__(self, root: str):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def save(self, user_id: int, filename: str, content: bytes) -> str:
        safe_name = Path(filename).name
        folder = self.root / str(user_id)
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / safe_name
        path.write_bytes(content)
        return str(path)

    def delete(self, storage_path: str) -> None:
        path = Path(storage_path)
        if path.exists() and path.is_file():
            path.unlink()
