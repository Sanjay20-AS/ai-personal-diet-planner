from pathlib import Path
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.models.uploaded_file import UploadedFile
from app.schemas.file import FileResponse
from app.core.security import get_current_user
from app.services.storage.factory import get_storage_provider
from app.core.config import get_settings

router = APIRouter(prefix="/files", tags=["Files"])
ALLOWED_TYPES = {"image/jpeg", "image/png", "application/pdf", "text/plain"}

@router.post("/upload", response_model=FileResponse)
async def upload_file(
    file: UploadFile = File(...),
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    settings = get_settings()
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Unsupported file type")
    content = await file.read()
    max_bytes = settings.max_upload_mb * 1024 * 1024
    if len(content) > max_bytes:
        raise HTTPException(status_code=413, detail="File is too large")

    safe_name = Path(file.filename or "upload.bin").name
    storage = get_storage_provider()
    storage_path = storage.save(user.id, safe_name, content)

    item = UploadedFile(
        user_id=user.id,
        original_filename=safe_name,
        storage_path=storage_path,
        content_type=file.content_type,
        file_size=len(content),
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("", response_model=list[FileResponse])
def list_files(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return db.query(UploadedFile).filter(
        UploadedFile.user_id == user.id
    ).order_by(UploadedFile.created_at.desc()).all()

@router.delete("/{file_id}")
def delete_file(
    file_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    item = db.query(UploadedFile).filter(
        UploadedFile.id == file_id,
        UploadedFile.user_id == user.id
    ).first()
    if not item:
        raise HTTPException(status_code=404, detail="File not found")

    get_storage_provider().delete(item.storage_path)
    db.delete(item)
    db.commit()
    return {"message": "File deleted"}
