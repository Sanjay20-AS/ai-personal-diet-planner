from datetime import datetime
from sqlalchemy import ForeignKey, String, Float, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.database import Base

class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), unique=True, index=True)
    age: Mapped[int] = mapped_column(Integer)
    height_cm: Mapped[float] = mapped_column(Float)
    weight_kg: Mapped[float] = mapped_column(Float)
    activity_level: Mapped[str] = mapped_column(String(30))
    diet_preference: Mapped[str] = mapped_column(String(50))
    allergies: Mapped[str] = mapped_column(String(500), default="")
    goal: Mapped[str] = mapped_column(String(50))
    meals_per_day: Mapped[int] = mapped_column(Integer, default=3)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="profile")
