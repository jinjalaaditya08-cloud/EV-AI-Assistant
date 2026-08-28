"""
LocalProvider - a simple local AI provider stub for Phase 2.
This provider is deterministic and runs without external network calls.
It is intended as a placeholder and test harness until real providers are added.
"""

from typing import Dict, Any
from ai_provider.base import AIProvider
from core.intent_engine import IntentEngine

class LocalProvider(AIProvider):
    def __init__(self, config: Dict = None):
        super().__init__(config=config)
        self.intent_engine = IntentEngine()

    def generate(self, prompt: str, **kwargs) -> Dict[str, Any]:
        # Very small generation stub: echoes and provides safe metadata.
        text = f"[LocalProvider] {prompt}"
        return {
            'text': text,
            'meta': {
                'provider': 'local',
            }
        }

    def classify_intent(self, text: str, **kwargs) -> str:
        # Use the existing rule-based intent engine for Phase 2
        return self.intent_engine.classify(text)
