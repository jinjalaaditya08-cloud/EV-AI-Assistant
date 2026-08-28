"""
AI Brain core orchestrator (Phase 1)
Very small orchestrator that routes text input to intent engine and context manager.
"""

from core.intent_engine import IntentEngine
from core.context_manager import ContextManager

class AIBrain:
    def __init__(self, memory_manager=None, ai_provider=None):
        self.intent = IntentEngine()
        self.context = ContextManager()
        self.memory = memory_manager
        self.ai_provider = ai_provider

    def handle_text(self, text, metadata=None):
        """Main entrypoint for text queries.
        Returns a dictionary with: {status, intent, response}
        """
        intent = self.intent.classify(text)
        context = self.context.get_context()

        # Minimal behavior for Phase 1: echo with intent
        response = f"[Phase1-DEMO] Recognized intent: {intent}. You said: {text}"

        return {
            'status': 'ok',
            'intent': intent,
            'response': response,
        }
