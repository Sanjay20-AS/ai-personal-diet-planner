from app.services.ai.base import DietAIProvider, AIPlanResult

class LocalDietProvider(DietAIProvider):
    def generate(self, profile: dict) -> AIPlanResult:
        goal = profile["goal"].lower()
        diet = profile["diet_preference"].lower()
        meals = profile["meals_per_day"]

        base = 2000
        if goal in {"weight loss", "fat loss"}:
            base = 1800
        elif goal in {"weight gain", "muscle gain"}:
            base = 2300

        if profile["activity_level"].lower() == "high":
            base += 200
        elif profile["activity_level"].lower() == "low":
            base -= 150

        if diet == "vegetarian":
            breakfast = "Oats with banana and milk"
            lunch = "Rice, dal, mixed vegetables and curd"
            dinner = "Chapati, paneer/tofu and vegetables"
            snack = "Fruit with seeds"
        elif diet == "vegan":
            breakfast = "Oats with banana and plant milk"
            lunch = "Rice, lentils and mixed vegetables"
            dinner = "Chapati, tofu and vegetables"
            snack = "Fruit and roasted chickpeas"
        else:
            breakfast = "Oats, fruit and eggs"
            lunch = "Rice, dal, vegetables and a protein source"
            dinner = "Chapati, vegetables and a protein source"
            snack = "Fruit and yogurt"

        plan = {
            "breakfast": {"meal": breakfast, "calories": round(base * 0.20)},
            "lunch": {"meal": lunch, "calories": round(base * 0.30)},
            "snack": {"meal": snack, "calories": round(base * 0.10)},
            "dinner": {"meal": dinner, "calories": round(base * 0.30)},
            "notes": [
                "This is a demonstration plan, not medical advice.",
                f"Requested meals per day: {meals}.",
                "Adjust portions based on personal needs and professional guidance."
            ]
        }
        return AIPlanResult(provider="local", daily_calories=base, plan_data=plan)
