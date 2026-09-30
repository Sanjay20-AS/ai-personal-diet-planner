from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.models.diet_plan import DietPlan
from app.models.uploaded_file import UploadedFile
from app.core.security import get_current_user

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("")
def dashboard(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    plans = db.query(func.count(DietPlan.id)).filter(DietPlan.user_id == user.id).scalar() or 0
    files = db.query(func.count(UploadedFile.id)).filter(UploadedFile.user_id == user.id).scalar() or 0
    latest = db.query(DietPlan).filter(
        DietPlan.user_id == user.id
    ).order_by(DietPlan.created_at.desc()).first()

    return {
        "email": user.email,
        "plan_count": plans,
        "file_count": files,
        "latest_plan_id": latest.id if latest else None,
        "latest_provider": latest.ai_provider if latest else None,
    }
