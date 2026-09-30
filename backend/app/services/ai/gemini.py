import json
from google import genai
from app.services.ai.base import DietAIProvider, AIPlanResult

class GeminiDietProvider(DietAIProvider):
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("GEMINI_API_KEY is not configured")
        self.client = genai.Client(api_key=api_key)

    def generate(self, profile: dict) -> AIPlanResult:
        prompt = f"""
Generate a simple educational meal plan as valid JSON.

This is NOT medical or clinical nutrition advice.
Do not diagnose disease or prescribe treatment.
Use the following synthetic/demo profile:

{json.dumps(profile)}

Return exactly this JSON structure:
{{
  "daily_calories": 2000,
  "breakfast": {{"meal": "...", "calories": 400}},
  "lunch": {{"meal": "...", "calories": 600}},
  "snack": {{"meal": "...", "calories": 200}},
  "dinner": {{"meal": "...", "calories": 600}},
  "notes": ["..."]
}}
"""
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        raw = response.text.strip()
        if raw.startswith("```"):
            raw = raw.replace("```json", "").replace("```", "").strip()
        data = json.loads(raw)
        daily = int(data.pop("daily_calories"))
        return AIPlanResult(provider="gemini", daily_calories=daily, plan_data=data)
