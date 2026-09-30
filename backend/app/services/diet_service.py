import time
from app.services.ai.factory import get_ai_provider
from app.models.diet_plan import DietPlan
from app.models.generation_log import GenerationLog

def generate_and_save_plan(db, user, profile):
    provider = get_ai_provider()
    profile_dict = {
        "age": profile.age,
        "height_cm": profile.height_cm,
        "weight_kg": profile.weight_kg,
        "activity_level": profile.activity_level,
        "diet_preference": profile.diet_preference,
        "allergies": profile.allergies,
        "goal": profile.goal,
        "meals_per_day": profile.meals_per_day,
    }

    started = time.perf_counter()
    try:
        result = provider.generate(profile_dict)
        plan = DietPlan(
            user_id=user.id,
            title="Personal Demo Meal Plan",
            goal=profile.goal,
            daily_calories=result.daily_calories,
            plan_data=result.plan_data,
            ai_provider=result.provider,
        )
        db.add(plan)
        db.flush()
        elapsed = int((time.perf_counter() - started) * 1000)
        db.add(GenerationLog(
            user_id=user.id,
            plan_id=plan.id,
            provider=result.provider,
            response_time_ms=elapsed,
            status="success",
        ))
        db.commit()
        db.refresh(plan)
        return plan
    except Exception as exc:
        db.rollback()
        db.add(GenerationLog(
            user_id=user.id,
            provider=getattr(provider, "__class__", type(provider)).__name__,
            response_time_ms=int((time.perf_counter() - started) * 1000),
            status="failed",
            error_message=str(exc)[:500],
        ))
        db.commit()
        raise
