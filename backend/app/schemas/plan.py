from datetime import datetime
from pydantic import BaseModel

class PlanResponse(BaseModel):
    id: int
    title: str
    goal: str
    daily_calories: int
    plan_data: dict
    ai_provider: str
    created_at: datetime
