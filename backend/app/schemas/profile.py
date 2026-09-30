from pydantic import BaseModel, Field

class ProfileCreate(BaseModel):
    age: int = Field(ge=13, le=100)
    height_cm: float = Field(gt=80, lt=250)
    weight_kg: float = Field(gt=20, lt=300)
    activity_level: str
    diet_preference: str
    allergies: str = ""
    goal: str
    meals_per_day: int = Field(default=3, ge=2, le=6)

class ProfileResponse(ProfileCreate):
    id: int
    user_id: int
