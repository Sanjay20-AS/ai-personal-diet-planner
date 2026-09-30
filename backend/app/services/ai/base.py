from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class AIPlanResult:
    provider: str
    daily_calories: int
    plan_data: dict

class DietAIProvider(ABC):
    @abstractmethod
    def generate(self, profile: dict) -> AIPlanResult:
        raise NotImplementedError
