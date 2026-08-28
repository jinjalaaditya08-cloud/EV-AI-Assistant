"""
Updated AI Brain for Phase 2: uses AIProvider abstraction.
"""

from core.context_manager import ContextManager

# Import typing helpers to allow optional provider
from typing import Optional

class AIBrain:
    def __init__(self, memory_manager=None, ai_provider=None):
        # Context manager remains local and in-memory for short-term context
        self.context = ContextManager()
        self.memory = memory_manager
        self.ai_provider = ai_provider

        # If no provider is supplied, lazily import and use LocalProvider
        if self.ai_provider is None:
            try:
                from ai_provider.local_provider import LocalProvider
                self.ai_provider = LocalProvider()
            except Exception:
                # Fallback: provider remains None and AIBrain will still work in a degraded mode
                self.ai_provider = None

    def handle_text(self, text: str, metadata: Optional[dict] = None):
        """Main entrypoint for text queries.
        Returns a dictionary with keys: {status, intent, response, provider_meta}
        """
        self.context.push_message('user', text)

        # Intent classification via provider if available
        intent = None
        provider_meta = None
        if self.ai_provider is not None:
            try:
                intent = self.ai_provider.classify_intent(text)
            except Exception:
                intent = None

        # Fallback intent detection (very small) if provider didn't produce one
        if not intent:
            # lightweight fallback: classify using a small rule set
            try:
                from core.intent_engine import IntentEngine
                intent = IntentEngine().classify(text)
            except Exception:
                intent = 'unknown'

        # Generate response via provider if possible
        response_text = None
        if self.ai_provider is not None:
            try:
                result = self.ai_provider.generate(prompt=text, intent=intent, metadata=metadata or {})
                response_text = result.get('text') if isinstance(result, dict) else str(result)
                provider_meta = result.get('meta') if isinstance(result, dict) else None
            except Exception:
                response_text = None

        # Final fallback response
        if not response_text:
            response_text = f"[Phase2-Fallback] Recognized intent: {intent}. You said: {text}"

        # push assistant response to context
        self.context.push_message('assistant', response_text)

        return {
            'status': 'ok',
            'intent': intent,
            'response': response_text,
            'provider_meta': provider_meta,
        }
