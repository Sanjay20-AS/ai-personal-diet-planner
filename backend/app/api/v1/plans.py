from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.models.profile import Profile
from app.models.diet_plan import DietPlan
from app.schemas.plan import PlanResponse
from app.core.security import get_current_user
from app.services.diet_service import generate_and_save_plan

router = APIRouter(prefix="/plans", tags=["Diet Plans"])

@router.post("/generate", response_model=PlanResponse)
def generate_plan(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    profile = db.query(Profile).filter(Profile.user_id == user.id).first()
    if not profile:
        raise HTTPException(status_code=400, detail="Create your profile first")
    return generate_and_save_plan(db, user, profile)

@router.get("", response_model=list[PlanResponse])
def list_plans(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return db.query(DietPlan).filter(DietPlan.user_id == user.id).order_by(DietPlan.created_at.desc()).all()

@router.get("/{plan_id}", response_model=PlanResponse)
def get_plan(
    plan_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    plan = db.query(DietPlan).filter(
        DietPlan.id == plan_id,
        DietPlan.user_id == user.id
    ).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan

@router.delete("/{plan_id}")
def delete_plan(
    plan_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    plan = db.query(DietPlan).filter(
        DietPlan.id == plan_id,
        DietPlan.user_id == user.id
    ).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    db.delete(plan)
    db.commit()
    return {"message": "Plan deleted"}
