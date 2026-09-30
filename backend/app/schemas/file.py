from datetime import datetime
from pydantic import BaseModel

class FileResponse(BaseModel):
    id: int
    original_filename: str
    storage_path: str
    content_type: str
    file_size: int
    created_at: datetime
