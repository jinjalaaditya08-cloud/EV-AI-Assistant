"""
AIProvider base interface.
Defines the methods the AI providers must implement.
"""

from typing import Any, Dict

class AIProvider:
    """Abstract AI provider interface.

    Implementations should be lightweight adapters around model APIs or local
    inference engines. Methods must be synchronous for Phase 2; async variants
    can be added later.
    """
    def __init__(self, config: Dict = None):
        self.config = config or {}

    def generate(self, prompt: str, **kwargs) -> Dict[str, Any]:
        """Generate a text response for a prompt.
        Returns a dict with at least a 'text' field and optional metadata.
        """
        raise NotImplementedError()

    def classify_intent(self, text: str, **kwargs) -> str:
        """Return an intent string for a given text input."""
        raise NotImplementedError()
