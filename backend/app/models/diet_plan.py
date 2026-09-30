from datetime import datetime
from sqlalchemy import ForeignKey, String, Integer, JSON, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.database import Base

class DietPlan(Base):
    __tablename__ = "diet_plans"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    title: Mapped[str] = mapped_column(String(150))
    goal: Mapped[str] = mapped_column(String(50))
    daily_calories: Mapped[int] = mapped_column(Integer)
    plan_data: Mapped[dict] = mapped_column(JSON)
    ai_provider: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="plans")
